Auth
====

Every validator in the :doc:`Auth <../../library/auth/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/auth/index>`.

.. py:data:: edify.library.apikey

   Callable :class:`Pattern` for an opaque API-key shape: 20-128 URL-safe characters.

   Full description: :doc:`API key <../../library/auth/apikey>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      apikey = (
          Pattern()
          .start_of_input()
          .between(20, 128)
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("_-")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Za-z0-9_-]{20,128}$``

.. py:data:: edify.library.bearer

   Callable :class:`Pattern` for the ``Bearer <token>`` HTTP header shape.

   Full description: :doc:`Bearer <../../library/auth/bearer>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      bearer = (
          Pattern()
          .start_of_input()
          .string("Bearer ")
          .one_or_more()
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("._-")
          .end()
          .end_of_input()
      )

   **Emits** ``^Bearer [A-Za-z0-9._-]+$``

.. py:data:: edify.library.challenge

   Callable :class:`Pattern` for an authentication challenge / nonce:
   16-128 URL-safe characters.

   Full description: :doc:`Challenge <../../library/auth/challenge>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      challenge = (
          Pattern()
          .start_of_input()
          .between(16, 128)
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("_-")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Za-z0-9_-]{16,128}$``

.. py:data:: edify.library.csrf

   Callable :class:`Pattern` for a CSRF-token shape: 32-128 URL-safe characters.

   Full description: :doc:`CSRF token <../../library/auth/csrf>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      csrf = (
          Pattern()
          .start_of_input()
          .between(32, 128)
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("_-")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Za-z0-9_-]{32,128}$``

.. py:data:: edify.library.hmac

   Callable :class:`Pattern` for a hex HMAC digest: 32-128 hex characters.

   Full description: :doc:`HMAC <../../library/auth/hmac>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      hmac = (
          Pattern()
          .start_of_input()
          .between(32, 128)
          .any_of()
          .range("0", "9")
          .range("a", "f")
          .range("A", "F")
          .end()
          .end_of_input()
      )

   **Emits** ``^[0-9a-fA-F]{32,128}$``

.. py:data:: edify.library.jwt

   Callable :class:`Pattern` for the JWT shape: three base64url-encoded
   segments separated by dots (``header.payload.signature``).

   Full description: :doc:`JWT <../../library/auth/jwt>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      jwt = (
          Pattern()
          .start_of_input()
          .one_or_more()
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("_-")
          .end()
          .char(".")
          .one_or_more()
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("_-")
          .end()
          .char(".")
          .one_or_more()
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("_-")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+$``

.. py:data:: edify.library.mfa

   Callable :class:`Pattern` for the MFA/TOTP code shape: 6-8 decimal digits.

   Full description: :doc:`MFA code <../../library/auth/mfa>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      mfa = Pattern().start_of_input().between(6, 8).digit().end_of_input()

   **Emits** ``^\d{6,8}$``

.. py:data:: edify.library.mnemonic

   Callable :class:`Pattern` for a BIP-39 mnemonic phrase: 12 to 24
   lowercase words separated by single spaces.

   Full description: :doc:`Mnemonic <../../library/auth/mnemonic>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      mnemonic = (
          Pattern()
          .start_of_input()
          .between(11, 23)
          .group()
          .one_or_more()
          .lowercase()
          .char(" ")
          .end()
          .one_or_more()
          .lowercase()
          .end_of_input()
      )

   **Emits** ``^(?:[a-z]+ ){11,23}[a-z]+$``

.. py:data:: edify.library.otp

   Callable :class:`Pattern` for the one-time-password shape: 6-8 digits or
   6-8 uppercase-alphanumerics.

   Full description: :doc:`OTP <../../library/auth/otp>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      otp = any_of(
          Pattern().start_of_input().between(6, 8).digit().end_of_input(),
          Pattern()
          .start_of_input()
          .between(6, 8)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .end_of_input(),
      )

   **Emits** ``(?:^\d{6,8}$|^[A-Z0-9]{6,8}$)``

.. py:data:: edify.library.passkey

   Callable :class:`Pattern` for a WebAuthn passkey credential-ID shape:
   22-512 base64url characters.

   Full description: :doc:`Passkey <../../library/auth/passkey>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      passkey = (
          Pattern()
          .start_of_input()
          .between(22, 512)
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("_-")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Za-z0-9_-]{22,512}$``

.. py:data:: edify.library.password

   Callable :class:`Pattern` (subclass) that enforces configurable password-strength thresholds.

   Call as ``password(value)`` for the defaults or ``password(value, min_length=12, min_special=2)``
   to tighten specific thresholds.

   Default policy:
       * Length between 8 and 64 characters inclusive.
       * At least one uppercase letter, one lowercase letter, one decimal digit, and
         one special character from the default set (``!@#$%^&*()_+-=[]{}|;':",./<>?``).

   Guarantees:
       * Every threshold is checked exactly as configured — no silent lower/upper bound.
       * The special-character set is overridable per call via ``special_chars=``.

   Does not guarantee:
       * Passphrase strength beyond the counted-class thresholds — e.g. does not
         reject dictionary words, common patterns, keyboard walks, or breached-password
         corpora.
       * Non-ASCII character-class handling — the class regex targets ASCII letters
         and digits.

   Full description: :doc:`Password <../../library/auth/password>`

   **How it is built**

   .. code-block:: python

      import re

      from edify.pattern.composition import Pattern

      _DEFAULT_SPECIAL_CHARS = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
      _UPPERCASE_RE = re.compile("[A-Z]")
      _LOWERCASE_RE = re.compile("[a-z]")
      _DIGIT_RE = re.compile("[0-9]")


      class _PasswordPattern(Pattern):
          """Callable :class:`Pattern` that checks configurable password thresholds.

          Attributes:
              min_length: Minimum length inclusive.
              max_length: Maximum length inclusive.
              min_upper: Minimum required uppercase letters.
              min_lower: Minimum required lowercase letters.
              min_digit: Minimum required decimal digits.
              min_special: Minimum required special characters.
              special_chars: The set of characters counted toward ``min_special``.
          """

          def __init__(
              self,
              min_length: int = 8,
              max_length: int = 64,
              min_upper: int = 1,
              min_lower: int = 1,
              min_digit: int = 1,
              min_special: int = 1,
              special_chars: str = _DEFAULT_SPECIAL_CHARS,
          ) -> None:
              super().__init__()
              self.min_length = min_length
              self.max_length = max_length
              self.min_upper = min_upper
              self.min_lower = min_lower
              self.min_digit = min_digit
              self.min_special = min_special
              self.special_chars = special_chars

          def __call__(
              self,
              value: str,
              min_length: int | None = None,
              max_length: int | None = None,
              min_upper: int | None = None,
              min_lower: int | None = None,
              min_digit: int | None = None,
              min_special: int | None = None,
              special_chars: str | None = None,
          ) -> bool:
              """Return True when ``value`` meets every configured threshold."""
              effective_min_length = self.min_length if min_length is None else min_length
              effective_max_length = self.max_length if max_length is None else max_length
              effective_min_upper = self.min_upper if min_upper is None else min_upper
              effective_min_lower = self.min_lower if min_lower is None else min_lower
              effective_min_digit = self.min_digit if min_digit is None else min_digit
              effective_min_special = self.min_special if min_special is None else min_special
              effective_special = self.special_chars if special_chars is None else special_chars
              length_ok = effective_min_length <= len(value) <= effective_max_length
              upper_ok = len(_UPPERCASE_RE.findall(value)) >= effective_min_upper
              lower_ok = len(_LOWERCASE_RE.findall(value)) >= effective_min_lower
              digit_ok = len(_DIGIT_RE.findall(value)) >= effective_min_digit
              special_flags = [1 for character in value if character in effective_special]
              special_count = sum(special_flags)
              special_ok = special_count >= effective_min_special
              return length_ok and upper_ok and lower_ok and digit_ok and special_ok


      password = _PasswordPattern()

   **Emits** ``(?:)``

.. py:data:: edify.library.pin

   Callable :class:`Pattern` for the numeric PIN shape: 4-12 digits.

   Full description: :doc:`PIN <../../library/auth/pin>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      pin = Pattern().start_of_input().between(4, 12).digit().end_of_input()

   **Emits** ``^\d{4,12}$``

.. py:data:: edify.library.refresh

   Callable :class:`Pattern` for an OAuth refresh-token shape: 32-512
   opaque characters (URL-safe plus common padding symbols).

   Full description: :doc:`Refresh token <../../library/auth/refresh>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      refresh = (
          Pattern()
          .start_of_input()
          .between(32, 512)
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("._-~+/=")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Za-z0-9._\-~+/=]{32,512}$``

.. py:data:: edify.library.secret

   Callable :class:`Pattern` for an opaque secret string: 16-256 URL-safe characters.

   Full description: :doc:`Secret <../../library/auth/secret>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      secret = (
          Pattern()
          .start_of_input()
          .between(16, 256)
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("_-")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Za-z0-9_-]{16,256}$``

.. py:data:: edify.library.session

   Callable :class:`Pattern` for a session-identifier shape: 16-128 URL-safe characters.

   Full description: :doc:`Session ID <../../library/auth/session>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      session = (
          Pattern()
          .start_of_input()
          .between(16, 128)
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("_-")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Za-z0-9_-]{16,128}$``

.. py:data:: edify.library.signing

   Callable :class:`Pattern` for a request-signature payload: 32-256
   base64-family characters.

   Full description: :doc:`Signing key <../../library/auth/signing>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      signing = (
          Pattern()
          .start_of_input()
          .between(32, 256)
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("+/=_-")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Za-z0-9+/=_-]{32,256}$``

.. py:data:: edify.library.sso

   Callable :class:`Pattern` for an SSO ticket/assertion opaque payload:
   20-2048 base64-family characters (letters, digits, ``+``, ``/``, ``=``,
   ``_``, ``-``, ``.``).

   Full description: :doc:`SSO <../../library/auth/sso>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      sso = (
          Pattern()
          .start_of_input()
          .between(20, 2048)
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("+/=_-.")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Za-z0-9+/=_\-.]{20,2048}$``

.. py:data:: edify.library.token

   Callable :class:`Pattern` for opaque token strings: 24-256 URL-safe characters.

   Full description: :doc:`Token <../../library/auth/token>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      token = (
          Pattern()
          .start_of_input()
          .between(24, 256)
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("_-.")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Za-z0-9_\-.]{24,256}$``

.. py:data:: edify.library.webauthn

   Callable :class:`Pattern` for a WebAuthn credential/assertion base64url shape.

   Full description: :doc:`WebAuthn <../../library/auth/webauthn>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      webauthn = (
          Pattern()
          .start_of_input()
          .between(43, 512)
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .any_of_chars("_-")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Za-z0-9_-]{43,512}$``

