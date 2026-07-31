Numeric
=======

**Numeric** matches a non-empty run of
`decimal digits <https://en.wikipedia.org/wiki/Numerical_digit>`__ — the check for a field that
holds digits *as text*, such as an account number, a zero-padded code, or an
identifier where the leading zeros matter.

The construction is :meth:`~edify.RegexBuilder.one_or_more`
:meth:`~edify.RegexBuilder.digit`, anchored end to end. There is no sign, no decimal
point, and no separator — those belong to the :doc:`../numeric/index` category.

Digit strings
-------------

.. edify-playground::

   from edify.library import numeric

   numeric("12345")      # a plain run
   numeric("007")        # leading zeros are preserved
   numeric("0")          # a single digit
   numeric("9" * 40)     # any length

Digits and nothing else
-----------------------

Signs, decimal points, separators, and whitespace all fall outside:

.. edify-playground::

   from edify.library import numeric

   numeric("12345")     # digits only
   numeric("-12345")    # a sign
   numeric("123.45")    # a decimal point
   numeric("1,234")     # a thousands separator
   numeric("12 345")    # a space
   numeric("")          # empty

Use this when the value is *text that happens to be digits* — the distinction
matters, because converting to a number would destroy the leading zeros. For actual
numbers with signs and decimals see :doc:`../numeric/integer` and
:doc:`../numeric/number`; for letters and digits together, :doc:`alphanumeric`.
