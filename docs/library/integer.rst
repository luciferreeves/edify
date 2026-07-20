integer
=======

**Numeric** · :doc:`Back to the library <index>`

An integer.

.. code-block:: python

   from edify.library import integer

   integer('42')   # True
   integer('3.14')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 42|-7|0|3.14|abc

   from edify.library import integer
   integer

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[+-]?\d+$

How it reads
------------

.. code-block:: text

   - Optional: one character from the set "+-".
   - Then the text must have one or more digits (0-9).

See the other validators in the :doc:`library <index>`.
