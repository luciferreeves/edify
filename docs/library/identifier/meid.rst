MEID
====

A `MEID <https://en.wikipedia.org/wiki/Mobile_equipment_identifier>`__ identifies a
CDMA mobile device — the counterpart to the :doc:`imei` used on GSM networks. It is
14 hexadecimal characters, and **MEID** matches that.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(14)`` over an
:meth:`~edify.RegexBuilder.any_of` class of digits and uppercase ``A``–``F``.

Device identifiers
------------------

.. edify-playground::

   from edify.library import meid

   meid("A0000012345678")
   meid("99000012345678")
   meid("FFFFFFFFFFFFFF")

Uppercase hex, exactly fourteen
-------------------------------

.. edify-playground::

   from edify.library import meid

   meid("A0000012345678")    # fourteen characters
   meid("a0000012345678")    # lowercase
   meid("A000001234567")     # thirteen
   meid("A00000123456789")   # fifteen: that is an IMEI length
   meid("")                  # empty

The MEID has an optional 15th check digit that is normally omitted in transmission
and is not accepted here. For GSM devices see :doc:`imei`; for the SIM,
:doc:`iccid`.
