Identifiers
===========

Every validator in the :doc:`Identifiers <../../library/identifier/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/identifier/index>`.

.. py:data:: edify.library.arn

   Callable :class:`Pattern` for the AWS ARN shape:
   ``arn:PARTITION:SERVICE:REGION:ACCOUNT_ID:RESOURCE``.

   Full description: :doc:`ARN <../../library/identifier/arn>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      arn = (
          Pattern()
          .start_of_input()
          .string("arn:")
          .one_or_more()
          .any_of()
          .range("a", "z")
          .char("-")
          .end()
          .char(":")
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .char("-")
          .end()
          .char(":")
          .zero_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .char("-")
          .end()
          .char(":")
          .zero_or_more()
          .digit()
          .char(":")
          .one_or_more()
          .any_char()
          .end_of_input()
      )

   **Emits** ``^arn:[a-z\-]+:[a-z0-9\-]+:[a-z0-9\-]*:\d*:.+$``

.. py:data:: edify.library.asin

   Callable :class:`Pattern` for the 10-character alphanumeric ASIN shape.

   Full description: :doc:`ASIN <../../library/identifier/asin>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      asin = (
          Pattern()
          .start_of_input()
          .exactly(10)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Z0-9]{10}$``

.. py:data:: edify.library.bic

   Callable :class:`Pattern` for the ISO 9362 BIC/SWIFT shape:
   4-letter bank code + 2-letter country + 2-alphanumeric location + optional
   3-alphanumeric branch (8 or 11 characters total).

   Full description: :doc:`BIC <../../library/identifier/bic>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      bic = (
          Pattern()
          .start_of_input()
          .exactly(4)
          .any_of()
          .range("A", "Z")
          .end()
          .exactly(2)
          .any_of()
          .range("A", "Z")
          .end()
          .exactly(2)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .optional()
          .subexpression(Pattern().exactly(3).any_of().range("A", "Z").range("0", "9").end())
          .end_of_input()
      )

   **Emits** ``^[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}(?:[A-Z0-9]{3})?$``

.. py:data:: edify.library.cusip

   Callable :class:`Pattern` for the 9-character alphanumeric CUSIP shape.

   Full description: :doc:`CUSIP <../../library/identifier/cusip>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      cusip = (
          Pattern()
          .start_of_input()
          .exactly(9)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Z0-9]{9}$``

.. py:data:: edify.library.did

   Callable :class:`Pattern` for the DID shape: literal ``did:`` +
   lowercase-alphanumeric method name + colon + identifier body.

   Full description: :doc:`DID <../../library/identifier/did>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      did = (
          Pattern()
          .start_of_input()
          .string("did:")
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .end()
          .char(":")
          .one_or_more()
          .any_char()
          .end_of_input()
      )

   **Emits** ``^did:[a-z0-9]+:.+$``

.. py:data:: edify.library.ein

   Callable :class:`Pattern` for the US EIN ``XX-XXXXXXX`` shape.

   Full description: :doc:`EIN <../../library/identifier/ein>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      ein = Pattern().start_of_input().exactly(2).digit().char("-").exactly(7).digit().end_of_input()

   **Emits** ``^\d{2}\-\d{7}$``

.. py:data:: edify.library.guid

   Callable :class:`Pattern` for the Microsoft-flavour GUID 8-4-4-4-12 hex shape.

   Guarantees:
       * 32 hex digits in 8-4-4-4-12 layout with hyphen separators.
       * Either case is accepted; the braces are optional and independent.
       * Anchored at both ends.

   Does not guarantee:
       * Balanced-brace enforcement — a leading ``{`` without a trailing ``}`` and vice
         versa both pass. Use :data:`edify.library.uuid` for the version- and variant-locked
         RFC 4122 form, or validate braces separately if you require them matched.
       * Version or variant digit values — every hex digit passes.

   Full description: :doc:`GUID <../../library/identifier/guid>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      guid = (
          Pattern()
          .start_of_input()
          .optional()
          .char("{")
          .exactly(8)
          .any_of()
          .range("0", "9")
          .range("a", "f")
          .range("A", "F")
          .end()
          .char("-")
          .exactly(4)
          .any_of()
          .range("0", "9")
          .range("a", "f")
          .range("A", "F")
          .end()
          .char("-")
          .exactly(4)
          .any_of()
          .range("0", "9")
          .range("a", "f")
          .range("A", "F")
          .end()
          .char("-")
          .exactly(4)
          .any_of()
          .range("0", "9")
          .range("a", "f")
          .range("A", "F")
          .end()
          .char("-")
          .exactly(12)
          .any_of()
          .range("0", "9")
          .range("a", "f")
          .range("A", "F")
          .end()
          .optional()
          .char("}")
          .end_of_input()
      )

   **Emits** ``^\{?[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}\}?$``

.. py:data:: edify.library.iata

   Callable :class:`Pattern` for the IATA code shape: 2 uppercase letters
   (airline) or 3 uppercase letters (airport).

   Full description: :doc:`IATA <../../library/identifier/iata>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      iata = Pattern().start_of_input().between(2, 3).any_of().range("A", "Z").end().end_of_input()

   **Emits** ``^[A-Z]{2,3}$``

.. py:data:: edify.library.iban

   Callable :class:`Pattern` for the IBAN shape: 2-letter ISO country code +
   2 check digits + 1-30 uppercase-alphanumeric BBAN characters.

   Full description: :doc:`IBAN <../../library/identifier/iban>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      iban = (
          Pattern()
          .start_of_input()
          .exactly(2)
          .any_of()
          .range("A", "Z")
          .end()
          .exactly(2)
          .digit()
          .between(1, 30)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Z]{2}\d{2}[A-Z0-9]{1,30}$``

.. py:data:: edify.library.icao

   Callable :class:`Pattern` for the ICAO code shape: 3 uppercase letters
   (airline) or 4 uppercase letters (airport).

   Full description: :doc:`ICAO <../../library/identifier/icao>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      icao = Pattern().start_of_input().between(3, 4).any_of().range("A", "Z").end().end_of_input()

   **Emits** ``^[A-Z]{3,4}$``

.. py:data:: edify.library.iccid

   Callable :class:`Pattern` for the ICCID shape: 19 to 22 decimal digits.

   Full description: :doc:`ICCID <../../library/identifier/iccid>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      iccid = Pattern().start_of_input().between(19, 22).digit().end_of_input()

   **Emits** ``^\d{19,22}$``

.. py:data:: edify.library.imei

   Callable :class:`Pattern` for the 15-digit IMEI shape.

   Full description: :doc:`IMEI <../../library/identifier/imei>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      imei = Pattern().start_of_input().exactly(15).digit().end_of_input()

   **Emits** ``^\d{15}$``

.. py:data:: edify.library.imo

   Callable :class:`Pattern` for the IMO ship-number shape: literal
   ``IMO`` followed by 7 digits.

   Full description: :doc:`IMO <../../library/identifier/imo>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      imo = Pattern().start_of_input().string("IMO").exactly(7).digit().end_of_input()

   **Emits** ``^IMO\d{7}$``

.. py:data:: edify.library.isin

   Callable :class:`Pattern` for the ISO 6166 ISIN shape: 2-letter country
   code + 9 alphanumeric identifier characters + 1 check digit.

   Full description: :doc:`ISIN <../../library/identifier/isin>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      isin = (
          Pattern()
          .start_of_input()
          .exactly(2)
          .any_of()
          .range("A", "Z")
          .end()
          .exactly(9)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .digit()
          .end_of_input()
      )

   **Emits** ``^[A-Z]{2}[A-Z0-9]{9}\d$``

.. py:data:: edify.library.itin

   Callable :class:`Pattern` for the US ITIN ``9NN-YY-ZZZZ`` shape (area starts
   with 9; group in ``50``-``65``, ``70``-``88``, ``90``-``92``, or ``94``-``99``).

   Full description: :doc:`ITIN <../../library/identifier/itin>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      _group_range = any_of(
          Pattern().char("5").digit(),
          Pattern().char("6").range("0", "5"),
          Pattern().char("7").digit(),
          Pattern().char("8").range("0", "8"),
          Pattern().char("9").range("0", "2"),
          Pattern().char("9").range("4", "9"),
      )

      itin = (
          Pattern()
          .start_of_input()
          .char("9")
          .exactly(2)
          .digit()
          .char("-")
          .subexpression(_group_range)
          .char("-")
          .exactly(4)
          .digit()
          .end_of_input()
      )

      del _group_range

   **Emits** ``^9\d{2}\-(?:5\d|6[0-5]|7\d|8[0-8]|9[0-2]|9[4-9])\-\d{4}$``

.. py:data:: edify.library.lei

   Callable :class:`Pattern` for the ISO 17442 LEI: 20 uppercase-alphanumeric characters.

   Full description: :doc:`LEI <../../library/identifier/lei>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      lei = (
          Pattern()
          .start_of_input()
          .exactly(20)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Z0-9]{20}$``

.. py:data:: edify.library.mac

   Callable :class:`Pattern` for the IEEE 802 MAC-address shape.

   Guarantees:
       * Six 2-hex-digit octets separated by ``:`` or ``-``.
       * Either case is accepted.
       * Separator is uniform: mixed ``:`` and ``-`` in the same address is rejected.
       * Anchored at both ends.

   Does not guarantee:
       * OUI or IANA-assignment validity — every syntactically-valid octet passes.
       * Dot-separated Cisco-style ``0000.5e00.53af``, bare 12-hex-digit ``00005e0053af``,
         or EUI-64 8-octet ``00:00:5e:ff:fe:00:53:af`` — those forms require dedicated
         validators.

   Full description: :doc:`MAC <../../library/identifier/mac>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      mac = (
          Pattern()
          .start_of_input()
          .exactly(5)
          .group()
          .exactly(2)
          .any_of()
          .range("0", "9")
          .range("a", "f")
          .range("A", "F")
          .end()
          .any_of_chars(":-")
          .end()
          .exactly(2)
          .any_of()
          .range("0", "9")
          .range("a", "f")
          .range("A", "F")
          .end()
          .end_of_input()
      )

   **Emits** ``^(?:[0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}$``

.. py:data:: edify.library.meid

   Callable :class:`Pattern` for the 14-character uppercase-hex MEID shape.

   Full description: :doc:`MEID <../../library/identifier/meid>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      meid = (
          Pattern()
          .start_of_input()
          .exactly(14)
          .any_of()
          .range("0", "9")
          .range("A", "F")
          .end()
          .end_of_input()
      )

   **Emits** ``^[0-9A-F]{14}$``

.. py:data:: edify.library.mmsi

   Callable :class:`Pattern` for the 9-digit MMSI shape.

   Full description: :doc:`MMSI <../../library/identifier/mmsi>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      mmsi = Pattern().start_of_input().exactly(9).digit().end_of_input()

   **Emits** ``^\d{9}$``

.. py:data:: edify.library.orcid

   Callable :class:`Pattern` for the ORCID identifier shape:
   four hyphen-separated groups of four digits, with the last position
   allowing an ``X`` check character.

   Full description: :doc:`ORCID <../../library/identifier/orcid>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      orcid = (
          Pattern()
          .start_of_input()
          .exactly(4)
          .digit()
          .char("-")
          .exactly(4)
          .digit()
          .char("-")
          .exactly(4)
          .digit()
          .char("-")
          .exactly(3)
          .digit()
          .any_of()
          .digit()
          .char("X")
          .end()
          .end_of_input()
      )

   **Emits** ``^\d{4}\-\d{4}\-\d{4}\-\d{3}(?:\d|[X])$``

.. py:data:: edify.library.sedol

   Callable :class:`Pattern` for the 7-character SEDOL shape:
   6 body characters (consonants + digits, excluding vowels) + 1 check digit.

   Full description: :doc:`SEDOL <../../library/identifier/sedol>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      sedol = (
          Pattern()
          .start_of_input()
          .exactly(6)
          .any_of()
          .range("B", "D")
          .range("F", "H")
          .range("J", "N")
          .range("P", "T")
          .range("V", "X")
          .range("Y", "Z")
          .range("0", "9")
          .end()
          .digit()
          .end_of_input()
      )

   **Emits** ``^[B-DF-HJ-NP-TV-XY-Z0-9]{6}\d$``

.. py:data:: edify.library.sku

   Callable :class:`Pattern` for a permissive SKU shape: 4-20 characters
   drawn from letters, digits, and common product-code separators
   (``-``, ``_``, ``.``, ``/``).

   Full description: :doc:`SKU <../../library/identifier/sku>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      sku = (
          Pattern()
          .start_of_input()
          .between(4, 20)
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("-_./")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Za-z0-9-_./]{4,20}$``

.. py:data:: edify.library.ssn

   Callable :class:`Pattern` for the US ``AAA-GG-SSSS`` Social Security Number shape.

   Guarantees:
       * Three-digit area, two-digit group, four-digit serial, hyphen-separated.
       * Documented blocked ranges rejected: ``000`` / ``666`` / ``9xx`` area, ``00``
         group, ``0000`` serial.
       * Anchored at both ends.

   Does not guarantee:
       * Assignment or issuance history — a shape that clears the blocked ranges may
         still be unassigned.
       * Non-US national identifiers (SIN, NIN, DNI, etc.) — those need dedicated
         validators.

   Full description: :doc:`SSN <../../library/identifier/ssn>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      _blocked_area = any_of(
          Pattern().string("666"),
          Pattern().string("000"),
          Pattern().char("9").exactly(2).digit(),
      )

      ssn = (
          Pattern()
          .start_of_input()
          .assert_not_ahead()
          .subexpression(_blocked_area)
          .end()
          .exactly(3)
          .digit()
          .char("-")
          .assert_not_ahead()
          .string("00")
          .end()
          .exactly(2)
          .digit()
          .char("-")
          .assert_not_ahead()
          .exactly(4)
          .char("0")
          .end()
          .exactly(4)
          .digit()
          .end_of_input()
      )

      del _blocked_area

   **Emits** ``^(?!(?:666|000|9\d{2}))\d{3}\-(?!00)\d{2}\-(?!0{4})\d{4}$``

.. py:data:: edify.library.tin

   Callable :class:`Pattern` that accepts any US Taxpayer ID form: SSN
   (``AAA-GG-SSSS``), EIN (``XX-XXXXXXX``), or ITIN (``9NN-YY-ZZZZ``).

   Full description: :doc:`TIN <../../library/identifier/tin>`

   **How it is built**

   .. code-block:: python

      from edify import any_of
      from edify.library.identifier.ein import ein
      from edify.library.identifier.itin import itin
      from edify.library.identifier.ssn import ssn

      tin = any_of(ssn, ein, itin)

   **Emits** ``(?:^(?!(?:666|000|9\d{2}))\d{3}\-(?!00)\d{2}\-(?!0{4})\d{4}$|^\d{2}\-\d{7}$|^9\d{2}\-(?:5\d|6[0-5]|7\d|8[0-8]|9[0-2]|9[4-9])\-\d{4}$)``

.. py:data:: edify.library.uuid

   Callable :class:`Pattern` for the canonical UUID 8-4-4-4-12 lowercase-hex shape.

   Guarantees:
       * Exactly 32 lowercase hex digits arranged 8-4-4-4-12 with hyphen separators.
       * Version digit pinned to ``1``-``5`` and variant digit pinned to ``8``-``b``.
       * Anchored at both ends.

   Does not guarantee:
       * Uppercase hex — use :data:`edify.library.guid` if either case is required.
       * Brace-wrapped, urn-prefixed, or version-6/7/8 UUIDs.

   Full description: :doc:`UUID <../../library/identifier/uuid>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      uuid = (
          Pattern()
          .start_of_input()
          .exactly(8)
          .any_of()
          .range("0", "9")
          .range("a", "f")
          .end()
          .char("-")
          .exactly(4)
          .any_of()
          .range("0", "9")
          .range("a", "f")
          .end()
          .char("-")
          .range("0", "5")
          .exactly(3)
          .any_of()
          .range("0", "9")
          .range("a", "f")
          .end()
          .char("-")
          .any_of_chars("089ab")
          .exactly(3)
          .any_of()
          .range("0", "9")
          .range("a", "f")
          .end()
          .char("-")
          .exactly(12)
          .any_of()
          .range("0", "9")
          .range("a", "f")
          .end()
          .end_of_input()
      )

   **Emits** ``^[0-9a-f]{8}\-[0-9a-f]{4}\-[0-5][0-9a-f]{3}\-[089ab][0-9a-f]{3}\-[0-9a-f]{12}$``

.. py:data:: edify.library.vin

   Callable :class:`Pattern` for the ISO 3779 VIN shape: 17 uppercase-alphanumeric
   characters excluding ``I``, ``O``, and ``Q``.

   Full description: :doc:`VIN <../../library/identifier/vin>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      vin = (
          Pattern()
          .start_of_input()
          .exactly(17)
          .any_of()
          .range("A", "H")
          .range("J", "N")
          .char("P")
          .range("R", "Z")
          .range("0", "9")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-HJ-NPR-Z0-9]{17}$``

