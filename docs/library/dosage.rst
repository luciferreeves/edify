dosage
======

**Medical** · :doc:`Back to the library <index>`

A medication dosage.

.. code-block:: python

   from edify.library import dosage

   dosage('123.123 mg/kg')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 123.123 mg/kg|2345g

   from edify.library import dosage
   dosage

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d+(?:\.\d+)?\s?(?:mg|kg|ml|mcg|iu|[gl])(?:/(?:kg|day|dose))?$

How it reads
------------

.. code-block:: text

   - The text must start with one or more digits (0-9).
   - Optional: ".", then one or more digits (0-9).
   - Optional: one whitespace character (space, tab, newline, etc.).
   - Then the text must have either "mg", "g", "kg", "ml", "l", "mcg", or "iu".
   - Optional: "/", then either "kg", "day", or "dose".

See the other validators in the :doc:`library <index>`.
