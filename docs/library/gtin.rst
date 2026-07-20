gtin
====

**Product** · :doc:`Back to the library <index>`

A Global Trade Item Number.

.. code-block:: python

   from edify.library import gtin

   gtin('12345678')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 12345678|234567890123

   from edify.library import gtin
   gtin

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:\d{8}|\d{12}|\d{13}|\d{14})$

How it reads
------------

.. code-block:: text

   - The text must start with either exactly 8 digits (0-9), exactly 12 digits (0-9), exactly 13 digits (0-9), or exactly 14 digits (0-9).

See the other validators in the :doc:`library <index>`.
