arxiv
=====

**Publishing** · :doc:`Back to the library <index>`

An arXiv paper identifier.

.. code-block:: python

   from edify.library import arxiv

   arxiv('2401.12345')   # True
   arxiv('arxiv')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 2401.12345|1234.5678|arxiv|abc

   from edify.library import arxiv
   arxiv

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:\d{4}\.\d{4,5}(?:v\d+)?|[a-z]{2,10}(?:\.[A-Z]{2})?/\d{7}(?:v\d+)?)$

How it reads
------------

.. code-block:: text

   - The text must start with either exactly 4 digits (0-9), then ".", then between 4 and 5 digits (0-9), then an optional "v", then one or more digits (0-9) or between 2 and 10 lowercase letters (a-z), then an optional ".", then exactly 2 uppercase letters (A-Z), then "/", then exactly 7 digits (0-9), then an optional "v", then one or more digits (0-9).

See the other validators in the :doc:`library <index>`.
