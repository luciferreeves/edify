Geo
===

Positions on the earth and the notations that describe them — coordinates, grid
references, bearings, and postal codes. Each validator is a callable
:class:`~edify.Pattern`: import it, call it with a string, get a ``bool``.

.. code-block:: python

   from edify.library import coordinate, geohash, bearing

   coordinate("40.7128,-74.0060")   # True
   geohash("u4pruydqqvj")           # True
   bearing("90.5")                  # True

.. toctree::
   :hidden:

   altitude
   bearing
   coordinate
   geohash
   mgrs
   place
   plus
   postal

Positions
---------

- :doc:`coordinate` — a decimal latitude and longitude pair.
- :doc:`geohash` — a position encoded as a short string.
- :doc:`plus` — an Open Location Code; :doc:`mgrs` — a military grid reference.

Direction and height
--------------------

- :doc:`bearing` — a compass bearing in degrees.
- :doc:`altitude` — a height with an optional unit.

Names and codes
---------------

- :doc:`place` — a settlement name; :doc:`postal` — an international postal code.
