Scientific
==========

**Scientific** matches a number in
`scientific notation <https://en.wikipedia.org/wiki/Scientific_notation>`__ — a
mantissa followed by a mandatory exponent. That requirement is the whole point: it
is :doc:`number` narrowed to values that *must* carry an ``e``.

The construction is an optional sign, digits, an
:meth:`~edify.RegexBuilder.optional` fractional part, then an
:meth:`~edify.RegexBuilder.any_of_chars` over ``e``/``E``, an optional exponent
sign, and one or more digits.

Mantissa and exponent
---------------------

.. edify-playground::

   from edify.library import scientific

   scientific("1.2e9")      # lowercase exponent marker
   scientific("1.2E-9")     # uppercase, negative exponent
   scientific("1e5")        # no fractional part
   scientific("6.022e23")   # Avogadro's number
   scientific("-1.6e-19")   # signed mantissa and exponent

The exponent is required
------------------------

This is what separates it from :doc:`number`:

.. edify-playground::

   from edify.library import scientific

   scientific("1.2e9")   # has an exponent
   scientific("1.2")     # a plain decimal: use number
   scientific("42")      # a plain integer
   scientific("1.2e")    # no exponent digits
   scientific("abc")     # text

Use this when a field must be written in normalised form — instrument readings and
scientific data exports, where a bare decimal usually signals a formatting mistake.
For any decimal see :doc:`number`.
