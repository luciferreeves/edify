sku
===

**Identifiers** · :doc:`Back to the library <index>`

A stock-keeping unit code.

.. code-block:: python

   from edify.library import sku

   sku('Aa0/')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: Aa0/|a0/Aa

   from edify.library import sku
   sku

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Za-z0-9-_./]{4,20}$

How it reads
------------

.. code-block:: text

   - The text must start with between 4 and 20 of either one character from "A" through "Z", one character from "a" through "z", one character from "0" through "9", or one character from the set "-_./".

See the other validators in the :doc:`library <index>`.
