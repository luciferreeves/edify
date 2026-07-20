coordinate
==========

**Geo** · :doc:`Back to the library <index>`

A latitude/longitude coordinate.

.. code-block:: python

   from edify.library import coordinate

   coordinate('40.7128,-74.0060')   # True
   coordinate('abc')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 40.7128,-74.0060|0,0|abc|200,200

   from edify.library import coordinate
   coordinate

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\-?(?:90(?:\.0+)?|[0-8]?\d(?:\.\d+)?)\s*,\s*\-?(?:180(?:\.0+)?|(?:1[0-7]\d|[0-9]?\d)(?:\.\d+)?)$

See the other validators in the :doc:`library <index>`.
