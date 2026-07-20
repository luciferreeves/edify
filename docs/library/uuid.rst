uuid
====

**Identifiers** · :doc:`Back to the library <index>`

A universally unique identifier (UUID).

.. code-block:: python

   from edify.library import uuid

   uuid('550e8400-e29b-41d4-a716-446655440000')   # True
   uuid('not-a-uuid')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 550e8400-e29b-41d4-a716-446655440000|not-a-uuid|12345

   from edify.library import uuid
   uuid

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[0-9a-f]{8}\-[0-9a-f]{4}\-[0-5][0-9a-f]{3}\-[089ab][0-9a-f]{3}\-[0-9a-f]{12}$

See the other validators in the :doc:`library <index>`.
