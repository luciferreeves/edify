Geohash
=======

A `geohash <https://en.wikipedia.org/wiki/Geohash>`__ encodes a position as a short
string, with a useful property: nearby places share a prefix, so proximity becomes
string comparison. **Geohash** matches 1 to 12 characters of its base-32 alphabet.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(1, 12)`` over an
:meth:`~edify.RegexBuilder.any_of` class of digits and lowercase letters **excluding**
``a``, ``i``, ``l``, and ``o`` — the geohash alphabet omits them to avoid visual
confusion.

Hashes at any precision
-----------------------

Each character roughly quarters the area, so length is precision:

.. edify-playground::

   from edify.library import geohash

   geohash("u4pruydqqvj")   # a precise location
   geohash("9q8yy")         # a neighbourhood
   geohash("9q")            # a large region
   geohash("u")             # a continent-sized cell

The restricted alphabet
-----------------------

.. edify-playground::

   from edify.library import geohash

   geohash("9q8yy")          # valid characters
   geohash("aiou")           # a, i, l, o are excluded
   geohash("U4PRUY")         # uppercase
   geohash("u4pruydqqvjxyz") # longer than twelve
   geohash("")               # empty

A geohash names a *cell*, not a point, so two nearby places can fall either side of a
cell boundary and share no prefix at all — the prefix trick is a useful heuristic
rather than a distance function. For an exact position see :doc:`coordinate`.
