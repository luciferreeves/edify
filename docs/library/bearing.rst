bearing
=======

**Geo** · :doc:`Back to the library <index>`

A compass bearing in degrees.

.. code-block:: python

   from edify.library import bearing

   bearing('122')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 122

   from edify.library import bearing
   bearing

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:360(?:\.0+)?|(?:3[0-5]\d|[1-2]\d\d|\d{1,2})(?:\.\d+)?)°?$

How it reads
------------

.. code-block:: text

   - The text must start with either "360", then an optional ".", then one or more copies of the character "0" or either "3", then one character from "0" through "5", then one digit (0-9), one character from "1" through "2", then one digit (0-9), then one digit (0-9), or between 1 and 2 digits (0-9), then an optional ".", then one or more digits (0-9).
   - Optional: "°".

See the other validators in the :doc:`library <index>`.
