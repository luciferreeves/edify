iata
====

**Identifiers** · :doc:`Back to the library <index>`

An IATA airport code.

.. code-block:: python

   from edify.library import iata

   iata('AA')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: AA|AAA

   from edify.library import iata
   iata

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z]{2,3}$

How it reads
------------

.. code-block:: text

   - The text must start with between 2 and 3 of one character from "A" through "Z".

See the other validators in the :doc:`library <index>`.
