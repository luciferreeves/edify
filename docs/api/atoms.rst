Atoms
=====

``edify.atoms`` ships 83 named regex fragments — the pieces the
:doc:`../library/index` validators are assembled from. Each is a
:class:`~edify.Pattern`, so it composes with :meth:`~edify.RegexBuilder.use`,
the ``+`` and ``|`` operators, and every other pattern method.

.. code-block:: python

   from edify import Pattern
   from edify.atoms import octet

   quad = Pattern().start_of_input().use(octet).end_of_input()
   quad("255")   # True

.. warning::

   Atoms are **unanchored fragments**, not validators. Calling one directly uses
   search semantics, so ``slug("xx hello-world xx")`` is ``True``. Compose an atom
   into an anchored pattern when you mean "the whole string is this" — see
   :doc:`../guide/atoms/index`.

Each entry below states what the fragment is, shows the chain that builds it, and
ends with the regex it emits. For prose with worked examples and a live playground,
use :doc:`../guide/atoms/index`.

Network
-------

Addresses, hosts, and the pieces they are assembled from. Covered with examples in
:doc:`../guide/atoms/network`.

.. py:data:: edify.atoms.cidr

   Composable :class:`Pattern` fragment for IPv4 CIDR notation.

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of
      from edify.atoms.ipv4 import ipv4

      prefix = any_of(
          Pattern().char("3").range("0", "2"),
          Pattern().range("1", "2").digit(),
          Pattern().digit(),
      )

      cidr = Pattern().use(ipv4).char("/").use(prefix)

   **Emits** ``(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}/(?:3[0-2]|[1-2]\d|\d)``

.. py:data:: edify.atoms.email

   Composable :class:`Pattern` fragment for a permissive email address.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      email = (
          Pattern()
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char(".")
          .char("_")
          .char("+")
          .char("-")
          .end()
          .char("@")
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char(".")
          .char("-")
          .end()
      )

   **Emits** ``[a-zA-Z0-9\._\+\-]+@[a-zA-Z0-9\.\-]+``

.. py:data:: edify.atoms.hostname

   Composable :class:`Pattern` fragment for an RFC 1123 hostname.

   **How it is built**

   .. code-block:: python

      from edify import Pattern
      from edify.atoms.label import label

      hostname = Pattern().use(label).zero_or_more().group().char(".").use(label).end()

   **Emits** ``[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*``

.. py:data:: edify.atoms.ipv4

   Composable :class:`Pattern` fragment for a dotted-quad IPv4 address.

   **How it is built**

   .. code-block:: python

      from edify import Pattern
      from edify.atoms.octet import octet

      ipv4 = Pattern().use(octet).exactly(3).group().char(".").use(octet).end()

   **Emits** ``(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}``

.. py:data:: edify.atoms.ipv6

   Composable :class:`Pattern` fragment for an IPv6 address.

   **How it is built**

   Nine branches: the full eight-group form, a trailing-``::`` form, the six
   interior-compression forms, and a leading-``::`` form.

   .. code-block:: python

      from edify import Pattern, any_of
      from edify.atoms.nibble import nibble

      def hex_group():
          return Pattern().between(1, 4).use(nibble)

      def leading(groups):
          if groups == 1:
              return hex_group().char(":")
          return Pattern().between(1, groups).group().use(hex_group()).char(":").end()

      def trailing(groups):
          if groups == 1:
              return Pattern().char(":").use(hex_group())
          return Pattern().between(1, groups).group().char(":").use(hex_group()).end()

      def compressed(leading_groups, trailing_groups):
          return leading(leading_groups).use(trailing(trailing_groups))

      ipv6 = any_of(
          Pattern().exactly(7).group().use(hex_group()).char(":").end().use(hex_group()),
          leading(7).char(":"),
          compressed(6, 1),
          compressed(5, 2),
          compressed(4, 3),
          compressed(3, 4),
          compressed(2, 5),
          compressed(1, 6),
          Pattern().char(":").group().any_of().use(trailing(7)).char(":").end().end(),
      )

   **Emits** ``(?:(?:(?:[0-9a-fA-F]){1,4}:){7}(?:[0-9a-fA-F]){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,7}:|(?:(?:[0-9a-fA-F]){1,4}:){1,6}:(?:[0-9a-fA-F]){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,5}(?::(?:[0-9a-fA-F]){1,4}){1,2}|(?:(?:[0-9a-fA-F]){1,4}:){1,4}(?::(?:[0-9a-fA-F]){1,4}){1,3}|(?:(?:[0-9a-fA-F]){1,4}:){1,3}(?::(?:[0-9a-fA-F]){1,4}){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,2}(?::(?:[0-9a-fA-F]){1,4}){1,5}|(?:[0-9a-fA-F]){1,4}:(?::(?:[0-9a-fA-F]){1,4}){1,6}|:(?:(?:(?::(?:[0-9a-fA-F]){1,4}){1,7}|[:])))``

.. py:data:: edify.atoms.label

   Composable :class:`Pattern` fragment for one RFC 1123 DNS label
   (letter/digit start, up to 63 chars, letter/digit end).

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      label = (
          Pattern()
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .end()
          .optional()
          .group()
          .between(0, 61)
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char("-")
          .end()
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .end()
          .end()
      )

   **Emits** ``[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?``

.. py:data:: edify.atoms.localpart

   Composable :class:`Pattern` fragment for the local part of an email address.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      localpart = (
          Pattern()
          .between(1, 64)
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char("!")
          .char("#")
          .char("$")
          .char("%")
          .char("&")
          .char("'")
          .char("*")
          .char("+")
          .char("/")
          .char("=")
          .char("?")
          .char("^")
          .char("_")
          .char("`")
          .char("{")
          .char("|")
          .char("}")
          .char("~")
          .char(".")
          .char("-")
          .end()
      )

   **Emits** ``[a-zA-Z0-9!\#\$%\&'\*\+/=\?\^_`\{\|\}\~\.\-]{1,64}``

.. py:data:: edify.atoms.mac

   Composable :class:`Pattern` fragment for a MAC address.

   **How it is built**

   .. code-block:: python

      from edify import Pattern
      from edify.atoms.nibble import nibble

      mac = (
          Pattern()
          .exactly(2)
          .use(nibble)
          .exactly(5)
          .group()
          .any_of_chars(":-")
          .exactly(2)
          .use(nibble)
          .end()
      )

   **Emits** ``(?:[0-9a-fA-F]){2}(?:[:-](?:[0-9a-fA-F]){2}){5}``

.. py:data:: edify.atoms.nibble

   Composable :class:`Pattern` fragment for one mixed-case hex nibble.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      nibble = Pattern().any_of().range("0", "9").range("a", "f").range("A", "F").end()

   **Emits** ``[0-9a-fA-F]``

.. py:data:: edify.atoms.octet

   Composable :class:`Pattern` fragment for a single IPv4 octet (``0``-``255``).

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      octet = any_of(
          Pattern().string("25").range("0", "5"),
          Pattern().char("2").range("0", "4").digit(),
          Pattern().char("1").digit().digit(),
          Pattern().range("1", "9").digit(),
          Pattern().digit(),
      )

   **Emits** ``(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)``

.. py:data:: edify.atoms.port

   Composable :class:`Pattern` fragment for a TCP/UDP port number.

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      port = any_of(
          Pattern().string("6553").range("0", "5"),
          Pattern().string("655").range("0", "2").digit(),
          Pattern().string("65").range("0", "4").digit().digit(),
          Pattern().char("6").range("0", "4").digit().digit().digit(),
          Pattern().range("1", "5").exactly(4).digit(),
          Pattern().range("1", "9").between(0, 3).digit(),
          Pattern().char("0"),
      )

   **Emits** ``(?:6553[0-5]|655[0-2]\d|65[0-4]\d\d|6[0-4]\d\d\d|[1-5]\d{4}|[1-9]\d{0,3}|[0])``

.. py:data:: edify.atoms.protocol

   Composable :class:`Pattern` fragment for a common protocol name.

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      protocol = any_of(
          Pattern().string("https"),
          Pattern().string("http"),
          Pattern().string("ftps"),
          Pattern().string("ftp"),
          Pattern().string("wss"),
          Pattern().string("ws"),
          Pattern().string("ssh"),
          Pattern().string("git"),
          Pattern().string("file"),
      )

   **Emits** ``(?:https|http|ftps|ftp|wss|ws|ssh|git|file)``

.. py:data:: edify.atoms.scheme

   Composable :class:`Pattern` fragment for a URI scheme.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      scheme = (
          Pattern()
          .letter()
          .zero_or_more()
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char("+")
          .char(".")
          .char("-")
          .end()
      )

   **Emits** ``[a-zA-Z][a-zA-Z0-9\+\.\-]*``

.. py:data:: edify.atoms.tld

   Composable :class:`Pattern` fragment for a top-level domain.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      tld = Pattern().between(2, 63).letter()

   **Emits** ``[a-zA-Z]{2,63}``

.. py:data:: edify.atoms.uri

   Composable :class:`Pattern` fragment for a generic URI.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      uri = (
          Pattern()
          .letter()
          .zero_or_more()
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char("+")
          .char(".")
          .char("-")
          .end()
          .char(":")
          .one_or_more()
          .anything_but_chars(" \t\r\n")
      )

   **Emits** ``[a-zA-Z][a-zA-Z0-9\+\.\-]*:[^ \t\r\n]+``

.. py:data:: edify.atoms.url

   Composable :class:`Pattern` fragment for an HTTP/HTTPS URL.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      url = (
          Pattern()
          .string("http")
          .optional()
          .char("s")
          .string("://")
          .one_or_more()
          .anything_but_chars(" \t\r\n")
      )

   **Emits** ``https?://[^ \t\r\n]+``

.. py:data:: edify.atoms.username

   Composable :class:`Pattern` fragment for a social-handle username.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      username = (
          Pattern()
          .between(3, 30)
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char(".")
          .char("_")
          .char("-")
          .end()
      )

   **Emits** ``[a-zA-Z0-9\._\-]{3,30}``

Numbers
-------

Whole numbers, decimals, alternative bases, and money. Covered with examples in
:doc:`../guide/atoms/numbers`.

.. py:data:: edify.atoms.binnum

   Composable :class:`Pattern` fragment for a ``0bNN``-shaped binary literal.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      binnum = Pattern().char("0").any_of_chars("bB").one_or_more().any_of_chars("01")

   **Emits** ``0[bB][01]+``

.. py:data:: edify.atoms.currency

   Composable :class:`Pattern` fragment for an ISO 4217 currency code.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      currency = Pattern().exactly(3).uppercase()

   **Emits** ``[A-Z]{3}``

.. py:data:: edify.atoms.decimal

   Composable :class:`Pattern` fragment for a decimal number ``digits.digits``.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      decimal = Pattern().one_or_more().digit().char(".").one_or_more().digit()

   **Emits** ``\d+\.\d+``

.. py:data:: edify.atoms.floatnum

   Composable :class:`Pattern` fragment for a general floating-point number.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      floatnum = (
          Pattern()
          .optional()
          .any_of_chars("+-")
          .one_or_more()
          .digit()
          .optional()
          .group()
          .char(".")
          .one_or_more()
          .digit()
          .end()
          .optional()
          .group()
          .any_of_chars("eE")
          .optional()
          .any_of_chars("+-")
          .one_or_more()
          .digit()
          .end()
      )

   **Emits** ``[+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?``

.. py:data:: edify.atoms.hexnum

   Composable :class:`Pattern` fragment for a ``0xNN``-shaped hexadecimal literal.

   **How it is built**

   .. code-block:: python

      from edify import Pattern
      from edify.atoms.nibble import nibble

      hexnum = Pattern().char("0").any_of_chars("xX").one_or_more().use(nibble)

   **Emits** ``0[xX](?:[0-9a-fA-F])+``

.. py:data:: edify.atoms.integer

   Composable :class:`Pattern` fragment for a signed decimal integer.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      integer = Pattern().optional().any_of_chars("+-").one_or_more().digit()

   **Emits** ``[+-]?\d+``

.. py:data:: edify.atoms.money

   Composable :class:`Pattern` fragment for a currency + amount value.

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      _amount = Pattern().one_or_more().digit().optional().group().char(".").one_or_more().digit().end()

      money = any_of(
          Pattern().exactly(3).uppercase().optional().whitespace_char().use(_amount),
          Pattern().use(_amount).optional().whitespace_char().exactly(3).uppercase(),
      )

   **Emits** ``(?:[A-Z]{3}\s?\d+(?:\.\d+)?|\d+(?:\.\d+)?\s?[A-Z]{3})``

.. py:data:: edify.atoms.natural

   Composable :class:`Pattern` fragment for a positive integer without a leading zero.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      natural = Pattern().range("1", "9").zero_or_more().digit()

   **Emits** ``[1-9]\d*``

.. py:data:: edify.atoms.octnum

   Composable :class:`Pattern` fragment for a ``0oNN``-shaped octal literal.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      octnum = Pattern().char("0").any_of_chars("oO").one_or_more().range("0", "7")

   **Emits** ``0[oO][0-7]+``

.. py:data:: edify.atoms.percent

   Composable :class:`Pattern` fragment for a percentage value.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      percent = (
          Pattern()
          .one_or_more()
          .digit()
          .optional()
          .group()
          .char(".")
          .one_or_more()
          .digit()
          .end()
          .char("%")
      )

   **Emits** ``\d+(?:\.\d+)?%``

.. py:data:: edify.atoms.ratio

   Composable :class:`Pattern` fragment for a ratio value.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      ratio = Pattern().one_or_more().digit().char(":").one_or_more().digit()

   **Emits** ``\d+:\d+``

.. py:data:: edify.atoms.scientific

   Composable :class:`Pattern` fragment for a number in scientific notation.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      scientific = (
          Pattern()
          .optional()
          .any_of_chars("+-")
          .one_or_more()
          .digit()
          .optional()
          .group()
          .char(".")
          .one_or_more()
          .digit()
          .end()
          .any_of_chars("eE")
          .optional()
          .any_of_chars("+-")
          .one_or_more()
          .digit()
      )

   **Emits** ``[+-]?\d+(?:\.\d+)?[eE][+-]?\d+``

.. py:data:: edify.atoms.signed

   Composable :class:`Pattern` fragment for a signed integer with the sign required.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      signed = Pattern().any_of_chars("+-").one_or_more().digit()

   **Emits** ``[+-]\d+``

.. py:data:: edify.atoms.unsigned

   Composable :class:`Pattern` fragment for an unsigned integer.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      unsigned = Pattern().one_or_more().digit()

   **Emits** ``\d+``

Text
----

Characters, classes, and simple word shapes. Covered with examples in
:doc:`../guide/atoms/text`.

.. py:data:: edify.atoms.alnum

   Composable :class:`Pattern` fragment for one alphanumeric char ``[a-zA-Z0-9]``.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      alnum = Pattern().alphanumeric()

   **Emits** ``[a-zA-Z0-9]``

.. py:data:: edify.atoms.ascii

   Composable :class:`Pattern` fragment for any ASCII code point.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      ascii = Pattern().range("\x00", "\x7f")

   **Emits** ``[\x00-]``

.. py:data:: edify.atoms.boolean

   Composable :class:`Pattern` fragment for any common boolean spelling.

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      boolean = any_of(
          Pattern().string("true"),
          Pattern().string("false"),
          Pattern().string("True"),
          Pattern().string("False"),
          Pattern().string("TRUE"),
          Pattern().string("FALSE"),
          Pattern().string("yes"),
          Pattern().string("no"),
          Pattern().string("Yes"),
          Pattern().string("No"),
          Pattern().string("YES"),
          Pattern().string("NO"),
          Pattern().string("on"),
          Pattern().string("off"),
          Pattern().string("On"),
          Pattern().string("Off"),
          Pattern().string("ON"),
          Pattern().string("OFF"),
          Pattern().string("1"),
          Pattern().string("0"),
      )

   **Emits** ``(?:true|false|True|False|TRUE|FALSE|yes|no|Yes|No|YES|NO|on|off|On|Off|ON|OFF|[10])``

.. py:data:: edify.atoms.letter

   Composable :class:`Pattern` fragment for one ASCII letter ``[a-zA-Z]``.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      letter = Pattern().letter()

   **Emits** ``[a-zA-Z]``

.. py:data:: edify.atoms.line

   Composable :class:`Pattern` fragment for one line of text.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      line = Pattern().one_or_more().anything_but_chars("\r\n")

   **Emits** ``[^\r\n]+``

.. py:data:: edify.atoms.lower

   Composable :class:`Pattern` fragment for one lowercase letter ``[a-z]``.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      lower = Pattern().lowercase()

   **Emits** ``[a-z]``

.. py:data:: edify.atoms.printable

   Composable :class:`Pattern` fragment for one printable-ASCII character.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      printable = Pattern().range("\x20", "\x7e")

   **Emits** ``[ -~]``

.. py:data:: edify.atoms.quoted

   Composable :class:`Pattern` fragment for a ``"..."`` string.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      quoted = Pattern().char('"').zero_or_more().anything_but_chars('"').char('"')

   **Emits** ``"[^"]*"``

.. py:data:: edify.atoms.slug

   Composable :class:`Pattern` fragment for a URL-safe slug.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      slug = (
          Pattern()
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .end()
          .zero_or_more()
          .group()
          .char("-")
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .end()
          .end()
      )

   **Emits** ``[a-z0-9]+(?:\-[a-z0-9]+)*``

.. py:data:: edify.atoms.space

   Composable :class:`Pattern` fragment for one whitespace character.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      space = Pattern().whitespace_char()

   **Emits** ``\s``

.. py:data:: edify.atoms.truefalse

   Composable :class:`Pattern` fragment for a true/false boolean.

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      truefalse = any_of(
          Pattern().string("true"),
          Pattern().string("false"),
          Pattern().string("True"),
          Pattern().string("False"),
          Pattern().string("TRUE"),
          Pattern().string("FALSE"),
      )

   **Emits** ``(?:true|false|True|False|TRUE|FALSE)``

.. py:data:: edify.atoms.upper

   Composable :class:`Pattern` fragment for one uppercase letter ``[A-Z]``.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      upper = Pattern().uppercase()

   **Emits** ``[A-Z]``

.. py:data:: edify.atoms.word

   Composable :class:`Pattern` fragment for a run of word characters.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      word = Pattern().one_or_more().word()

   **Emits** ``\w+``

.. py:data:: edify.atoms.yesno

   Composable :class:`Pattern` fragment for a yes/no boolean.

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      yesno = any_of(
          Pattern().string("yes"),
          Pattern().string("no"),
          Pattern().string("Yes"),
          Pattern().string("No"),
          Pattern().string("YES"),
          Pattern().string("NO"),
          Pattern().string("y"),
          Pattern().string("n"),
          Pattern().string("Y"),
          Pattern().string("N"),
      )

   **Emits** ``(?:yes|no|Yes|No|YES|NO|[ynYN])``

Encodings
---------

Base-N alphabets, hash digests, and unique identifiers. Covered with examples in
:doc:`../guide/atoms/encodings`.

.. py:data:: edify.atoms.base32

   Composable :class:`Pattern` fragment for a base32 string.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      base32 = (
          Pattern().one_or_more().any_of().range("A", "Z").range("2", "7").end().zero_or_more().char("=")
      )

   **Emits** ``[A-Z2-7]+=*``

.. py:data:: edify.atoms.base58

   Composable :class:`Pattern` fragment for a base58 string.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      base58 = (
          Pattern()
          .one_or_more()
          .any_of()
          .range("1", "9")
          .range("A", "H")
          .range("J", "N")
          .range("P", "Z")
          .range("a", "k")
          .range("m", "z")
          .end()
      )

   **Emits** ``[1-9A-HJ-NP-Za-km-z]+``

.. py:data:: edify.atoms.base64

   Composable :class:`Pattern` fragment for a standard base64 string.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      base64 = (
          Pattern()
          .one_or_more()
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .char("+")
          .char("/")
          .end()
          .zero_or_more()
          .char("=")
      )

   **Emits** ``[A-Za-z0-9\+/]+=*``

.. py:data:: edify.atoms.base64url

   Composable :class:`Pattern` fragment for a URL-safe base64 string.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      base64url = (
          Pattern()
          .one_or_more()
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .char("_")
          .char("-")
          .end()
      )

   **Emits** ``[A-Za-z0-9_\-]+``

.. py:data:: edify.atoms.guid

   Composable :class:`Pattern` fragment for an any-version UUID/GUID.

   **How it is built**

   .. code-block:: python

      from edify import Pattern
      from edify.atoms.nibble import nibble

      guid = (
          Pattern()
          .exactly(8)
          .use(nibble)
          .char("-")
          .exactly(4)
          .use(nibble)
          .char("-")
          .exactly(4)
          .use(nibble)
          .char("-")
          .exactly(4)
          .use(nibble)
          .char("-")
          .exactly(12)
          .use(nibble)
      )

   **Emits** ``(?:[0-9a-fA-F]){8}\-(?:[0-9a-fA-F]){4}\-(?:[0-9a-fA-F]){4}\-(?:[0-9a-fA-F]){4}\-(?:[0-9a-fA-F]){12}``

.. py:data:: edify.atoms.hexstring

   Composable :class:`Pattern` fragment for a hex character string.

   **How it is built**

   .. code-block:: python

      from edify import Pattern
      from edify.atoms.nibble import nibble

      hexstring = Pattern().one_or_more().use(nibble)

   **Emits** ``(?:[0-9a-fA-F])+``

.. py:data:: edify.atoms.md5

   Composable :class:`Pattern` fragment for an MD5 hex digest.

   **How it is built**

   .. code-block:: python

      from edify import Pattern
      from edify.atoms.nibble import nibble

      md5 = Pattern().exactly(32).use(nibble)

   **Emits** ``(?:[0-9a-fA-F]){32}``

.. py:data:: edify.atoms.objectid

   Composable :class:`Pattern` fragment for a 24-hex-character ObjectId.

   **How it is built**

   .. code-block:: python

      from edify import Pattern
      from edify.atoms.nibble import nibble

      objectid = Pattern().exactly(24).use(nibble)

   **Emits** ``(?:[0-9a-fA-F]){24}``

.. py:data:: edify.atoms.oid

   Composable :class:`Pattern` fragment for a dotted numeric OID.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      oid = Pattern().one_or_more().digit().one_or_more().group().char(".").one_or_more().digit().end()

   **Emits** ``\d+(?:\.\d+)+``

.. py:data:: edify.atoms.sha256

   Composable :class:`Pattern` fragment for a SHA-256 hex digest.

   **How it is built**

   .. code-block:: python

      from edify import Pattern
      from edify.atoms.nibble import nibble

      sha256 = Pattern().exactly(64).use(nibble)

   **Emits** ``(?:[0-9a-fA-F]){64}``

.. py:data:: edify.atoms.ulid

   Composable :class:`Pattern` fragment for a Crockford-base32 ULID.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      ulid = (
          Pattern()
          .exactly(26)
          .any_of()
          .range("0", "9")
          .range("A", "H")
          .range("J", "K")
          .char("M")
          .char("N")
          .range("P", "T")
          .range("V", "Z")
          .end()
      )

   **Emits** ``[0-9A-HJ-KMNP-TV-Z]{26}``

.. py:data:: edify.atoms.uuid

   Composable :class:`Pattern` fragment for a version-4 UUID.

   **How it is built**

   .. code-block:: python

      from edify import Pattern
      from edify.atoms.nibble import nibble

      uuid = (
          Pattern()
          .exactly(8)
          .use(nibble)
          .char("-")
          .exactly(4)
          .use(nibble)
          .char("-")
          .char("4")
          .exactly(3)
          .use(nibble)
          .char("-")
          .any_of_chars("89ab")
          .exactly(3)
          .use(nibble)
          .char("-")
          .exactly(12)
          .use(nibble)
      )

   **Emits** ``(?:[0-9a-fA-F]){8}\-(?:[0-9a-fA-F]){4}\-4(?:[0-9a-fA-F]){3}\-[89ab](?:[0-9a-fA-F]){3}\-(?:[0-9a-fA-F]){12}``

Date and time
-------------

Date, time, and duration components. Covered with examples in
:doc:`../guide/atoms/datetime`.

.. py:data:: edify.atoms.clock

   Composable :class:`Pattern` fragment for a 24-hour clock time.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      clock = (
          Pattern()
          .any_of()
          .subexpression(Pattern().char("2").range("0", "3"))
          .subexpression(Pattern().range("0", "1").digit())
          .end()
          .char(":")
          .range("0", "5")
          .digit()
          .optional()
          .group()
          .char(":")
          .range("0", "5")
          .digit()
          .end()
      )

   **Emits** ``(?:2[0-3]|[0-1]\d):[0-5]\d(?::[0-5]\d)?``

.. py:data:: edify.atoms.clock12

   Composable :class:`Pattern` fragment for a 12-hour clock time with AM/PM.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      clock12 = (
          Pattern()
          .any_of()
          .subexpression(Pattern().char("1").range("0", "2"))
          .subexpression(Pattern().optional().char("0").range("1", "9"))
          .end()
          .char(":")
          .range("0", "5")
          .digit()
          .optional()
          .group()
          .char(":")
          .range("0", "5")
          .digit()
          .end()
          .optional()
          .whitespace_char()
          .any_of_chars("AaPp")
          .any_of_chars("Mm")
      )

   **Emits** ``(?:1[0-2]|0?[1-9]):[0-5]\d(?::[0-5]\d)?\s?[AaPp][Mm]``

.. py:data:: edify.atoms.day

   Composable :class:`Pattern` fragment for a two-digit day-of-month.

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      day = any_of(
          Pattern().char("0").range("1", "9"),
          Pattern().range("1", "2").digit(),
          Pattern().char("3").range("0", "1"),
      )

   **Emits** ``(?:0[1-9]|[1-2]\d|3[0-1])``

.. py:data:: edify.atoms.duration

   Composable :class:`Pattern` fragment for an ISO 8601 duration.

   **How it is built**

   .. code-block:: python

      from edify import Pattern


      def _num_with_letter(letter: str) -> Pattern:
          return (
              Pattern()
              .optional()
              .group()
              .one_or_more()
              .digit()
              .optional()
              .group()
              .char(".")
              .one_or_more()
              .digit()
              .end()
              .char(letter)
              .end()
          )


      duration = (
          Pattern()
          .char("P")
          .assert_ahead()
          .any_char()
          .end()
          .subexpression(_num_with_letter("Y"))
          .subexpression(_num_with_letter("M"))
          .subexpression(_num_with_letter("W"))
          .subexpression(_num_with_letter("D"))
          .optional()
          .group()
          .char("T")
          .assert_ahead()
          .digit()
          .end()
          .subexpression(_num_with_letter("H"))
          .subexpression(_num_with_letter("M"))
          .subexpression(_num_with_letter("S"))
          .end()
      )

   **Emits** ``P(?=.)(?:\d+(?:\.\d+)?Y)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?=\d)(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?``

.. py:data:: edify.atoms.epoch

   Composable :class:`Pattern` fragment for a 10-digit Unix epoch timestamp.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      epoch = Pattern().exactly(10).digit()

   **Emits** ``\d{10}``

.. py:data:: edify.atoms.isodate

   Composable :class:`Pattern` fragment for an ISO 8601 ``YYYY-MM-DD`` date.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      isodate = Pattern().exactly(4).digit().char("-").exactly(2).digit().char("-").exactly(2).digit()

   **Emits** ``\d{4}\-\d{2}\-\d{2}``

.. py:data:: edify.atoms.isodatetime

   Composable :class:`Pattern` fragment for an ISO 8601 combined date-time.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      isodatetime = (
          Pattern()
          .exactly(4)
          .digit()
          .char("-")
          .exactly(2)
          .digit()
          .char("-")
          .exactly(2)
          .digit()
          .any_of_chars("Tt ")
          .exactly(2)
          .digit()
          .char(":")
          .exactly(2)
          .digit()
          .optional()
          .group()
          .char(":")
          .exactly(2)
          .digit()
          .optional()
          .group()
          .char(".")
          .one_or_more()
          .digit()
          .end()
          .end()
          .optional()
          .group()
          .any_of()
          .any_of_chars("Zz")
          .subexpression(
              Pattern().any_of_chars("+-").exactly(2).digit().optional().char(":").exactly(2).digit()
          )
          .end()
          .end()
      )

   **Emits** ``\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:(?:[+-]\d{2}:?\d{2}|[Zz]))?``

.. py:data:: edify.atoms.month

   Composable :class:`Pattern` fragment for a two-digit calendar month.

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      month = any_of(
          Pattern().char("0").range("1", "9"),
          Pattern().char("1").range("0", "2"),
      )

   **Emits** ``(?:0[1-9]|1[0-2])``

.. py:data:: edify.atoms.timezone

   Composable :class:`Pattern` fragment for a timezone offset.

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      timezone = any_of(
          Pattern().char("Z"),
          Pattern().any_of_chars("+-").exactly(2).digit().optional().char(":").exactly(2).digit(),
      )

   **Emits** ``(?:[+-]\d{2}:?\d{2}|[Z])``

.. py:data:: edify.atoms.weekday

   Composable :class:`Pattern` fragment for an English weekday name.

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      weekday = any_of(
          Pattern().string("Monday"),
          Pattern().string("Tuesday"),
          Pattern().string("Wednesday"),
          Pattern().string("Thursday"),
          Pattern().string("Friday"),
          Pattern().string("Saturday"),
          Pattern().string("Sunday"),
          Pattern().string("Mon"),
          Pattern().string("Tue"),
          Pattern().string("Wed"),
          Pattern().string("Thu"),
          Pattern().string("Fri"),
          Pattern().string("Sat"),
          Pattern().string("Sun"),
      )

   **Emits** ``(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|Mon|Tue|Wed|Thu|Fri|Sat|Sun)``

.. py:data:: edify.atoms.year

   Composable :class:`Pattern` fragment for a four-digit calendar year.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      year = Pattern().exactly(4).digit()

   **Emits** ``\d{4}``

Web and files
-------------

HTTP values, media types, file naming, and colours. Covered with examples in
:doc:`../guide/atoms/web`.

.. py:data:: edify.atoms.extension

   Composable :class:`Pattern` fragment for a file extension.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      extension = Pattern().char(".").one_or_more().alphanumeric()

   **Emits** ``\.[a-zA-Z0-9]+``

.. py:data:: edify.atoms.filename

   Composable :class:`Pattern` fragment for a filename with no path separators.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      filename = Pattern().one_or_more().anything_but_chars('/\\<>:"|?*\x00')

   **Emits** ``[^/\\<>:"|?*\x00]+``

.. py:data:: edify.atoms.filepath

   Composable :class:`Pattern` fragment for a filesystem path.

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      _posix = (
          Pattern()
          .optional()
          .char("/")
          .one_or_more()
          .group()
          .anything_but_chars("/\x00")
          .optional()
          .char("/")
          .end()
      )
      _windows = (
          Pattern()
          .letter()
          .string(":")
          .one_or_more()
          .group()
          .char("\\")
          .anything_but_chars('/\\<>:"|?*\x00\n')
          .end()
      )

      filepath = any_of(_posix, _windows)

   **Emits** ``(?:/?(?:[^/\x00]/?)+|[a-zA-Z]:(?:\\[^/\\<>:"|?*\x00\n])+)``

.. py:data:: edify.atoms.hexcolor

   Composable :class:`Pattern` fragment for a CSS hex colour.

   **How it is built**

   .. code-block:: python

      from edify import Pattern
      from edify.atoms.nibble import nibble

      hexcolor = (
          Pattern()
          .char("#")
          .any_of()
          .exactly(8)
          .use(nibble)
          .exactly(6)
          .use(nibble)
          .exactly(4)
          .use(nibble)
          .exactly(3)
          .use(nibble)
          .end()
      )

   **Emits** ``\#(?:(?:[0-9a-fA-F]){8}|(?:[0-9a-fA-F]){6}|(?:[0-9a-fA-F]){4}|(?:[0-9a-fA-F]){3})``

.. py:data:: edify.atoms.httpmethod

   Composable :class:`Pattern` fragment for an HTTP request method.

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      httpmethod = any_of(
          Pattern().string("OPTIONS"),
          Pattern().string("GET"),
          Pattern().string("HEAD"),
          Pattern().string("POST"),
          Pattern().string("PUT"),
          Pattern().string("DELETE"),
          Pattern().string("TRACE"),
          Pattern().string("CONNECT"),
          Pattern().string("PATCH"),
      )

   **Emits** ``(?:OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT|PATCH)``

.. py:data:: edify.atoms.httpstatus

   Composable :class:`Pattern` fragment for a three-digit HTTP status code.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      httpstatus = Pattern().range("1", "5").exactly(2).digit()

   **Emits** ``[1-5]\d{2}``

.. py:data:: edify.atoms.mimetype

   Composable :class:`Pattern` fragment for a ``type/subtype`` MIME identifier.

   **How it is built**

   .. code-block:: python

      from edify import Pattern


      def _token() -> Pattern:
          return (
              Pattern()
              .letter()
              .zero_or_more()
              .any_of()
              .range("a", "z")
              .range("A", "Z")
              .range("0", "9")
              .char("+")
              .char("-")
              .char(".")
              .end()
          )


      mimetype = Pattern().use(_token()).char("/").use(_token())

   **Emits** ``[a-zA-Z][a-zA-Z0-9\+\-\.]*/[a-zA-Z][a-zA-Z0-9\+\-\.]*``

.. py:data:: edify.atoms.rgbcolor

   Composable :class:`Pattern` fragment for a CSS ``rgb()``/``rgba()`` colour.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      rgbcolor = (
          Pattern()
          .string("rgb")
          .optional()
          .char("a")
          .char("(")
          .zero_or_more()
          .whitespace_char()
          .one_or_more()
          .digit()
          .zero_or_more()
          .group()
          .char(",")
          .zero_or_more()
          .whitespace_char()
          .one_or_more()
          .digit()
          .end()
          .char(")")
      )

   **Emits** ``rgba?\(\s*\d+(?:,\s*\d+)*\)``

Finance and versions
--------------------

Payment and banking fragments, plus version numbers. Covered with examples in
:doc:`../guide/atoms/finance`.

.. py:data:: edify.atoms.bic

   Composable :class:`Pattern` fragment for a BIC/SWIFT code.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      bic = (
          Pattern()
          .exactly(4)
          .uppercase()
          .exactly(2)
          .uppercase()
          .exactly(2)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .optional()
          .group()
          .exactly(3)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .end()
      )

   **Emits** ``[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}(?:[A-Z0-9]{3})?``

.. py:data:: edify.atoms.creditcard

   Composable :class:`Pattern` fragment for a credit-card number shape.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      creditcard = Pattern().between(13, 19).digit()

   **Emits** ``\d{13,19}``

.. py:data:: edify.atoms.iban

   Composable :class:`Pattern` fragment for an IBAN.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      iban = (
          Pattern()
          .exactly(2)
          .uppercase()
          .exactly(2)
          .digit()
          .between(11, 30)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
      )

   **Emits** ``[A-Z]{2}\d{2}[A-Z0-9]{11,30}``

.. py:data:: edify.atoms.semver

   Composable :class:`Pattern` fragment for a SemVer ``MAJOR.MINOR.PATCH`` core.

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of


      def _core() -> Pattern:
          return any_of(
              Pattern().char("0"),
              Pattern().range("1", "9").zero_or_more().digit(),
          )


      semver = Pattern().use(_core()).char(".").use(_core()).char(".").use(_core())

   **Emits** ``(?:[1-9]\d*|[0])\.(?:[1-9]\d*|[0])\.(?:[1-9]\d*|[0])``

Grouping
--------

Bracket-delimited spans. Covered with examples in
:doc:`../guide/atoms/grouping`.

.. py:data:: edify.atoms.braces

   Composable :class:`Pattern` fragment for a ``{...}`` group.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      braces = Pattern().char("{").zero_or_more().anything_but_chars("}").char("}")

   **Emits** ``\{[^}]*\}``

.. py:data:: edify.atoms.brackets

   Composable :class:`Pattern` fragment for a ``[...]`` group.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      brackets = Pattern().char("[").zero_or_more().anything_but_chars("]").char("]")

   **Emits** ``\[[^\]]*\]``

.. py:data:: edify.atoms.parens

   Composable :class:`Pattern` fragment for a ``(...)`` group.

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      parens = Pattern().char("(").zero_or_more().anything_but_chars(")").char(")")

   **Emits** ``\([^)]*\)``

