TIN
===

A `taxpayer identification number <https://www.irs.gov/individuals/international-taxpayers/taxpayer-identification-numbers-tin>`__
is whichever US tax identifier applies — an :doc:`ssn` for an individual, an
:doc:`ein` for a business, or an :doc:`itin` for a foreign filer. **TIN** accepts any
of them, which makes it the validator for a field that takes "your tax ID".

The forms are the branches of an :func:`~edify.any_of`, each carrying the same
exclusions as its dedicated validator — including the never-issued SSN ranges.

Any of the three forms
----------------------

.. edify-playground::

   from edify.library import tin

   tin("123-45-6789")   # an SSN
   tin("12-3456789")    # an EIN
   tin("912-70-1234")   # an ITIN

Exclusions still apply
----------------------

Accepting several forms does not mean accepting anything:

.. edify-playground::

   from edify.library import tin

   tin("123-45-6789")   # issuable
   tin("000-45-6789")   # a never-issued SSN area
   tin("666-45-6789")   # likewise
   tin("123456789")     # hyphens are required
   tin("")              # empty

Because the branches overlap in shape, a match does not tell you *which* kind of
identifier you have — check the grouping yourself if the distinction matters. All
three are sensitive: collect and retain them only where legally required.
