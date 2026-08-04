WebAuthn
========

`WebAuthn <https://www.w3.org/TR/webauthn-2/>`__ replaces passwords with public-key
credentials held in an authenticator — a security key, phone, or platform TPM. The
credential ID a browser returns is base64url-encoded and never short: **WebAuthn**
matches 43 to 512 characters of letters, digits, ``-``, and ``_``.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(43, 512)`` over an
:meth:`~edify.RegexBuilder.any_of` class. The 43-character floor is what a
32-byte identifier becomes once base64url-encoded without padding — the smallest
credential ID in practice.

Credential identifiers
----------------------

Unpadded base64url, at the sizes real authenticators emit:

.. edify-playground::

   from edify.library import webauthn

   webauthn("a" * 43)                              # a 32-byte identifier
   webauthn("AQIDBAUGBwgJCgsMDQ4PEBESExQVFhcYGRobHB0eHyA")
   webauthn("a" * 512)                             # at the maximum

Unpadded base64url only
-----------------------

The transport is URL-safe and unpadded, so standard base64 characters and ``=``
padding do not appear:

.. edify-playground::

   from edify.library import webauthn

   webauthn("abc-def_ghi" + "j" * 32)   # the URL-safe marks
   webauthn("abc+def/ghi" + "j" * 32)   # + and / are standard base64
   webauthn("a" * 43 + "=")             # padding is stripped

Length bounds
-------------

.. edify-playground::

   from edify.library import webauthn

   webauthn("a" * 43)    # at the minimum
   webauthn("a" * 42)    # too short
   webauthn("a" * 513)   # too long

A credential ID is a public identifier, not a secret — it is safe to store, but it
proves nothing on its own. Authentication happens when the authenticator signs the
server's :doc:`challenge` and you verify that signature against the registered public
key, checking the origin and relying-party ID as you go. For the closely related
credential see :doc:`passkey`.
