Session ID
==========

A `session identifier <https://owasp.org/www-community/attacks/Session_hijacking_attack>`__
is the opaque handle a server stores in a cookie to recognise a returning visitor.
It carries no meaning to the client — it is a lookup key — so its only observable
property is being long and unguessable. **Session ID** matches 16 to 128
characters of letters, digits, ``-``, and ``_``.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(16, 128)`` over an
:meth:`~edify.RegexBuilder.any_of` class of alphanumerics and the two URL-safe
marks, which is the alphabet cookie values use without escaping.

Framework formats
-----------------

Hex, base64url, and prefixed identifiers all fit:

.. edify-playground::

   from edify.library import session

   session("38afes7a8aef2b0c5d4e6f7a")         # a hex identifier
   session("s%3A9vKQ_xR2-abcdefghij")          # (percent signs are not allowed)
   session("aBcDeF0123456789_-xyz")            # base64url characters
   session("0123456789abcdef")                 # the sixteen-character minimum

Length bounds
-------------

Sixteen characters is the practical floor for an unguessable handle; anything
shorter is brute-forceable:

.. edify-playground::

   from edify.library import session

   session("a" * 16)    # at the minimum
   session("a" * 128)   # at the maximum
   session("a" * 15)    # too short
   session("a" * 129)   # too long

Outside the alphabet
--------------------

A signed or percent-encoded cookie value must be decoded before validating:

.. edify-playground::

   from edify.library import session

   session("abcdefghij0123456")   # valid
   session("abcdef.ghij01234567") # a dot: see token
   session("abcdef ghij01234567") # a space

A well-formed identifier is not a valid one: it may be expired, revoked, or forged,
so always resolve it against your session store. Issue identifiers from a
cryptographically secure generator, regenerate on privilege change to prevent
fixation, and set ``HttpOnly``, ``Secure``, and ``SameSite`` on the cookie carrying
it. For the anti-forgery token that accompanies it see :doc:`csrf`.
