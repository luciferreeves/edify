bearer
======

**Auth** · :doc:`Back to the library <index>`

A bearer authorization token.

.. code-block:: python

   from edify.library import bearer

   bearer('Bearer Aa0')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: Bearer Aa0|Bearer a0.A

   from edify.library import bearer
   bearer

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^Bearer [A-Za-z0-9._-]+$

How it reads
------------

.. code-block:: text

   - The text must start with "Bearer ".
   - Then the text must have one or more of either one character from "A" through "Z", one character from "a" through "z", one character from "0" through "9", or one character from the set "._-".

See the other validators in the :doc:`library <index>`.
