Dosage
======

**Dosage** matches a `medication amount <https://en.wikipedia.org/wiki/Dose_(biochemistry)>`__
— a number, a unit, and optionally a rate such as ``/day`` or ``/kg``.

The construction is digits with an optional fractional part, optional whitespace, a
unit from an :func:`~edify.any_of` — ``mg``, ``kg``, ``ml``, ``mcg``, ``iu``, ``g``,
``l`` — and an :meth:`~edify.RegexBuilder.optional` ``/`` plus ``kg``, ``day``, or
``dose``.

Amounts and units
-----------------

.. edify-playground::

   from edify.library import dosage

   dosage("500mg")
   dosage("5 ml")        # with a space
   dosage("0.5mg")       # fractional
   dosage("250mcg")      # micrograms
   dosage("1000iu")      # international units

Rates
-----

.. edify-playground::

   from edify.library import dosage

   dosage("5mg/kg")      # weight-based
   dosage("500mg/day")   # daily total
   dosage("10ml/dose")   # per administration

A known unit is required
------------------------

.. edify-playground::

   from edify.library import dosage

   dosage("500mg")      # a known unit
   dosage("2 tablets")  # a dose form, not a unit
   dosage("500")        # no unit
   dosage("")           # empty

A dosage that matches can still be wrong, and in this domain wrong is dangerous:
``500mg`` and ``500mcg`` differ by a factor of a thousand and both match here.
Nothing about the shape catches a decimal-point error or a unit confusion, so
dosages need clinical range checks, not pattern matching, before they reach a
patient.
