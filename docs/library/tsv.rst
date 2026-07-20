tsv
===

**Data** · :doc:`Back to the library <index>`

A tab-separated-values row.

.. code-block:: python

   from edify.library import tsv

   tsv('Aa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: Aa|a0_

   from edify.library import tsv
   tsv

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Za-z0-9_\.\-/\+]{2,256}$

How it reads
------------

.. code-block:: text

   - The text must start with between 2 and 256 of either one character from "A" through "Z", one character from "a" through "z", one character from "0" through "9", "_", ".", "-", "/", or "+".

See the other validators in the :doc:`library <index>`.
