hostname
========

**Address** · :doc:`Back to the library <index>`

A host name — a domain or a bare label.

.. code-block:: python

   from edify.library import hostname

   hostname('example.com')   # True
   hostname('not a host')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: example.com|localhost|sub.example.io|not a host|@@@

   from edify.library import hostname
   hostname

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?=.{1,253}$)(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*$

See the other validators in the :doc:`library <index>`.
