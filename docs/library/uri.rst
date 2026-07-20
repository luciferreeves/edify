uri
===

**Address** · :doc:`Back to the library <index>`

A URI with a scheme and path.

.. code-block:: python

   from edify.library import uri

   uri('https://example.com/x')   # True
   uri('  ')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: https://example.com/x|mailto:a@b.com|  |no scheme

   from edify.library import uri
   uri

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-zA-Z][a-zA-Z0-9\+\.\-]*:\S+$

How it reads
------------

.. code-block:: text

   - The text must start with one letter (a-z or A-Z).
   - Then the text must have zero or more of either one character from "a" through "z", one character from "A" through "Z", one character from "0" through "9", "+", ".", or "-".
   - Then the text must have ":".
   - Then the text must have one or more non-whitespace characters.

See the other validators in the :doc:`library <index>`.
