numeric
=======

**Text** · :doc:`Back to the library <index>`

Numeric text (digits only).

.. code-block:: python

   from edify.library import numeric

   numeric('12345')   # True
   numeric('12a')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 12345|007|12a|1.2

   from edify.library import numeric
   numeric

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d+$

How it reads
------------

.. code-block:: text

   - The text must start with one or more digits (0-9).

See the other validators in the :doc:`library <index>`.
