Signature
=========

A `digital signature <https://en.wikipedia.org/wiki/Digital_signature>`__ proves a
message came from the holder of a private key and has not been altered. Transmitted
as base64, it is long — an Ed25519 signature is 64 bytes, RSA signatures far more.
**Signature** matches 64 to 4096 base64 characters.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(64, 4096)`` over an
:meth:`~edify.RegexBuilder.any_of` class covering both base64 alphabets. The
64-character floor is what separates a signature from the shorter tokens and nonces
that share the same character set.

Signature values
----------------

.. edify-playground::

   from edify.library import signature

   signature("a" * 64)      # at the minimum
   signature("a" * 88)      # an Ed25519 signature, base64-encoded
   signature("MEUCIQDx" + "b" * 90)   # an ECDSA signature
   signature("a" * 4096)    # at the maximum

Length bounds
-------------

.. edify-playground::

   from edify.library import signature

   signature("a" * 64)     # at the minimum
   signature("a" * 63)     # too short: see nonce
   signature("a" * 4097)   # too long
   signature("has spaces in it" + "a" * 60)   # outside the alphabet

A signature is meaningless until verified. Matching this pattern tells you a field
*looks* like a signature — it cannot tell you the signature is over the message you
received, was made by the key you expect, or was not replayed from an earlier
request. Verify it with the public key, over the exact bytes, using a constant-time
comparison. For the keyed-hash equivalent see :doc:`../auth/hmac`.
