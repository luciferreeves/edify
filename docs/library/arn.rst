arn
===

**Identifiers** · :doc:`Back to the library <index>`

An Amazon Resource Name.

.. code-block:: python

   from edify.library import arn

   arn('arn:a-a:a0-:a0-:123:eoa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: arn:a-a:a0-:a0-:123:eoa|arn:-a-a:0-a0:0-a0:2345:oaiu

   from edify.library import arn
   arn

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^arn:[a-z\-]+:[a-z0-9\-]+:[a-z0-9\-]*:\d*:.+$

See the other validators in the :doc:`library <index>`.
