crypto
======

**Finance** · :doc:`Back to the library <index>`

A cryptocurrency address.

.. code-block:: python

   from edify.library import crypto

   crypto('A0A')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: A0A|0A0A

   from edify.library import crypto
   crypto

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z0-9]{3,10}$

How it reads
------------

.. code-block:: text

   - The text must start with between 3 and 10 of either one character from "A" through "Z" or one character from "0" through "9".

See the other validators in the :doc:`library <index>`.
