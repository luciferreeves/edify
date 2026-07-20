glob
====

**Media** · :doc:`Back to the library <index>`

A glob pattern.

.. code-block:: python

   from edify.library import glob

   glob('eoa*eoa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: eoa*eoa|oaiu?oaiu

   from edify.library import glob
   glob

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?![\0-\x1f]).)*[*?[\]](?:(?![\0-\x1f]).)*$

How it reads
------------

.. code-block:: text

   - The text must start with zero or more of AssertNotAheadElement, then any single character.
   - Then the text must have one character from the set "*?[\]".
   - Then the text must have zero or more of AssertNotAheadElement, then any single character.

See the other validators in the :doc:`library <index>`.
