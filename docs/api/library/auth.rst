Auth
====

Every validator in the :doc:`auth <../../library/auth/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/auth/index>`.

.. py:function:: edify.library.apikey(value: str) -> bool

   API key. See :doc:`../../library/auth/apikey` for the full description.

   Emits ``^[A-Za-z0-9_-]{20,128}$``

.. py:function:: edify.library.bearer(value: str) -> bool

   Bearer. See :doc:`../../library/auth/bearer` for the full description.

   Emits ``^Bearer [A-Za-z0-9._-]+$``

.. py:function:: edify.library.challenge(value: str) -> bool

   Challenge. See :doc:`../../library/auth/challenge` for the full description.

   Emits ``^[A-Za-z0-9_-]{16,128}$``

.. py:function:: edify.library.csrf(value: str) -> bool

   CSRF token. See :doc:`../../library/auth/csrf` for the full description.

   Emits ``^[A-Za-z0-9_-]{32,128}$``

.. py:function:: edify.library.hmac(value: str) -> bool

   HMAC. See :doc:`../../library/auth/hmac` for the full description.

   Emits ``^[0-9a-fA-F]{32,128}$``

.. py:function:: edify.library.jwt(value: str) -> bool

   JWT. See :doc:`../../library/auth/jwt` for the full description.

   Emits ``^[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+$``

.. py:function:: edify.library.mfa(value: str) -> bool

   MFA code. See :doc:`../../library/auth/mfa` for the full description.

   Emits ``^\d{6,8}$``

.. py:function:: edify.library.mnemonic(value: str) -> bool

   Mnemonic. See :doc:`../../library/auth/mnemonic` for the full description.

   Emits ``^(?:[a-z]+ ){11,23}[a-z]+$``

.. py:function:: edify.library.otp(value: str) -> bool

   OTP. See :doc:`../../library/auth/otp` for the full description.

   Emits ``(?:^\d{6,8}$|^[A-Z0-9]{6,8}$)``

.. py:function:: edify.library.passkey(value: str) -> bool

   Passkey. See :doc:`../../library/auth/passkey` for the full description.

   Emits ``^[A-Za-z0-9_-]{22,512}$``

.. py:function:: edify.library.password(value: str) -> bool

   Password. See :doc:`../../library/auth/password` for the full description.

   Emits ``(?:)``

.. py:function:: edify.library.pin(value: str) -> bool

   PIN. See :doc:`../../library/auth/pin` for the full description.

   Emits ``^\d{4,12}$``

.. py:function:: edify.library.refresh(value: str) -> bool

   Refresh token. See :doc:`../../library/auth/refresh` for the full description.

   Emits ``^[A-Za-z0-9._\-~+/=]{32,512}$``

.. py:function:: edify.library.secret(value: str) -> bool

   Secret. See :doc:`../../library/auth/secret` for the full description.

   Emits ``^[A-Za-z0-9_-]{16,256}$``

.. py:function:: edify.library.session(value: str) -> bool

   Session ID. See :doc:`../../library/auth/session` for the full description.

   Emits ``^[A-Za-z0-9_-]{16,128}$``

.. py:function:: edify.library.signing(value: str) -> bool

   Signing key. See :doc:`../../library/auth/signing` for the full description.

   Emits ``^[A-Za-z0-9+/=_-]{32,256}$``

.. py:function:: edify.library.sso(value: str) -> bool

   SSO. See :doc:`../../library/auth/sso` for the full description.

   Emits ``^[A-Za-z0-9+/=_\-.]{20,2048}$``

.. py:function:: edify.library.token(value: str) -> bool

   Token. See :doc:`../../library/auth/token` for the full description.

   Emits ``^[A-Za-z0-9_\-.]{24,256}$``

.. py:function:: edify.library.webauthn(value: str) -> bool

   WebAuthn. See :doc:`../../library/auth/webauthn` for the full description.

   Emits ``^[A-Za-z0-9_-]{43,512}$``

