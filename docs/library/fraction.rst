fraction
========

**Numeric** · :doc:`Back to the library <index>`

A fraction such as ``3/4``.

.. code-block:: python

   from edify.library import fraction

   fraction('3/4')   # True
   fraction('3')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 3/4|22/7|3|abc

   from edify.library import fraction
   fraction

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\-?(?:\d+\s+)?\d+/\d+$

How it reads
------------

.. code-block:: text

   - Optional: "-".
   - Optional: one or more digits (0-9), then one or more whitespace characters (space, tab, newline, etc.).
   - Then the text must have one or more digits (0-9).
   - Then the text must have "/".
   - Then the text must have one or more digits (0-9).

See the other validators in the :doc:`library <index>`.
