timezone
========

**Temporal** · :doc:`Back to the library <index>`

A timezone name or offset.

.. code-block:: python

   from edify.library import timezone

   timezone('UTC')   # True
   timezone('nope')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: UTC|nope|99:99

   from edify.library import timezone
   timezone

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:[A-Z][a-zA-Z_\+\-]+(?:/[A-Z][a-zA-Z_\+\-]+)+|(?:UTC|GMT|UT|[Z])|[A-Z]{2,5})$

How it reads
------------

.. code-block:: text

   - The text must start with either one uppercase letter (A-Z), then one or more of either one character from "a" through "z", one character from "A" through "Z", "_", "+", or "-", then one or more of "/", then one uppercase letter (A-Z), then one or more of either one character from "a" through "z", one character from "A" through "Z", "_", "+", or "-", either "UTC", "GMT", "UT", or "Z", or between 2 and 5 uppercase letters (A-Z).

See the other validators in the :doc:`library <index>`.
