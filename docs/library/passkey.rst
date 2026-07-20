passkey
=======

**Auth** · :doc:`Back to the library <index>`

A passkey / WebAuthn credential id.

.. code-block:: python

   from edify.library import passkey

   passkey('Aa0-Aa0-Aa0-Aa0-Aa0-Aa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: Aa0-Aa0-Aa0-Aa0-Aa0-Aa|a0-Aa0-Aa0-Aa0-Aa0-Aa0-

   from edify.library import passkey
   passkey

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Za-z0-9_-]{22,512}$

How it reads
------------

.. code-block:: text

   - The text must start with between 22 and 512 of either one character from "A" through "Z", one character from "a" through "z", one character from "0" through "9", or one character from the set "_-".

See the other validators in the :doc:`library <index>`.
