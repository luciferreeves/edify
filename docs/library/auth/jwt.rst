JWT
===

A `JSON Web Token <https://jwt.io/introduction>`__ (:rfc:`7519`) is three
base64url-encoded parts joined by dots: a header describing the algorithm, a
payload of claims, and a signature over the first two. **JWT** checks that
three-part structure.

Each part is :meth:`~edify.RegexBuilder.one_or_more` of a base64url
:meth:`~edify.RegexBuilder.any_of` class — letters, digits, ``-`` and ``_`` — and
the parts are joined by literal dots. The character set is the URL-safe alphabet,
which is why ``+`` and ``/`` do not appear.

The three parts
---------------

Header, payload, and signature, each non-empty:

.. edify-playground::

   from edify.library import jwt

   jwt("eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIn0.dBjftJeZ4CVP-mB92K27uhbUJU1p1r")
   jwt("aaa.bbb.ccc")                      # the minimal shape
   jwt("eyJ0eXAiOiJKV1QifQ.e30.signature")

Base64url, not standard base64
------------------------------

The URL-safe alphabet substitutes ``-`` and ``_`` for ``+`` and ``/``, so a token
containing the standard characters is malformed:

.. edify-playground::

   from edify.library import jwt

   jwt("abc-def.ghi_jkl.mno-pqr")   # the URL-safe characters
   jwt("abc+def.ghi/jkl.mno")       # standard base64 characters
   jwt("abc.def.ghi=")              # padding is not used

Exactly three parts
-------------------

Two parts is an unsigned token in a different serialisation, five is JWE, and an
empty segment is never valid:

.. edify-playground::

   from edify.library import jwt

   jwt("aaa.bbb.ccc")     # three parts
   jwt("aaa.bbb")         # too few
   jwt("aaa.bbb.ccc.ddd") # too many
   jwt("aaa..ccc")        # an empty segment
   jwt("hello-world")     # no dots at all

This is a structural check only. It does **not** verify the signature, decode the
claims, or check ``exp`` — a well-formed token from an attacker looks exactly like
a real one, so always verify the signature before trusting any claim. For the
header that carries a token see :doc:`bearer`; for opaque tokens with no internal
structure, :doc:`token`.
