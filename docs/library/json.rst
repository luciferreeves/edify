json
====

**Data** · :doc:`Back to the library <index>`

A JSON identifier or token.

.. code-block:: python

   from edify.library import json

   json('name')   # True
   json('  ')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: name|user_id|  |a b

   from edify.library import json
   json

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
