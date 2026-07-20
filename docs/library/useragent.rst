useragent
=========

**Web** · :doc:`Back to the library <index>`

A browser User-Agent string.

.. code-block:: python

   from edify.library import useragent

   useragent('Aa0/')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: Aa0/|a0/.-

   from edify.library import useragent
   useragent

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Za-z0-9/\.\-\(\) ;\+_,:]{4,1024}$

How it reads
------------

.. code-block:: text

   - The text must start with between 4 and 1024 of either one character from "A" through "Z", one character from "a" through "z", one character from "0" through "9", "/", ".", "-", "(", ")", " ", ";", "+", "_", ",", or ":".

See the other validators in the :doc:`library <index>`.
