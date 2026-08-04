Sort code
=========

A `sort code <https://en.wikipedia.org/wiki/Sort_code>`__ identifies a UK bank
branch. It is six digits, conventionally written in three hyphenated pairs —
``12-34-56`` — and **Sort code** accepts both that form and the bare digits.

The two forms are the branches of an :func:`~edify.any_of`, each separately anchored:
three pairs joined by hyphens, or six digits with no separators.

Both written forms
------------------

.. edify-playground::

   from edify.library import sortcode

   sortcode("12-34-56")   # the conventional form
   sortcode("123456")     # bare digits
   sortcode("00-00-00")   # shape-valid

Exactly six digits
------------------

The hyphens are all-or-nothing — a partially separated code is not a recognised form:

.. edify-playground::

   from edify.library import sortcode

   sortcode("12-34-56")   # fully separated
   sortcode("1234-56")    # partially
   sortcode("12 34 56")   # spaces instead of hyphens
   sortcode("12345")      # too few digits
   sortcode("")           # empty

Sort codes have no check digit, so shape is genuinely all you can verify offline —
validity requires a bank reference table, and a payment needs the account number
alongside. For the US equivalent see :doc:`routing`.
