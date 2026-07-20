issn
====

**Publishing** · :doc:`Back to the library <index>`

An International Standard Serial Number.

.. code-block:: python

   from edify.library import issn

   issn('2049-3630')   # True
   issn('123')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 2049-3630|0378-5955|123|abcd

   from edify.library import issn
   issn

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{4}\-\d{3}(?:\d|[Xx])$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 4 digits (0-9).
   - Then the text must have "-".
   - Then the text must have exactly 3 digits (0-9).
   - Then the text must have either one digit (0-9), "X", or "x".

See the other validators in the :doc:`library <index>`.
