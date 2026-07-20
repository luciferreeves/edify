vat
===

**Finance** · :doc:`Back to the library <index>`

A VAT registration number.

.. code-block:: python

   from edify.library import vat

   vat('AB123456')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: AB123456|BC2345678

   from edify.library import vat
   vat

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z]{2}\d{6,12}$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 2 uppercase letters (A-Z).
   - Then the text must have between 6 and 12 digits (0-9).

See the other validators in the :doc:`library <index>`.
