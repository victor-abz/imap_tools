"""IMAP Query builder"""
import datetime
import collections

from .utils import cleaned_uid_set, short_month_names, quote


class LogicOperator(collections.UserString):
    def __init__(self, *args, **kwargs):
        self.converted = args
        self.unconverted = kwargs
        for val in self.converted:
            if not any(isinstance(val, t) for t in (str, collections.UserString)):
                raise ValueError('Unexpected type "{}" for converted part, str like obj expected'.format(type(val)))
        converted_as_str = ' '.join((str(i) for i in self.converted))
        unconverted_as_str = ParamConverter(self.unconverted).to_str()
        self.full_str = ' '.join((unconverted_as_str, converted_as_str)).strip()
        super().__init__(self._build_query())

    def _build_query(self):
        raise NotImplementedError


class AND(LogicOperator):
    """When multiple keys are specified, the result is the intersection of all the messages that match those keys."""

    def _build_query(self):
        return self.full_str


class OR(LogicOperator):
    """OR <search-key1> <search-key2> Messages that match either search key."""

    def _build_query(self):
        return '(OR {})'.format(self.full_str)


class NOT(LogicOperator):
    """NOT <search-key> Messages that do not match the specified search key."""

    def _build_query(self):
        return '(NOT {})'.format(self.full_str)


Q = AND  # Short alias for AND


class ParamConverter:
    """Convert search params to IMAP format"""

    def __init__(self, params):
        self.params = params

    def to_str(self) -> str:
        converted = []
        for key, val in self.params.items():
            convert_func = getattr(self, 'convert_{}'.format(key), None)
            if not convert_func:
                raise KeyError('"{}" is an invalid parameter.'.format(key))
            converted.append(convert_func(key, val))
        return ' '.join(converted)

    @classmethod
    def format_date(cls, value: datetime.date) -> str:
        """To avoid locale affects"""
        return '{}-{}-{}'.format(value.day, short_month_names[value.month - 1], value.year)

    @staticmethod
    def cleaned_str(key, value) -> str:
        if type(value) is not str:
            raise ValueError('"{}" expected str value, "{}" received'.format(key, type(value)))
        return str(value)

    @staticmethod
    def cleaned_date(key, value) -> datetime.date:
        if type(value) is not datetime.date:
            raise ValueError('"{}" expected datetime.date value, "{}" received'.format(key, type(value)))
        return value

    @staticmethod
    def cleaned_bool(key, value) -> bool:
        if type(value) is not bool:
            raise ValueError('"{}" expected bool value, "{}" received'.format(key, type(value)))
        return bool(value)

    @staticmethod
    def cleaned_true(key, value) -> True:
        if value is not True:
            raise ValueError('"{}" expected "True", "{}" received'.format(key, type(value)))
        return True

    @staticmethod
    def cleaned_uint(key, value) -> int:
        if type(value) is not int or int(value) < 0:
            raise ValueError('"{}" expected int value >= 0, "{}" received'.format(key, type(value)))
        return int(value)

    @staticmethod
    def cleaned_uid(key, value) -> str:
        try:
            uid_set = cleaned_uid_set(value)
        except ValueError as e:
            raise ValueError('{} parse error: {}'.format(key, str(e)))
        return uid_set

    @staticmethod
    def cleaned_header(key, value) -> (str, str):
        if type(value) is str or type(value) is bytes:
            raise ValueError('"{}" expected (str, str) value, "{}" received'.format(key, type(value)))
        try:
            val1, val2 = value[0], value[1]
        except Exception:
            raise ValueError('"{}" expected (str, str) value, "{}" received'.format(key, type(value)))
        if type(val1) is not str:
            raise ValueError('"{}" field-name expected str value, "{}" received'.format(key, type(value)))
        if type(val2) is not str:
            raise ValueError('"{}" field-value expected str value, "{}" received'.format(key, type(value)))
        return quote(val1), quote(val2)

    def convert_answered(self, key, value):
        """Messages [with/without] the Answered flag set. (ANSWERED, UNANSWERED)"""
        return 'ANSWERED' if self.cleaned_bool(key, value) else 'UNANSWERED'

    def convert_seen(self, key, value):
        """Messages that [have/do not have] the Seen flag set. (SEEN, UNSEEN)"""
        return 'SEEN' if self.cleaned_bool(key, value) else 'UNSEEN'

    def convert_flagged(self, key, value):
        """Messages [with/without] the Flagged flag set. (FLAGGED, UNFLAGGED)"""
        return 'FLAGGED' if self.cleaned_bool(key, value) else 'UNFLAGGED'

    def convert_draft(self, key, value):
        """Messages that [have/do not have] the Draft flag set. (DRAFT, UNDRAFT)"""
        return 'DRAFT' if self.cleaned_bool(key, value) else 'UNDRAFT'

    def convert_deleted(self, key, value):
        """Messages that [have/do not have] the Deleted flag set. (DELETED, UNDELETED)"""
        return 'DELETED' if self.cleaned_bool(key, value) else 'UNDELETED'

    def convert_keyword(self, key, value):
        """Messages with the specified keyword flag set. (KEYWORD)"""
        return 'KEYWORD {}'.format(self.cleaned_str(key, value))

    def convert_no_keyword(self, key, value):
        """Messages that do not have the specified keyword flag set. (UNKEYWORD)"""
        return 'UNKEYWORD {}'.format(self.cleaned_str(key, value))

    def convert_from_(self, key, value):
        """Messages that contain the specified string in the envelope structure's FROM field."""
        return 'FROM {}'.format(quote(self.cleaned_str(key, value)))

    def convert_to(self, key, value):
        """Messages that contain the specified string in the envelope structure's TO field."""
        return 'TO {}'.format(quote(self.cleaned_str(key, value)))

    def convert_subject(self, key, value):
        """Messages that contain the specified string in the envelope structure's SUBJECT field."""
        return 'SUBJECT {}'.format(quote(self.cleaned_str(key, value)))

    def convert_body(self, key, value):
        """Messages that contain the specified string in the body of the message."""
        return 'BODY {}'.format(quote(self.cleaned_str(key, value)))

    def convert_text(self, key, value):
        """Messages that contain the specified string in the header or body of the message."""
        return 'TEXT {}'.format(quote(self.cleaned_str(key, value)))

    def convert_bcc(self, key, value):
        """Messages that contain the specified string in the envelope structure's BCC field."""
        return 'BCC {}'.format(quote(self.cleaned_str(key, value)))

    def convert_cc(self, key, value):
        """Messages that contain the specified string in the envelope structure's CC field."""
        return 'CC {}'.format(quote(self.cleaned_str(key, value)))

    def convert_date(self, key, value):
        """
        Messages whose internal date (disregarding time and timezone)
        is within the specified date. (ON)
        """
        return 'ON {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_date_gte(self, key, value):
        """
        Messages whose internal date (disregarding time and timezone)
        is within or later than the specified date. (SINCE)
        """
        return 'SINCE {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_date_lt(self, key, value):
        """
        Messages whose internal date (disregarding time and timezone)
        is earlier than the specified date. (BEFORE)
        """
        return 'BEFORE {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_sent_date(self, key, value):
        """
        Messages whose [RFC-2822] Date: header (disregarding time and timezone)
        is within the specified date. (SENTON)
        """
        return 'SENTON {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_sent_date_gte(self, key, value):
        """
        Messages whose [RFC-2822] Date: header (disregarding time and timezone)
        is within or later than the specified date. (SENTSINCE)
        """
        return 'SENTSINCE {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_sent_date_lt(self, key, value):
        """
        Messages whose [RFC-2822] Date: header (disregarding time and timezone)
        is earlier than the specified date. (SENTBEFORE)
        """
        return 'SENTBEFORE {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_size_gt(self, key, value):
        """Messages with an [RFC-2822] size larger than the specified number of octets. (LARGER)"""
        return 'LARGER {}'.format(self.cleaned_uint(key, value))

    def convert_size_lt(self, key, value):
        """Messages with an [RFC-2822] size smaller than the specified number of octets. (SMALLER)"""
        return 'SMALLER {}'.format(self.cleaned_uint(key, value))

    def convert_new(self, key, value):
        """
        Messages that have the Recent flag set but not the Seen flag.
        This is functionally equivalent to "(RECENT UNSEEN)".
        """
        self.cleaned_true(key, value)
        return 'NEW'

    def convert_old(self, key, value):
        """
        Messages that do not have the Recent flag set.
        This is functionally equivalent to "NOT RECENT" (as opposed to "NOT NEW").
        """
        self.cleaned_true(key, value)
        return 'OLD'

    def convert_recent(self, key, value):
        """Messages that have the Recent flag set."""
        self.cleaned_true(key, value)
        return 'RECENT'

    def convert_all(self, key, value):
        """All messages in the mailbox; the default initial key for ANDing."""
        self.cleaned_true(key, value)
        return 'ALL'

    def convert_header(self, key, value):
        """
        Messages that have a header with the specified field-name (as defined in [RFC-2822])
        and that contains the specified string in the text of the header (what comes after the colon).
        If the string to search is zero-length, this matches all messages that have a header line
        with the specified field-name regardless of the contents.
        """
        return 'HEADER {} {}'.format(*self.cleaned_header(key, value))

    def convert_uid(self, key, value):
        """Messages with unique identifiers corresponding to the specified unique identifier set."""
        return 'UID {}'.format(self.cleaned_uid(key, value))
