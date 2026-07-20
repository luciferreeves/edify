icao
====

**Identifiers** · :doc:`Back to the library <index>`

An ICAO airport code.

.. code-block:: python

   from edify.library import icao

   icao('AAA')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: AAA|AAAA

   from edify.library import icao
   icao

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z]{3,4}$

How it reads
------------

.. code-block:: text

   - The text must start with between 3 and 4 of one character from "A" through "Z".

See the other validators in the :doc:`library <index>`.
