base
====

**Text** · :doc:`Back to the library <index>`

A base-encoded string.

.. code-block:: python

   from edify.library import base

   base('0Aa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 0Aa|2A2A====

   from edify.library import base
   base

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:[0-9A-Fa-f]+|[A-Z2-7]+=*|[1-9A-HJ-NP-Za-km-z]+|[A-Za-z0-9\+/]+=*|[A-Za-z0-9_\-]+)$

See the other validators in the :doc:`library <index>`.
