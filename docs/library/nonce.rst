nonce
=====

**Security** · :doc:`Back to the library <index>`

A cryptographic nonce.

.. code-block:: python

   from edify.library import nonce

   nonce('Aa0+/=_-Aa0+/=_-')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: Aa0+/=_-Aa0+/=_-|a0+/=_-Aa0+/=_-Aa

   from edify.library import nonce
   nonce

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Za-z0-9\+/=_\-]{16,256}$

How it reads
------------

.. code-block:: text

   - The text must start with between 16 and 256 of either one character from "A" through "Z", one character from "a" through "z", one character from "0" through "9", "+", "/", "=", "_", or "-".

See the other validators in the :doc:`library <index>`.
