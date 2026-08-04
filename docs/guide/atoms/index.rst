Atoms
=====

An **atom** is a named, reusable regex fragment — the smallest meaningful piece of a
pattern. ``edify.atoms`` ships 83 of them: a ``nibble`` is one hex digit, an
``octet`` is a number from 0 to 255, a ``label`` is one DNS name segment.

Atoms are what the :doc:`../../library/index` validators are built from. The
:doc:`../../library/address/ipv4` validator is four ``octet`` atoms joined by dots;
:doc:`../../library/address/ipv6` is ``nibble`` atoms grouped into hex groups. When
you build your own pattern, reach for an atom before writing the character class by
hand.

Atoms are fragments, not validators
-----------------------------------

This is the one thing to understand before using them. A :doc:`../../library/index`
validator is **anchored** — it matches the whole string. An atom is **not**: it is a
fragment meant to sit inside a larger pattern, so calling one directly searches
rather than matching end to end.

.. edify-playground::

   from edify.atoms import slug

   slug("hello-world")        # the whole string is a slug
   slug("xx hello-world xx")  # True as well — it found a slug inside

That second result is the trap. To ask "is this string *exactly* an octet?", compose
the atom into an anchored pattern:

.. edify-playground::

   from edify import Pattern
   from edify.atoms import octet

   exact = Pattern().start_of_input().use(octet).end_of_input()

   exact("200")   # a valid octet
   exact("255")   # the maximum
   exact("256")   # out of range
   exact("x200")  # anchoring rejects the surrounding text

Composing them
--------------

Drop an atom into a chain with :meth:`~edify.RegexBuilder.use`, repeat it with a
quantifier, or join several — exactly as the library validators do:

.. edify-playground::

   from edify import Pattern
   from edify.atoms import octet

   quad = (
       Pattern().start_of_input()
       .use(octet).exactly(3).group().char(".").use(octet).end()
       .end_of_input()
   )

   quad("192.168.0.1")   # four octets
   quad("256.0.0.1")     # the octet range still applies
   quad("1.2.3")         # only three

Every atom
----------

All 83, alphabetically, with the group page that covers each in full:

.. list-table::
   :header-rows: 1
   :widths: 22 52 26

   * - Atom
     - Matches
     - Group
   * - ``alnum``
     - one ASCII letter or digit
     - :doc:`text`
   * - ``ascii``
     - one character in the 7-bit range
     - :doc:`text`
   * - ``base32``
     - uppercase base32 with optional padding
     - :doc:`encodings`
   * - ``base58``
     - base58, excluding 0 O I l
     - :doc:`encodings`
   * - ``base64``
     - base64 with optional padding
     - :doc:`encodings`
   * - ``base64url``
     - URL-safe base64, unpadded
     - :doc:`encodings`
   * - ``bic``
     - a bank identifier code, 8 or 11 characters
     - :doc:`finance`
   * - ``binnum``
     - a 0b-prefixed binary literal
     - :doc:`numbers`
   * - ``boolean``
     - true/false, yes/no, on/off, or 1/0
     - :doc:`text`
   * - ``braces``
     - a brace-delimited span
     - :doc:`grouping`
   * - ``brackets``
     - a square-bracketed span
     - :doc:`grouping`
   * - ``cidr``
     - an IPv4 address with a prefix length
     - :doc:`network`
   * - ``clock``
     - a 24-hour time, seconds optional
     - :doc:`datetime`
   * - ``clock12``
     - a 12-hour time with AM/PM
     - :doc:`datetime`
   * - ``creditcard``
     - 13 to 19 bare digits
     - :doc:`finance`
   * - ``currency``
     - a three-letter uppercase code
     - :doc:`numbers`
   * - ``day``
     - a day number, 01 to 31
     - :doc:`datetime`
   * - ``decimal``
     - digits on both sides of a point
     - :doc:`numbers`
   * - ``duration``
     - an ISO 8601 duration
     - :doc:`datetime`
   * - ``email``
     - an address in permissive form
     - :doc:`network`
   * - ``epoch``
     - a ten-digit second count
     - :doc:`datetime`
   * - ``extension``
     - a dot and one filename suffix
     - :doc:`web`
   * - ``filename``
     - a name without path separators
     - :doc:`web`
   * - ``filepath``
     - a POSIX or Windows path
     - :doc:`web`
   * - ``floatnum``
     - any float form, exponent optional
     - :doc:`numbers`
   * - ``guid``
     - a hyphenated identifier, any version
     - :doc:`encodings`
   * - ``hexcolor``
     - a #-prefixed colour, 3/4/6/8 digits
     - :doc:`web`
   * - ``hexnum``
     - a 0x-prefixed hex literal
     - :doc:`numbers`
   * - ``hexstring``
     - a bare run of hex digits
     - :doc:`encodings`
   * - ``hostname``
     - dot-joined DNS labels
     - :doc:`network`
   * - ``httpmethod``
     - one of the nine standard verbs
     - :doc:`web`
   * - ``httpstatus``
     - a status code, 100 to 599
     - :doc:`web`
   * - ``iban``
     - an international bank account number
     - :doc:`finance`
   * - ``integer``
     - digits with an optional sign
     - :doc:`numbers`
   * - ``ipv4``
     - four range-checked octets
     - :doc:`network`
   * - ``ipv6``
     - the full, trailing-:: and bare :: forms
     - :doc:`network`
   * - ``isodate``
     - YYYY-MM-DD, shape only
     - :doc:`datetime`
   * - ``isodatetime``
     - a date and time with optional zone
     - :doc:`datetime`
   * - ``label``
     - one DNS name segment
     - :doc:`network`
   * - ``letter``
     - one ASCII letter
     - :doc:`text`
   * - ``line``
     - everything up to a line break
     - :doc:`text`
   * - ``localpart``
     - the part before an @, up to 64 characters
     - :doc:`network`
   * - ``lower``
     - one lowercase ASCII letter
     - :doc:`text`
   * - ``mac``
     - a hardware address, colons or hyphens
     - :doc:`network`
   * - ``md5``
     - 32 hex characters
     - :doc:`encodings`
   * - ``mimetype``
     - type/subtype
     - :doc:`web`
   * - ``money``
     - an amount and a currency code
     - :doc:`numbers`
   * - ``month``
     - a month number, 01 to 12
     - :doc:`datetime`
   * - ``natural``
     - 1 upward, no leading zeros
     - :doc:`numbers`
   * - ``nibble``
     - one hex digit
     - :doc:`network`
   * - ``objectid``
     - 24 hex characters
     - :doc:`encodings`
   * - ``octet``
     - a number from 0 to 255
     - :doc:`network`
   * - ``octnum``
     - a 0o-prefixed octal literal
     - :doc:`numbers`
   * - ``oid``
     - a dotted numeric identifier
     - :doc:`encodings`
   * - ``parens``
     - a parenthesised span
     - :doc:`grouping`
   * - ``percent``
     - a number with a trailing sign
     - :doc:`numbers`
   * - ``port``
     - a port number, 0 to 65535
     - :doc:`network`
   * - ``printable``
     - one visible ASCII character or a space
     - :doc:`text`
   * - ``protocol``
     - one of nine known schemes
     - :doc:`network`
   * - ``quoted``
     - a double-quoted span
     - :doc:`text`
   * - ``ratio``
     - two colon-separated numbers
     - :doc:`numbers`
   * - ``rgbcolor``
     - rgb() or rgba() notation
     - :doc:`web`
   * - ``scheme``
     - any letter-led URI scheme
     - :doc:`network`
   * - ``scientific``
     - a number with a required exponent
     - :doc:`numbers`
   * - ``semver``
     - three dot-joined version numbers
     - :doc:`finance`
   * - ``sha256``
     - 64 hex characters
     - :doc:`encodings`
   * - ``signed``
     - digits with a required sign
     - :doc:`numbers`
   * - ``slug``
     - lowercase words joined by single hyphens
     - :doc:`text`
   * - ``space``
     - one whitespace character
     - :doc:`text`
   * - ``timezone``
     - an offset or Z
     - :doc:`datetime`
   * - ``tld``
     - 2 to 63 letters
     - :doc:`network`
   * - ``truefalse``
     - true or false, any case
     - :doc:`text`
   * - ``ulid``
     - 26 Crockford base32 characters
     - :doc:`encodings`
   * - ``unsigned``
     - bare digits
     - :doc:`numbers`
   * - ``upper``
     - one uppercase ASCII letter
     - :doc:`text`
   * - ``uri``
     - a scheme and a non-space remainder
     - :doc:`network`
   * - ``url``
     - an http or https locator
     - :doc:`network`
   * - ``username``
     - a 3 to 30 character handle
     - :doc:`network`
   * - ``uuid``
     - a hyphenated identifier, version 4 only
     - :doc:`encodings`
   * - ``weekday``
     - a day name or abbreviation
     - :doc:`datetime`
   * - ``word``
     - a run of word characters
     - :doc:`text`
   * - ``year``
     - four digits
     - :doc:`datetime`
   * - ``yesno``
     - yes or no, or y or n
     - :doc:`text`

The eight groups
----------------

.. toctree::
   :hidden:

   network
   numbers
   text
   encodings
   datetime
   web
   finance
   grouping

- :doc:`network` — addresses, hosts, ports, and the pieces they are made of.
- :doc:`numbers` — integers, decimals, bases, and money.
- :doc:`text` — characters, classes, and simple word shapes.
- :doc:`encodings` — base-N alphabets, hashes, and unique identifiers.
- :doc:`datetime` — date, time, and duration components.
- :doc:`web` — HTTP methods and statuses, media types, file names, colours.
- :doc:`finance` — payment and banking fragments, plus version numbers.
- :doc:`grouping` — bracket-delimited spans.
