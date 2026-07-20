codec
=====

**Media** · :doc:`Back to the library <index>`

A media codec name.

.. code-block:: python

   from edify.library import codec

   codec('ea')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: ea|oA0

   from edify.library import codec
   codec

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-zA-Z][a-zA-Z0-9_\.\-]{1,29}$

How it reads
------------

.. code-block:: text

   - The text must start with one letter (a-z or A-Z).
   - Then the text must have between 1 and 29 of either one character from "a" through "z", one character from "A" through "Z", one character from "0" through "9", "_", ".", or "-".

See the other validators in the :doc:`library <index>`.
