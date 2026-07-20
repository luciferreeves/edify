isbn
====

**Publishing** · :doc:`Back to the library <index>`

An International Standard Book Number.

.. code-block:: python

   from edify.library import isbn

   isbn('9780306406157')   # True
   isbn('123')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 9780306406157|0-306-40615-2|123|abcd

   from edify.library import isbn
   isbn

Pattern
-------

The regex this validator emits:

.. code-block:: text

   (?:^(?:\d[- ]?){9}(?:\d|[Xx])$|^(?:\d[- ]?){12}\d$)

How it reads
------------

.. code-block:: text

   - The text must contain either the very beginning of the text, then exactly 9 of one digit (0-9), then an optional one character from the set "- ", then either one digit (0-9), "X", or "x", then the very end of the text or the very beginning of the text, then exactly 12 of one digit (0-9), then an optional one character from the set "- ", then one digit (0-9), then the very end of the text.

See the other validators in the :doc:`library <index>`.
