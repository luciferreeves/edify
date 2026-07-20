epoch
=====

**Temporal** · :doc:`Back to the library <index>`

A Unix epoch timestamp.

.. code-block:: python

   from edify.library import epoch

   epoch('-1')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: -1|23

   from edify.library import epoch
   epoch

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\-?\d{1,10}$

How it reads
------------

.. code-block:: text

   - Optional: "-".
   - Then the text must have between 1 and 10 digits (0-9).

See the other validators in the :doc:`library <index>`.
