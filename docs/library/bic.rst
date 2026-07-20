bic
===

**Identifiers** · :doc:`Back to the library <index>`

A bank BIC / SWIFT code.

.. code-block:: python

   from edify.library import bic

   bic('DEUTDEFF')   # True
   bic('abc')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: DEUTDEFF|NEDSZAJJXXX|abc|12345

   from edify.library import bic
   bic

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}(?:[A-Z0-9]{3})?$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 4 of one character from "A" through "Z".
   - Then the text must have exactly 2 of one character from "A" through "Z".
   - Then the text must have exactly 2 of either one character from "A" through "Z" or one character from "0" through "9".
   - Optional: exactly 3 of either one character from "A" through "Z" or one character from "0" through "9".

See the other validators in the :doc:`library <index>`.
