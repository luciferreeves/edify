plate
=====

**Transport** · :doc:`Back to the library <index>`

A vehicle license plate.

.. code-block:: python

   from edify.library import plate

   plate('A-A')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: A-A|0A0A

   from edify.library import plate
   plate

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z0-9]{1,3}[- ]?[A-Z0-9]{1,4}$

How it reads
------------

.. code-block:: text

   - The text must start with between 1 and 3 of either one character from "A" through "Z" or one character from "0" through "9".
   - Optional: one character from the set "- ".
   - Then the text must have between 1 and 4 of either one character from "A" through "Z" or one character from "0" through "9".

See the other validators in the :doc:`library <index>`.
