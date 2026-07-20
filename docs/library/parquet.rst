parquet
=======

**Data** · :doc:`Back to the library <index>`

A Parquet columnar-file marker.

.. code-block:: python

   from edify.library import parquet

   parquet('PAR1eoa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: PAR1eoa|PAR1oaiu

   from edify.library import parquet
   parquet

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^PAR1.*$

How it reads
------------

.. code-block:: text

   - The text must start with "PAR1".
   - Then the text must have zero or more characters (any character).

See the other validators in the :doc:`library <index>`.
