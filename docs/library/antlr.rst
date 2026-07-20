antlr
=====

**Grammar** · :doc:`Back to the library <index>`

An ANTLR grammar rule.

.. code-block:: python

   from edify.library import antlr

   antlr('grammar   eaA0;eoa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: grammar   eaA0;eoa|grammar    oA0_a;oaiu

   from edify.library import antlr
   antlr

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^grammar\s+[a-zA-Z][a-zA-Z0-9_]*;.*$

How it reads
------------

.. code-block:: text

   - The text must start with "grammar".
   - Then the text must have one or more whitespace characters (space, tab, newline, etc.).
   - Then the text must have one letter (a-z or A-Z).
   - Then the text must have zero or more of either one character from "a" through "z", one character from "A" through "Z", one character from "0" through "9", or "_".
   - Then the text must have ";".
   - Then the text must have zero or more characters (any character).

See the other validators in the :doc:`library <index>`.
