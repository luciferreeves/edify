subdomain
=========

**Address** · :doc:`Back to the library <index>`

A subdomain label under a parent domain.

.. code-block:: python

   from edify.library import subdomain

   subdomain('aa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: aa|AAA

   from edify.library import subdomain
   subdomain

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]$

How it reads
------------

.. code-block:: text

   - The text must start with either one character from "a" through "z", one character from "A" through "Z", or one character from "0" through "9".
   - Then the text must have between 0 and 61 of either one character from "a" through "z", one character from "A" through "Z", one character from "0" through "9", or "-".
   - Then the text must have either one character from "a" through "z", one character from "A" through "Z", or one character from "0" through "9".

See the other validators in the :doc:`library <index>`.
