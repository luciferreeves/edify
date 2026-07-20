currency
========

**Finance** · :doc:`Back to the library <index>`

A currency amount or code.

.. code-block:: python

   from edify.library import currency

   currency('AAA')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: AAA

   from edify.library import currency
   currency

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z]{3}$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 3 of one character from "A" through "Z".

See the other validators in the :doc:`library <index>`.
