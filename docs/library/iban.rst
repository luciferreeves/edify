iban
====

**Identifiers** · :doc:`Back to the library <index>`

An International Bank Account Number.

.. code-block:: python

   from edify.library import iban

   iban('GB82WEST12345698765432')   # True
   iban('GB00')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: GB82WEST12345698765432|DE89370400440532013000|GB00|12345

   from edify.library import iban
   iban

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Z]{2}\d{2}[A-Z0-9]{1,30}$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 2 of one character from "A" through "Z".
   - Then the text must have exactly 2 digits (0-9).
   - Then the text must have between 1 and 30 of either one character from "A" through "Z" or one character from "0" through "9".

See the other validators in the :doc:`library <index>`.
