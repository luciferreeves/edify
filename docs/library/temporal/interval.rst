Interval
========

An `ISO 8601 interval <https://en.wikipedia.org/wiki/ISO_8601#Time_intervals>`__ is a
span between two points in time, written as two values joined by ``/``. **Interval**
matches the start/end form and the start/duration form.

The construction is a :doc:`datetime` value, a ``/``, then an
:func:`~edify.any_of` of either another datetime or a :doc:`duration`. Both branches
reuse the same component patterns those validators use.

Start and end
-------------

.. edify-playground::

   from edify.library import interval

   interval("2024-01-01T00:00:00Z/2024-12-31T23:59:59Z")
   interval("2024-01-01T00:00/2024-12-31T23:59")
   interval("2024-01-15 09:00/2024-01-15 17:00")

Start and duration
------------------

.. edify-playground::

   from edify.library import interval

   interval("2024-01-01T00:00:00Z/P1Y")     # a year from the start
   interval("2024-01-15T09:00:00/PT8H")     # an eight-hour shift
   interval("2024-01-01T00:00/P30D")

Both endpoints need a time
--------------------------

The start must be a full datetime, so a date-only span does not match:

.. edify-playground::

   from edify.library import interval

   interval("2024-01-01T00:00/2024-12-31T23:59")   # full datetimes
   interval("2024-01-01/2024-12-31")                # dates only
   interval("2024-01-01T00:00")                     # no separator
   interval("")                                     # empty

The duration-first form (``P1Y/2024-12-31``) and repeating intervals (``R5/…``) are
part of the standard but are not matched here. Nothing checks that the end follows
the start, either — an inverted range still matches.
