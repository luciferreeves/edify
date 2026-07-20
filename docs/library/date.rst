date
====

**Temporal** · :doc:`Back to the library <index>`

A calendar date.

.. code-block:: python

   from edify.library import date

   date('2024-07-16')   # True
   date('not a date')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 2024-07-16|16/07/2024|not a date|abcd

   from edify.library import date
   date

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:\d{1,2}/\d{1,2}/\d{4}|\d{4}\-\d{2}\-\d{2}|\d{2}\-\d{2}\-\d{4}|\d{4}/\d{2}/\d{2}|\d{1,2}\.\d{1,2}\.\d{4}|\d{4}\.\d{2}\.\d{2}|\d{8})$

See the other validators in the :doc:`library <index>`.
