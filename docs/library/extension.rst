extension
=========

**Media** · :doc:`Back to the library <index>`

A file extension.

.. code-block:: python

   from edify.library import extension

   extension('.a')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: .a|.1b

   from edify.library import extension
   extension

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\.[a-zA-Z0-9]{1,10}$

How it reads
------------

.. code-block:: text

   - The text must start with ".".
   - Then the text must have between 1 and 10 letters or digits (a-z, A-Z, or 0-9).

See the other validators in the :doc:`library <index>`.
