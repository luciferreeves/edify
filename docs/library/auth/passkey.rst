Passkey
=======

A `passkey <https://fidoalliance.org/passkeys/>`__ is a discoverable
:doc:`webauthn` credential — one the authenticator can find without being told which
account it belongs to, which is what allows a truly password-free sign-in. The
identifier is base64url like any credential ID, and **Passkey** matches 22 to 512
characters of letters, digits, ``-``, and ``_``.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(22, 512)`` over an
:meth:`~edify.RegexBuilder.any_of` class. The lower bound is more permissive than
:doc:`webauthn`'s, since a 16-byte identifier encodes to 22 characters and some
platform authenticators use exactly that.

Credential identifiers
----------------------

.. edify-playground::

   from edify.library import passkey

   passkey("a" * 22)                                # a 16-byte identifier
   passkey("AQIDBAUGBwgJCgsMDQ4PEBESExQVFhcYGRob")  # a longer one
   passkey("a" * 512)                               # at the maximum

URL-safe alphabet
-----------------

.. edify-playground::

   from edify.library import passkey

   passkey("abc-def_ghij0123456789")    # the URL-safe marks
   passkey("abc+def/ghij0123456789")    # standard base64 characters
   passkey("abc=def=ghij0123456789")    # padding

Length bounds
-------------

.. edify-playground::

   from edify.library import passkey

   passkey("a" * 22)    # at the minimum
   passkey("a" * 21)    # too short
   passkey("a" * 513)   # too long

Like any credential ID this is public data — the private key never leaves the
authenticator, and possession of the identifier grants nothing. Verify the signed
:doc:`challenge` on every sign-in. For the broader specification see
:doc:`webauthn`.
