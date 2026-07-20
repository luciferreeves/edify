card
====

**Finance** · :doc:`Back to the library <index>`

A payment-card number.

.. code-block:: python

   from edify.library import card

   card('4111111111111111')   # True
   card('1234')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 4111111111111111|5500005555555559|1234|abcd

   from edify.library import card
   card

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{1,7}$

How it reads
------------

.. code-block:: text

   - The text must start with exactly 4 digits (0-9).
   - Optional: one character from the set "- ".
   - Then the text must have exactly 4 digits (0-9).
   - Optional: one character from the set "- ".
   - Then the text must have exactly 4 digits (0-9).
   - Optional: one character from the set "- ".
   - Then the text must have between 1 and 7 digits (0-9).

See the other validators in the :doc:`library <index>`.
