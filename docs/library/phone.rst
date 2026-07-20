phone
=====

**Contact** · :doc:`Back to the library <index>`

A telephone number.

.. code-block:: python

   from edify.library import phone

   phone('+1 555 123 4567')   # True
   phone('abc')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: +1 555 123 4567|555-123-4567|abc|phone

   from edify.library import phone
   phone

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:(?:00|[\+])[ .-]?)?(?:\d{1,4}|\(\d{1,4}\))(?:[ .-]?(?:\d{1,4}|\(\d{1,4}\))){1,7}|\d{2,6})$

How it reads
------------

.. code-block:: text

   - The text must start with either an optional either "+" or "00", then an optional one character from the set " .-", then either between 1 and 4 digits (0-9) or "(", then between 1 and 4 digits (0-9), then ")", then between 1 and 7 of an optional one character from the set " .-", then either between 1 and 4 digits (0-9) or "(", then between 1 and 4 digits (0-9), then ")" or between 2 and 6 digits (0-9).

See the other validators in the :doc:`library <index>`.
