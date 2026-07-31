Hash
====

**Hash** matches a `hash digest <https://en.wikipedia.org/wiki/Cryptographic_hash_function>`__
written as hexadecimal — 8 to 128 hex digits, which spans a CRC32 through a
SHA-512.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(8, 128)`` over an
:meth:`~edify.RegexBuilder.any_of` class of ``0``–``9``, ``a``–``f``, and
``A``–``F``, so either case matches.

Digest widths
-------------

Each algorithm produces a fixed number of hex characters:

.. edify-playground::

   from edify.library import hash

   hash("deadbeef")                                   # 8: a CRC32
   hash("5d41402abc4b2a76b9719d911017c592")           # 32: an MD5
   hash("a" * 40)                                     # 40: a SHA-1
   hash("a" * 64)                                     # 64: a SHA-256
   hash("a" * 128)                                    # 128: a SHA-512

Hexadecimal in either case
--------------------------

.. edify-playground::

   from edify.library import hash

   hash("DEADBEEF")   # uppercase
   hash("deadbeef")   # lowercase
   hash("DeadBeef")   # mixed
   hash("deadbeeg")   # g is not a hex digit

Width bounds
------------

.. edify-playground::

   from edify.library import hash

   hash("a" * 8)     # at the minimum
   hash("a" * 7)     # too short
   hash("a" * 129)   # too long
   hash("")          # empty

Because the range is wide, matching does not identify *which* algorithm produced a
digest — check the length yourself if that matters. Base64-encoded digests use a
different alphabet; see :doc:`../text/base`. For keyed authentication codes see
:doc:`../auth/hmac`.
