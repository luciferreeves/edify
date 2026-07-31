Library
=======

Edify ships **228 ready-made validators** across 22 topical categories. Each is a
callable :class:`~edify.Pattern`: import it, call it, get a ``bool``.

.. code-block:: python

   from edify.library import email, semver, iban

   email("a@b.com")                  # True
   semver("1.2.3")                   # True
   iban("GB82WEST12345698765432")    # True

Every validator has its own page covering what it matches, each variant with
verified examples and a live playground you can edit. Browse by category in the
sidebar, or start here:

.. toctree::
   :maxdepth: 1

   address/index
   api/index
   data/index

Categories
----------

- :doc:`address/index` — IP addresses, host and domain names, ports, URLs, paths,
  and postal codes.
- :doc:`api/index` — specification documents and protocol payloads: OpenAPI,
  GraphQL, OAuth, SAML, feeds, and webhooks.
- :doc:`data/index` — serialisation formats: JSON, YAML, XML, CSV, and the binary
  containers behind analytics pipelines.
- **Auth, Color, Contact, Documents, Finance, Geo, Grammar, Identifiers, Media,
  Medical, Numeric, Product, Publishing, Security, Software, Temporal, Text,
  Transport, Web** — being handcrafted, one validator at a time.
