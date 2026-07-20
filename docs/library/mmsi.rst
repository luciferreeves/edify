mmsi
====

**Identifiers** · :doc:`Back to the library <index>`

A Maritime Mobile Service Identity.

.. code-block:: python

   from edify.library import mmsi

   mmsi('123456789')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 123456789|234567890

   from edify.library import mmsi
   mmsi

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{9}$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 9 digits (0-9).

See the other validators in the :doc:`library <index>`.
