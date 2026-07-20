year
====

**Temporal** · :doc:`Back to the library <index>`

A four-digit year.

.. code-block:: python

   from edify.library import year

   year('2024')   # True
   year('24')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 2024|1999|24|abcd

   from edify.library import year
   year

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{4}$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 4 digits (0-9).

See the other validators in the :doc:`library <index>`.
