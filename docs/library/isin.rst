isin
====

**Identifiers** · :doc:`Back to the library <index>`

An International Securities Identification Number.

.. code-block:: python

   from edify.library import isin

   isin('US0378331005')   # True
   isin('123')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: US0378331005|GB0002634946|123|abcd

   from edify.library import isin
   isin

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z]{2}[A-Z0-9]{9}\d$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 2 of one character from "A" through "Z".
   - Then the text must have exactly 9 of either one character from "A" through "Z" or one character from "0" through "9".
   - Then the text must have one digit (0-9).

See the other validators in the :doc:`library <index>`.
