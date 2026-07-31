Time
====

**Time** matches a clock time in either the
`24-hour or 12-hour <https://en.wikipedia.org/wiki/12-hour_clock>`__ convention, with
optional seconds and fractional seconds. Unlike the date validators, the components
here *are* range-checked — hours stop at 23, minutes and seconds at 59.

The two conventions are branches of an :func:`~edify.any_of`. The 24-hour branch
allows ``0``–``23`` hours; the 12-hour branch allows ``1``–``12`` with an
``AM``/``PM`` suffix. Both take optional ``:seconds`` and a fractional part.

Twenty-four hour
----------------

.. edify-playground::

   from edify.library import time

   time("10:30")            # hours and minutes
   time("10:30:00")         # with seconds
   time("23:59:59")         # the end of the day
   time("00:00")            # midnight
   time("10:30:00.123456")  # fractional seconds

Twelve hour
-----------

.. edify-playground::

   from edify.library import time

   time("10:30 AM")
   time("11:59 PM")
   time("12:00 PM")

Components are range-checked
----------------------------

This is where the temporal validators are stricter than the date ones:

.. edify-playground::

   from edify.library import time

   time("23:59")   # the maximum
   time("24:00")   # hour out of range
   time("10:60")   # minute out of range
   time("10:30:60")  # second out of range
   time("")        # empty

Leap seconds — a legitimate ``23:59:60`` — are not accepted, and no time zone is
implied: a bare clock time is ambiguous without one. For the zone see :doc:`offset`
or :doc:`timezone`; for a date and time together, :doc:`datetime`.
