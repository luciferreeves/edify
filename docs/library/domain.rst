domain
======

**Address** · :doc:`Back to the library <index>`

A DNS domain name such as ``example.com``.

.. code-block:: python

   from edify.library import domain

   domain('example.com')   # True
   domain('not a domain')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: example.com|sub.example.io|not a domain|@@@

   from edify.library import domain
   domain

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}$

How it reads
------------

.. code-block:: text

   - The text must start with one or more of one letter or digit (a-z, A-Z, or 0-9), then an optional at most 61 of either one character from "a" through "z", one character from "A" through "Z", one character from "0" through "9", or "-", then one letter or digit (a-z, A-Z, or 0-9), then ".".
   - Then the text must have between 2 and 63 letters (a-z or A-Z).

See the other validators in the :doc:`library <index>`.
