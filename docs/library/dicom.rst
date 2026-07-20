dicom
=====

**Medical** · :doc:`Back to the library <index>`

A DICOM identifier.

.. code-block:: python

   from edify.library import dicom

   dicom('123.123.2345.34567')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 123.123.2345.34567|2345.2345.34567.456.5678

   from edify.library import dicom
   dicom

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d+(?:\.\d+)+$

How it reads
------------

.. code-block:: text

   - The text must start with one or more digits (0-9).
   - Then the text must have one or more of ".", then one or more digits (0-9).

See the other validators in the :doc:`library <index>`.
