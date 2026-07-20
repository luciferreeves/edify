mpn
===

**Product** · :doc:`Back to the library <index>`

A manufacturer part number.

.. code-block:: python

   from edify.library import mpn

   mpn('AA')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: AA|00-

   from edify.library import mpn
   mpn

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z0-9][A-Z0-9\-_\.]{1,63}$

How it reads
------------

.. code-block:: text

   - The text must start with either one character from "A" through "Z" or one character from "0" through "9".
   - Then the text must have between 1 and 63 of either one character from "A" through "Z", one character from "0" through "9", "-", "_", or ".".

See the other validators in the :doc:`library <index>`.
