geohash
=======

**Geo** · :doc:`Back to the library <index>`

A geohash string.

.. code-block:: python

   from edify.library import geohash

   geohash('u4pruydqqvj')   # True
   geohash('!!!')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: u4pruydqqvj|gbsuv7ztq|!!!

   from edify.library import geohash
   geohash

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[0-9bcdefghjkmnpqrstuvwxyz]{1,12}$

How it reads
------------

.. code-block:: text

   - The text must start with between 1 and 12 of either one character from "0" through "9" or one character from the set "bcdefghjkmnpqrstuvwxyz".

See the other validators in the :doc:`library <index>`.
