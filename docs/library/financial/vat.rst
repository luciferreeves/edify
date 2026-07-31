VAT
===

A `VAT number <https://en.wikipedia.org/wiki/VAT_identification_number>`__ identifies
a business registered for value-added tax. It opens with a two-letter country prefix
followed by the national registration digits, and **VAT** matches that shape.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(2)``
:meth:`~edify.RegexBuilder.uppercase` then
:meth:`~edify.RegexBuilder.between`\ ``(6, 12)`` :meth:`~edify.RegexBuilder.digit` —
a span wide enough to cover the differing national lengths.

Country prefix and digits
-------------------------

.. edify-playground::

   from edify.library import vat

   vat("GB123456789")     # United Kingdom
   vat("DE123456789")     # Germany
   vat("FR12345678901")   # France
   vat("IE1234567")       # Ireland, a shorter number

The prefix is required
----------------------

.. edify-playground::

   from edify.library import vat

   vat("GB123456789")   # prefixed
   vat("123456789")     # no country code
   vat("gb123456789")   # lowercase prefix
   vat("GB12345")       # too few digits
   vat("")              # empty

Two real limitations. Several countries include letters in the national part —
Ireland's ``IE1234567FA`` among them — and those are not matched here. And each
country has its own check-digit algorithm, none of which a pattern can run: confirm a
number against the VIES service before relying on it for tax treatment.
