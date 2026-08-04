Challenge
=========

In a `challenge-response <https://en.wikipedia.org/wiki/Challenge%E2%80%93response_authentication>`__
exchange the server sends a fresh unpredictable value and the client proves itself by
transforming it — signing it with a key, or hashing it with a password. The
challenge itself is an opaque nonce, and **Challenge** matches 16 to 128 characters
of letters, digits, ``-``, and ``_``.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(16, 128)`` over an
:meth:`~edify.RegexBuilder.any_of` class — the URL-safe alphabet, since a challenge
is commonly delivered in JSON or a header.

Server-issued nonces
--------------------

.. edify-playground::

   from edify.library import challenge

   challenge("Y2hhbGxlbmdlLXZhbHVl")             # a base64url nonce
   challenge("0123456789abcdef")                  # the sixteen-character minimum
   challenge("nonce_2024-abcdefghijklmnop")       # both punctuation marks

Length bounds
-------------

.. edify-playground::

   from edify.library import challenge

   challenge("a" * 16)    # at the minimum
   challenge("a" * 128)   # at the maximum
   challenge("a" * 15)    # too short
   challenge("a" * 129)   # too long

Outside the alphabet
--------------------

.. edify-playground::

   from edify.library import challenge

   challenge("abcdefghij0123456")    # valid
   challenge("abcdef ghij012345")    # a space
   challenge("abcdef+ghij012345")    # + is not URL-safe

The security of a challenge rests on being used once and never predicted — a
matching shape says nothing about either. Generate it from a cryptographically
secure source, bind it to the pending request, expire it quickly, and reject any
replay. For the credential type built on this exchange see :doc:`webauthn`.
