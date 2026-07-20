printable
=========

**Text** · :doc:`Back to the library <index>`

Printable characters.

.. code-block:: python

   from edify.library import printable

   printable('eoa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: eoa|oaiu

   from edify.library import printable
   printable

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?![\0-\x1f]).)+$

How it reads
------------

.. code-block:: text

   - The text must start with one or more of AssertNotAheadElement, then any single character.

See the other validators in the :doc:`library <index>`.
