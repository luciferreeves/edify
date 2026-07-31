MMSI
====

An `MMSI <https://www.itu.int/en/ITU-R/terrestrial/fmd/Pages/mmsi.aspx>`__ identifies
a ship's radio station — the number transmitted by AIS and used for digital selective
calling. It is nine digits, and **MMSI** matches that.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(9)``
:meth:`~edify.RegexBuilder.digit`, anchored end to end.

Radio identifiers
-----------------

.. edify-playground::

   from edify.library import mmsi

   mmsi("235760000")   # a UK-flagged vessel
   mmsi("366123456")   # a US-flagged vessel
   mmsi("000000000")   # shape-valid

Exactly nine digits
-------------------

.. edify-playground::

   from edify.library import mmsi

   mmsi("235760000")    # nine digits
   mmsi("23576000")     # eight
   mmsi("2357600000")   # ten
   mmsi("23576000a")    # a letter
   mmsi("")             # empty

The first three digits are a Maritime Identification Digit code identifying the flag
state, which this does not validate. An MMSI is reassigned when a vessel changes flag
or owner, so it is not a permanent identity — the :doc:`imo` number is. Note also
that this shape is identical to a US bank :doc:`../financial/routing` number;
context decides which you have.
