hmac
====

**Auth** · :doc:`Back to the library <index>`

An HMAC signature digest.

.. code-block:: python

   from edify.library import hmac

   hmac('0aA0aA0aA0aA0aA0aA0aA0aA0aA0aA0a')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 0aA0aA0aA0aA0aA0aA0aA0aA0aA0aA0a|aA0aA0aA0aA0aA0aA0aA0aA0aA0aA0aA0

   from edify.library import hmac
   hmac

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[0-9a-fA-F]{32,128}$

How it reads
------------

.. code-block:: text

   - The text must start with between 32 and 128 of either one character from "0" through "9", one character from "a" through "f", or one character from "A" through "F".

See the other validators in the :doc:`library <index>`.
