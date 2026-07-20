did
===

**Identifiers** · :doc:`Back to the library <index>`

A Decentralized Identifier.

.. code-block:: python

   from edify.library import did

   did('did:a0a:eoa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: did:a0a:eoa|did:0a0a:oaiu

   from edify.library import did
   did

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^did:[a-z0-9]+:.+$

How it reads
------------

.. code-block:: text

   - The text must start with "did:".
   - Then the text must have one or more of either one character from "a" through "z" or one character from "0" through "9".
   - Then the text must have ":".
   - Then the text must have one or more characters (any character).

See the other validators in the :doc:`library <index>`.
