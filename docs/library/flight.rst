flight
======

**Transport** · :doc:`Back to the library <index>`

A flight number.

.. code-block:: python

   from edify.library import flight

   flight('AB1A')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: AB1A|BC23

   from edify.library import flight
   flight

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z]{2}\d{1,4}[A-Z]?$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 2 uppercase letters (A-Z).
   - Then the text must have between 1 and 4 digits (0-9).
   - Optional: one uppercase letter (A-Z).

See the other validators in the :doc:`library <index>`.
