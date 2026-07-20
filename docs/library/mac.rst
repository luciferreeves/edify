mac
===

**Identifiers** · :doc:`Back to the library <index>`

A MAC hardware address.

.. code-block:: python

   from edify.library import mac

   mac('01:23:45:67:89:ab')   # True
   mac('gg:hh')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 01:23:45:67:89:ab|gg:hh|12345

   from edify.library import mac
   mac

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:[0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 5 of exactly 2 of either one character from "0" through "9", one character from "a" through "f", or one character from "A" through "F", then one character from the set ":-".
   - Then the text must have exactly 2 of either one character from "0" through "9", one character from "a" through "f", or one character from "A" through "F".

See the other validators in the :doc:`library <index>`.
