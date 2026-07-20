unicode
=======

**Text** · :doc:`Back to the library <index>`

Unicode text.

.. code-block:: python

   from edify.library import unicode

   unicode('eoa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: eoa|oaiu

   from edify.library import unicode
   unicode

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
