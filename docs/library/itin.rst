itin
====

**Identifiers** · :doc:`Back to the library <index>`

A US Individual Taxpayer Identification Number.

.. code-block:: python

   from edify.library import itin

   itin('912-51-1234')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 912-51-1234|923-60-2345

   from edify.library import itin
   itin

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^9\d{2}\-(?:5\d|6[0-5]|7\d|8[0-8]|9[0-2]|9[4-9])\-\d{4}$

How it reads
------------

.. code-block:: text

   - The text must start with "9".
   - Then the text must have exactly 2 digits (0-9).
   - Then the text must have "-".
   - Then the text must have either "5", then one digit (0-9), "6", then one character from "0" through "5", "7", then one digit (0-9), "8", then one character from "0" through "8", "9", then one character from "0" through "2", or "9", then one character from "4" through "9".
   - Then the text must have "-".
   - Then the text must have exactly 4 digits (0-9).

See the other validators in the :doc:`library <index>`.
