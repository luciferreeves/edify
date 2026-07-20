scientific
==========

**Numeric** · :doc:`Back to the library <index>`

A number in scientific notation.

.. code-block:: python

   from edify.library import scientific

   scientific('1.5e10')   # True
   scientific('abc')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 1.5e10|6.022e23|-2E-5|abc|1.2.3

   from edify.library import scientific
   scientific

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[+-]?\d+(?:\.\d+)?[eE][+-]?\d+$

How it reads
------------

.. code-block:: text

   - Optional: one character from the set "+-".
   - Then the text must have one or more digits (0-9).
   - Optional: ".", then one or more digits (0-9).
   - Then the text must have one character from the set "eE".
   - Optional: one character from the set "+-".
   - Then the text must have one or more digits (0-9).

See the other validators in the :doc:`library <index>`.
