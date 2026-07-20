address
=======

**Contact** · :doc:`Back to the library <index>`

A postal address line.

.. code-block:: python

   from edify.library import address

   address('123   Aa0')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 123   Aa0|2345    a0 #

   from edify.library import address
   address

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d+\s+(?:\s|[A-Za-z0-9.,'\-#/])+$

How it reads
------------

.. code-block:: text

   - The text must start with one or more digits (0-9).
   - Then the text must have one or more whitespace characters (space, tab, newline, etc.).
   - Then the text must have one or more of either one character from "A" through "Z", one character from "a" through "z", one character from "0" through "9", one whitespace character (space, tab, newline, etc.), or one character from the set ".,'\-#/".

See the other validators in the :doc:`library <index>`.
