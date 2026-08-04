Contact
=======

Every validator in the :doc:`Contact <../../library/contact/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/contact/index>`.

.. py:data:: edify.library.address

   Callable :class:`Pattern` for a permissive street-address shape:
   one or more digits followed by whitespace and address body characters.

   Full description: :doc:`Address <../../library/contact/address>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      address = (
          Pattern()
          .start_of_input()
          .one_or_more()
          .digit()
          .one_or_more()
          .whitespace_char()
          .one_or_more()
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .whitespace_char()
          .any_of_chars(".,'-#/")
          .end()
          .end_of_input()
      )

   **Emits** ``^\d+\s+(?:\s|[A-Za-z0-9.,'\-#/])+$``

.. py:data:: edify.library.email

   Callable :class:`Pattern` for either the common permissive or the strict RFC 5322 email shape.

   Guarantees:
       * Accepts the everyday ``local@domain`` shape used across the web (letters, digits,
         dot, hyphen, underscore, plus common special characters in the local part).
       * Accepts the RFC 5322 mailbox shape — quoted local parts, dot-atoms, and
         domain-literal addresses (``user@[192.0.2.1]``).
       * Anchored at both ends, so the whole string must match.

   Does not guarantee:
       * Deliverability, DNS resolution, or MX-record presence — this is a shape check.
       * Full RFC 5322 group / display-name syntax (``Name <user@example.com>``).
       * Internationalised domain names beyond ASCII / punycode.

   Full description: :doc:`Email <../../library/contact/email>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of


      def _local_char_class() -> Pattern:
          return (
              Pattern()
              .any_of()
              .range("a", "z")
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
              .char("-")
              .end()
          )


      def _domain_label() -> Pattern:
          return (
              Pattern()
              .any_of()
              .range("a", "z")
              .range("0", "9")
              .end()
              .optional()
              .group()
              .zero_or_more()
              .any_of()
              .range("a", "z")
              .range("0", "9")
              .char("-")
              .end()
              .any_of()
              .range("a", "z")
              .range("0", "9")
              .end()
              .end()
          )


      _basic_local = (
          Pattern()
          .one_or_more()
          .subexpression(_local_char_class())
          .zero_or_more()
          .group()
          .char(".")
          .one_or_more()
          .subexpression(_local_char_class())
          .end()
      )

      _basic_domain = (
          Pattern()
          .one_or_more()
          .group()
          .subexpression(_domain_label())
          .char(".")
          .end()
          .subexpression(_domain_label())
      )

      _basic = Pattern().subexpression(_basic_local).char("@").subexpression(_basic_domain)


      def _quoted_text() -> Pattern:
          return (
              Pattern()
              .any_of()
              .range("\x01", "\x08")
              .char("\x0b")
              .char("\x0c")
              .range("\x0e", "\x1f")
              .char("\x21")
              .range("\x23", "\x5b")
              .range("\x5d", "\x7f")
              .end()
          )


      def _quoted_escape() -> Pattern:
          return (
              Pattern()
              .char("\\")
              .any_of()
              .range("\x01", "\x09")
              .char("\x0b")
              .char("\x0c")
              .range("\x0e", "\x7f")
              .end()
          )


      _quoted_local = (
          Pattern()
          .char('"')
          .zero_or_more()
          .subexpression(any_of(_quoted_text(), _quoted_escape()))
          .char('"')
      )


      def _octet() -> Pattern:
          return any_of(
              Pattern().string("25").range("0", "5"),
              Pattern().char("2").range("0", "4").digit(),
              Pattern().optional().any_of_chars("01").digit().optional().digit(),
          )


      def _bracket_text() -> Pattern:
          return (
              Pattern()
              .any_of()
              .range("\x01", "\x08")
              .char("\x0b")
              .char("\x0c")
              .range("\x0e", "\x1f")
              .range("\x21", "\x5a")
              .range("\x53", "\x7f")
              .end()
          )


      def _bracket_escape() -> Pattern:
          return (
              Pattern()
              .char("\\")
              .any_of()
              .range("\x01", "\x09")
              .char("\x0b")
              .char("\x0c")
              .range("\x0e", "\x7f")
              .end()
          )


      _ip_literal_tail = any_of(
          _octet(),
          (
              Pattern()
              .zero_or_more()
              .any_of()
              .range("a", "z")
              .range("0", "9")
              .char("-")
              .end()
              .any_of()
              .range("a", "z")
              .range("0", "9")
              .end()
              .char(":")
              .one_or_more()
              .subexpression(any_of(_bracket_text(), _bracket_escape()))
          ),
      )

      _ip_literal = (
          Pattern()
          .char("[")
          .exactly(3)
          .group()
          .subexpression(_octet())
          .char(".")
          .end()
          .subexpression(_ip_literal_tail)
          .char("]")
      )

      _rfc_local = any_of(_basic_local, _quoted_local)
      _rfc_domain = any_of(_basic_domain, _ip_literal)
      _rfc = Pattern().subexpression(_rfc_local).char("@").subexpression(_rfc_domain)

      email = Pattern().start_of_input().subexpression(any_of(_basic, _rfc)).end_of_input()

      email_rfc_5322 = Pattern().start_of_input().subexpression(_rfc).end_of_input()

   **Emits** ``^(?:(?:[a-z0-9!\#\$%\&'\*\+/=\?\^_`\{\|\}\~\-])+(?:\.(?:[a-z0-9!\#\$%\&'\*\+/=\?\^_`\{\|\}\~\-])+)*@(?:[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?|(?:(?:[a-z0-9!\#\$%\&'\*\+/=\?\^_`\{\|\}\~\-])+(?:\.(?:[a-z0-9!\#\$%\&'\*\+/=\?\^_`\{\|\}\~\-])+)*|"(?:(?:[-\\-!#-[\]-]|\\[-\t\\-]))*")@(?:(?:[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)|[a-z0-9\-]*[a-z0-9]:(?:(?:[-\\-!-ZS-]|\\[-\t\\-]))+)\]))$``

.. py:data:: edify.library.email_rfc_5322

   Callable :class:`Pattern` for the strict RFC 5322 mailbox shape only.

   Rejects everyday but non-compliant addresses that :data:`email` accepts.

   Guarantees:
       * Accepts every dot-atom and quoted-string local part permitted by RFC 5322.
       * Accepts domain literals (``user@[192.0.2.1]``) and IPv6 literals
         (``user@[IPv6:::1]``).
       * Anchored at both ends.

   Does not guarantee:
       * Deliverability, DNS resolution, or MX-record presence — this is a shape check.
       * Full RFC 5322 group / display-name syntax.

   Full description: :doc:`Email (RFC 5322) <../../library/contact/email_rfc_5322>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of


      def _local_char_class() -> Pattern:
          return (
              Pattern()
              .any_of()
              .range("a", "z")
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
              .char("-")
              .end()
          )


      def _domain_label() -> Pattern:
          return (
              Pattern()
              .any_of()
              .range("a", "z")
              .range("0", "9")
              .end()
              .optional()
              .group()
              .zero_or_more()
              .any_of()
              .range("a", "z")
              .range("0", "9")
              .char("-")
              .end()
              .any_of()
              .range("a", "z")
              .range("0", "9")
              .end()
              .end()
          )


      _basic_local = (
          Pattern()
          .one_or_more()
          .subexpression(_local_char_class())
          .zero_or_more()
          .group()
          .char(".")
          .one_or_more()
          .subexpression(_local_char_class())
          .end()
      )

      _basic_domain = (
          Pattern()
          .one_or_more()
          .group()
          .subexpression(_domain_label())
          .char(".")
          .end()
          .subexpression(_domain_label())
      )

      _basic = Pattern().subexpression(_basic_local).char("@").subexpression(_basic_domain)


      def _quoted_text() -> Pattern:
          return (
              Pattern()
              .any_of()
              .range("\x01", "\x08")
              .char("\x0b")
              .char("\x0c")
              .range("\x0e", "\x1f")
              .char("\x21")
              .range("\x23", "\x5b")
              .range("\x5d", "\x7f")
              .end()
          )


      def _quoted_escape() -> Pattern:
          return (
              Pattern()
              .char("\\")
              .any_of()
              .range("\x01", "\x09")
              .char("\x0b")
              .char("\x0c")
              .range("\x0e", "\x7f")
              .end()
          )


      _quoted_local = (
          Pattern()
          .char('"')
          .zero_or_more()
          .subexpression(any_of(_quoted_text(), _quoted_escape()))
          .char('"')
      )


      def _octet() -> Pattern:
          return any_of(
              Pattern().string("25").range("0", "5"),
              Pattern().char("2").range("0", "4").digit(),
              Pattern().optional().any_of_chars("01").digit().optional().digit(),
          )


      def _bracket_text() -> Pattern:
          return (
              Pattern()
              .any_of()
              .range("\x01", "\x08")
              .char("\x0b")
              .char("\x0c")
              .range("\x0e", "\x1f")
              .range("\x21", "\x5a")
              .range("\x53", "\x7f")
              .end()
          )


      def _bracket_escape() -> Pattern:
          return (
              Pattern()
              .char("\\")
              .any_of()
              .range("\x01", "\x09")
              .char("\x0b")
              .char("\x0c")
              .range("\x0e", "\x7f")
              .end()
          )


      _ip_literal_tail = any_of(
          _octet(),
          (
              Pattern()
              .zero_or_more()
              .any_of()
              .range("a", "z")
              .range("0", "9")
              .char("-")
              .end()
              .any_of()
              .range("a", "z")
              .range("0", "9")
              .end()
              .char(":")
              .one_or_more()
              .subexpression(any_of(_bracket_text(), _bracket_escape()))
          ),
      )

      _ip_literal = (
          Pattern()
          .char("[")
          .exactly(3)
          .group()
          .subexpression(_octet())
          .char(".")
          .end()
          .subexpression(_ip_literal_tail)
          .char("]")
      )

      _rfc_local = any_of(_basic_local, _quoted_local)
      _rfc_domain = any_of(_basic_domain, _ip_literal)
      _rfc = Pattern().subexpression(_rfc_local).char("@").subexpression(_rfc_domain)

      email = Pattern().start_of_input().subexpression(any_of(_basic, _rfc)).end_of_input()

      email_rfc_5322 = Pattern().start_of_input().subexpression(_rfc).end_of_input()

   **Emits** ``^(?:(?:[a-z0-9!\#\$%\&'\*\+/=\?\^_`\{\|\}\~\-])+(?:\.(?:[a-z0-9!\#\$%\&'\*\+/=\?\^_`\{\|\}\~\-])+)*|"(?:(?:[-\\-!#-[\]-]|\\[-\t\\-]))*")@(?:(?:[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)|[a-z0-9\-]*[a-z0-9]:(?:(?:[-\\-!-ZS-]|\\[-\t\\-]))+)\])$``

.. py:data:: edify.library.fax

   Callable :class:`Pattern` for the permissive international fax-number shape.

   Full description: :doc:`Fax <../../library/contact/fax>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      fax = (
          Pattern()
          .start_of_input()
          .optional()
          .char("+")
          .between_lazy(1, 4)
          .digit()
          .optional()
          .any_of()
          .char("-")
          .char(".")
          .whitespace_char()
          .end()
          .optional()
          .char("(")
          .between_lazy(1, 3)
          .digit()
          .optional()
          .char(")")
          .optional()
          .any_of()
          .char("-")
          .char(".")
          .whitespace_char()
          .end()
          .between(1, 4)
          .digit()
          .optional()
          .any_of()
          .char("-")
          .char(".")
          .whitespace_char()
          .end()
          .between(1, 4)
          .digit()
          .optional()
          .any_of()
          .char("-")
          .char(".")
          .whitespace_char()
          .end()
          .between(1, 9)
          .digit()
          .end_of_input()
      )

   **Emits** ``^\+?\d{1,4}?(?:\s|[\-\.])?\(?\d{1,3}?\)?(?:\s|[\-\.])?\d{1,4}(?:\s|[\-\.])?\d{1,4}(?:\s|[\-\.])?\d{1,9}$``

.. py:data:: edify.library.handle

   Callable :class:`Pattern` for a social-media ``@handle`` shape.

   Full description: :doc:`Handle <../../library/contact/handle>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      handle = (
          Pattern()
          .start_of_input()
          .char("@")
          .between(1, 30)
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char("_")
          .end()
          .end_of_input()
      )

   **Emits** ``^@[a-zA-Z0-9_]{1,30}$``

.. py:data:: edify.library.pager

   Callable :class:`Pattern` for the numeric pager-number shape: 4-10 digits.

   Full description: :doc:`Pager <../../library/contact/pager>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      pager = Pattern().start_of_input().between(4, 10).digit().end_of_input()

   **Emits** ``^\d{4,10}$``

.. py:data:: edify.library.phone

   Callable :class:`Pattern` for multi-locale phone-number display shapes.

   Guarantees:
       * International form: an optional ``+`` or ``00`` prefix, then two to eight
         digit groups of one to four digits each, separated by an optional single
         space, dot, or dash.
       * Any single group may be parenthesised, covering leading and inline area
         codes such as ``(555) 123-4567`` and ``+44 (0)20 7946 0958``.
       * Variable national grouping — three-group North American, five-group French,
         and every shape in between are accepted.
       * Service and short codes of two to six digits, covering emergency and
         abbreviated-dialling numbers.
       * Anchored at both ends.

   Does not guarantee:
       * ITU E.164 canonical form or per-country structural validity — the pattern
         accepts the permissive display forms real inputs use, not a single locale's
         exact digit count.
       * Separator discipline beyond a single character between groups — doubled
         separators such as ``555--123--4567`` are rejected.
       * Letters or vanity spellings — only digits, separators, and parentheses match.

   Full description: :doc:`Phone <../../library/contact/phone>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      _separator = Pattern().optional().any_of_chars(" .-")

      _plain_group = Pattern().between(1, 4).digit()
      _parenthesised_group = Pattern().char("(").between(1, 4).digit().char(")")
      _group = any_of(_plain_group, _parenthesised_group)

      _international_prefix = (
          Pattern()
          .optional()
          .group()
          .any_of()
          .char("+")
          .string("00")
          .end()
          .optional()
          .any_of_chars(" .-")
          .end()
      )

      _number = (
          Pattern()
          .subexpression(_international_prefix)
          .subexpression(_group)
          .between(1, 7)
          .group()
          .subexpression(_separator)
          .subexpression(_group)
          .end()
      )

      _service = Pattern().between(2, 6).digit()

      phone = Pattern().start_of_input().subexpression(any_of(_number, _service)).end_of_input()

   **Emits** ``^(?:(?:(?:00|[\+])[ .-]?)?(?:\d{1,4}|\(\d{1,4}\))(?:[ .-]?(?:\d{1,4}|\(\d{1,4}\))){1,7}|\d{2,6})$``

.. py:data:: edify.library.username

   Callable :class:`Pattern` for a permissive username/handle shape:
   starts with a letter or digit, 3-30 characters total, remaining characters
   alphanumeric plus ``_``, ``.``, or ``-``.

   Full description: :doc:`Username <../../library/contact/username>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      username = (
          Pattern()
          .start_of_input()
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .end()
          .between(2, 29)
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .any_of_chars("_.-")
          .end()
          .end_of_input()
      )

   **Emits** ``^[a-zA-Z0-9][a-zA-Z0-9_.-]{2,29}$``

