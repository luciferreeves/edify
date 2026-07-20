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
:meth:`~edify.RegexBuilder.use`, or emit its regex with ``to_regex_string()``.

Try any of them right here — change the import to any name below, and the emitted
regex plus your test strings update live:

.. edify-playground::
   :tests: user@example.com|a.b@test.co|not-an-email|@no.com

   from edify.library import email
   email

Address
-------

16 validators:

``cidr`` ``domain`` ``hostname`` ``ip`` ``ipv4`` ``ipv6`` ``path`` ``port`` ``ptr`` ``socket`` ``subdomain`` ``subnet`` ``tld`` ``uri`` ``url`` ``zip_code``

API
---

12 validators:

``atom`` ``graphql`` ``hal`` ``jsonapi`` ``oauth`` ``openapi`` ``openid`` ``rss`` ``saml`` ``soap`` ``swagger`` ``webhook``

Auth
----

19 validators:

``apikey`` ``bearer`` ``challenge`` ``csrf`` ``hmac`` ``jwt`` ``mfa`` ``mnemonic`` ``otp`` ``passkey`` ``password`` ``pin`` ``refresh`` ``secret`` ``session`` ``signing`` ``sso`` ``token`` ``webauthn``

Color
-----

5 validators:

``color`` ``filter`` ``gradient`` ``palette`` ``swatch``

Contact
-------

8 validators:

``address`` ``email`` ``email_rfc_5322`` ``fax`` ``handle`` ``pager`` ``phone`` ``username``

Data
----

14 validators:

``avro`` ``csv`` ``hdf5`` ``html`` ``ini`` ``json`` ``msgpack`` ``orc`` ``parquet`` ``protobuf`` ``toml`` ``tsv`` ``xml`` ``yaml``

Documents
---------

11 validators:

``docx`` ``epub`` ``mobi`` ``odt`` ``pdf`` ``pptx`` ``readme`` ``rtf`` ``svg`` ``tex`` ``xlsx``

Finance
-------

7 validators:

``card`` ``crypto`` ``currency`` ``routing`` ``sortcode`` ``vat`` ``wallet``

Geo
---

8 validators:

``altitude`` ``bearing`` ``coordinate`` ``geohash`` ``mgrs`` ``place`` ``plus`` ``postal``

Grammar
-------

6 validators:

``abnf`` ``antlr`` ``bnf`` ``ebnf`` ``peg`` ``pest``

Identifiers
-----------

26 validators:

``arn`` ``asin`` ``bic`` ``cusip`` ``did`` ``ein`` ``guid`` ``iata`` ``iban`` ``icao`` ``iccid`` ``imei`` ``imo`` ``isin`` ``itin`` ``lei`` ``mac`` ``meid`` ``mmsi`` ``orcid`` ``sedol`` ``sku`` ``ssn`` ``tin`` ``uuid`` ``vin``

Media
-----

11 validators:

``charset`` ``codec`` ``encoding`` ``extension`` ``favicon`` ``filename`` ``glob`` ``locale`` ``mimetype`` ``regex`` ``shebang``

Medical
-------

4 validators:

``blood`` ``dicom`` ``dosage`` ``medical``

Numeric
-------

10 validators:

``fraction`` ``hash`` ``integer`` ``natural`` ``number`` ``ordinal`` ``percentage`` ``ratio`` ``roman`` ``scientific``

Product
-------

3 validators:

``barcode`` ``gtin`` ``mpn``

Publishing
----------

6 validators:

``arxiv`` ``doi`` ``isbn`` ``issn`` ``pmc`` ``pmid``

Security
--------

11 validators:

``age`` ``certificate`` ``csr`` ``der`` ``keyring`` ``nonce`` ``pem`` ``pgp`` ``signature`` ``ssh`` ``x509``

Software
--------

13 validators:

``bump`` ``cargo`` ``checksum`` ``component`` ``digest`` ``docker`` ``git`` ``image`` ``makefile`` ``package`` ``ref`` ``semver`` ``version``

Temporal
--------

12 validators:

``cron`` ``date`` ``datetime`` ``duration`` ``epoch`` ``interval`` ``iso_date`` ``offset`` ``time`` ``timestamp`` ``timezone`` ``year``

Text
----

11 validators:

``alpha`` ``alphanumeric`` ``ascii`` ``base`` ``emoji`` ``numeric`` ``printable`` ``script`` ``slug`` ``unicode`` ``word``

Transport
---------

4 validators:

``aircraft`` ``flight`` ``plate`` ``vehicle``

Web
---

11 validators:

``apache`` ``captcha`` ``cookie`` ``csp`` ``htaccess`` ``humans`` ``manifest`` ``nginx`` ``robots`` ``sitemap`` ``useragent``

