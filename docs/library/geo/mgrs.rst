MGRS
====

The `Military Grid Reference System <https://en.wikipedia.org/wiki/Military_Grid_Reference_System>`__
names a position by grid square: a UTM zone number, a latitude band letter, a
two-letter square identifier, then an even number of digits giving easting and
northing. **MGRS** matches that structure.

The construction is 1–2 :meth:`~edify.RegexBuilder.digit` characters, a band letter
from a :meth:`~edify.RegexBuilder.range` that **excludes** ``I`` and ``O`` — they are
omitted to avoid confusion with 1 and 0 — then two letters, then an
:func:`~edify.any_of` over the even digit counts from 2 to 10.

Grid references at each precision
---------------------------------

Each pair of digits refines the position tenfold:

.. edify-playground::

   from edify.library import mgrs

   mgrs("33UXP0450106400")   # 10 digits: one-metre precision
   mgrs("4QFJ1267")          # 8 digits
   mgrs("33UXP04")           # 4 digits
   mgrs("18SUJ23")           # a coarser reference

Structure is enforced
---------------------

.. edify-playground::

   from edify.library import mgrs

   mgrs("4QFJ1267")     # valid
   mgrs("4QFJ123")      # an odd number of digits
   mgrs("4IFJ1267")     # I is not a band letter
   mgrs("QFJ1267")      # no zone number
   mgrs("")             # empty

The odd-digit rejection is meaningful: easting and northing must have equal digits, so
an odd count is always a transcription error. The zone and band are not cross-checked
for consistency, though — decode the reference to confirm it names a real square.
