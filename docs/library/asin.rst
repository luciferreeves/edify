asin
====

**Identifiers** · :doc:`Back to the library <index>`

An Amazon Standard Identification Number.

.. code-block:: python

   from edify.library import asin

   asin('A0A0A0A0A0')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: A0A0A0A0A0|0A0A0A0A0A

   from edify.library import asin
   asin

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z0-9]{10}$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 10 of either one character from "A" through "Z" or one character from "0" through "9".

See the other validators in the :doc:`library <index>`.
