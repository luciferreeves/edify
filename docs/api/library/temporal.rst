Temporal
========

Every validator in the :doc:`Temporal <../../library/temporal/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/temporal/index>`.

.. py:data:: edify.library.cron

   Callable :class:`Pattern` for cron-expression shapes: shortcut aliases
   (``@daily`` etc.) or 5-/6-field whitespace-separated expressions.

   Full description: :doc:`Cron <../../library/temporal/cron>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      _alias = (
          Pattern()
          .char("@")
          .group()
          .any_of()
          .string("annually")
          .string("yearly")
          .string("monthly")
          .string("weekly")
          .string("daily")
          .string("hourly")
          .string("reboot")
          .end()
          .end()
      )
      _field = (
          Pattern()
          .one_or_more()
          .any_of()
          .char("*")
          .char("?")
          .range("0", "9")
          .char("/")
          .char(",")
          .char("-")
          .end()
      )
      _expr = (
          Pattern()
          .between(4, 5)
          .group()
          .subexpression(_field)
          .one_or_more()
          .whitespace_char()
          .end()
          .subexpression(_field)
      )

      cron = Pattern().start_of_input().subexpression(any_of(_alias, _expr)).end_of_input()

   **Emits** ``^(?:@(?:(?:annually|yearly|monthly|weekly|daily|hourly|reboot))|(?:[\*\?0-9/,\-]+\s+){4,5}[\*\?0-9/,\-]+)$``

.. py:data:: edify.library.date

   Callable :class:`Pattern` for common calendar-date shapes.

   Accepts ``M/D/YYYY``, ``YYYY-MM-DD``, ``DD-MM-YYYY``, ``YYYY/MM/DD``,
   ``DD.MM.YYYY``, ``YYYY.MM.DD``, or ``YYYYMMDD``.

   Guarantees:
       * Anchored at both ends — the whole input must be one of the accepted shapes.
       * Separators are fixed per shape; mixed separators are rejected.

   Does not guarantee:
       * Calendar validity — accepts ``02/30/2026`` and other structurally-valid but
         calendar-invalid shapes.
       * Strict ISO 8601 output — use :data:`edify.library.iso_date` for that.
       * Locale-specific day-first vs month-first disambiguation — a two-digit head
         that could be either month or day is accepted by both branches.

   Full description: :doc:`Date <../../library/temporal/date>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      _d1 = Pattern().between(1, 2).digit().char("/").between(1, 2).digit().char("/").exactly(4).digit()
      _d2 = Pattern().exactly(4).digit().char("-").exactly(2).digit().char("-").exactly(2).digit()
      _d3 = Pattern().exactly(2).digit().char("-").exactly(2).digit().char("-").exactly(4).digit()
      _d4 = Pattern().exactly(4).digit().char("/").exactly(2).digit().char("/").exactly(2).digit()
      _d5 = Pattern().between(1, 2).digit().char(".").between(1, 2).digit().char(".").exactly(4).digit()
      _d6 = Pattern().exactly(4).digit().char(".").exactly(2).digit().char(".").exactly(2).digit()
      _d7 = Pattern().exactly(8).digit()

      date = (
          Pattern()
          .start_of_input()
          .subexpression(any_of(_d1, _d2, _d3, _d4, _d5, _d6, _d7))
          .end_of_input()
      )

   **Emits** ``^(?:\d{1,2}/\d{1,2}/\d{4}|\d{4}\-\d{2}\-\d{2}|\d{2}\-\d{2}\-\d{4}|\d{4}/\d{2}/\d{2}|\d{1,2}\.\d{1,2}\.\d{4}|\d{4}\.\d{2}\.\d{2}|\d{8})$``

.. py:data:: edify.library.datetime

   Callable :class:`Pattern` for combined date-time shapes: ISO 8601 /
   RFC 3339 forms with ``T`` or space separator, optional fractional seconds,
   optional timezone suffix.

   Full description: :doc:`Datetime <../../library/temporal/datetime>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of


      def _iso_extended() -> Pattern:
          return (
              Pattern()
              .exactly(4)
              .digit()
              .char("-")
              .exactly(2)
              .digit()
              .char("-")
              .exactly(2)
              .digit()
              .any_of_chars("Tt ")
              .exactly(2)
              .digit()
              .char(":")
              .exactly(2)
              .digit()
              .optional()
              .group()
              .char(":")
              .exactly(2)
              .digit()
              .optional()
              .group()
              .char(".")
              .one_or_more()
              .digit()
              .end()
              .end()
              .optional()
              .group()
              .any_of()
              .any_of_chars("Zz")
              .subexpression(
                  Pattern().any_of_chars("+-").exactly(2).digit().optional().char(":").exactly(2).digit()
              )
              .end()
              .end()
          )


      def _iso_basic() -> Pattern:
          return (
              Pattern()
              .exactly(4)
              .digit()
              .exactly(2)
              .digit()
              .exactly(2)
              .digit()
              .any_of_chars("Tt")
              .exactly(2)
              .digit()
              .exactly(2)
              .digit()
              .exactly(2)
              .digit()
              .optional()
              .group()
              .any_of()
              .any_of_chars("Zz")
              .subexpression(Pattern().any_of_chars("+-").exactly(4).digit())
              .end()
              .end()
          )


      datetime = (
          Pattern().start_of_input().subexpression(any_of(_iso_extended(), _iso_basic())).end_of_input()
      )

   **Emits** ``^(?:\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:(?:[+-]\d{2}:?\d{2}|[Zz]))?|\d{4}\d{2}\d{2}[Tt]\d{2}\d{2}\d{2}(?:(?:[+-]\d{4}|[Zz]))?)$``

.. py:data:: edify.library.duration

   Callable :class:`Pattern` for the ISO 8601 duration shape:
   ``PnYnMnDTnHnMnS`` with optional fractional components.

   Full description: :doc:`Duration <../../library/temporal/duration>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern


      def _num_with_letter(letter: str) -> Pattern:
          return (
              Pattern()
              .optional()
              .group()
              .one_or_more()
              .digit()
              .optional()
              .group()
              .char(".")
              .one_or_more()
              .digit()
              .end()
              .char(letter)
              .end()
          )


      def _duration_body() -> Pattern:
          return (
              Pattern()
              .char("P")
              .assert_ahead()
              .any_char()
              .end()
              .subexpression(_num_with_letter("Y"))
              .subexpression(_num_with_letter("M"))
              .subexpression(_num_with_letter("W"))
              .subexpression(_num_with_letter("D"))
              .optional()
              .group()
              .char("T")
              .assert_ahead()
              .digit()
              .end()
              .subexpression(_num_with_letter("H"))
              .subexpression(_num_with_letter("M"))
              .subexpression(_num_with_letter("S"))
              .end()
          )


      duration = Pattern().start_of_input().subexpression(_duration_body()).end_of_input()

   **Emits** ``^P(?=.)(?:\d+(?:\.\d+)?Y)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?=\d)(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$``

.. py:data:: edify.library.epoch

   Callable :class:`Pattern` for a Unix epoch-seconds value: optional sign
   followed by 1-10 digits (fits in a 32-bit signed integer).

   Full description: :doc:`Epoch <../../library/temporal/epoch>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      epoch = Pattern().start_of_input().optional().char("-").between(1, 10).digit().end_of_input()

   **Emits** ``^\-?\d{1,10}$``

.. py:data:: edify.library.interval

   Callable :class:`Pattern` for the ISO 8601 time-interval shape:
   ``start-datetime/end-datetime`` or ``start-datetime/duration``.

   Full description: :doc:`Interval <../../library/temporal/interval>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of


      def _iso_extended() -> Pattern:
          return (
              Pattern()
              .exactly(4)
              .digit()
              .char("-")
              .exactly(2)
              .digit()
              .char("-")
              .exactly(2)
              .digit()
              .any_of_chars("Tt ")
              .exactly(2)
              .digit()
              .char(":")
              .exactly(2)
              .digit()
              .optional()
              .group()
              .char(":")
              .exactly(2)
              .digit()
              .optional()
              .group()
              .char(".")
              .one_or_more()
              .digit()
              .end()
              .end()
              .optional()
              .group()
              .any_of()
              .any_of_chars("Zz")
              .subexpression(
                  Pattern().any_of_chars("+-").exactly(2).digit().optional().char(":").exactly(2).digit()
              )
              .end()
              .end()
          )


      def _num_with_letter(letter: str) -> Pattern:
          return (
              Pattern()
              .optional()
              .group()
              .one_or_more()
              .digit()
              .optional()
              .group()
              .char(".")
              .one_or_more()
              .digit()
              .end()
              .char(letter)
              .end()
          )


      def _duration_body() -> Pattern:
          return (
              Pattern()
              .char("P")
              .assert_ahead()
              .any_char()
              .end()
              .subexpression(_num_with_letter("Y"))
              .subexpression(_num_with_letter("M"))
              .subexpression(_num_with_letter("W"))
              .subexpression(_num_with_letter("D"))
              .optional()
              .group()
              .char("T")
              .assert_ahead()
              .digit()
              .end()
              .subexpression(_num_with_letter("H"))
              .subexpression(_num_with_letter("M"))
              .subexpression(_num_with_letter("S"))
              .end()
          )


      interval = (
          Pattern()
          .start_of_input()
          .subexpression(_iso_extended())
          .char("/")
          .subexpression(any_of(_iso_extended(), _duration_body()))
          .end_of_input()
      )

   **Emits** ``^\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:(?:[+-]\d{2}:?\d{2}|[Zz]))?/(?:\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:(?:[+-]\d{2}:?\d{2}|[Zz]))?|P(?=.)(?:\d+(?:\.\d+)?Y)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?=\d)(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?)$``

.. py:data:: edify.library.iso_date

   Callable :class:`Pattern` for the ISO 8601 calendar-date shape ``YYYY-MM-DD``.

   Guarantees:
       * Exactly four year digits, two month digits, two day digits.
       * Hyphen separators, no whitespace, no time component.
       * Anchored at both ends.

   Does not guarantee:
       * Calendar validity — accepts shapes like ``2026-02-30`` that the ISO
         grammar allows but the calendar does not.
       * ISO 8601 time or datetime shapes — use :data:`edify.library.datetime`
         for those.

   Full description: :doc:`ISO date <../../library/temporal/iso_date>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      iso_date = (
          Pattern()
          .start_of_input()
          .exactly(4)
          .digit()
          .char("-")
          .exactly(2)
          .digit()
          .char("-")
          .exactly(2)
          .digit()
          .end_of_input()
      )

   **Emits** ``^\d{4}\-\d{2}\-\d{2}$``

.. py:data:: edify.library.offset

   Callable :class:`Pattern` for the UTC-offset shape: ``Z`` for UTC or
   ``±HH:MM`` / ``±HHMM`` with range ``-14:00`` to ``+14:00``.

   Full description: :doc:`Offset <../../library/temporal/offset>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      _hh = any_of(
          Pattern().char("0").digit(),
          Pattern().char("1").range("0", "4"),
      )

      offset = (
          Pattern()
          .start_of_input()
          .any_of()
          .char("Z")
          .subexpression(
              Pattern().any_of_chars("+-").subexpression(_hh).optional().char(":").range("0", "5").digit()
          )
          .end()
          .end_of_input()
      )

   **Emits** ``^(?:[+-](?:0\d|1[0-4]):?[0-5]\d|[Z])$``

.. py:data:: edify.library.time

   Callable :class:`Pattern` for clock-time shapes: 24-hour
   ``HH:MM[:SS[.ffffff]]`` or 12-hour ``H:MM[:SS] AM/PM``.

   Full description: :doc:`Time <../../library/temporal/time>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      _h24 = (
          Pattern()
          .any_of()
          .subexpression(Pattern().char("2").range("0", "3"))
          .subexpression(Pattern().optional().any_of_chars("01").digit())
          .end()
          .char(":")
          .range("0", "5")
          .digit()
          .optional()
          .group()
          .char(":")
          .range("0", "5")
          .digit()
          .optional()
          .group()
          .char(".")
          .between(1, 6)
          .digit()
          .end()
          .end()
      )

      _h12 = (
          Pattern()
          .any_of()
          .subexpression(Pattern().char("1").range("0", "2"))
          .subexpression(Pattern().optional().char("0").range("1", "9"))
          .end()
          .char(":")
          .range("0", "5")
          .digit()
          .optional()
          .group()
          .char(":")
          .range("0", "5")
          .digit()
          .end()
          .optional()
          .whitespace_char()
          .any_of_chars("AaPp")
          .any_of_chars("Mm")
      )

      time = Pattern().start_of_input().subexpression(any_of(_h24, _h12)).end_of_input()

   **Emits** ``^(?:(?:2[0-3]|[01]?\d):[0-5]\d(?::[0-5]\d(?:\.\d{1,6})?)?|(?:1[0-2]|0?[1-9]):[0-5]\d(?::[0-5]\d)?\s?[AaPp][Mm])$``

.. py:data:: edify.library.timestamp

   Callable :class:`Pattern` for a Unix epoch timestamp in seconds or
   milliseconds: optional sign followed by 10-13 digits.

   Full description: :doc:`Timestamp <../../library/temporal/timestamp>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      timestamp = Pattern().start_of_input().optional().char("-").between(10, 13).digit().end_of_input()

   **Emits** ``^\-?\d{10,13}$``

.. py:data:: edify.library.timezone

   Callable :class:`Pattern` for the timezone shape:
   IANA region/city (``America/Los_Angeles``), or short abbreviation
   (``UTC``, ``PST``, ``EST``, …).

   Full description: :doc:`Timezone <../../library/temporal/timezone>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      _iana_seg = (
          Pattern()
          .uppercase()
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .char("_")
          .char("+")
          .char("-")
          .end()
      )
      _iana = (
          Pattern()
          .subexpression(_iana_seg)
          .one_or_more()
          .group()
          .char("/")
          .subexpression(_iana_seg)
          .end()
      )
      _short = any_of(
          Pattern().string("UTC"),
          Pattern().string("GMT"),
          Pattern().string("UT"),
          Pattern().string("Z"),
      )
      _abbrev = Pattern().between(2, 5).uppercase()

      timezone = Pattern().start_of_input().subexpression(any_of(_iana, _short, _abbrev)).end_of_input()

   **Emits** ``^(?:[A-Z][a-zA-Z_\+\-]+(?:/[A-Z][a-zA-Z_\+\-]+)+|(?:UTC|GMT|UT|[Z])|[A-Z]{2,5})$``

.. py:data:: edify.library.year

   Callable :class:`Pattern` for the 4-digit calendar-year shape.

   Full description: :doc:`Year <../../library/temporal/year>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      year = Pattern().start_of_input().exactly(4).digit().end_of_input()

   **Emits** ``^\d{4}$``

