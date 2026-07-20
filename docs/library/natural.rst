natural
=======

**Numeric** · :doc:`Back to the library <index>`

A natural number (non-negative integer).

.. code-block:: python

   from edify.library import natural

   natural('42')   # True
   natural('-1')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 42|1000|-1|3.14

   from edify.library import natural
   natural

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[1-9]\d*$

How it reads
------------

.. code-block:: text

   - The text must start with one character from "1" through "9".
   - Then the text must have zero or more digits (0-9).

See the other validators in the :doc:`library <index>`.
