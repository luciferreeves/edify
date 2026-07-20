vin
===

**Identifiers** · :doc:`Back to the library <index>`

A vehicle identification number.

.. code-block:: python

   from edify.library import vin

   vin('1HGCM82633A004352')   # True
   vin('short')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 1HGCM82633A004352|short|12345

   from edify.library import vin
   vin

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-HJ-NPR-Z0-9]{17}$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 17 of either one character from "A" through "H", one character from "J" through "N", "P", one character from "R" through "Z", or one character from "0" through "9".

See the other validators in the :doc:`library <index>`.
