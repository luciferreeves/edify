zip_code
========

**Address** · :doc:`Back to the library <index>`

A postal / ZIP code.

.. code-block:: python

   from edify.library import zip_code

   zip_code('90210')   # True
   zip_code('abc')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 90210|12345-6789|abc|1

   from edify.library import zip_code
   zip_code

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{5}(?:\-\d{4})?$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 5 digits (0-9).
   - Optional: "-", then exactly 4 digits (0-9).

See the other validators in the :doc:`library <index>`.
