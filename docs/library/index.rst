Library
=======

Edify ships **228 ready-made validators** — email, URL, semver, IBAN, phone, and
hundreds more. Each is a callable :class:`~edify.Pattern`: import it, call it, get
a ``bool``.

.. code-block:: python

   from edify.library import email, semver, iban

   email("a@b.com")                  # True
   semver("1.2.3")                   # True
   iban("GB82WEST12345698765432")    # True

Every validator is also composable — drop it into a chain with
:meth:`~edify.RegexBuilder.use`, emit its regex with ``to_regex_string()``, or
explain it with :meth:`~edify.Regex.explain` (see :doc:`../guide/seeing`). They're
grouped into topical modules, so ``from edify.library.temporal import date`` and
``from edify.library import date`` reach the same validator.

Try any of them right here — change the import to any name below, and the emitted
regex plus your test strings update live:

.. edify-playground::
   :tests: user@example.com|a.b@test.co|not-an-email|@no.com

   from edify.library import email
   email

Address
-------

Network and location addressing — IP addresses, hostnames, URLs, ports, subnets,
and postal codes.

16 validators:

``cidr`` ``domain`` ``hostname`` ``ip`` ``ipv4`` ``ipv6`` ``path`` ``port`` ``ptr`` ``socket`` ``subdomain`` ``subnet`` ``tld`` ``uri`` ``url`` ``zip_code``

API
---

API-surface and protocol formats — OAuth, OpenAPI, GraphQL, webhooks, and syndication feeds.

12 validators:

``atom`` ``graphql`` ``hal`` ``jsonapi`` ``oauth`` ``openapi`` ``openid`` ``rss`` ``saml`` ``soap`` ``swagger`` ``webhook``

Auth
----

Credentials and secrets — tokens, API keys, one-time passwords, and configurable password policies.

19 validators:

``apikey`` ``bearer`` ``challenge`` ``csrf`` ``hmac`` ``jwt`` ``mfa`` ``mnemonic`` ``otp`` ``passkey`` ``password`` ``pin`` ``refresh`` ``secret`` ``session`` ``signing`` ``sso`` ``token`` ``webauthn``

Color
-----

Color values and palettes — hex and RGB colors, gradients, filters, and swatches.

5 validators:

``color`` ``filter`` ``gradient`` ``palette`` ``swatch``

Contact
-------

Ways to reach a person — email addresses, phone and fax numbers, handles, and usernames.

8 validators:

``address`` ``email`` ``email_rfc_5322`` ``fax`` ``handle`` ``pager`` ``phone`` ``username``

Data
----

Serialization and data-file formats — JSON, YAML, TOML, CSV, XML, and columnar/binary formats.

14 validators:

``avro`` ``csv`` ``hdf5`` ``html`` ``ini`` ``json`` ``msgpack`` ``orc`` ``parquet`` ``protobuf`` ``toml`` ``tsv`` ``xml`` ``yaml``

Documents
---------

Document and office-file types — PDF, DOCX, EPUB, SVG, and their relatives.

11 validators:

``docx`` ``epub`` ``mobi`` ``odt`` ``pdf`` ``pptx`` ``readme`` ``rtf`` ``svg`` ``tex`` ``xlsx``

Finance
-------

Money and banking — card numbers, routing and sort codes, VAT numbers, and crypto wallets.

7 validators:

``card`` ``crypto`` ``currency`` ``routing`` ``sortcode`` ``vat`` ``wallet``

Geo
---

Geographic coordinates and grids — latitude/longitude, geohash, MGRS, and plus codes.

8 validators:

``altitude`` ``bearing`` ``coordinate`` ``geohash`` ``mgrs`` ``place`` ``plus`` ``postal``

Grammar
-------

Grammar-notation formats — BNF, EBNF, ABNF, PEG, ANTLR, and pest.

6 validators:

``abnf`` ``antlr`` ``bnf`` ``ebnf`` ``peg`` ``pest``

Identifiers
-----------

Standardized identifiers — UUID, IBAN, ISIN, VIN, MAC, SSN, and two dozen more.

26 validators:

``arn`` ``asin`` ``bic`` ``cusip`` ``did`` ``ein`` ``guid`` ``iata`` ``iban`` ``icao`` ``iccid`` ``imei`` ``imo`` ``isin`` ``itin`` ``lei`` ``mac`` ``meid`` ``mmsi`` ``orcid`` ``sedol`` ``sku`` ``ssn`` ``tin`` ``uuid`` ``vin``

Media
-----

Media and file metadata — MIME types, encodings, extensions, locales, and globs.

11 validators:

``charset`` ``codec`` ``encoding`` ``extension`` ``favicon`` ``filename`` ``glob`` ``locale`` ``mimetype`` ``regex`` ``shebang``

Medical
-------

Medical data — blood types, DICOM identifiers, and dosages.

4 validators:

``blood`` ``dicom`` ``dosage`` ``medical``

Numeric
-------

Numbers in every shape — integers, decimals, fractions, ratios, percentages, and Roman numerals.

10 validators:

``fraction`` ``hash`` ``integer`` ``natural`` ``number`` ``ordinal`` ``percentage`` ``ratio`` ``roman`` ``scientific``

Product
-------

Product and retail codes — barcodes, GTINs, and manufacturer part numbers.

3 validators:

``barcode`` ``gtin`` ``mpn``

Publishing
----------

Publication identifiers — ISBN, ISSN, DOI, arXiv, and PubMed IDs.

6 validators:

``arxiv`` ``doi`` ``isbn`` ``issn`` ``pmc`` ``pmid``

Security
--------

Cryptographic material — certificates, signing requests, keys, and PEM/PGP/SSH blocks.

11 validators:

``age`` ``certificate`` ``csr`` ``der`` ``keyring`` ``nonce`` ``pem`` ``pgp`` ``signature`` ``ssh`` ``x509``

Software
--------

Software and versioning — semver, Git refs, Docker images, package names, and checksums.

13 validators:

``bump`` ``cargo`` ``checksum`` ``component`` ``digest`` ``docker`` ``git`` ``image`` ``makefile`` ``package`` ``ref`` ``semver`` ``version``

Temporal
--------

Dates, times, and durations — ISO dates, timestamps, cron expressions, and timezones.

12 validators:

``cron`` ``date`` ``datetime`` ``duration`` ``epoch`` ``interval`` ``iso_date`` ``offset`` ``time`` ``timestamp`` ``timezone`` ``year``

Text
----

Text shapes and scripts — alphanumeric, slugs, ASCII, Unicode, emoji, and words.

11 validators:

``alpha`` ``alphanumeric`` ``ascii`` ``base`` ``emoji`` ``numeric`` ``printable`` ``script`` ``slug`` ``unicode`` ``word``

Transport
---------

Transport identifiers — vehicle plates, flight numbers, and aircraft registrations.

4 validators:

``aircraft`` ``flight`` ``plate`` ``vehicle``

Web
---

Web-server and site files — robots.txt, nginx and Apache configs, cookies, and user agents.

11 validators:

``apache`` ``captcha`` ``cookie`` ``csp`` ``htaccess`` ``humans`` ``manifest`` ``nginx`` ``robots`` ``sitemap`` ``useragent``
