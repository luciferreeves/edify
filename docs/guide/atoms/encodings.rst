Encoding atoms
==============

Twelve fragments for base-N alphabets, hash digests, and unique identifiers — the
pieces behind :doc:`../../library/text/base`,
:doc:`../../library/numeric/hash`, and :doc:`../../library/identifier/uuid`.

Compose them into an anchored pattern rather than calling them directly; see
:doc:`index`.

Base alphabets
--------------

Four alphabets, differing in which characters they use and whether they pad:

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Atom
     - Alphabet
     - Padding
   * - ``base32``
     - ``A-Z`` and ``2-7``, uppercase only
     - optional trailing ``=``
   * - ``base58``
     - alphanumerics minus ``0``, ``O``, ``I``, ``l``
     - none — the encoding has no padding
   * - ``base64``
     - alphanumerics plus ``+`` and ``/``
     - optional trailing ``=``
   * - ``base64url``
     - alphanumerics plus ``-`` and ``_``
     - **none** — padding is rejected

The exclusions in ``base58`` are the point of that alphabet: ``0``/``O`` and
``I``/``l`` are the character pairs people mistranscribe, so leaving them out makes
an identifier safe to read aloud or copy by hand.

The ``base64``/``base64url`` split matters more than it looks. They use different
characters for the last two slots *and* differ on padding, so a value valid in one
is often invalid in the other — which is exactly why the URL-safe variant exists,
since ``+`` and ``/`` need escaping in a query string.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import base32, base58, base64, base64url

   b32 = Pattern().start_of_input().use(base32).end_of_input()
   b58 = Pattern().start_of_input().use(base58).end_of_input()
   b64 = Pattern().start_of_input().use(base64).end_of_input()
   b64u = Pattern().start_of_input().use(base64url).end_of_input()

   b32("JBSWY3DP")        # uppercase and 2-7
   b32("MZXW6===")        # padding is allowed
   b32("jbswy3dp")        # lowercase is not base32
   b58("1BvBMSEYstWet")   # no 0, O, I or l
   b64("SGVsbG8=")        # padding allowed
   b64("a+b/c")           # plus and slash
   b64u("SGVsbG8-_")      # URL-safe marks instead of + and /
   b64u("SGVsbG8=")       # and no padding

None of these verifies that the payload decodes — they check the alphabet and the
shape. A string of the right characters and a wrong length still matches; decode it
to find out.

Hash digests
------------

``hexstring`` is any run of hex digits, either case, with no prefix — so ``0xFF``
does **not** match it (that is ``hexnum``, in :doc:`numbers`). ``md5`` and
``sha256`` are the same alphabet with the width pinned exactly, 32 and 64
characters respectively.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import hexstring, md5, sha256

   hx = Pattern().start_of_input().use(hexstring).end_of_input()
   m = Pattern().start_of_input().use(md5).end_of_input()
   s = Pattern().start_of_input().use(sha256).end_of_input()

   hx("deadBEEF")     # any length, either case
   hx("0xFF")         # but no prefix
   m("a" * 32)        # exactly 32
   m("a" * 31)        # one short
   s("b" * 64)        # exactly 64

Because the width is the only thing distinguishing them, any 32-character hex
string matches ``md5`` — including a truncated SHA-256. The pattern tells you the
shape is right, never that the digest is.

Unique identifiers
------------------

Five identifier schemes, and the ``uuid``/``guid`` distinction is the one to
remember.

``uuid`` pins **version 4** specifically: it requires a literal ``4`` in the
version position and one of ``8``, ``9``, ``a``, ``b`` in the variant position.
``guid`` accepts any version in that slot. So a v1 identifier — the timestamp-based
kind — matches ``guid`` and not ``uuid``.

``ulid`` is 26 characters of Crockford base32, which excludes ``I``, ``L``, ``O``,
and ``U`` and is uppercase-only. ``objectid`` is 24 hex characters. ``oid`` is a
dotted numeric identifier requiring at least two components, so a bare ``1`` does
not match.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import guid, objectid, oid, ulid, uuid

   u = Pattern().start_of_input().use(uuid).end_of_input()
   g = Pattern().start_of_input().use(guid).end_of_input()
   ul = Pattern().start_of_input().use(ulid).end_of_input()
   ob = Pattern().start_of_input().use(objectid).end_of_input()
   o = Pattern().start_of_input().use(oid).end_of_input()

   u("550e8400-e29b-41d4-a716-446655440000")   # version 4
   u("550e8400-e29b-11d4-a716-446655440000")   # version 1: uuid is v4-only
   g("550e8400-e29b-11d4-a716-446655440000")   # guid accepts it
   ul("01ARZ3NDEKTSV4RRFFQ69G5FAV")            # 26 Crockford base32 characters
   ul("01arz3ndektsv4rrffq69g5fav")            # uppercase only
   ob("507f1f77bcf86cd799439011")              # 24 hex characters
   o("1.2.840.10008")                          # a dotted object identifier
   o("1")                                      # two components minimum

Reach for ``uuid`` when you want randomly generated identifiers specifically — a
v1 identifier leaks a timestamp and a MAC address, which is sometimes exactly what
you are trying to exclude. Reach for ``guid`` when accepting whatever a system
hands you.

Next: :doc:`datetime`.
