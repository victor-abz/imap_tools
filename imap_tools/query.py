"""IMAP Query builder"""
import datetime
import itertools
import functools
from collections import UserString
from typing import Iterable, Optional, Dict, Any, List, Union

from .consts import SHORT_MONTH_NAMES
from .utils import clean_uids, quote


class Header:
    """Header value for search by header key"""
    __slots__ = ('name', 'value')

    def __init__(self, name: str, value: str):
        if not isinstance(name, str):
            raise TypeError('Header-name expected str value, "{}" received'.format(type(name)))
        self.name = quote(name)
        if not isinstance(value, str):
            raise TypeError('Header-value expected str value, "{}" received'.format(type(value)))
        self.value = quote(value)

    def __str__(self):
        return '{0.name}: {0.value}'.format(self)


class UidRange:
    """
    UID range value for search by uid key
    * - represents the largest number in use.
    x:y - represents sequence range, example: 4:*
    NOTE: UID range of <value>:* always includes the UID of the last message in the mailbox,
    even if <value> is higher than any assigned UID value ->
    any UID range with * indicates at least one message (with the highest numbered UID), unless the mailbox is empty.
    """
    __slots__ = ('start', 'end')

    def __init__(self, start: str, end: Optional[str] = None):
        self.start = str(start).strip()
        if not (self.start.isdigit() or self.start == '*'):
            raise TypeError('UidRange start arg must be str with digits or *')
        if end is None:
            self.end = None
        else:
            self.end = str(end).strip()
            if not (self.end.isdigit() or self.end == '*'):
                raise TypeError('UidRange end arg must be str with digits or *')

    def __str__(self):
        return '{}{}'.format(self.start, ':{}'.format(self.end) if self.end else '')


class LogicOperator(UserString):
    def __init__(
            self,
            *converted_strings: Union[str, UserString],
            answered: Optional[bool] = None,
            seen: Optional[bool] = None,
            flagged: Optional[bool] = None,
            draft: Optional[bool] = None,
            deleted: Optional[bool] = None,
            keyword: Optional[Union[str, List[str]]] = None,
            no_keyword: Optional[Union[str, List[str]]] = None,
            from_: Optional[Union[str, List[str]]] = None,
            to: Optional[Union[str, List[str]]] = None,
            subject: Optional[Union[str, List[str]]] = None,
            body: Optional[Union[str, List[str]]] = None,
            text: Optional[Union[str, List[str]]] = None,
            bcc: Optional[Union[str, List[str]]] = None,
            cc: Optional[Union[str, List[str]]] = None,
            date: Optional[Union[datetime.date, List[datetime.date]]] = None,
            date_gte: Optional[Union[datetime.date, List[datetime.date]]] = None,
            date_lt: Optional[Union[datetime.date, List[datetime.date]]] = None,
            sent_date: Optional[Union[datetime.date, List[datetime.date]]] = None,
            sent_date_gte: Optional[Union[datetime.date, List[datetime.date]]] = None,
            sent_date_lt: Optional[Union[datetime.date, List[datetime.date]]] = None,
            size_gt: Optional[int] = None,
            size_lt: Optional[int] = None,
            new: Optional[bool] = None,
            old: Optional[bool] = None,
            recent: Optional[bool] = None,
            all: Optional[bool] = None,  # noqa
            uid: Optional[Union[str, Iterable[str], UidRange]] = None,
            header: Optional[Header] = None,
            gmail_label: Optional[Union[str, List[str]]] = None):  # todo newline after drop 3.5
        self.converted_strings = converted_strings
        for val in converted_strings:
            if not any(isinstance(val, t) for t in (str, UserString)):
                raise TypeError('Unexpected type "{}" for converted part, str like obj expected'.format(type(val)))
        unconverted_dict = {k: v for k, v in locals().items() if k in SEARCH_KEYS and v is not None}
        self.converted_params = ParamConverter(unconverted_dict).convert()
        if not any((self.converted_strings, self.converted_params)):
            raise ValueError('{} expects params'.format(self.__class__.__name__))
        super().__init__(self.combine_params())

    def combine_params(self) -> str:
        """combine self.converted_strings and self.converted_params to IMAP search criteria format"""
        raise NotImplementedError

    @staticmethod
    def prefix_join(operator: str, params: Iterable[str]) -> str:
        """Join params by prefix notation rules, enclose group in parenthesis"""
        return '({})'.format(functools.reduce(lambda a, b: '{}{} {}'.format(operator, a, b), params))


class AND(LogicOperator):
    """Combines conditions by logical AND"""

    def combine_params(self) -> str:
        return self.prefix_join('', itertools.chain(self.converted_strings, self.converted_params))


class OR(LogicOperator):
    """Combines conditions by logical OR"""

    def combine_params(self) -> str:
        return self.prefix_join('OR ', itertools.chain(self.converted_strings, self.converted_params))


class NOT(LogicOperator):
    """Inverts the result of a logical expression"""

    def combine_params(self) -> str:
        return 'NOT {}'.format(self.prefix_join('', itertools.chain(self.converted_strings, self.converted_params)))


class ParamConverter:
    """Convert search params to IMAP format"""

    multi_key_allowed = (
        'keyword', 'no_keyword', 'from_', 'to', 'subject', 'body', 'text', 'bcc', 'cc',
        'date', 'date_gte', 'date_lt', 'sent_date', 'sent_date_gte', 'sent_date_lt',
        'header', 'gmail_label',
    )

    def __init__(self, params: Dict[str, Any]):
        self.params = params

    def _gen_values(self, key: str, value: Any) -> Iterable[Any]:
        """Values generator"""
        # single value
        if key not in self.multi_key_allowed or isinstance(value, str):
            yield value
        else:
            try:
                # multiple values
                for i in value:
                    yield i
            except TypeError:
                # single value
                yield value

    def convert(self) -> List[str]:
        """
        :return: params in IMAP format
        """
        converted = []
        for key, raw_val in sorted(self.params.items(), key=lambda x: x[0]):
            for val in sorted(self._gen_values(key, raw_val)):
                convert_func = getattr(self, 'convert_{}'.format(key), None)
                if not convert_func:
                    raise KeyError('"{}" is an invalid parameter.'.format(key))
                converted.append(convert_func(key, val))
        return converted

    @classmethod
    def format_date(cls, value: datetime.date) -> str:
        """To avoid locale affects"""
        return '{}-{}-{}'.format(value.day, SHORT_MONTH_NAMES[value.month - 1], value.year)

    @staticmethod
    def cleaned_str(key: str, value: str) -> str:
        if type(value) is not str:
            raise TypeError('"{}" expected str value, "{}" received'.format(key, type(value)))
        return str(value)

    @staticmethod
    def cleaned_date(key: str, value: datetime.date) -> datetime.date:
        if type(value) is not datetime.date:
            raise TypeError('"{}" expected datetime.date value, "{}" received'.format(key, type(value)))
        return value

    @staticmethod
    def cleaned_bool(key: str, value: bool) -> bool:
        if type(value) is not bool:
            raise TypeError('"{}" expected bool value, "{}" received'.format(key, type(value)))
        return bool(value)

    @staticmethod
    def cleaned_true(key: str, value: bool) -> True:
        if value is not True:
            raise TypeError('"{}" expected "True", "{}" received'.format(key, type(value)))
        return True

    @staticmethod
    def cleaned_uint(key: str, value: int) -> int:
        if type(value) is not int or int(value) < 0:
            raise TypeError('"{}" expected int value >= 0, "{}" received'.format(key, type(value)))
        return int(value)

    @staticmethod
    def cleaned_uid(key: str, value: Union[str, Iterable[str], UidRange]) -> str:
        # range
        if isinstance(value, UidRange):
            return str(value)
        # set
        try:
            return clean_uids(value)
        except TypeError as e:
            raise TypeError('{} parse error: {}'.format(key, str(e)))

    @staticmethod
    def cleaned_header(key: str, value: Header) -> Header:
        if not isinstance(value, Header):
            raise TypeError('"{}" expected Header (H) value, "{}" received'.format(key, type(value)))
        return value

    def convert_answered(self, key, value) -> str:
        """Messages [with/without] the Answered flag set. (ANSWERED, UNANSWERED)"""
        return 'ANSWERED' if self.cleaned_bool(key, value) else 'UNANSWERED'

    def convert_seen(self, key, value) -> str:
        """Messages that [have/do not have] the Seen flag set. (SEEN, UNSEEN)"""
        return 'SEEN' if self.cleaned_bool(key, value) else 'UNSEEN'

    def convert_flagged(self, key, value) -> str:
        """Messages [with/without] the Flagged flag set. (FLAGGED, UNFLAGGED)"""
        return 'FLAGGED' if self.cleaned_bool(key, value) else 'UNFLAGGED'

    def convert_draft(self, key, value) -> str:
        """Messages that [have/do not have] the Draft flag set. (DRAFT, UNDRAFT)"""
        return 'DRAFT' if self.cleaned_bool(key, value) else 'UNDRAFT'

    def convert_deleted(self, key, value) -> str:
        """Messages that [have/do not have] the Deleted flag set. (DELETED, UNDELETED)"""
        return 'DELETED' if self.cleaned_bool(key, value) else 'UNDELETED'

    def convert_keyword(self, key, value) -> str:
        """Messages with the specified keyword flag set. (KEYWORD)"""
        return 'KEYWORD {}'.format(self.cleaned_str(key, value))

    def convert_no_keyword(self, key, value) -> str:
        """Messages that do not have the specified keyword flag set. (UNKEYWORD)"""
        return 'UNKEYWORD {}'.format(self.cleaned_str(key, value))

    def convert_from_(self, key, value) -> str:
        """Messages that contain the specified string in the envelope structure's FROM field."""
        return 'FROM {}'.format(quote(self.cleaned_str(key, value)))

    def convert_to(self, key, value) -> str:
        """Messages that contain the specified string in the envelope structure's TO field."""
        return 'TO {}'.format(quote(self.cleaned_str(key, value)))

    def convert_subject(self, key, value) -> str:
        """Messages that contain the specified string in the envelope structure's SUBJECT field."""
        return 'SUBJECT {}'.format(quote(self.cleaned_str(key, value)))

    def convert_body(self, key, value) -> str:
        """Messages that contain the specified string in the body of the message."""
        return 'BODY {}'.format(quote(self.cleaned_str(key, value)))

    def convert_text(self, key, value) -> str:
        """Messages that contain the specified string in the header or body of the message."""
        return 'TEXT {}'.format(quote(self.cleaned_str(key, value)))

    def convert_bcc(self, key, value) -> str:
        """Messages that contain the specified string in the envelope structure's BCC field."""
        return 'BCC {}'.format(quote(self.cleaned_str(key, value)))

    def convert_cc(self, key, value) -> str:
        """Messages that contain the specified string in the envelope structure's CC field."""
        return 'CC {}'.format(quote(self.cleaned_str(key, value)))

    def convert_date(self, key, value) -> str:
        """
        Messages whose internal date (disregarding time and timezone)
        is within the specified date. (ON)
        """
        return 'ON {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_date_gte(self, key, value) -> str:
        """
        Messages whose internal date (disregarding time and timezone)
        is within or later than the specified date. (SINCE)
        """
        return 'SINCE {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_date_lt(self, key, value) -> str:
        """
        Messages whose internal date (disregarding time and timezone)
        is earlier than the specified date. (BEFORE)
        """
        return 'BEFORE {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_sent_date(self, key, value) -> str:
        """
        Messages whose [RFC-2822] Date: header (disregarding time and timezone)
        is within the specified date. (SENTON)
        """
        return 'SENTON {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_sent_date_gte(self, key, value) -> str:
        """
        Messages whose [RFC-2822] Date: header (disregarding time and timezone)
        is within or later than the specified date. (SENTSINCE)
        """
        return 'SENTSINCE {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_sent_date_lt(self, key, value) -> str:
        """
        Messages whose [RFC-2822] Date: header (disregarding time and timezone)
        is earlier than the specified date. (SENTBEFORE)
        """
        return 'SENTBEFORE {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_size_gt(self, key, value) -> str:
        """Messages with an [RFC-2822] size larger than the specified number of octets. (LARGER)"""
        return 'LARGER {}'.format(self.cleaned_uint(key, value))

    def convert_size_lt(self, key, value) -> str:
        """Messages with an [RFC-2822] size smaller than the specified number of octets. (SMALLER)"""
        return 'SMALLER {}'.format(self.cleaned_uint(key, value))

    def convert_new(self, key, value) -> str:
        """
        Messages that have the Recent flag set but not the Seen flag.
        This is functionally equivalent to "(RECENT UNSEEN)".
        """
        self.cleaned_true(key, value)
        return 'NEW'

    def convert_old(self, key, value) -> str:
        """
        Messages that do not have the Recent flag set.
        This is functionally equivalent to "NOT RECENT" (as opposed to "NOT NEW").
        """
        self.cleaned_true(key, value)
        return 'OLD'

    def convert_recent(self, key, value) -> str:
        """Messages that have the Recent flag set."""
        self.cleaned_true(key, value)
        return 'RECENT'

    def convert_all(self, key, value) -> str:
        """All messages in the mailbox; the default initial key for ANDing."""
        self.cleaned_true(key, value)
        return 'ALL'

    def convert_header(self, key, value) -> str:
        """
        Messages that have a header with the specified field-name (as defined in [RFC-2822])
        and that contains the specified string in the text of the header (what comes after the colon).
        If the string to search is zero-length, this matches all messages that have a header line
        with the specified field-name regardless of the contents.
        """
        return 'HEADER {0.name} {0.value}'.format(self.cleaned_header(key, value))

    def convert_uid(self, key, value) -> str:
        """Messages with unique identifiers corresponding to the specified unique identifier set."""
        return 'UID {}'.format(self.cleaned_uid(key, value))

    def convert_gmail_label(self, key, value) -> str:
        return 'X-GM-LABELS {}'.format(quote(self.cleaned_str(key, value)))


SEARCH_KEYS = tuple(i.replace('convert_', '') for i in dir(ParamConverter) if 'convert_' in i)

# Short alias set:
A = AND
O = OR  # noqa
N = NOT
H = Header
U = UidRange
