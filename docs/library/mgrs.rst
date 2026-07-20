mgrs
====

**Geo** · :doc:`Back to the library <index>`

A Military Grid Reference System coordinate.

.. code-block:: python

   from edify.library import mgrs

   mgrs('1CAB12')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 1CAB12|23JBC2345

   from edify.library import mgrs
   mgrs

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{1,2}[C-HJ-NP-X][A-Z]{2}(?:\d{2}|\d{4}|\d{6}|\d{8}|\d{10})$

How it reads
------------

.. code-block:: text

   - The text must start with between 1 and 2 digits (0-9).
   - Then the text must have either one character from "C" through "H", one character from "J" through "N", or one character from "P" through "X".
   - Then the text must have exactly 2 uppercase letters (A-Z).
   - Then the text must have either exactly 2 digits (0-9), exactly 4 digits (0-9), exactly 6 digits (0-9), exactly 8 digits (0-9), or exactly 10 digits (0-9).

See the other validators in the :doc:`library <index>`.
