guid
====

**Identifiers** · :doc:`Back to the library <index>`

A globally unique identifier.

.. code-block:: python

   from edify.library import guid

   guid('550e8400-e29b-41d4-a716-446655440000')   # True
   guid('nope')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 550e8400-e29b-41d4-a716-446655440000|nope|123

   from edify.library import guid
   guid

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\{?[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}\}?$

See the other validators in the :doc:`library <index>`.
