iccid
=====

**Identifiers** · :doc:`Back to the library <index>`

A SIM card ICCID.

.. code-block:: python

   from edify.library import iccid

   iccid('1234567890123456789')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 1234567890123456789|23456789012345678901

   from edify.library import iccid
   iccid

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{19,22}$

How it reads
------------

.. code-block:: text

   - The text must start with between 19 and 22 digits (0-9).

See the other validators in the :doc:`library <index>`.
