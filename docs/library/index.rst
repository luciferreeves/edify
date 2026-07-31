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
   auth/index
   color/index
   contact/index
   data/index
   document/index
   financial/index
   grammar/index
   media/index
   numeric/index
   security/index
   software/index
   temporal/index
   text/index
   web/index

Categories
----------

- :doc:`address/index` — IP addresses, host and domain names, ports, URLs, paths,
  and postal codes.
- :doc:`api/index` — specification documents and protocol payloads: OpenAPI,
  GraphQL, OAuth, SAML, feeds, and webhooks.
- :doc:`auth/index` — credentials and tokens: JWTs, API keys, one-time codes,
  session and CSRF tokens, passkeys.
- :doc:`color/index` — CSS colours, gradients, filters, and palettes.
- :doc:`contact/index` — email addresses, phone numbers, usernames, and handles.
- :doc:`data/index` — serialisation formats: JSON, YAML, XML, CSV, and the binary
  containers behind analytics pipelines.
- :doc:`document/index` — document formats identified by their content
  signature: PDF, office packages, e-books, and source formats.
- :doc:`financial/index` — payment cards, bank routing identifiers, currency codes,
  and wallet addresses.
- :doc:`grammar/index` — grammar notations: BNF, EBNF, ABNF, PEG, pest, ANTLR.
- :doc:`media/index` — file names, media types, encodings, locales, and globs.
- :doc:`numeric/index` — integers, decimals, percentages, fractions, and Roman
  numerals.
- :doc:`security/index` — cryptographic artifacts: PEM blocks, certificates, SSH
  and PGP keys, nonces, and signatures.
- :doc:`software/index` — versions, package names, container images, and build
  identifiers.
- :doc:`temporal/index` — dates, times, durations, time zones, and cron
  expressions.
- :doc:`text/index` — character classes, encodings, scripts, and slugs.
- :doc:`web/index` — server configuration, site metadata, and HTTP header values.
- **Geo, Identifiers, Medical, Product, Publishing,
  Transport** — being handcrafted, one validator at a time.
