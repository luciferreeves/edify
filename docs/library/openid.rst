openid
======

**API** · :doc:`Back to the library <index>`

An OpenID Connect identifier.

.. code-block:: python

   from edify.library import openid

   openid('Aa0')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: Aa0|a0_.

   from edify.library import openid
   openid

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Za-z0-9_\.\-/\+]{3,256}$

How it reads
------------

.. code-block:: text

   - The text must start with between 3 and 256 of either one character from "A" through "Z", one character from "a" through "z", one character from "0" through "9", "_", ".", "-", "/", or "+".

See the other validators in the :doc:`library <index>`.
