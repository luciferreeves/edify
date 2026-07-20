checksum
========

**Software** · :doc:`Back to the library <index>`

A checksum digest.

.. code-block:: python

   from edify.library import checksum

   checksum('aA0aA0aA')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: aA0aA0aA|A0aA0aA0a

   from edify.library import checksum
   checksum

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-fA-F0-9]{8,128}$

How it reads
------------

.. code-block:: text

   - The text must start with between 8 and 128 of either one character from "a" through "f", one character from "A" through "F", or one character from "0" through "9".

See the other validators in the :doc:`library <index>`.
