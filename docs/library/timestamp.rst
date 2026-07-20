timestamp
=========

**Temporal** · :doc:`Back to the library <index>`

A timestamp.

.. code-block:: python

   from edify.library import timestamp

   timestamp('-1234567890')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: -1234567890|23456789012

   from edify.library import timestamp
   timestamp

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\-?\d{10,13}$

How it reads
------------

.. code-block:: text

   - Optional: "-".
   - Then the text must have between 10 and 13 digits (0-9).

See the other validators in the :doc:`library <index>`.
