pmid
====

**Publishing** · :doc:`Back to the library <index>`

A PubMed identifier.

.. code-block:: python

   from edify.library import pmid

   pmid('1')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 1|23

   from edify.library import pmid
   pmid

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{1,8}$

How it reads
------------

.. code-block:: text

   - The text must start with between 1 and 8 digits (0-9).

See the other validators in the :doc:`library <index>`.
