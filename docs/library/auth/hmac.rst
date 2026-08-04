HMAC
====

An `HMAC <https://datatracker.ietf.org/doc/html/rfc2104>`__ (:rfc:`2104`) is a
message authentication code: a hash of the payload keyed with a shared secret, sent
alongside the message so the receiver can confirm both origin and integrity. It is
normally transmitted as hexadecimal, and **HMAC** matches 32 to 128 hex digits —
the range spanning MD5 through SHA-512 output.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(32, 128)`` over an
:meth:`~edify.RegexBuilder.any_of` class of ``0``–``9``, ``a``–``f``, and
``A``–``F``, so either case of hex is accepted.

Digest lengths
--------------

Each algorithm produces a fixed width, and all the common ones fall in range:

.. edify-playground::

   from edify.library import hmac

   hmac("5d41402abc4b2a76b9719d911017c592")                    # 32 hex digits
   hmac("a" * 40)                                              # SHA-1 width
   hmac("2c26b46b68ffc68ff99b453c1d304134" * 2)                # SHA-256 width
   hmac("f" * 128)                                             # SHA-512 width

Hexadecimal in either case
--------------------------

Upper and lower case both appear in the wild; base64-encoded codes do not match,
since they use a different alphabet:

.. edify-playground::

   from edify.library import hmac

   hmac("ABCDEF0123456789" * 2)     # uppercase hex
   hmac("abcdef0123456789" * 2)     # lowercase hex
   hmac("g" * 32)                   # g is not a hex digit
   hmac("YWJjZGVmZ2hpamtsbW5vcA==")  # base64, not hex

Width bounds
------------

.. edify-playground::

   from edify.library import hmac

   hmac("a" * 32)    # at the minimum
   hmac("a" * 31)    # too short
   hmac("a" * 129)   # too long

Matching the shape says nothing about whether the code is *correct* — that requires
recomputing it with the shared secret over the exact payload received. Compare the
result with a constant-time function: a plain ``==`` leaks timing information that
lets an attacker forge a code byte by byte. For the secret behind it see
:doc:`signing` and :doc:`secret`.
