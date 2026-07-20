alpha
=====

**Text** · :doc:`Back to the library <index>`

Alphabetic text (letters only).

.. code-block:: python

   from edify.library import alpha

   alpha('hello')   # True
   alpha('hello1')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: hello|World|hello1|123

   from edify.library import alpha
   alpha

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-zA-Z]+$

How it reads
------------

.. code-block:: text

   - The text must start with one or more letters (a-z or A-Z).

See the other validators in the :doc:`library <index>`.
