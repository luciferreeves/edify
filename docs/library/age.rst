age
===

**Security** · :doc:`Back to the library <index>`

An age-encryption recipient or identity.

.. code-block:: python

   from edify.library import age

   age('Aa0+/=_-.: Aa0+/')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: Aa0+/=_-.: Aa0+/|a0+/=_-.: Aa0+/=_

   from edify.library import age
   age

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:\s|[A-Za-z0-9\+/=_\-\.:]){16,4096}$

How it reads
------------

.. code-block:: text

   - The text must start with between 16 and 4096 of either one character from "A" through "Z", one character from "a" through "z", one character from "0" through "9", "+", "/", "=", "_", "-", ".", ":", or one whitespace character (space, tab, newline, etc.).

See the other validators in the :doc:`library <index>`.
