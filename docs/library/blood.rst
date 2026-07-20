blood
=====

**Medical** · :doc:`Back to the library <index>`

A blood type such as ``O+``.

.. code-block:: python

   from edify.library import blood

   blood('AB+')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: AB+|A-

   from edify.library import blood
   blood

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:AB|[ABO]))[+-]$

How it reads
------------

.. code-block:: text

   - The text must start with either "AB", "A", "B", or "O".
   - Then the text must have one character from the set "+-".

See the other validators in the :doc:`library <index>`.
