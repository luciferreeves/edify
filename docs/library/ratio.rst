ratio
=====

**Numeric** · :doc:`Back to the library <index>`

A ratio such as ``16:9``.

.. code-block:: python

   from edify.library import ratio

   ratio('16:9')   # True
   ratio('16')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 16:9|4:3|16|abc

   from edify.library import ratio
   ratio

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d+:\d+$

How it reads
------------

.. code-block:: text

   - The text must start with one or more digits (0-9).
   - Then the text must have ":".
   - Then the text must have one or more digits (0-9).

See the other validators in the :doc:`library <index>`.
