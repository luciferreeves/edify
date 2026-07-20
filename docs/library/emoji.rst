emoji
=====

**Text** · :doc:`Back to the library <index>`

An emoji character.

.. code-block:: python

   from edify.library import emoji

   emoji('😀')   # True
   emoji('abc')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 😀|❤|abc|123

   from edify.library import emoji
   emoji

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[🌀-🫿☀-➿]+$

How it reads
------------

.. code-block:: text

   - The text must start with one or more of either one character from "🌀" through "🫿" or one character from "☀" through "➿".

See the other validators in the :doc:`library <index>`.
