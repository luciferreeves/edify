jwt
===

**Auth** · :doc:`Back to the library <index>`

A JSON Web Token in ``header.payload.signature`` form.

.. code-block:: python

   from edify.library import jwt

   jwt('eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIn0.abc123')   # True
   jwt('notajwt')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIn0.abc123|notajwt|a.b

   from edify.library import jwt
   jwt

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+$

See the other validators in the :doc:`library <index>`.
