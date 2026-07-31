GraphQL
=======

A `GraphQL <https://spec.graphql.org/>`__ document is either an *executable*
document — the queries and mutations a client sends — or a *type system* document,
the schema a server publishes. **GraphQL** recognises both, because both are
written in the same language and both begin with a small, fixed set of openings.

Those openings are the branches of an :func:`~edify.any_of`: a definition keyword
followed by whitespace or a punctuator, a ``#`` comment, or the shorthand anonymous
query — a selection set in braces. The anonymous form requires a field name after
the brace, which is what keeps a JSON object from being mistaken for a query.

Executable documents
--------------------

Named or anonymous operations, and the fragments they use:

.. edify-playground::

   from edify.library import graphql

   graphql("query GetUser { user { id } }")    # a named query
   graphql("mutation { addUser(name: \"a\") }")  # a mutation
   graphql("subscription { events }")           # a subscription
   graphql("fragment F on User { id }")         # a fragment
   graphql("{ user { id } }")                   # the anonymous shorthand

Type system documents
---------------------

The schema side of the language — the definitions a server exposes:

.. edify-playground::

   from edify.library import graphql

   graphql("type User {\n  id: ID!\n}")     # an object type
   graphql("schema {\n  query: Query\n}")   # the schema entry point
   graphql("enum Role { ADMIN USER }")      # an enum
   graphql("input Filter { q: String }")    # an input type
   graphql("scalar DateTime")               # a custom scalar

Why JSON is not a query
-----------------------

The anonymous shorthand is a brace followed by a *field name*, so a JSON object —
whose first token inside the brace is a quoted key — is rejected. That distinction
matters when the same endpoint handles both:

.. edify-playground::

   from edify.library import graphql

   graphql("{ me { name } }")   # a field name follows the brace
   graphql('{"a": 1}')          # a quoted key: JSON, not GraphQL
   graphql("hello-world")       # not a document

It checks that a document opens as GraphQL, not that the whole document parses or
that the fields exist in a schema. For the JSON payload a GraphQL server returns,
see :doc:`jsonapi` or :doc:`hal` for the REST equivalents.
