ISIN
====

An `ISIN <https://www.isin.org/>`__ identifies a security internationally: a
two-letter country code, a nine-character national identifier, and a final check
digit. **ISIN** matches that 12-character structure.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(2)``
:meth:`~edify.RegexBuilder.uppercase`, nine uppercase alphanumerics, then a single
:meth:`~edify.RegexBuilder.digit` — the check digit is always numeric, which the
pattern does enforce.

Security identifiers
--------------------

.. edify-playground::

   from edify.library import isin

   isin("US0378331005")   # Apple
   isin("GB0002634946")   # BAE Systems
   isin("DE000BAY0017")   # Bayer, with letters in the national part
   isin("XS1234567890")   # an international issue

The structure is fixed
----------------------

.. edify-playground::

   from edify.library import isin

   isin("US0378331005")   # valid shape
   isin("us0378331005")   # lowercase country code
   isin("US037833100A")   # the check digit must be numeric
   isin("US03783310")     # too short
   isin("")               # empty

The final digit is a Luhn checksum over the whole identifier, and this cannot compute
it — ``US0378331006`` matches and is invalid. Run the checksum before trading on an
identifier. For the national schemes an ISIN wraps see :doc:`cusip` and
:doc:`sedol`.
