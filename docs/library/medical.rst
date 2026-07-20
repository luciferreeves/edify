medical
=======

**Medical** · :doc:`Back to the library <index>`

A medical record identifier.

.. code-block:: python

   from edify.library import medical

   medical('123456')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 123456|V20

   from edify.library import medical
   medical

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:\d{6,18}|[A-TV-Z]\d[A-Z0-9](?:\.[A-Z0-9]{1,4})?|\d{10}|\d{1,7}\-\d)$

How it reads
------------

.. code-block:: text

   - The text must start with either between 6 and 18 digits (0-9), either one character from "A" through "T" or one character from "V" through "Z", then one digit (0-9), then either one character from "A" through "Z" or one character from "0" through "9", then an optional ".", then between 1 and 4 of either one character from "A" through "Z" or one character from "0" through "9", exactly 10 digits (0-9), or between 1 and 7 digits (0-9), then "-", then one digit (0-9).

See the other validators in the :doc:`library <index>`.
