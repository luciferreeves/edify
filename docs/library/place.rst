place
=====

**Geo** · :doc:`Back to the library <index>`

A place name.

.. code-block:: python

   from edify.library import place

   place('eA')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: eA|oa

   from edify.library import place
   place

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-zA-Z][A-Za-z \.,'\-]{1,99}$

How it reads
------------

.. code-block:: text

   - The text must start with one letter (a-z or A-Z).
   - Then the text must have between 1 and 99 of either one character from "A" through "Z", one character from "a" through "z", " ", ".", ",", "'", or "-".

See the other validators in the :doc:`library <index>`.
