pager
=====

**Contact** · :doc:`Back to the library <index>`

A pager number.

.. code-block:: python

   from edify.library import pager

   pager('1234')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 1234|23456

   from edify.library import pager
   pager

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{4,10}$

How it reads
------------

.. code-block:: text

   - The text must start with between 4 and 10 digits (0-9).

See the other validators in the :doc:`library <index>`.
