offset
======

**Temporal** · :doc:`Back to the library <index>`

A UTC offset such as ``+05:30``.

.. code-block:: python

   from edify.library import offset

   offset('+05:30')   # True
   offset('nope')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: +05:30|-08:00|+00:00|nope|5:30

   from edify.library import offset
   offset

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:[+-](?:0\d|1[0-4]):?[0-5]\d|[Z])$

How it reads
------------

.. code-block:: text

   - The text must start with either "Z" or one character from the set "+-", then either "0", then one digit (0-9) or "1", then one character from "0" through "4", then an optional ":", then one character from "0" through "5", then one digit (0-9).

See the other validators in the :doc:`library <index>`.
