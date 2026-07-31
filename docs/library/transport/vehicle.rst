Vehicle
=======

A `vehicle identification number <https://en.wikipedia.org/wiki/Vehicle_identification_number>`__
is the 17-character serial that uniquely identifies a road vehicle. **Vehicle**
matches an uppercase alphanumeric run of that shape, allowing hyphens and spaces
where a record has them.

The construction is a leading uppercase alphanumeric then
:meth:`~edify.RegexBuilder.between`\ ``(3, 17)`` over an
:meth:`~edify.RegexBuilder.any_of` class of uppercase alphanumerics, ``-``, and
space.

Identification numbers
----------------------

.. edify-playground::

   from edify.library import vehicle

   vehicle("1HGBH41JXMN109186")   # a 17-character VIN
   vehicle("JH4TB2H26CC000000")
   vehicle("WBA3A5C55DF123456")

Uppercase alphanumeric
----------------------

.. edify-playground::

   from edify.library import vehicle

   vehicle("1HGBH41JXMN109186")   # valid
   vehicle("abc")                  # lowercase and too short
   vehicle("1HG")                  # too short
   vehicle("")                     # empty

Two real limitations. A VIN excludes the letters ``I``, ``O``, and ``Q`` to avoid
digit confusion, and this does not enforce that — so ``IOQ``-bearing strings match.
And position 9 is a computed check digit that a pattern cannot verify. Run the VIN
checksum before trusting one, and decode it to confirm the manufacturer and year.
