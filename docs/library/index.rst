Library
=======

Edify ships **228 ready-made validators** — email, URL, semver, IBAN,
phone, and hundreds more. Each is a callable :class:`~edify.Pattern`:
import it, call it, get a ``bool``. Every one has its own page below with a
live playground, its emitted regex, and a plain-English reading.

.. code-block:: python

   from edify.library import email, semver, iban

   email("a@b.com")                  # True
   semver("1.2.3")                   # True
   iban("GB82WEST12345698765432")    # True

Validators are also composable — drop one into a chain with
:meth:`~edify.RegexBuilder.use`, or emit its regex with ``to_regex_string()``.

Address
-------

Network and location addressing.

.. toctree::
   :maxdepth: 1

   cidr
   domain
   hostname
   ip
   ipv4
   ipv6
   path
   port
   ptr
   socket
   subdomain
   subnet
   tld
   uri
   url
   zip_code

API
---

API-surface and protocol formats.

.. toctree::
   :maxdepth: 1

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

Auth
----

Credentials and secrets.

.. toctree::
   :maxdepth: 1

   apikey
   bearer
   challenge
   csrf
   hmac
   jwt
   mfa
   mnemonic
   otp
   passkey
   password
   pin
   refresh
   secret
   session
   signing
   sso
   token
   webauthn

Color
-----

Color values and palettes.

.. toctree::
   :maxdepth: 1

   color
   filter
   gradient
   palette
   swatch

Contact
-------

Ways to reach a person.

.. toctree::
   :maxdepth: 1

   address
   email
   email_rfc_5322
   fax
   handle
   pager
   phone
   username

Data
----

Serialization and data-file formats.

.. toctree::
   :maxdepth: 1

   avro
   csv
   hdf5
   html
   ini
   json
   msgpack
   orc
   parquet
   protobuf
   toml
   tsv
   xml
   yaml

Documents
---------

Document and office-file types.

.. toctree::
   :maxdepth: 1

   docx
   epub
   mobi
   odt
   pdf
   pptx
   readme
   rtf
   svg
   tex
   xlsx

Finance
-------

Money and banking.

.. toctree::
   :maxdepth: 1

   card
   crypto
   currency
   routing
   sortcode
   vat
   wallet

Geo
---

Geographic coordinates and grids.

.. toctree::
   :maxdepth: 1

   altitude
   bearing
   coordinate
   geohash
   mgrs
   place
   plus
   postal

Grammar
-------

Grammar-notation formats.

.. toctree::
   :maxdepth: 1

   abnf
   antlr
   bnf
   ebnf
   peg
   pest

Identifiers
-----------

Standardized identifiers.

.. toctree::
   :maxdepth: 1

   arn
   asin
   bic
   cusip
   did
   ein
   guid
   iata
   iban
   icao
   iccid
   imei
   imo
   isin
   itin
   lei
   mac
   meid
   mmsi
   orcid
   sedol
   sku
   ssn
   tin
   uuid
   vin

Media
-----

Media and file metadata.

.. toctree::
   :maxdepth: 1

   charset
   codec
   encoding
   extension
   favicon
   filename
   glob
   locale
   mimetype
   regex
   shebang

Medical
-------

Medical data.

.. toctree::
   :maxdepth: 1

   blood
   dicom
   dosage
   medical

Numeric
-------

Numbers in every shape.

.. toctree::
   :maxdepth: 1

   fraction
   hash
   integer
   natural
   number
   ordinal
   percentage
   ratio
   roman
   scientific

Product
-------

Product and retail codes.

.. toctree::
   :maxdepth: 1

   barcode
   gtin
   mpn

Publishing
----------

Publication identifiers.

.. toctree::
   :maxdepth: 1

   arxiv
   doi
   isbn
   issn
   pmc
   pmid

Security
--------

Cryptographic material.

.. toctree::
   :maxdepth: 1

   age
   certificate
   csr
   der
   keyring
   nonce
   pem
   pgp
   signature
   ssh
   x509

Software
--------

Software and versioning.

.. toctree::
   :maxdepth: 1

   bump
   cargo
   checksum
   component
   digest
   docker
   git
   image
   makefile
   package
   ref
   semver
   version

Temporal
--------

Dates, times, and durations.

.. toctree::
   :maxdepth: 1

   cron
   date
   datetime
   duration
   epoch
   interval
   iso_date
   offset
   time
   timestamp
   timezone
   year

Text
----

Text shapes and scripts.

.. toctree::
   :maxdepth: 1

   alpha
   alphanumeric
   ascii
   base
   emoji
   numeric
   printable
   script
   slug
   unicode
   word

Transport
---------

Transport identifiers.

.. toctree::
   :maxdepth: 1

   aircraft
   flight
   plate
   vehicle

Web
---

Web-server and site files.

.. toctree::
   :maxdepth: 1

   apache
   captcha
   cookie
   csp
   htaccess
   humans
   manifest
   nginx
   robots
   sitemap
   useragent
