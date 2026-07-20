sedol
=====

**Identifiers** · :doc:`Back to the library <index>`

A SEDOL security identifier.

.. code-block:: python

   from edify.library import sedol

   sedol('BFJPVY1')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: BFJPVY1|FJPVY02

   from edify.library import sedol
   sedol

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[B-DF-HJ-NP-TV-XY-Z0-9]{6}\d$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 6 of either one character from "B" through "D", one character from "F" through "H", one character from "J" through "N", one character from "P" through "T", one character from "V" through "X", one character from "Y" through "Z", or one character from "0" through "9".
   - Then the text must have one digit (0-9).

See the other validators in the :doc:`library <index>`.
