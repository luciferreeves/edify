Fraction
========

**Fraction** matches a written
`fraction <https://en.wikipedia.org/wiki/Fraction>`__ — a numerator over a
denominator, optionally negative, and optionally preceded by a whole number to form
a mixed number such as ``1 1/2``.

The construction is an :meth:`~edify.RegexBuilder.optional` ``-``, an optional
whole-number part followed by whitespace, then digits, ``/``, and digits.

Simple and mixed
----------------

.. edify-playground::

   from edify.library import fraction

   fraction("1/2")      # a simple fraction
   fraction("10/3")     # improper
   fraction("-3/4")     # negative
   fraction("1 1/2")    # a mixed number
   fraction("2 3/4")

Whole numbers only
------------------

Both parts are integers — a decimal inside a fraction is not a written fraction:

.. edify-playground::

   from edify.library import fraction

   fraction("1/2")      # valid
   fraction("1.5/2")    # a decimal numerator
   fraction("1/2.5")    # a decimal denominator
   fraction("½")        # the Unicode character, not a written fraction
   fraction("")         # empty

Zero denominators pass
----------------------

The pattern checks shape, not arithmetic, so a division by zero is well formed:

.. edify-playground::

   from edify.library import fraction

   fraction("1/0")   # syntactically fine, mathematically undefined
   fraction("0/5")   # a legitimate zero value

Guard against a zero denominator yourself before evaluating. For the ``a:b`` form
see :doc:`ratio`; for a decimal value, :doc:`number`.
