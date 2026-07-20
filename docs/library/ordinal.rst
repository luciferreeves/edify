ordinal
=======

**Numeric** · :doc:`Back to the library <index>`

An ordinal such as ``1st`` or ``22nd``.

.. code-block:: python

   from edify.library import ordinal

   ordinal('123st')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 123st|2345nd

   from edify.library import ordinal
   ordinal

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d+(?:(?:st|nd|rd|th))$

How it reads
------------

.. code-block:: text

   - The text must start with one or more digits (0-9).
   - Then the text must have either "st", "nd", "rd", or "th".

See the other validators in the :doc:`library <index>`.
