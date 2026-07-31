GTIN
====

A `GTIN <https://www.gs1.org/standards/id-keys/gtin>`__ identifies a trade item. It
comes in four lengths — 8, 12, 13, and 14 digits — which correspond to the older
regional schemes (UPC-E, UPC-A, EAN-13) folded into one standard. **GTIN** matches
all four.

The construction is an :func:`~edify.any_of` over
:meth:`~edify.RegexBuilder.exactly` digit counts of 8, 12, 13, and 14. No separators:
a GTIN is a bare digit run.

The four lengths
----------------

.. edify-playground::

   from edify.library import gtin

   gtin("12345670")         # GTIN-8
   gtin("012345678905")     # GTIN-12, a UPC-A
   gtin("4006381333931")    # GTIN-13, an EAN-13
   gtin("00012345600012")   # GTIN-14, a case code

Only those lengths
------------------

The length *is* the format, so anything else is not a GTIN:

.. edify-playground::

   from edify.library import gtin

   gtin("012345678905")   # twelve digits
   gtin("1234567")        # seven
   gtin("12345678901")    # eleven
   gtin("012345-678905")  # separators are not part of a GTIN
   gtin("")               # empty

Every GTIN carries a modulo-10 check digit that this cannot compute — ``12345678``
matches and is almost certainly not a real item. Run the checksum, then look the
number up: a valid GTIN still says nothing about which product it identifies. For the
scanned payload see :doc:`barcode`.
