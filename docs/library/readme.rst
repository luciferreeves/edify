readme
======

**Documents** · :doc:`Back to the library <index>`

A README file name.

.. code-block:: python

   from edify.library import readme

   readme('A')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: A|a0

   from edify.library import readme
   readme

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Za-z0-9_\.\-/]{1,256}$

How it reads
------------

.. code-block:: text

   - The text must start with between 1 and 256 of either one character from "A" through "Z", one character from "a" through "z", one character from "0" through "9", "_", ".", "-", or "/".

See the other validators in the :doc:`library <index>`.
