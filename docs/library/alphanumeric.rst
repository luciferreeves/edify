alphanumeric
============

**Text** · :doc:`Back to the library <index>`

Alphanumeric text (letters and digits).

.. code-block:: python

   from edify.library import alphanumeric

   alphanumeric('abc123')   # True
   alphanumeric('a-b')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: abc123|Test9|a-b|hi there

   from edify.library import alphanumeric
   alphanumeric

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-zA-Z0-9]+$

How it reads
------------

.. code-block:: text

   - The text must start with one or more letters or digits (a-z, A-Z, or 0-9).

See the other validators in the :doc:`library <index>`.
