Secret
======

A shared secret is the value two parties both hold — a client secret in an OAuth
exchange, a webhook signing secret, or an application key. **Secret** matches 16 to
256 characters of letters, digits, ``-``, and ``_``.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(16, 256)`` over an
:meth:`~edify.RegexBuilder.any_of` class of alphanumerics plus the two URL-safe
marks. The 16-character floor is the practical minimum for a value that must resist
offline guessing.

Common forms
------------

Prefixed client secrets and raw random strings alike:

.. edify-playground::

   from edify.library import secret

   secret("cs_test_a1B2c3D4e5F6g7H8i9J0")   # a prefixed client secret
   secret("whsec_ZGVmYXVsdF9zZWNyZXQ")      # a webhook signing secret
   secret("0123456789abcdef")               # the sixteen-character minimum

Alphabet and bounds
-------------------

.. edify-playground::

   from edify.library import secret

   secret("a" * 256)                # at the maximum
   secret("0123456789abcde")        # fifteen: too short
   secret("a" * 257)                # too long
   secret("secret with spaces!!")   # spaces and punctuation

A secret's whole value is that it stays unknown, so this checks shape only — it
cannot tell you whether the value has leaked. Keep secrets out of source control
and logs, compare them with a constant-time check rather than ``==``, and rotate
them on any suspicion of exposure. For the key used to sign payloads see
:doc:`signing`; for the resulting code, :doc:`hmac`.
