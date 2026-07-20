ein
===

**Identifiers** · :doc:`Back to the library <index>`

A US Employer Identification Number.

.. code-block:: python

   from edify.library import ein

   ein('12-1234567')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 12-1234567|23-2345678

   from edify.library import ein
   ein

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{2}\-\d{7}$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 2 digits (0-9).
   - Then the text must have "-".
   - Then the text must have exactly 7 digits (0-9).

See the other validators in the :doc:`library <index>`.
