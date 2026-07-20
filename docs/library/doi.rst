doi
===

**Publishing** · :doc:`Back to the library <index>`

A Digital Object Identifier.

.. code-block:: python

   from edify.library import doi

   doi('10.1000/xyz123')   # True
   doi('not-a-doi')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 10.1000/xyz123|10.1234/abcd.efgh|not-a-doi|10

   from edify.library import doi
   doi

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^10\.\d{4,9}/[\-\._;\(\)/:A-Za-z0-9]+$

How it reads
------------

.. code-block:: text

   - The text must start with "10.".
   - Then the text must have between 4 and 9 digits (0-9).
   - Then the text must have "/".
   - Then the text must have one or more of either "-", ".", "_", ";", "(", ")", "/", ":", one character from "A" through "Z", one character from "a" through "z", or one character from "0" through "9".

See the other validators in the :doc:`library <index>`.
