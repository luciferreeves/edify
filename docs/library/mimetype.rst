mimetype
========

**Media** · :doc:`Back to the library <index>`

A MIME media type.

.. code-block:: python

   from edify.library import mimetype

   mimetype('text/html')   # True
   mimetype('nope')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: text/html|application/json|image/png|nope|text

   from edify.library import mimetype
   mimetype

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-zA-Z][a-zA-Z0-9!\#\$\&\-\^_\.\+]*/[a-zA-Z][a-zA-Z0-9!\#\$\&\-\^_\.\+]*$

See the other validators in the :doc:`library <index>`.
