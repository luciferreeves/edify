iso_date
========

**Temporal** · :doc:`Back to the library <index>`

An ISO 8601 date (``YYYY-MM-DD``).

.. code-block:: python

   from edify.library import iso_date

   iso_date('2024-07-16')   # True
   iso_date('2024/07/16')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 2024-07-16|1999-12-31|2024/07/16|16-07-2024

   from edify.library import iso_date
   iso_date

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{4}\-\d{2}\-\d{2}$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 4 digits (0-9).
   - Then the text must have "-".
   - Then the text must have exactly 2 digits (0-9).
   - Then the text must have "-".
   - Then the text must have exactly 2 digits (0-9).

See the other validators in the :doc:`library <index>`.
