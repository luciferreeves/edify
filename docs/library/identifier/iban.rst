IBAN
====

An `IBAN <https://www.iso.org/standard/81090.html>`__ identifies a bank account
internationally: a two-letter country code, two check digits, then the national
account identifier. **IBAN** matches that structure.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(2)``
:meth:`~edify.RegexBuilder.uppercase`, two :meth:`~edify.RegexBuilder.digit`
characters, then :meth:`~edify.RegexBuilder.between`\ ``(1, 30)`` uppercase
alphanumerics — a span wide enough for every national length.

Account numbers
---------------

Lengths differ by country, from 15 characters to 34:

.. edify-playground::

   from edify.library import iban

   iban("GB82WEST12345698765432")        # United Kingdom
   iban("DE89370400440532013000")        # Germany
   iban("FR1420041010050500013M02606")   # France, with a letter
   iban("NO9386011117947")               # Norway, the shortest

Country code and check digits
-----------------------------

.. edify-playground::

   from edify.library import iban

   iban("GB82WEST12345698765432")   # valid shape
   iban("gb82WEST12345698765432")   # lowercase country code
   iban("GBXXWEST12345698765432")   # check digits must be numeric
   iban("GB82")                     # no account identifier
   iban("")                         # empty

The two digits after the country code are a **mod-97 checksum** over the whole
number, and this cannot compute it — ``GB00WEST12345698765432`` matches and is
invalid. Run the mod-97 check before initiating a transfer; it is the whole reason
those digits exist. Spaces are also often used for display and must be stripped
first. For the bank itself see :doc:`bic`.
