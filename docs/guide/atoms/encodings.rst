Encoding atoms
==============

Twelve fragments for base-N alphabets, hash digests, and unique identifiers — the
pieces behind :doc:`../../library/text/base`,
:doc:`../../library/numeric/hash`, and :doc:`../../library/identifier/uuid`.

Compose them into an anchored pattern rather than calling them directly; see
:doc:`index`.

Base alphabets
--------------

Four alphabets, differing in which characters they use and whether they pad.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import base32, base58, base64, base64url

   b32 = Pattern().start_of_input().use(base32).end_of_input()
   b58 = Pattern().start_of_input().use(base58).end_of_input()
   b64 = Pattern().start_of_input().use(base64).end_of_input()
   b64u = Pattern().start_of_input().use(base64url).end_of_input()

   b32("JBSWY3DP")        # uppercase and 2-7
   b32("jbswy3dp")        # lowercase is not base32
   b58("1BvBMSEYstWet")   # no 0, O, I or l
   b64("SGVsbG8=")        # padding allowed
   b64u("SGVsbG8-_")      # URL-safe marks instead of + and /

Hash digests
------------

``hexstring`` is any run of hex; ``md5`` and ``sha256`` pin the exact widths.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import hexstring, md5, sha256

   hx = Pattern().start_of_input().use(hexstring).end_of_input()
   m = Pattern().start_of_input().use(md5).end_of_input()
   s = Pattern().start_of_input().use(sha256).end_of_input()

   hx("deadbeef")     # any length
   m("a" * 32)        # exactly 32
   m("a" * 31)        # one short
   s("b" * 64)        # exactly 64

Unique identifiers
------------------

``uuid`` pins version 4 specifically; ``guid`` accepts any version. ``ulid``,
``objectid``, and ``oid`` cover the other common schemes.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import uuid, guid, ulid, objectid, oid

   u = Pattern().start_of_input().use(uuid).end_of_input()
   g = Pattern().start_of_input().use(guid).end_of_input()
   ul = Pattern().start_of_input().use(ulid).end_of_input()
   ob = Pattern().start_of_input().use(objectid).end_of_input()
   o = Pattern().start_of_input().use(oid).end_of_input()

   u("550e8400-e29b-41d4-a716-446655440000")   # version 4
   u("550e8400-e29b-11d4-a716-446655440000")   # version 1: uuid is v4-only
   g("550e8400-e29b-11d4-a716-446655440000")   # guid accepts it
   ul("01ARZ3NDEKTSV4RRFFQ69G5FAV")            # 26 Crockford base32 characters
   ob("507f1f77bcf86cd799439011")              # 24 hex characters
   o("1.2.840.10008")                          # a dotted object identifier

The ``uuid``/``guid`` split is the one to remember: reach for ``uuid`` when you want
randomly generated identifiers specifically, and ``guid`` when accepting whatever a
system hands you.

Next: :doc:`datetime`.
