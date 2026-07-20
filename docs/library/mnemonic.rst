mnemonic
========

**Auth** · :doc:`Back to the library <index>`

A BIP-39 style mnemonic phrase.

.. code-block:: python

   from edify.library import mnemonic


Edit the string, or the pattern itself:

.. edify-playground::

   from edify.library import mnemonic
   mnemonic

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:[a-z]+ ){11,23}[a-z]+$

How it reads
------------

.. code-block:: text

   - The text must start with between 11 and 23 of one or more lowercase letters (a-z), then " ".
   - Then the text must have one or more lowercase letters (a-z).

See the other validators in the :doc:`library <index>`.
