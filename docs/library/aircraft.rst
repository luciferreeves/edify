aircraft
========

**Transport** · :doc:`Back to the library <index>`

An aircraft registration.

.. code-block:: python

   from edify.library import aircraft

   aircraft('A-A')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: A-A|BC0A

   from edify.library import aircraft
   aircraft

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z]{1,2}\-?[A-Z0-9]{1,5}$

How it reads
------------

.. code-block:: text

   - The text must start with between 1 and 2 uppercase letters (A-Z).
   - Optional: "-".
   - Then the text must have between 1 and 5 of either one character from "A" through "Z" or one character from "0" through "9".

See the other validators in the :doc:`library <index>`.
