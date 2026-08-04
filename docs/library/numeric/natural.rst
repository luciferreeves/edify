Natural
=======

**Natural** matches a `natural number <https://en.wikipedia.org/wiki/Natural_number>`__
in the strict sense — a positive whole number, with no sign, no zero, and no leading
zeros. It is the check for a quantity, a page number, or a one-based index.

The construction is a single :meth:`~edify.RegexBuilder.range` from ``1`` to ``9``
followed by :meth:`~edify.RegexBuilder.zero_or_more`
:meth:`~edify.RegexBuilder.digit`. Requiring a non-zero first digit is what
excludes both ``0`` and padded forms in one stroke.

Positive whole numbers
----------------------

.. edify-playground::

   from edify.library import natural

   natural("1")       # the smallest natural number
   natural("42")
   natural("1000000") # any magnitude

Zero and signs excluded
-----------------------

.. edify-playground::

   from edify.library import natural

   natural("42")    # positive
   natural("0")     # zero is not included
   natural("-42")   # no sign is permitted
   natural("+42")   # not even a plus

No leading zeros
----------------

A padded value is a *string* that looks numeric rather than a natural number:

.. edify-playground::

   from edify.library import natural

   natural("7")     # canonical
   natural("007")   # padded
   natural("")      # empty

Whether zero counts as natural is a genuine convention split — this validator takes
the "counting numbers" side. If you need zero included, use :doc:`integer` and check
the sign yourself.
