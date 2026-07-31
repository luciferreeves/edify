OpenAPI
=======

An `OpenAPI <https://spec.openapis.org/oas/latest.html>`__ document describes an
HTTP API — its paths, operations, and schemas. Every version 3 document declares
itself with a top-level ``openapi`` field carrying a ``3.x`` version string, and
that declaration is what **OpenAPI** looks for. It accepts both serialisations the
specification allows, YAML and JSON, because the declaration looks slightly
different in each.

The two forms are the branches of an :func:`~edify.any_of`. The JSON branch expects
the key quoted inside an object; the YAML branch expects it bare at the start of a
document. Both then require a version beginning ``3.``, which is what separates an
OpenAPI document from its predecessor :doc:`swagger`.

YAML documents
--------------

The common form: ``openapi:`` at the top of the file, with the version quoted or
bare. Whitespace around the colon is free:

.. edify-playground::

   from edify.library import openapi

   openapi("openapi: 3.0.0\ninfo:\n  title: Orders")  # a full document
   openapi('openapi: "3.1.0"')                        # a quoted version
   openapi("openapi:   3.0.3")                        # loose spacing
   openapi("openapi: 2.0")                            # version 2 is Swagger

JSON documents
--------------

The same declaration as a quoted member of the root object. It may appear after
other members, so the key is found anywhere inside the braces:

.. edify-playground::

   from edify.library import openapi

   openapi('{"openapi": "3.0.3", "info": {}}')   # the declaration first
   openapi('{"info": {}, "openapi": "3.1.0"}')   # or later in the object
   openapi('{"swagger": "2.0"}')                 # that is Swagger

What it does not check
----------------------

It confirms the document announces itself as OpenAPI 3 — not that the rest of the
specification is valid, that paths resolve, or that schemas are well formed. A
random word or an unrelated document is rejected outright:

.. edify-playground::

   from edify.library import openapi

   openapi("hello-world")   # not a specification
   openapi("")              # empty

For the 2.0 specification use :doc:`swagger`; for the schema language of a
GraphQL API, :doc:`graphql`.
