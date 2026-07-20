signature
=========

**Security** · :doc:`Back to the library <index>`

A cryptographic signature.

.. code-block:: python

   from edify.library import signature


Edit the string, or the pattern itself:

.. edify-playground::

   from edify.library import signature
   signature

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Za-z0-9\+/=_\-]{64,4096}$

How it reads
------------

.. code-block:: text

   - The text must start with between 64 and 4096 of either one character from "A" through "Z", one character from "a" through "z", one character from "0" through "9", "+", "/", "=", "_", or "-".

See the other validators in the :doc:`library <index>`.
