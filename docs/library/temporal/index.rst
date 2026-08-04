Temporal
========

Dates, times, durations, and the notations that schedule them. Each validator is a
callable :class:`~edify.Pattern`: import it, call it with a string, get a ``bool``.

A shared caveat runs through this category: matching a date's *shape* is not the same
as it being a real date. ``2024-02-31`` and ``2023-02-29`` both match
:doc:`iso_date`, because month lengths and leap years are arithmetic, not pattern
matching. Parse before you trust.

.. code-block:: python

   from edify.library import iso_date, duration, cron

   iso_date("2024-01-15")   # True
   duration("PT1H30M")      # True
   cron("0 9 * * 1-5")      # True

.. toctree::
   :hidden:

   cron
   date
   datetime
   duration
   epoch
   interval
   iso_date
   offset
   time
   timestamp
   timezone
   year

Dates and times
---------------

- :doc:`iso_date` — the strict ``YYYY-MM-DD`` form; :doc:`date` — several regional
  layouts.
- :doc:`time` — a clock time; :doc:`datetime` — a date and time together.
- :doc:`year` — a four-digit year.

Machine time
------------

- :doc:`epoch` — seconds since 1970; :doc:`timestamp` — seconds or milliseconds.

Ranges and zones
----------------

- :doc:`duration` — an ISO 8601 length of time; :doc:`interval` — a span between two
  points.
- :doc:`offset` — a UTC offset; :doc:`timezone` — a named zone.

Scheduling
----------

- :doc:`cron` — a crontab expression.
