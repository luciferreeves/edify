makefile
========

**Software** · :doc:`Back to the library <index>`

A Makefile target.

.. code-block:: python

   from edify.library import makefile

   makefile('.eaA0   eaA0    oA0._     a0._-a   :eoa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: .eaA0   eaA0    oA0._     a0._-a   :eoa

   from edify.library import makefile
   makefile

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\.?[a-zA-Z][a-zA-Z0-9\._\-]*(?:\s+[a-zA-Z][a-zA-Z0-9\._\-]*)*\s*:.*$

See the other validators in the :doc:`library <index>`.
