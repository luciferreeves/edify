Bearing
=======

A `bearing <https://en.wikipedia.org/wiki/Bearing_(navigation)>`__ is a compass
direction in degrees, from 0 through 360. **Bearing** range-checks the value and
allows an optional ``°`` symbol.

The construction is an :func:`~edify.any_of` handling 360 as a special case, then the
300s, 100s–200s, and one- or two-digit values — which together enforce the upper
bound without arithmetic. A fractional part is optional.

Degrees around the compass
--------------------------

.. edify-playground::

   from edify.library import bearing

   bearing("0")       # north
   bearing("90")      # east
   bearing("180")     # south
   bearing("270")     # west
   bearing("360")     # north again
   bearing("90.5")    # fractional degrees
   bearing("45°")     # with the degree symbol

The range is enforced
---------------------

.. edify-playground::

   from edify.library import bearing

   bearing("360")     # the maximum
   bearing("361")     # past it
   bearing("-90")     # negative bearings are not used
   bearing("")        # empty

One thing to watch: zero-padded forms such as ``045`` — common in aviation, where
bearings are always spoken as three digits — are **not** matched, because the pattern
treats a leading zero as a different number. Strip padding before validating. Note
also that 0 and 360 both name north.
