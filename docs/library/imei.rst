imei
====

**Identifiers** · :doc:`Back to the library <index>`

A mobile device IMEI.

.. code-block:: python

   from edify.library import imei

   imei('123456789012345')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 123456789012345|234567890123456

   from edify.library import imei
   imei

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{15}$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 15 digits (0-9).

See the other validators in the :doc:`library <index>`.
