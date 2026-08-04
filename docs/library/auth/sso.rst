SSO
===

`Single sign-on <https://en.wikipedia.org/wiki/Single_sign-on>`__ lets one identity
provider authenticate a user for many applications, and the artifact passed between
them — an assertion, an ID token, or a relay-state blob — is base64 and can be
large. **SSO** matches 20 to 2048 characters of letters, digits, ``+``, ``/``,
``=``, ``_``, ``-``, and ``.``.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(20, 2048)`` over an
:meth:`~edify.RegexBuilder.any_of` class covering both base64 alphabets plus the dot
that separates the parts of a token. The 2048 ceiling accommodates a base64-encoded
SAML assertion, which dwarfs an ordinary token.

Payload forms
-------------

A dotted ID token, a base64 assertion, and a relay state all fit:

.. edify-playground::

   from edify.library import sso

   sso("eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxIn0.c2ln")   # an ID token
   sso("PHNhbWxwOlJlc3BvbnNlIHhtbG5zPSJ1cm46b2Fz")    # a base64 assertion
   sso("a" * 2048)                                     # at the maximum

Both base64 alphabets
---------------------

.. edify-playground::

   from edify.library import sso

   sso("abc+def/ghi=jkl01234")   # standard base64
   sso("abc-def_ghi.jkl01234")   # URL-safe plus a dot
   sso("abc def ghi jkl01234")   # spaces are not part of a payload

Length bounds
-------------

.. edify-playground::

   from edify.library import sso

   sso("a" * 20)     # at the minimum
   sso("a" * 19)     # too short
   sso("a" * 2049)   # too long

An SSO payload asserts who the user is, so it must be cryptographically verified —
signature, issuer, audience, and expiry — before any claim inside it is trusted. A
well-formed blob from an attacker is indistinguishable from a genuine one at this
level. For the protocols that carry these payloads see :doc:`../api/saml` and
:doc:`../api/openid`.
