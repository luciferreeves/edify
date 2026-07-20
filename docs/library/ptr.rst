ptr
===

**Address** · :doc:`Back to the library <index>`

A reverse-DNS PTR name.

.. code-block:: python

   from edify.library import ptr

   ptr('1.23.345.4.in-addr.arpa.')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 1.23.345.4.in-addr.arpa.|345.4.56.678.in-addr.arpa.

   from edify.library import ptr
   ptr

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:\d{1,3}\.){4}in\-addr\.arpa\.?|(?:[0-9a-fA-F]\.){32}ip6\.arpa\.?)$

How it reads
------------

.. code-block:: text

   - The text must start with either exactly 4 of between 1 and 3 digits (0-9), then ".", then "in-addr", then ".", then "arpa", then an optional "." or exactly 32 of either one character from "0" through "9", one character from "a" through "f", or one character from "A" through "F", then ".", then "ip6", then ".", then "arpa", then an optional ".".

See the other validators in the :doc:`library <index>`.
