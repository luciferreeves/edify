ssn
===

**Identifiers** · :doc:`Back to the library <index>`

A US Social Security Number.

.. code-block:: python

   from edify.library import ssn

   ssn('123-45-6789')   # True
   ssn('12-3456')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 123-45-6789|12-3456|abc

   from edify.library import ssn
   ssn

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?!(?:666|000|9\d{2}))\d{3}\-(?!00)\d{2}\-(?!0{4})\d{4}$

How it reads
------------

.. code-block:: text

   - Then the text must NOT be followed by either "666", "000", or "9", then exactly 2 digits (0-9).
   - Then the text must have exactly 3 digits (0-9).
   - Then the text must have "-".
   - Then the text must NOT be followed by "00".
   - Then the text must have exactly 2 digits (0-9).
   - Then the text must have "-".
   - Then the text must NOT be followed by exactly 4 copies of the character "0".
   - Then the text must have exactly 4 digits (0-9).

See the other validators in the :doc:`library <index>`.
