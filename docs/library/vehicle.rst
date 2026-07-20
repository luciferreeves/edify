vehicle
=======

**Transport** · :doc:`Back to the library <index>`

A vehicle identifier.

.. code-block:: python

   from edify.library import vehicle

   vehicle('AA0-')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: AA0-|00- A

   from edify.library import vehicle
   vehicle

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z0-9][A-Z0-9\- ]{3,17}$

How it reads
------------

.. code-block:: text

   - The text must start with either one character from "A" through "Z" or one character from "0" through "9".
   - Then the text must have between 3 and 17 of either one character from "A" through "Z", one character from "0" through "9", "-", or " ".

See the other validators in the :doc:`library <index>`.
