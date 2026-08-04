Year
====

**Year** matches a four-digit `calendar year <https://en.wikipedia.org/wiki/Year>`__
— ``2024``, ``1999`` — the form used in dates, copyright notices, and model years.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(4)``
:meth:`~edify.RegexBuilder.digit`, anchored end to end. Four digits exactly: no
two-digit shorthand, no sign, no era suffix.

Four-digit years
----------------

.. edify-playground::

   from edify.library import year

   year("2024")
   year("1999")
   year("0001")   # any four-digit value
   year("9999")

Exactly four digits
-------------------

.. edify-playground::

   from edify.library import year

   year("2024")    # four digits
   year("24")      # the two-digit shorthand
   year("12345")   # five digits
   year("2024 AD") # an era suffix
   year("")        # empty

Rejecting the two-digit form is deliberate: ``24`` could mean 1924 or 2024, and
guessing is how the year-2000 problem happened. The range is not bounded to plausible
years either — ``0001`` and ``9999`` both match, so apply your own bounds if the
field is a birth year or a model year. For a full date see :doc:`iso_date`.
