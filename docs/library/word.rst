word
====

**Text** · :doc:`Back to the library <index>`

A single word.

.. code-block:: python

   from edify.library import word

   word('hello')   # True
   word('two words')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: hello|world_1|two words|!!!

   from edify.library import word
   word

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\w+$

How it reads
------------

.. code-block:: text

   - The text must start with one or more letters, digits, or underscores.

See the other validators in the :doc:`library <index>`.
