orc
===

**Data** · :doc:`Back to the library <index>`

An ORC columnar-file marker.

.. code-block:: python

   from edify.library import orc

   orc('ORCeoa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: ORCeoa|ORCoaiu

   from edify.library import orc
   orc

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^ORC.*$

How it reads
------------

.. code-block:: text

   - The text must start with "ORC".
   - Then the text must have zero or more characters (any character).

See the other validators in the :doc:`library <index>`.
