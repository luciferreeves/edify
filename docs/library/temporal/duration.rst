Duration
========

An `ISO 8601 duration <https://en.wikipedia.org/wiki/ISO_8601#Durations>`__ measures
a *length* of time rather than a point in it: ``P1Y2M3D`` is one year, two months,
three days; ``PT1H30M`` is ninety minutes. **Duration** matches that notation.

The construction opens with ``P`` and a :meth:`~edify.RegexBuilder.assert_ahead`
requiring at least one component to follow — which is what stops a bare ``P`` from
matching. Then come optional year, month, week, and day parts, and after a ``T``
marker the optional hour, minute, and second parts. The ``T`` is what separates
months from minutes, since both use ``M``.

Date components
---------------

.. edify-playground::

   from edify.library import duration

   duration("P1Y")        # one year
   duration("P1Y2M3D")    # years, months, days
   duration("P3W")        # three weeks
   duration("P30D")       # thirty days

Time components
---------------

Everything after ``T`` is a time part:

.. edify-playground::

   from edify.library import duration

   duration("PT1H30M")        # ninety minutes
   duration("PT30S")          # thirty seconds
   duration("P1DT12H")        # a day and a half
   duration("PT0.5S")         # a fractional second

The designators are required
----------------------------

.. edify-playground::

   from edify.library import duration

   duration("PT1H")    # with designators
   duration("P")       # no components
   duration("1h30m")   # informal notation
   duration("PT")      # a marker with nothing after it
   duration("")        # empty

Note that ``P1M`` and ``PT1M`` mean different things — one month against one minute —
so the ``T`` is not optional decoration. Calendar components are also inexact: a
month is not a fixed number of days, which matters when adding a duration to a date.
For a span between two points see :doc:`interval`.
