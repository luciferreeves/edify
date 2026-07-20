cookie
======

**Web** · :doc:`Back to the library <index>`

An HTTP cookie name/value.

.. code-block:: python

   from edify.library import cookie

   cookie('aA0=eoa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: aA0=eoa|A0_-=oaiu

   from edify.library import cookie
   cookie

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-zA-Z0-9_\-]+=(?:(?!(?:\s|[;])).)+$

How it reads
------------

.. code-block:: text

   - The text must start with one or more of either one character from "a" through "z", one character from "A" through "Z", one character from "0" through "9", "_", or "-".
   - Then the text must have "=".
   - Then the text must have one or more of AssertNotAheadElement, then any single character.

See the other validators in the :doc:`library <index>`.
