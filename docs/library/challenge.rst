challenge
=========

**Auth** · :doc:`Back to the library <index>`

An authentication challenge value.

.. code-block:: python

   from edify.library import challenge

   challenge('Aa0-Aa0-Aa0-Aa0-')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: Aa0-Aa0-Aa0-Aa0-|a0-Aa0-Aa0-Aa0-Aa

   from edify.library import challenge
   challenge

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Za-z0-9_-]{16,128}$

How it reads
------------

.. code-block:: text

   - The text must start with between 16 and 128 of either one character from "A" through "Z", one character from "a" through "z", one character from "0" through "9", or one character from the set "_-".

See the other validators in the :doc:`library <index>`.
