time
====

**Temporal** · :doc:`Back to the library <index>`

A time of day.

.. code-block:: python

   from edify.library import time

   time('10:30')   # True
   time('25:00')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 10:30|23:59:59|25:00|abc

   from edify.library import time
   time

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:2[0-3]|[01]?\d):[0-5]\d(?::[0-5]\d(?:\.\d{1,6})?)?|(?:1[0-2]|0?[1-9]):[0-5]\d(?::[0-5]\d)?\s?[AaPp][Mm])$

See the other validators in the :doc:`library <index>`.
