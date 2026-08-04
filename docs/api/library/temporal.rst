Temporal
========

Every validator in the :doc:`temporal <../../library/temporal/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/temporal/index>`.

.. py:function:: edify.library.cron(value: str) -> bool

   Cron. See :doc:`../../library/temporal/cron` for the full description.

   Emits ``^(?:@(?:(?:annually|yearly|monthly|weekly|daily|hourly|reboot))|(?:[\*\?0-9/,\-]+\s+){4,5}[\*\?0-9/,\-]+)$``

.. py:function:: edify.library.date(value: str) -> bool

   Date. See :doc:`../../library/temporal/date` for the full description.

   Emits ``^(?:\d{1,2}/\d{1,2}/\d{4}|\d{4}\-\d{2}\-\d{2}|\d{2}\-\d{2}\-\d{4}|\d{4}/\d{2}/\d{2}|\d{1,2}\.\d{1,2}\.\d{4}|\d{4}\.\d{2}\.\d{2}|\d{8})$``

.. py:function:: edify.library.datetime(value: str) -> bool

   Datetime. See :doc:`../../library/temporal/datetime` for the full description.

   Emits ``^(?:\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:(?:[+-]\d{2}:?\d{2}|[Zz]))?|\d{4}\d{2}\d{2}[Tt]\d{2}\d{2}\d{2}(?:(?:[+-]\d{4}|[Zz]))?)$``

.. py:function:: edify.library.duration(value: str) -> bool

   Duration. See :doc:`../../library/temporal/duration` for the full description.

   Emits ``^P(?=.)(?:\d+(?:\.\d+)?Y)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?=\d)(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$``

.. py:function:: edify.library.epoch(value: str) -> bool

   Epoch. See :doc:`../../library/temporal/epoch` for the full description.

   Emits ``^\-?\d{1,10}$``

.. py:function:: edify.library.interval(value: str) -> bool

   Interval. See :doc:`../../library/temporal/interval` for the full description.

   Emits ``^\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:(?:[+-]\d{2}:?\d{2}|[Zz]))?/(?:\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:(?:[+-]\d{2}:?\d{2}|[Zz]))?|P(?=.)(?:\d+(?:\.\d+)?Y)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?=\d)(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?)$``

.. py:function:: edify.library.iso_date(value: str) -> bool

   ISO date. See :doc:`../../library/temporal/iso_date` for the full description.

   Emits ``^\d{4}\-\d{2}\-\d{2}$``

.. py:function:: edify.library.offset(value: str) -> bool

   Offset. See :doc:`../../library/temporal/offset` for the full description.

   Emits ``^(?:[+-](?:0\d|1[0-4]):?[0-5]\d|[Z])$``

.. py:function:: edify.library.time(value: str) -> bool

   Time. See :doc:`../../library/temporal/time` for the full description.

   Emits ``^(?:(?:2[0-3]|[01]?\d):[0-5]\d(?::[0-5]\d(?:\.\d{1,6})?)?|(?:1[0-2]|0?[1-9]):[0-5]\d(?::[0-5]\d)?\s?[AaPp][Mm])$``

.. py:function:: edify.library.timestamp(value: str) -> bool

   Timestamp. See :doc:`../../library/temporal/timestamp` for the full description.

   Emits ``^\-?\d{10,13}$``

.. py:function:: edify.library.timezone(value: str) -> bool

   Timezone. See :doc:`../../library/temporal/timezone` for the full description.

   Emits ``^(?:[A-Z][a-zA-Z_\+\-]+(?:/[A-Z][a-zA-Z_\+\-]+)+|(?:UTC|GMT|UT|[Z])|[A-Z]{2,5})$``

.. py:function:: edify.library.year(value: str) -> bool

   Year. See :doc:`../../library/temporal/year` for the full description.

   Emits ``^\d{4}$``

