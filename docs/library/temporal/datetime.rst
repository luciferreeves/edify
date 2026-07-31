Datetime
========

**Datetime** matches a date and time together in
`ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`__ form —
``2024-01-15T10:30:00Z`` — the shape :rfc:`3339` fixes for internet timestamps.

The construction is the ``YYYY-MM-DD`` date, a separator that may be ``T``, ``t``, or
a space, then hours and minutes, an :meth:`~edify.RegexBuilder.optional` seconds and
fractional part, and an optional zone — either a ``±HH:MM`` offset or ``Z``.

Date and time
-------------

.. edify-playground::

   from edify.library import datetime

   datetime("2024-01-15T10:30:00Z")        # the canonical form
   datetime("2024-01-15T10:30:00")         # no zone
   datetime("2024-01-15 10:30:00")         # a space separator
   datetime("2024-01-15T10:30")            # no seconds
   datetime("2024-01-15T10:30:00.123Z")    # fractional seconds

Zone designators
----------------

.. edify-playground::

   from edify.library import datetime

   datetime("2024-01-15T10:30:00+05:30")   # a positive offset
   datetime("2024-01-15T10:30:00-08:00")   # a negative offset
   datetime("2024-01-15T10:30:00Z")        # UTC

Both halves are required
------------------------

.. edify-playground::

   from edify.library import datetime

   datetime("2024-01-15T10:30:00")   # complete
   datetime("2024-01-15")            # date only: see iso_date
   datetime("10:30:00")              # time only: see time
   datetime("")                      # empty

A value with no zone is ambiguous — it names a wall-clock reading without saying
where — so require the offset for anything you will compare or store. And as with
:doc:`iso_date`, the calendar itself is unchecked.
