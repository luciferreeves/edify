csp
===

**Web** · :doc:`Back to the library <index>`

A Content-Security-Policy directive.

.. code-block:: python

   from edify.library import csp


Edit the string, or the pattern itself:

.. edify-playground::

   from edify.library import csp
   csp

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-z\-]+\s+(?:(?!;).)+(?:;\s*[a-z\-]+\s+(?:(?!;).)+)*;?$

See the other validators in the :doc:`library <index>`.
