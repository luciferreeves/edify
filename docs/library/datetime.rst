datetime
========

**Temporal** · :doc:`Back to the library <index>`

A date and time.

.. code-block:: python

   from edify.library import datetime

   datetime('2024-07-16T10:30:00')   # True
   datetime('not-a-datetime')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 2024-07-16T10:30:00|2024-07-16 10:30|not-a-datetime|abcd

   from edify.library import datetime
   datetime

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:(?:[+-]\d{2}:?\d{2}|[Zz]))?|\d{4}\d{2}\d{2}[Tt]\d{2}\d{2}\d{2}(?:(?:[+-]\d{4}|[Zz]))?)$

See the other validators in the :doc:`library <index>`.
