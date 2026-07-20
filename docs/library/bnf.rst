bnf
===

**Grammar** · :doc:`Back to the library <index>`

A BNF grammar rule.

.. code-block:: python

   from edify.library import bnf

   bnf('Aa0_')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: Aa0_|a0_-<

   from edify.library import bnf
   bnf

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:\s|[A-Za-z0-9_\-<>:=\|\*\+\?\(\)\[\]\{\}\.'"/;,]){4,65536}$

See the other validators in the :doc:`library <index>`.
