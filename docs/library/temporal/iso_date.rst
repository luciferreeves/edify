ISO date
========

**ISO date** matches the calendar date form of
`ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`__ — exactly
``YYYY-MM-DD``, with no alternatives. It is the format to require in an API or a
data file, because it sorts lexicographically and carries no regional ambiguity.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(4)``
:meth:`~edify.RegexBuilder.digit`, ``-``, two digits, ``-``, two digits, anchored end
to end.

Calendar dates
--------------

.. edify-playground::

   from edify.library import iso_date

   iso_date("2024-01-15")
   iso_date("1999-12-31")
   iso_date("2024-02-29")     # a real leap day

Zero-padding is required
------------------------

The fixed widths are what make the format sortable, so a single-digit month or day
fails:

.. edify-playground::

   from edify.library import iso_date

   iso_date("2024-01-05")   # padded
   iso_date("2024-1-5")     # unpadded
   iso_date("20240115")     # the basic format, without hyphens
   iso_date("15-01-2024")   # a different order

Date only
---------

A time component belongs to :doc:`datetime`:

.. edify-playground::

   from edify.library import iso_date

   iso_date("2024-01-15")              # date only
   iso_date("2024-01-15T10:30:00Z")    # a datetime
   iso_date("")                        # empty

The important caveat: this checks digits and separators, not the calendar.
``2024-02-31`` and ``2023-02-29`` both match despite not existing, and month ``13``
would too — parse the value to confirm it is real. For regional layouts see
:doc:`date`.
