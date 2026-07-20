barcode
=======

**Product** · :doc:`Back to the library <index>`

A product barcode.

.. code-block:: python

   from edify.library import barcode

   barcode('A0A0A0')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: A0A0A0|0A0A0A0

   from edify.library import barcode
   barcode

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z0-9]{6,48}$

How it reads
------------

.. code-block:: text

   - The text must start with between 6 and 48 of either one character from "A" through "Z" or one character from "0" through "9".

See the other validators in the :doc:`library <index>`.
