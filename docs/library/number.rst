number
======

**Numeric** · :doc:`Back to the library <index>`

A number, integer or decimal.

.. code-block:: python

   from edify.library import number

   number('42')   # True
   number('abc')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 42|-3.14|0.5|abc|1,2

   from edify.library import number
   number

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:[+-]?\d+|[+-]?\d+\.\d+|[+-]?\.\d+|[+-]?\d+\.\d*[eE][+-]?\d+|[+-]?\d+[eE][+-]?\d+|0[xX][0-9a-fA-F]+|0[oO][0-7]+|0[bB][01]+|[+-]?\d+(?:\.\d+)?[+-]\d+(?:\.\d+)?[jJi])$

See the other validators in the :doc:`library <index>`.
