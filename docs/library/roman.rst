roman
=====

**Numeric** · :doc:`Back to the library <index>`

A Roman numeral.

.. code-block:: python

   from edify.library import roman

   roman('XIV')   # True
   roman('ABC')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: XIV|MMXXIV|IX|ABC|123

   from edify.library import roman
   roman

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^M{0,3}(?:(?:CM|CD|D?C{0,3}))(?:(?:XC|XL|L?X{0,3}))(?:(?:IX|IV|V?I{0,3}))$

How it reads
------------

.. code-block:: text

   - The text must start with between 0 and 3 copies of the character "M".
   - Then the text must have either "CM", "CD", or an optional "D", then between 0 and 3 copies of the character "C".
   - Then the text must have either "XC", "XL", or an optional "L", then between 0 and 3 copies of the character "X".
   - Then the text must have either "IX", "IV", or an optional "V", then between 0 and 3 copies of the character "I".

See the other validators in the :doc:`library <index>`.
