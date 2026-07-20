cargo
=====

**Software** · :doc:`Back to the library <index>`

A Cargo (Rust) package identifier.

.. code-block:: python

   from edify.library import cargo

   cargo('e@123-aA0')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: e@123-aA0|oA

   from edify.library import cargo
   cargo

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-zA-Z][a-zA-Z0-9_\-]{0,63}(?:@\d+(?:\.\d+){0,3}(?:[-.+][a-zA-Z0-9\.\-]+)?)?$

See the other validators in the :doc:`library <index>`.
