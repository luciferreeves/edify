pin
===

**Auth** · :doc:`Back to the library <index>`

A numeric PIN.

.. code-block:: python

   from edify.library import pin

   pin('1234')   # True
   pin('abc')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 1234|0000|abc|12

   from edify.library import pin
   pin

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{4,12}$

How it reads
------------

.. code-block:: text

   - The text must start with between 4 and 12 digits (0-9).

See the other validators in the :doc:`library <index>`.
