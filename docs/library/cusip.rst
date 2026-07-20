cusip
=====

**Identifiers** · :doc:`Back to the library <index>`

A CUSIP security identifier.

.. code-block:: python

   from edify.library import cusip

   cusip('A0A0A0A0A')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: A0A0A0A0A|0A0A0A0A0

   from edify.library import cusip
   cusip

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z0-9]{9}$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 9 of either one character from "A" through "Z" or one character from "0" through "9".

See the other validators in the :doc:`library <index>`.
