API
===

Specification documents and protocol payloads — the formats an API is described
in, and the messages it exchanges. Each validator is a callable
:class:`~edify.Pattern`: import it, call it with a string, get a ``bool``.

.. code-block:: python

   from edify.library import openapi, graphql, oauth

   openapi('openapi: 3.0.0')          # True
   graphql('query { user { id } }')   # True
   oauth('client_credentials')        # True

.. toctree::
   :hidden:

   atom
   graphql
   hal
   jsonapi
   oauth
   openapi
   openid
   rss
   saml
   soap
   swagger
   webhook

Describing an API
-----------------

- :doc:`openapi` — an ``openapi: 3.x`` specification document.
- :doc:`swagger` — the earlier ``swagger: "2.0"`` specification.
- :doc:`graphql` — a GraphQL query, mutation, or schema definition.

Authorisation and identity
--------------------------

- :doc:`oauth` — an OAuth 2.0 grant type.
- :doc:`openid` — an OpenID Connect discovery endpoint.
- :doc:`saml` — a SAML 2.0 assertion or protocol message.

Message and payload shapes
--------------------------

- :doc:`hal` — a hypertext application language document.
- :doc:`jsonapi` — a JSON:API document.
- :doc:`soap` — a SOAP envelope.
- :doc:`webhook` — a webhook callback endpoint.

Feeds
-----

- :doc:`rss` — an RSS feed; :doc:`atom` — an Atom feed.
