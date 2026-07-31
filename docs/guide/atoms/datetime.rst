Date and time atoms
===================

Eleven fragments for dates, clock times, and durations — the pieces behind the
:doc:`../../library/temporal/index` validators.

Compose them into an anchored pattern rather than calling them directly; see
:doc:`index`.

Whole dates and timestamps
--------------------------

``isodate`` is ``YYYY-MM-DD``; ``isodatetime`` adds a time and optional zone.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import isodate, isodatetime

   d = Pattern().start_of_input().use(isodate).end_of_input()
   dt = Pattern().start_of_input().use(isodatetime).end_of_input()

   d("2024-01-15")
   d("2024-1-5")                  # zero-padding is required
   dt("2024-01-15T10:30:00Z")
   dt("2024-01-15 10:30")         # a space separator and no seconds

Clock times
-----------

``clock`` is the 24-hour form with range-checked components; ``clock12`` requires an
AM/PM suffix.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import clock, clock12

   c = Pattern().start_of_input().use(clock).end_of_input()
   c12 = Pattern().start_of_input().use(clock12).end_of_input()

   c("23:59")        # the top of the range
   c("24:00")        # hours stop at 23
   c("10:30:00")     # seconds are optional
   c12("10:30 AM")   # the suffix is required
   c12("10:30")

Date components
---------------

``day``, ``month``, ``year``, and ``weekday`` match the parts individually — useful
when parsing a format the whole-date atoms do not cover.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import day, month, year, weekday

   dd = Pattern().start_of_input().use(day).end_of_input()
   mm = Pattern().start_of_input().use(month).end_of_input()
   yy = Pattern().start_of_input().use(year).end_of_input()
   wd = Pattern().start_of_input().use(weekday).end_of_input()

   dd("31")        # 01 to 31
   dd("32")
   mm("12")        # 01 to 12
   mm("13")
   yy("2024")      # four digits
   wd("Monday")    # full names and abbreviations
   wd("Mon")

Machine time and spans
----------------------

``epoch`` is a ten-digit second count, ``duration`` an ISO 8601 length, and
``timezone`` an offset or ``Z``.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import epoch, duration, timezone

   e = Pattern().start_of_input().use(epoch).end_of_input()
   du = Pattern().start_of_input().use(duration).end_of_input()
   tz = Pattern().start_of_input().use(timezone).end_of_input()

   e("1700000000")   # exactly ten digits
   e("170000")
   du("P1Y2M3D")     # date components
   du("PT1H30M")     # time components
   tz("+05:30")
   tz("Z")

Next: :doc:`web`.
