sortcode
========

**Finance** · :doc:`Back to the library <index>`

A UK bank sort code.

.. code-block:: python

   from edify.library import sortcode

   sortcode('12-12-12')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 12-12-12|234567

   from edify.library import sortcode
   sortcode

Pattern
-------

The regex this validator emits:

.. code-block:: text

   (?:^\d{2}\-\d{2}\-\d{2}$|^\d{6}$)

How it reads
------------

.. code-block:: text

   - The text must contain either the very beginning of the text, then exactly 2 digits (0-9), then "-", then exactly 2 digits (0-9), then "-", then exactly 2 digits (0-9), then the very end of the text or the very beginning of the text, then exactly 6 digits (0-9), then the very end of the text.

See the other validators in the :doc:`library <index>`.
