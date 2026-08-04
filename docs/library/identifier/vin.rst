VIN
===

A `VIN <https://en.wikipedia.org/wiki/Vehicle_identification_number>`__ is the
17-character identifier stamped on a road vehicle. **VIN** is stricter than the
:doc:`../transport/vehicle` validator: it enforces the alphabet exactly, excluding
the three letters the standard forbids.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(17)`` over an
:meth:`~edify.RegexBuilder.any_of` class built from
:meth:`~edify.RegexBuilder.range` runs that skip ``I``, ``O``, and ``Q`` — omitted
because they are too easily confused with ``1`` and ``0``.

Vehicle numbers
---------------

.. edify-playground::

   from edify.library import vin

   vin("1HGBH41JXMN109186")
   vin("JH4TB2H26CC000000")
   vin("WBA3A5C55DF123456")

The forbidden letters
---------------------

This is what makes it stricter than a plain alphanumeric check:

.. edify-playground::

   from edify.library import vin

   vin("1HGBH41JXMN109186")   # valid alphabet
   vin("1HGBH41IXMN109186")   # I is not permitted
   vin("1HGBH41OXMN109186")   # O is not permitted
   vin("1HGBH41QXMN109186")   # Q is not permitted

Exactly seventeen
-----------------

.. edify-playground::

   from edify.library import vin

   vin("1HGBH41JXMN109186")    # seventeen
   vin("1HGBH41JXMN10918")     # sixteen
   vin("1HGBH41JXMN1091866")   # eighteen
   vin("")                     # empty

Position 9 is a computed check digit that this cannot verify — decode the VIN to
confirm it, and to read the manufacturer, model year, and plant. For the laxer
transport-oriented check see :doc:`../transport/vehicle`.
