pmc
===

**Publishing** · :doc:`Back to the library <index>`

A PubMed Central identifier.

.. code-block:: python

   from edify.library import pmc

   pmc('PMC1')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: PMC1|PMC23

   from edify.library import pmc
   pmc

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^PMC\d{1,9}$

How it reads
------------

.. code-block:: text

   - The text must start with "PMC".
   - Then the text must have between 1 and 9 digits (0-9).

See the other validators in the :doc:`library <index>`.
