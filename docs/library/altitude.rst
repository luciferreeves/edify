altitude
========

**Geo** · :doc:`Back to the library <index>`

An altitude measurement.

.. code-block:: python

   from edify.library import altitude

   altitude('-123.123 m')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: -123.123 m|2345

   from edify.library import altitude
   altitude

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\-?\d+(?:\.\d+)?\s?(?:ft|km|mi|[m])?$

How it reads
------------

.. code-block:: text

   - Optional: "-".
   - Then the text must have one or more digits (0-9).
   - Optional: ".", then one or more digits (0-9).
   - Optional: one whitespace character (space, tab, newline, etc.).
   - Optional: either "m", "ft", "km", or "mi".

See the other validators in the :doc:`library <index>`.
