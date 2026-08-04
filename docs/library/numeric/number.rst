Number
======

**Number** is the broadest numeric validator: it matches any decimal a program would
parse as a `floating-point value <https://en.wikipedia.org/wiki/Floating-point_arithmetic>`__ — integers, fractional values, leading-dot forms, and anything with
an exponent.

The forms are the branches of an :func:`~edify.any_of`, each allowing an optional
leading sign: a bare integer, ``digits.digits``, a leading ``.digits``, and the
exponent variants of each.

Integers and decimals
---------------------

.. edify-playground::

   from edify.library import number

   number("42")      # an integer is a number
   number("-3.5")    # negative decimal
   number("+7")      # explicit plus
   number("0.5")     # leading zero
   number(".5")      # the leading-dot form

Exponents
---------

Scientific notation in either case, with a signed or unsigned exponent:

.. edify-playground::

   from edify.library import number

   number("1.2e9")     # lowercase e
   number("1.2E-9")    # uppercase, negative exponent
   number("1e5")       # no fractional part
   number("6.022e23")

Not numbers
-----------

Separators, trailing dots, and text all fail:

.. edify-playground::

   from edify.library import number

   number("42")       # valid
   number("1,000")    # a thousands separator
   number("1.2.3")    # two decimal points
   number("abc")      # text
   number("")         # empty

This validates notation, not magnitude — a value may match and still overflow the
type you parse it into, and ``0.1`` is exactly representable here but not in binary
floating point. For whole numbers see :doc:`integer`; to *require* an exponent,
:doc:`scientific`.
