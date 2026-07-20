percentage
==========

**Numeric** · :doc:`Back to the library <index>`

A percentage such as ``42%``.

.. code-block:: python

   from edify.library import percentage

   percentage('42%')   # True
   percentage('42')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 42%|100%|0.5%|42|abc%

   from edify.library import percentage
   percentage

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\-?\d+(?:\.\d+)?\s?%$

How it reads
------------

.. code-block:: text

   - Optional: "-".
   - Then the text must have one or more digits (0-9).
   - Optional: ".", then one or more digits (0-9).
   - Optional: one whitespace character (space, tab, newline, etc.).
   - Then the text must have "%".

See the other validators in the :doc:`library <index>`.
