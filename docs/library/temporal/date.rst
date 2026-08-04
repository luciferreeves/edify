Date
====

Where :doc:`iso_date` accepts one canonical layout, **Date** accepts the several
`written forms <https://en.wikipedia.org/wiki/Date_format_by_country>`__ people
actually use — slashes, hyphens, dots, and the compact digit run — in both
day-first and year-first orders.

The layouts are the branches of an :func:`~edify.any_of`: ``M/D/YYYY``,
``YYYY-MM-DD``, ``DD-MM-YYYY``, ``YYYY/MM/DD``, ``D.M.YYYY``, ``YYYY.MM.DD``, and
the eight-digit basic form.

Regional layouts
----------------

.. edify-playground::

   from edify.library import date

   date("2024-01-15")    # ISO order
   date("01/15/2024")    # month first
   date("15-01-2024")    # day first
   date("2024/01/15")    # slashes, year first
   date("15.01.2024")    # dots, common in Europe
   date("20240115")      # the compact basic form

Recognised separators only
--------------------------

.. edify-playground::

   from edify.library import date

   date("2024-01-15")     # valid
   date("Jan 15, 2024")   # a written month name
   date("2024-1-5")       # unpadded in a padded layout
   date("")               # empty

The ambiguity is the point to be careful about: ``01/02/2024`` matches, and whether
it means 1 February or 2 January depends on a convention this pattern cannot know.
Accepting many layouts means you must decide the order elsewhere — which is exactly
why :doc:`iso_date` is the better choice for machine interfaces. As there, the
calendar is not checked: ``2024-02-31`` still matches.
