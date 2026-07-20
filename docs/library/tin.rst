tin
===

**Identifiers** · :doc:`Back to the library <index>`

A taxpayer identification number.

.. code-block:: python

   from edify.library import tin

   tin('123-12-1234')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 123-12-1234|23-2345678

   from edify.library import tin
   tin

Pattern
-------

The regex this validator emits:

.. code-block:: text

   (?:^(?!(?:666|000|9\d{2}))\d{3}\-(?!00)\d{2}\-(?!0{4})\d{4}$|^\d{2}\-\d{7}$|^9\d{2}\-(?:5\d|6[0-5]|7\d|8[0-8]|9[0-2]|9[4-9])\-\d{4}$)

See the other validators in the :doc:`library <index>`.
