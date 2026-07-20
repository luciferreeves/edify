filename
========

**Media** · :doc:`Back to the library <index>`

A file name.

.. code-block:: python

   from edify.library import filename

   filename('eoa.a')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: eoa.a|oaiu.1b

   from edify.library import filename
   filename

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?![\0-\x1f/\\:\*\?"<>\|]).)+\.[a-zA-Z0-9]{1,10}$

How it reads
------------

.. code-block:: text

   - The text must start with one or more of AssertNotAheadElement, then any single character.
   - Then the text must have ".".
   - Then the text must have between 1 and 10 letters or digits (a-z, A-Z, or 0-9).

See the other validators in the :doc:`library <index>`.
