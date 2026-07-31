JSON:API
========

`JSON:API <https://jsonapi.org/>`__ is a specification for how a JSON response
should be shaped. Its central rule is that every document has at least one of three
top-level members — ``data`` for the primary resource, ``errors`` when the request
failed, or ``jsonapi`` describing the version in use — and that ``data`` and
``errors`` must never both appear. **JSON:API** looks for any of the three.

The document is a JSON object whose body carries one of those quoted keys followed
by a colon, matched with :meth:`~edify.RegexBuilder.any_of` over the three names.
:meth:`~edify.RegexBuilder.dot_all` allows the multi-line bodies real responses
have.

Primary data
------------

A single resource, a collection, or an explicit null for an empty to-one
relationship:

.. edify-playground::

   from edify.library import jsonapi

   jsonapi('{"data": {"type": "orders", "id": "1"}}')
   jsonapi('{"data": [{"type": "orders", "id": "1"}]}')
   jsonapi('{"data": null}')
   jsonapi('{\n  "data": {\n    "type": "users",\n    "id": "9"\n  }\n}')

Errors and version
------------------

A failed request returns ``errors`` instead of ``data``; the ``jsonapi`` member
declares the specification version:

.. edify-playground::

   from edify.library import jsonapi

   jsonapi('{"errors": [{"status": "404", "title": "Not Found"}]}')
   jsonapi('{"jsonapi": {"version": "1.1"}}')
   jsonapi('{"errors": []}')

Ordinary JSON is not JSON:API
-----------------------------

A document without any of the three members does not conform, however valid the
JSON:

.. edify-playground::

   from edify.library import jsonapi

   jsonapi('{"data": {"id": "1"}}')          # a top-level member is present
   jsonapi('{"id": 1, "type": "orders"}')   # no top-level member
   jsonapi("{}")                             # empty object
   jsonapi("hello-world")                    # not JSON

It checks that a top-level member is present — not the resource-object rules, the
``data``/``errors`` exclusion, or member ordering. For the other hypermedia
convention see :doc:`hal`.
