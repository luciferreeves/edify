username
========

**Contact** · :doc:`Back to the library <index>`

A username / login handle.

.. code-block:: python

   from edify.library import username

   username('jane_doe')   # True
   username('a')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: jane_doe|user123|a|no spaces here

   from edify.library import username
   username

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-zA-Z0-9][a-zA-Z0-9_.-]{2,29}$

How it reads
------------

.. code-block:: text

   - The text must start with either one character from "a" through "z", one character from "A" through "Z", or one character from "0" through "9".
   - Then the text must have between 2 and 29 of either one character from "a" through "z", one character from "A" through "Z", one character from "0" through "9", or one character from the set "_.-".

See the other validators in the :doc:`library <index>`.
