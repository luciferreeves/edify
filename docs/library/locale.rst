locale
======

**Media** · :doc:`Back to the library <index>`

A locale identifier such as ``en-US``.

.. code-block:: python

   from edify.library import locale

   locale('en-US')   # True
   locale('english')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: en-US|fr-CA|de|english|123

   from edify.library import locale
   locale

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-z]{2,3}(?:[_-][A-Z]{2})?(?:\.[a-zA-Z0-9\-]+)?(?:@[a-zA-Z0-9]+)?$

How it reads
------------

.. code-block:: text

   - The text must start with between 2 and 3 lowercase letters (a-z).
   - Optional: one character from the set "_-", then exactly 2 uppercase letters (A-Z).
   - Optional: ".", then one or more of either one character from "a" through "z", one character from "A" through "Z", one character from "0" through "9", or "-".
   - Optional: "@", then one or more letters or digits (a-z, A-Z, or 0-9).

See the other validators in the :doc:`library <index>`.
