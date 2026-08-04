Offset
======

A `UTC offset <https://en.wikipedia.org/wiki/UTC_offset>`__ says how far a local
time sits from Coordinated Universal Time — ``+05:30``, ``-08:00`` — or names UTC
itself with ``Z``. **Offset** matches both, with the colon optional.

The construction is an :func:`~edify.any_of`: a sign, hours range-checked to
``00``–``14``, an :meth:`~edify.RegexBuilder.optional` colon, and minutes
range-checked to ``00``–``59``; or the literal ``Z``.

Signed offsets
--------------

.. edify-playground::

   from edify.library import offset

   offset("+05:30")   # India
   offset("-08:00")   # US Pacific
   offset("+00:00")   # UTC written as an offset
   offset("+0530")    # without the colon
   offset("+14:00")   # the maximum in use

UTC
---

.. edify-playground::

   from edify.library import offset

   offset("Z")        # the UTC designator
   offset("+00:00")   # the equivalent offset

Range and sign are enforced
---------------------------

.. edify-playground::

   from edify.library import offset

   offset("+14:00")   # in range
   offset("+15:00")   # beyond the maximum
   offset("+05:60")   # minutes out of range
   offset("05:30")    # no sign
   offset("")         # empty

An offset is not a time zone: it is a fixed displacement, while a zone carries the
rules that change the offset across the year. Storing ``-08:00`` loses the
information that the zone shifts to ``-07:00`` in summer — keep the zone name for
future dates. See :doc:`timezone`.
