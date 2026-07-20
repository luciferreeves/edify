meid
====

**Identifiers** · :doc:`Back to the library <index>`

A mobile equipment MEID.

.. code-block:: python

   from edify.library import meid

   meid('0A0A0A0A0A0A0A')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 0A0A0A0A0A0A0A|A0A0A0A0A0A0A0

   from edify.library import meid
   meid

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[0-9A-F]{14}$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 14 of either one character from "0" through "9" or one character from "A" through "F".

See the other validators in the :doc:`library <index>`.
