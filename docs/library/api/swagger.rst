Swagger
=======

`Swagger <https://swagger.io/specification/v2/>`__ is the name the OpenAPI
specification carried before version 3, and a 2.0 document announces itself with a
top-level ``swagger`` field whose value is exactly the string ``2.0``. **Swagger**
looks for that declaration, which is the one reliable way to tell a 2.0 document
apart from the :doc:`openapi` documents that replaced it.

Like its successor the declaration appears in two serialisations, so the two forms
are the branches of an :func:`~edify.any_of`: a quoted member inside a JSON object,
or a bare key at the start of a YAML document. The version is pinned with
:meth:`~edify.RegexBuilder.string`, so only ``2.0`` matches.

Both serialisations
-------------------

YAML with the version quoted or bare, and the same declaration as a JSON member:

.. edify-playground::

   from edify.library import swagger

   swagger('swagger: "2.0"\ninfo:\n  title: Orders')   # YAML, quoted
   swagger("swagger: 2.0")                             # YAML, bare
   swagger('{"swagger": "2.0", "info": {}}')           # JSON
   swagger("swagger:   '2.0'")                         # loose spacing

Only version 2.0
----------------

The version is not a range. A 3.x document belongs to :doc:`openapi`, and a
``swagger`` key carrying any other value is not a Swagger 2.0 specification:

.. edify-playground::

   from edify.library import swagger

   swagger('swagger: "3.0"')     # no such Swagger version
   swagger("openapi: 3.0.0")     # that is OpenAPI
   swagger("hello-world")        # not a specification

It checks the declaration, not the body of the specification — paths, definitions,
and responses are left to a full parser. For the current specification see
:doc:`openapi`.
