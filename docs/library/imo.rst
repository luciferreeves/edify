imo
===

**Identifiers** · :doc:`Back to the library <index>`

An IMO ship identification number.

.. code-block:: python

   from edify.library import imo

   imo('IMO1234567')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: IMO1234567|IMO2345678

   from edify.library import imo
   imo

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^IMO\d{7}$

How it reads
------------

.. code-block:: text

   - The text must start with "IMO".
   - Then the text must have exactly 7 digits (0-9).

See the other validators in the :doc:`library <index>`.
