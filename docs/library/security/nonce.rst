Nonce
=====

A `nonce <https://en.wikipedia.org/wiki/Cryptographic_nonce>`__ is a number used
once — the value that makes an otherwise-identical request unrepeatable. It appears
in Content-Security-Policy headers, replay protection, and challenge-response
exchanges. **Nonce** matches 16 to 256 characters of base64, in either alphabet.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(16, 256)`` over an
:meth:`~edify.RegexBuilder.any_of` class covering standard base64 (``+`` ``/``
``=``) and the URL-safe variant (``-`` ``_``), so a nonce from any source matches.

Nonce values
------------

.. edify-playground::

   from edify.library import nonce

   nonce("Y2hhbGxlbmdlLXZhbHVl")          # base64url
   nonce("rAnd0m+Base64/Value==")         # standard base64 with padding
   nonce("0123456789abcdef")              # the sixteen-character minimum
   nonce("a" * 256)                       # at the maximum

Length bounds
-------------

Sixteen characters is the floor for a value that must not be predicted:

.. edify-playground::

   from edify.library import nonce

   nonce("a" * 16)    # at the minimum
   nonce("a" * 15)    # too short
   nonce("a" * 257)   # too long
   nonce("has space here!!")   # outside the alphabet

The security of a nonce comes from being unpredictable and never reused — neither of
which a pattern can check. Generate it from a cryptographically secure source, store
what you have issued, and reject any repeat. For the challenge-response use see
:doc:`../auth/challenge`; for CSP headers, :doc:`../web/csp`.
