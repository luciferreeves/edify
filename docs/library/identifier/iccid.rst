ICCID
=====

An `ICCID <https://en.wikipedia.org/wiki/SIM_card#ICCID>`__ identifies a SIM card
itself — as opposed to the handset it sits in, which is an :doc:`imei`. It is 19 to
22 digits, and **ICCID** matches that range.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(19, 22)``
:meth:`~edify.RegexBuilder.digit`. The range covers the 19- and 20-digit forms in
common use plus the padding some carriers add.

SIM identifiers
---------------

.. edify-playground::

   from edify.library import iccid

   iccid("8901260123456789012")      # 19 digits
   iccid("89012601234567890123")     # 20 digits
   iccid("8901260123456789012345")   # 22 digits

Within range, digits only
-------------------------

.. edify-playground::

   from edify.library import iccid

   iccid("8901260123456789012")       # in range
   iccid("890126012345678901")        # eighteen: too short
   iccid("89012601234567890123456")   # twenty-three: too long
   iccid("8901260123456789012a")      # a letter
   iccid("")                          # empty

An ICCID begins ``89`` for telecommunications under the ISO/IEC 7812 scheme, and ends
with a Luhn check digit — neither is enforced here. A SIM identifier is linked to a
subscriber, so treat it as personal data. For the device see :doc:`imei`.
