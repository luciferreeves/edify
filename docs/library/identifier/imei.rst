IMEI
====

An `IMEI <https://en.wikipedia.org/wiki/International_Mobile_Equipment_Identity>`__
identifies a mobile device on a cellular network. It is exactly 15 digits, and
**IMEI** matches that.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(15)``
:meth:`~edify.RegexBuilder.digit`, anchored end to end.

Device identifiers
------------------

.. edify-playground::

   from edify.library import imei

   imei("490154203237518")
   imei("356938035643809")
   imei("000000000000000")   # shape-valid

Exactly fifteen digits
----------------------

.. edify-playground::

   from edify.library import imei

   imei("490154203237518")    # fifteen
   imei("49015420323751")     # fourteen
   imei("4901542032375189")   # sixteen: that is an IMEISV
   imei("49015420323751a")    # a letter
   imei("")                   # empty

The final digit is a Luhn check digit that this cannot compute, so a mistyped IMEI
will still match — run the checksum. The 16-digit IMEISV, which appends a software
version, is a different identifier and is not matched here. For the SIM rather than
the handset see :doc:`iccid`; for CDMA devices, :doc:`meid`.
