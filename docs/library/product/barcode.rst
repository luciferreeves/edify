Barcode
=======

**Barcode** matches the payload a `barcode <https://en.wikipedia.org/wiki/Barcode>`__
scanner returns — 6 to 48 uppercase alphanumeric characters. It is deliberately
broader than :doc:`gtin`, because symbologies such as Code 39 and Code 128 encode
letters as well as digits.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(6, 48)`` over an
:meth:`~edify.RegexBuilder.any_of` class of uppercase letters and digits.

Scanned payloads
----------------

.. edify-playground::

   from edify.library import barcode

   barcode("012345678905")     # a numeric UPC payload
   barcode("1234567890128")    # an EAN payload
   barcode("ABC123XYZ")        # an alphanumeric Code 39 payload
   barcode("SN2024001")        # a serial number

Uppercase alphanumeric only
---------------------------

.. edify-playground::

   from edify.library import barcode

   barcode("ABC123")     # valid
   barcode("abc123")     # lowercase
   barcode("ABC-123")    # punctuation
   barcode("12345")      # too short
   barcode("")           # empty

This matches the decoded characters, not the symbology — it cannot tell you which
kind of barcode produced them, and Code 128 in particular can encode punctuation this
rejects. For the standardised trade-item number see :doc:`gtin`.
