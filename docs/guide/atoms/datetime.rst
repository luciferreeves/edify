Date and time atoms
===================

Eleven fragments for dates, clock times, and durations — the pieces behind the
:doc:`../../library/temporal/index` validators.

Compose them into an anchored pattern rather than calling them directly; see
:doc:`index`.

Whole dates and timestamps
--------------------------

``isodate`` is ``YYYY-MM-DD`` and ``isodatetime`` adds a time with an optional zone.
Both require zero-padding throughout, so ``2024-1-5`` does not match.

One thing to be clear about: ``isodate`` emits ``\d{4}\-\d{2}\-\d{2}``, which
checks the **shape** and not the values. ``2024-13-45`` matches it. That is the
right trade for a fragment you embed in a larger pattern — the component atoms
below do range-check, and :doc:`../../library/temporal/date` implements the full
calendar rules.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import isodate, isodatetime

   d = Pattern().start_of_input().use(isodate).end_of_input()
   dt = Pattern().start_of_input().use(isodatetime).end_of_input()

   d("2024-01-15")
   d("2024-1-5")                       # zero-padding is required
   d("2024-13-45")                     # but the ranges are not checked
   dt("2024-01-15T10:30:00Z")
   dt("2024-01-15 10:30")              # a space separator and no seconds
   dt("2024-01-15T10:30:00+05:30")     # or an explicit offset

``isodatetime`` is the more forgiving of the two by design: it accepts ``T``,
``t``, or a space as the separator, makes seconds and fractional seconds optional,
and allows a trailing offset or ``Z``. That covers what real systems emit.

Clock times
-----------

``clock`` is the 24-hour form with genuinely range-checked components — hours via
``(?:2[0-3]|[0-1]\d)`` and minutes via ``[0-5]\d``, so ``24:00`` and ``:60`` are
both rejected. It requires a zero-padded hour, and seconds are optional.

``clock12`` is the 12-hour form and differs in two ways: the hour may be unpadded
(``1:00`` is fine), and an AM/PM suffix is **required**. The suffix accepts either
case, with or without a space before it.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import clock, clock12

   c = Pattern().start_of_input().use(clock).end_of_input()
   c12 = Pattern().start_of_input().use(clock12).end_of_input()

   c("23:59")        # the top of the range
   c("24:00")        # hours stop at 23
   c("10:30:00")     # seconds are optional
   c("9:00")         # but the hour must be padded
   c12("10:30 AM")   # the suffix is required
   c12("1:00am")     # unpadded hour, either case, space optional
   c12("13:00 PM")   # twelve-hour clock stops at 12
   c12("10:30")

Date components
---------------

``day``, ``month``, ``year``, and ``weekday`` match the parts individually — useful
when parsing a format the whole-date atoms do not cover, and the place where the
range checks actually live.

.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Atom
     - Emits
     - Accepts
   * - ``year``
     - ``\d{4}``
     - any four digits — no era check
   * - ``month``
     - ``(?:0[1-9]|1[0-2])``
     - ``01``–``12``, zero-padded
   * - ``day``
     - ``(?:0[1-9]|[1-2]\d|3[0-1])``
     - ``01``–``31``, zero-padded
   * - ``weekday``
     - an alternation
     - full names and three-letter abbreviations

``day`` stops at 31 for every month — it has no way to know which month it sits
beside, so February 31st matches. Composition cannot express that dependency;
:doc:`../../library/temporal/date` is where it is handled.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import day, month, weekday, year

   dd = Pattern().start_of_input().use(day).end_of_input()
   mm = Pattern().start_of_input().use(month).end_of_input()
   yy = Pattern().start_of_input().use(year).end_of_input()
   wd = Pattern().start_of_input().use(weekday).end_of_input()

   dd("31")        # 01 to 31
   dd("32")
   mm("12")        # 01 to 12
   mm("1")         # padding required
   yy("2024")      # four digits
   wd("Monday")    # full names and abbreviations
   wd("Mon")
   wd("monday")    # capitalised only

Machine time and spans
----------------------

``epoch`` is a ten-digit second count — exactly ten, so it covers the range from
2001 to 2286 and rejects both a shorter and a longer number. Reach for
``unsigned`` if you need millisecond timestamps too.

``timezone`` is an offset in either ``+HH:MM`` or ``+HHMM`` form, or a literal
uppercase ``Z``. Lowercase ``z`` does not match, even though ``isodatetime``
accepts it in a full timestamp.

``duration`` is an ISO 8601 length. It is the most intricate atom here, and it uses
a lookahead to require at least one component after the ``P`` — so a bare ``P``
is rejected rather than matching a zero-length duration.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import duration, epoch, timezone

   e = Pattern().start_of_input().use(epoch).end_of_input()
   du = Pattern().start_of_input().use(duration).end_of_input()
   tz = Pattern().start_of_input().use(timezone).end_of_input()

   e("1700000000")   # exactly ten digits
   e("170000")
   du("P1Y2M3D")     # date components
   du("PT1H30M")     # time components
   du("P1DT2H")      # or both
   du("P")           # but at least one is required
   tz("+05:30")
   tz("-0800")       # the colon is optional
   tz("Z")

Next: :doc:`web`.
