orcid
=====

**Identifiers** · :doc:`Back to the library <index>`

An ORCID researcher identifier.

.. code-block:: python

   from edify.library import orcid

   orcid('1234-1234-1234-1231')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 1234-1234-1234-1231|2345-2345-2345-234X

   from edify.library import orcid
   orcid

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{4}\-\d{4}\-\d{4}\-\d{3}(?:\d|[X])$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 4 digits (0-9).
   - Then the text must have "-".
   - Then the text must have exactly 4 digits (0-9).
   - Then the text must have "-".
   - Then the text must have exactly 4 digits (0-9).
   - Then the text must have "-".
   - Then the text must have exactly 3 digits (0-9).
   - Then the text must have either one digit (0-9) or "X".

See the other validators in the :doc:`library <index>`.
