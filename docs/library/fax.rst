fax
===

**Contact** · :doc:`Back to the library <index>`

A fax number.

.. code-block:: python

   from edify.library import fax

   fax('+1-(1)-1-1-1')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: +1-(1)-1-1-1|2323232323

   from edify.library import fax
   fax

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\+?\d{1,4}?(?:\s|[\-\.])?\(?\d{1,3}?\)?(?:\s|[\-\.])?\d{1,4}(?:\s|[\-\.])?\d{1,4}(?:\s|[\-\.])?\d{1,9}$

See the other validators in the :doc:`library <index>`.
