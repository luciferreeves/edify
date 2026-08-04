Coordinate
==========

**Coordinate** matches a decimal
`latitude and longitude <https://en.wikipedia.org/wiki/Geographic_coordinate_system>`__
pair — ``40.7128,-74.0060``. Both halves are range-checked, which is unusual among
these validators and genuinely useful: latitude stops at ±90, longitude at ±180.

Each half is an :func:`~edify.any_of` over the boundary value and the values below
it, so the bounds are enforced by construction. The comma may carry whitespace on
either side.

Coordinate pairs
----------------

.. edify-playground::

   from edify.library import coordinate

   coordinate("40.7128,-74.0060")     # New York
   coordinate("40.7128, -74.0060")    # with a space
   coordinate("-33.8688,151.2093")    # Sydney
   coordinate("0,0")                  # null island
   coordinate("90,180")               # the extremes

The ranges are enforced
-----------------------

.. edify-playground::

   from edify.library import coordinate

   coordinate("90,180")     # at the limits
   coordinate("91,0")       # latitude out of range
   coordinate("0,181")      # longitude out of range
   coordinate("-90.1,0")    # below the southern limit

Decimal degrees only
--------------------

Degrees-minutes-seconds notation is a different format:

.. edify-playground::

   from edify.library import coordinate

   coordinate("40.7128,-74.0060")        # decimal
   coordinate("40°42'46\"N 74°00'21\"W")  # DMS
   coordinate("40.7128")                  # only one value
   coordinate("")                         # empty

Order matters and is not checkable: ``lat,lon`` is the convention here, but many
mapping APIs take ``lon,lat``, and a swapped pair is often still in range. Confirm
the order at the boundary of your system.
