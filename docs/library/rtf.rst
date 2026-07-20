rtf
===

**Documents** · :doc:`Back to the library <index>`

A Rich Text Format file name.

.. code-block:: python

   from edify.library import rtf

   rtf('{\\rtf1eoa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: {\rtf1eoa|{\rtfoaiu

   from edify.library import rtf
   rtf

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\{\\rtf\d?.*$

How it reads
------------

.. code-block:: text

   - The text must start with "{\rtf".
   - Optional: one digit (0-9).
   - Then the text must have zero or more characters (any character).

See the other validators in the :doc:`library <index>`.
