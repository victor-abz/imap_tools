import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='S19 IZM A7-342',
    from_='k1@yandex.ru',
    to=('rasp@wat.aero',),
    cc=('aa@com.ru', 'mm@com.ru'),
    bcc=('hello@yandex-team.ru',),
    reply_to=(),
    date=datetime.datetime(2019, 2, 7, 13, 18, 20, tzinfo=datetime.timezone(datetime.timedelta(seconds=18000))),
    date_str='Thu, 7 Feb 2019 13:18:20 +0500',
    text='SCR\r\n\r\n/\r\nS19\r\n07FEB\r\nwat\r\n\r\n-- \r\nотдел расписания\r\nтел. (343) 072-00-00 (вн.18-59)\r\ne-mail: e.sp@com.ru\r\n\r\nДобрый\xa0день,\xa0уважаемые\xa0коллеги!\r\n\r\n\r\n\r\n\r\n-------- Перенаправленное сообщение --------\r\nТема: \tВвод рейсов ТЮМ, ЧЛБ, ОМС на Лето 2019\r\nДата: \tFri, 7 Dec 2018 08:23:21 +0500\r\nОт: \tПлёткина <a.pl@com.ru>\r\nКому: \tБелобородова О.Н. <schedule@com.ru>\r\n\r\n\r\n\r\nДобрый\xa0день,\xa0уважаемые\xa0коллеги!\r\n\r\nПрошу ввести рейс на период летней навигации\r\n\r\n*ДМД-ТЮМ-ДМД \xa0 У6-341/342*\xa0 тип ВС А320\r\n\r\nВВ из ДМД 23:00 LT. ВВ из ТЮМ 06:45 LT\r\n\r\nисключение период с 25/05/19 по 13/10/19\r\n\r\nВВ из ДМД в 00:50 LT\r\n\r\nВВ из ТЮМ остается без изменения\r\n\r\n----------------------------------------\r\n\r\n*ДМД-ОМС-ДМД \xa0 У6-387/388*\xa0 тип ВС А321\r\n\r\nВВ из ДМД в 23:15. ВВ из ОМС 06:30 LT\r\n\r\n----------------------------------------\r\n\r\n*ДМД-ЧЛБ-ДМД \xa0 У6-610/609*\xa0 тип ВС А320\r\n\r\nВВ из ДМД в 23:30. ВВ из ЧЛБ 06:40 LT\r\n\r\n\r\n',
    html='<html>\r\n  <head>\r\n\r\n    <meta http-equiv="content-type" content="text/html; charset=utf-8">\r\n  </head>\r\n  <body text="#000000" bgcolor="#FFFFFF">\r\n    <p>SCR<br>\r\n    </p>\r\n    <div class="moz-forward-container">/<br>\r\n      S19<br>\r\n      07FEB<br>\r\n      wat<br></div>\r\n    <pre class="moz-signature" cols="72">-- \r\nотдел расписания\r\nтел. (343) 072-00-00 (вн.18-59)\r\ne-mail: <a class="moz-txt-link-abbreviated" href="mailto:e.sp@com.ru">e.sp@com.ru</a></pre>\r\n  </body>\r\n</html>\r\n<html>\r\n  <head>\r\n\r\n    <meta http-equiv="content-type" content="text/html; charset=utf-8">\r\n  </head>\r\n  <body smarttemplateinserted="true">\r\n    <div id="smartTemplate4-template">Добрый\xa0день,\xa0уважаемые\xa0коллеги!\r\n      <p>\xa0</p>\r\n    </div>\r\n    <br>\r\n    <div class="moz-forward-container"><br>\r\n      <br>\r\n      -------- Перенаправленное сообщение --------\r\n      <table class="moz-email-headers-table" cellspacing="0"\r\n        cellpadding="0" border="0">\r\n        <tbody>\r\n          <tr>\r\n            <th valign="BASELINE" nowrap="nowrap" align="RIGHT">Тема: </th>\r\n            <td>Ввод рейсов ТЮМ, ЧЛБ, ОМС на Лето 2019</td>\r\n          </tr>\r\n          <tr>\r\n            <th valign="BASELINE" nowrap="nowrap" align="RIGHT">Дата: </th>\r\n            <td>Fri, 7 Dec 2018 08:23:21 +0500</td>\r\n          </tr>\r\n          <tr>\r\n            <th valign="BASELINE" nowrap="nowrap" align="RIGHT">От: </th>\r\n            <td>1 <a class="moz-txt-link-rfc2396E" href="mailto:a.pl@com.ru">&lt;a.pl@com.ru&gt;</a></td>\r\n          </tr>\r\n          <tr>\r\n            <th valign="BASELINE" nowrap="nowrap" align="RIGHT">Кому: </th>\r\n            <td>2 <a class="moz-txt-link-rfc2396E" href="mailto:schedule@com.ru">&lt;schedule@com.ru&gt;</a></td>\r\n          </tr>\r\n        </tbody>\r\n      </table>\r\n      <br>\r\n      <br>\r\n      <meta http-equiv="content-type" content="text/html; charset=utf-8">\r\n      <div id="smartTemplate4-template">Добрый\xa0день,\xa0уважаемые\xa0коллеги!\r\n        <p>Прошу ввести рейс на период летней навигации <br>\r\n        </p>\r\n        <p>\xa0 тип ВС А320<br>\r\n        </p>\r\n        <p>ВВ из ДМД 23:00 LT. ВВ из ТЮМ 06:45 LT</p>\r\n        <p>исключение период с 25/05/19 по 13/10/19 <br>\r\n        </p>\r\n        <p>ВВ из ДМД в 00:50 LT<br>\r\n        </p>\r\n        <p>ВВ из ТЮМ остается без изменения <br>\r\n        </p>\r\n        <p>----------------------------------------</p>\r\n        <p>\xa0 тип ВС А321</p>\r\n        <p>ВВ из ДМД в 23:15. ВВ из ОМС 06:30 LT <br>\r\n        </p>\r\n        <p>----------------------------------------</p>\r\n        <p>\xa0 тип ВС А320</p>\r\n        <p>ВВ из ДМД в 23:30. ВВ из ЧЛБ 06:40 LT </p>\r\n      </div>\r\n      <br>\r\n    </div>\r\n  </body>\r\n</html>\r\n',
    headers={'return-path': ('e.sp@com.ru',), 'received': ('from m101.com.ru (LHLO m101.com.ru) (92.233.222.111) by m101.com.ru\r\n with LMTP; Thu, 7 Feb 2019 13:18:22 +0500 (YEKT)', 'from localhost (localhost [127.0.0.1])\r\n\tby m101.com.ru (Postfix) with ESMTP id 9A9181170B7;\r\n\tThu,  7 Feb 2019 13:18:22 +0500 (YEKT)', 'from m101.com.ru ([127.0.0.1])\r\n\tby localhost (m101.com.ru [127.0.0.1]) (amavisd-new, port 10026)\r\n\twith ESMTP id Q3OLc4gNDjjO; Thu,  7 Feb 2019 13:18:22 +0500 (YEKT)', 'from [192.168.104.100] (kom-420-1.hades.company [192.168.104.100])\r\n\tby m101.com.ru (Postfix) with ESMTPSA id DC7BB1170A1;\r\n\tThu,  7 Feb 2019 13:18:21 +0500 (YEKT)'), 'x-virus-scanned': ('amavisd-new at m101.com.ru',), 'subject': ('S19 IZM A7-342',), 'references': ('<1333139463.20190207083243@com.ru>',), 'to': ('=?UTF-8?B?0KLQrtCc0JXQndCs?= <rasp@wat.aero>',), 'from': ('=?utf-8?B?0JrQsNGD0LrQuNC9INCS0LvQsNC00LjQvNC40YA=?= <k1@yandex.ru>',), 'cc': ('aa@com.ru, mm@com.ru',), 'bcc': ('=?utf-8?b?0JrQvtC80LDQvdC00LAg0K/QvdC00LXQutGBLtCf0L7Rh9GC0Ys=?=\r\n\t<hello@yandex-team.ru>',), 'x-forwarded-message-id': ('<1333139463.20190207083243@com.ru>',), 'message-id': ('<2ffd4cec-d312-60da-72f3-5b6e4406fddf@com.ru>',), 'date': ('Thu, 7 Feb 2019 13:18:20 +0500',), 'user-agent': ('Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101\r\n Thunderbird/60.5.0',), 'mime-version': ('1.0',), 'in-reply-to': ('<1333139463.20190207083243@com.ru>',), 'content-type': ('multipart/mixed;\r\n boundary="------------FFFBFD561B1FF33B4E5E7050"',), 'content-language': ('ru',)},
    attachments=[
        dict(
            filename='Message01.eml',
            content_id='',
            content_disposition='attachment',
            content_type='message/rfc822',
            payload=b'Return-Path: a.pl@com.ru\nReceived: from m101.com.ru (LHLO m101.com.ru) (92.233.222.111) by m101.com.ru\n with LMTP; Thu, 7 Feb 2019 08:29:46 +0500 (YEKT)\nReceived: from localhost (localhost [127.0.0.1])\n\tby m101.com.ru (Postfix) with ESMTP id 5C11A78A70;\n\tThu,  7 Feb 2019 08:29:46 +0500 (YEKT)\nX-Virus-Scanned: amavisd-new at m101.com.ru\nReceived: from m101.com.ru ([127.0.0.1])\n\tby localhost (m101.com.ru [127.0.0.1]) (amavisd-new, port 10026)\n\twith ESMTP id qPDszqYc1_Us; Thu,  7 Feb 2019 08:29:46 +0500 (YEKT)\nReceived: from [192.168.104.53] (kom-419-31.hades.company [192.168.104.53])\n\tby m101.com.ru (Postfix) with ESMTPSA id 29D6C78A67\n\tfor <a.nov@company.ru>; Thu,  7 Feb 2019 08:29:46 +0500 (YEKT)\nSubject: S19 IZM A7-342\nReferences: <4a598974-6731-c4f3-0efa-2f1e2b044f08@com.ru>\nTo: Alla Nov <a.nov@company.ru>\nFrom: =?utf-8?B?0JrQsNGD0LrQuNC9INCS0LvQsNC00LjQvNC40YA=?= <k1@yandex.ru>\nX-Forwarded-Message-Id: <4a598974-6731-c4f3-0efa-2f1e2b044f08@com.ru>\nMessage-ID: <09ccd226-f9e9-77e0-e456-3490e024d16e@com.ru>\nDate: Thu, 7 Feb 2019 08:29:45 +0500\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101\n Thunderbird/60.4.0\nMIME-Version: 1.0\nIn-Reply-To: <4a598974-6731-c4f3-0efa-2f1e2b044f08@com.ru>\nContent-Type: multipart/alternative;\n boundary="------------CC10C5F7DB2594C21A5E2BDB"\nContent-Language: ru\n\n--------------CC10C5F7DB2594C21A5E2BDB\nContent-Type: text/plain; charset=utf-8; format=flowed\nContent-Transfer-Encoding: 8bit\n\n\xd0\x94\xd0\xbe\xd0\xb1\xd1\x80\xd1\x8b\xd0\xb9\xc2\xa0\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c,\xc2\xa0\xd1\x83\xd0\xb2\xd0\xb0\xd0\xb6\xd0\xb0\xd0\xb5\xd0\xbc\xd1\x8b\xd0\xb5\xc2\xa0\xd0\xba\xd0\xbe\xd0\xbb\xd0\xbb\xd0\xb5\xd0\xb3\xd0\xb8!\n\n\n\n\n-------- \xd0\x9f\xd0\xb5\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb5 \xd1\x81\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 --------\n\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0: \t\xd0\x92\xd0\xb2\xd0\xbe\xd0\xb4 \xd1\x80\xd0\xb5\xd0\xb9\xd1\x81\xd0\xbe\xd0\xb2 \xd0\xa2\xd0\xae\xd0\x9c, \xd0\xa7\xd0\x9b\xd0\x91, \xd0\x9e\xd0\x9c\xd0\xa1 \xd0\xbd\xd0\xb0 \xd0\x9b\xd0\xb5\xd1\x82\xd0\xbe 2019\n\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0: \tFri, 7 Dec 2018 08:23:21 +0500\n\xd0\x9e\xd1\x82: \t\xd0\x9f\xd0\xbb\xd1\x91\xd1\x82\xd0\xba\xd0\xb8\xd0\xbd\xd0\xb0 <a.pl@com.ru>\n\xd0\x9a\xd0\xbe\xd0\xbc\xd1\x83: \t\xd0\x91\xd0\xb5\xd0\xbb\xd0\xbe\xd0\xb1\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xb2\xd0\xb0 \xd0\x9e.\xd0\x9d. <schedule@com.ru>\n\n\n\n\xd0\x94\xd0\xbe\xd0\xb1\xd1\x80\xd1\x8b\xd0\xb9\xc2\xa0\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c,\xc2\xa0\xd1\x83\xd0\xb2\xd0\xb0\xd0\xb6\xd0\xb0\xd0\xb5\xd0\xbc\xd1\x8b\xd0\xb5\xc2\xa0\xd0\xba\xd0\xbe\xd0\xbb\xd0\xbb\xd0\xb5\xd0\xb3\xd0\xb8!\n\n\xd0\x9f\xd1\x80\xd0\xbe\xd1\x88\xd1\x83 \xd0\xb2\xd0\xb2\xd0\xb5\xd1\x81\xd1\x82\xd0\xb8 \xd1\x80\xd0\xb5\xd0\xb9\xd1\x81 \xd0\xbd\xd0\xb0 \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb8\xd0\xbe\xd0\xb4 \xd0\xbb\xd0\xb5\xd1\x82\xd0\xbd\xd0\xb5\xd0\xb9 \xd0\xbd\xd0\xb0\xd0\xb2\xd0\xb8\xd0\xb3\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8\n\n*\xd0\x94\xd0\x9c\xd0\x94-\xd0\xa2\xd0\xae\xd0\x9c-\xd0\x94\xd0\x9c\xd0\x94 \xc2\xa0 \xd0\xa36-341/342*\xc2\xa0 \xd1\x82\xd0\xb8\xd0\xbf \xd0\x92\xd0\xa1 \xd0\x90320\n\n\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 23:00 LT. \xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\xa2\xd0\xae\xd0\x9c 06:45 LT\n\n\xd0\xb8\xd1\x81\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb8\xd0\xbe\xd0\xb4 \xd1\x81 25/05/19 \xd0\xbf\xd0\xbe 13/10/19\n\n\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 \xd0\xb2 00:50 LT\n\n\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\xa2\xd0\xae\xd0\x9c \xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb5\xd1\x82\xd1\x81\xd1\x8f \xd0\xb1\xd0\xb5\xd0\xb7 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f\n\n----------------------------------------\n\n*\xd0\x94\xd0\x9c\xd0\x94-\xd0\x9e\xd0\x9c\xd0\xa1-\xd0\x94\xd0\x9c\xd0\x94 \xc2\xa0 \xd0\xa36-387/388*\xc2\xa0 \xd1\x82\xd0\xb8\xd0\xbf \xd0\x92\xd0\xa1 \xd0\x90321\n\n\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 \xd0\xb2 23:15. \xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x9e\xd0\x9c\xd0\xa1 06:30 LT\n\n----------------------------------------\n\n*\xd0\x94\xd0\x9c\xd0\x94-\xd0\xa7\xd0\x9b\xd0\x91-\xd0\x94\xd0\x9c\xd0\x94 \xc2\xa0 \xd0\xa36-610/609*\xc2\xa0 \xd1\x82\xd0\xb8\xd0\xbf \xd0\x92\xd0\xa1 \xd0\x90320\n\n\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 \xd0\xb2 23:30. \xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\xa7\xd0\x9b\xd0\x91 06:40 LT\n\n\n\n--------------CC10C5F7DB2594C21A5E2BDB\nContent-Type: text/html; charset=utf-8\nContent-Transfer-Encoding: 8bit\n\n<html>\n  <head>\n\n    <meta http-equiv="content-type" content="text/html; charset=UTF-8">\n  </head>\n  <body smarttemplateinserted="true">\n    <div id="smartTemplate4-template">\xd0\x94\xd0\xbe\xd0\xb1\xd1\x80\xd1\x8b\xd0\xb9\xc2\xa0\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c,\xc2\xa0\xd1\x83\xd0\xb2\xd0\xb0\xd0\xb6\xd0\xb0\xd0\xb5\xd0\xbc\xd1\x8b\xd0\xb5\xc2\xa0\xd0\xba\xd0\xbe\xd0\xbb\xd0\xbb\xd0\xb5\xd0\xb3\xd0\xb8!\n      <p>\xc2\xa0</p>\n    </div>\n    <br>\n    <div class="moz-forward-container"><br>\n      <br>\n      -------- \xd0\x9f\xd0\xb5\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb5 \xd1\x81\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 --------\n      <table class="moz-email-headers-table" cellspacing="0"\n        cellpadding="0" border="0">\n        <tbody>\n          <tr>\n            <th valign="BASELINE" nowrap="nowrap" align="RIGHT">\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0: </th>\n            <td>\xd0\x92\xd0\xb2\xd0\xbe\xd0\xb4 \xd1\x80\xd0\xb5\xd0\xb9\xd1\x81\xd0\xbe\xd0\xb2 \xd0\xa2\xd0\xae\xd0\x9c, \xd0\xa7\xd0\x9b\xd0\x91, \xd0\x9e\xd0\x9c\xd0\xa1 \xd0\xbd\xd0\xb0 \xd0\x9b\xd0\xb5\xd1\x82\xd0\xbe 2019</td>\n          </tr>\n          <tr>\n            <th valign="BASELINE" nowrap="nowrap" align="RIGHT">\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0: </th>\n            <td>Fri, 7 Dec 2018 08:23:21 +0500</td>\n          </tr>\n          <tr>\n            <th valign="BASELINE" nowrap="nowrap" align="RIGHT">\xd0\x9e\xd1\x82: </th>\n            <td>1 <a class="moz-txt-link-rfc2396E" href="mailto:a.pl@com.ru">&lt;a.pl@com.ru&gt;</a></td>\n          </tr>\n          <tr>\n            <th valign="BASELINE" nowrap="nowrap" align="RIGHT">\xd0\x9a\xd0\xbe\xd0\xbc\xd1\x83: </th>\n            <td>2 <a class="moz-txt-link-rfc2396E" href="mailto:schedule@com.ru">&lt;schedule@com.ru&gt;</a></td>\n          </tr>\n        </tbody>\n      </table>\n      <br>\n      <br>\n      <meta http-equiv="content-type" content="text/html; charset=UTF-8">\n      <div id="smartTemplate4-template">\xd0\x94\xd0\xbe\xd0\xb1\xd1\x80\xd1\x8b\xd0\xb9\xc2\xa0\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c,\xc2\xa0\xd1\x83\xd0\xb2\xd0\xb0\xd0\xb6\xd0\xb0\xd0\xb5\xd0\xbc\xd1\x8b\xd0\xb5\xc2\xa0\xd0\xba\xd0\xbe\xd0\xbb\xd0\xbb\xd0\xb5\xd0\xb3\xd0\xb8!\n        <p>\xd0\x9f\xd1\x80\xd0\xbe\xd1\x88\xd1\x83 \xd0\xb2\xd0\xb2\xd0\xb5\xd1\x81\xd1\x82\xd0\xb8 \xd1\x80\xd0\xb5\xd0\xb9\xd1\x81 \xd0\xbd\xd0\xb0 \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb8\xd0\xbe\xd0\xb4 \xd0\xbb\xd0\xb5\xd1\x82\xd0\xbd\xd0\xb5\xd0\xb9 \xd0\xbd\xd0\xb0\xd0\xb2\xd0\xb8\xd0\xb3\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8 <br>\n        </p>\n        <p>\xc2\xa0 \xd1\x82\xd0\xb8\xd0\xbf \xd0\x92\xd0\xa1 \xd0\x90320<br>\n        </p>\n        <p>\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 23:00 LT. \xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\xa2\xd0\xae\xd0\x9c 06:45 LT</p>\n        <p>\xd0\xb8\xd1\x81\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb8\xd0\xbe\xd0\xb4 \xd1\x81 25/05/19 \xd0\xbf\xd0\xbe 13/10/19 <br>\n        </p>\n        <p>\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 \xd0\xb2 00:50 LT<br>\n        </p>\n        <p>\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\xa2\xd0\xae\xd0\x9c \xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb5\xd1\x82\xd1\x81\xd1\x8f \xd0\xb1\xd0\xb5\xd0\xb7 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f <br>\n        </p>\n        <p>----------------------------------------</p>\n        <p>\xc2\xa0 \xd1\x82\xd0\xb8\xd0\xbf \xd0\x92\xd0\xa1 \xd0\x90321</p>\n        <p>\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 \xd0\xb2 23:15. \xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x9e\xd0\x9c\xd0\xa1 06:30 LT <br>\n        </p>\n        <p>----------------------------------------</p>\n        <p>\xc2\xa0 \xd1\x82\xd0\xb8\xd0\xbf \xd0\x92\xd0\xa1 \xd0\x90320</p>\n        <p>\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 \xd0\xb2 23:30. \xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\xa7\xd0\x9b\xd0\x91 06:40 LT </p>\n      </div>\n      <br>\n    </div>\n  </body>\n</html>\n\n--------------CC10C5F7DB2594C21A5E2BDB--\n\n',
        ),
        ],
    from_values=EmailAddress(name='Каукин Владимир', email='k1@yandex.ru'),
    to_values=(EmailAddress(name='ТЮМЕНЬ', email='rasp@wat.aero'),),
    cc_values=(EmailAddress(name='', email='aa@com.ru'), EmailAddress(name='', email='mm@com.ru')),
    bcc_values=(EmailAddress(name='Команда Яндекс.Почты', email='hello@yandex-team.ru'),),
    reply_to_values=(),
)