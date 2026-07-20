ipv4
====

An IPv4 address is 32 bits, written as four decimal octets joined by dots —
``192.168.0.1``. Each octet is 0 to 255, and ``ipv4`` enforces that range exactly:
it is a shape check on the dotted-quad, not a lookup of what the address means.

Under the hood, the range check lives in a single reusable
:doc:`octet <../../guide/composing>`
fragment — an :func:`~edify.any_of` over five branches that between them cover
0–255 with no overlap and no gap, which is why ``256`` has no branch to match:

.. code-block:: python

   from edify import Pattern, any_of

   octet = any_of(
       Pattern().string("25").any_of().range("0", "5").end(),       # 250–255
       Pattern().char("2").any_of().range("0", "4").end().digit(),  # 200–249
       Pattern().char("1").digit().digit(),                         # 100–199
       Pattern().any_of().range("1", "9").end().digit(),            # 10–99
       Pattern().digit(),                                           # 0–9
   )

``ipv4`` joins four of those octets with dots — :meth:`~edify.RegexBuilder.exactly`\
``(3)`` of a ``.``-plus-octet :meth:`~edify.RegexBuilder.group` after the first —
between :meth:`~edify.RegexBuilder.start_of_input` and
:meth:`~edify.RegexBuilder.end_of_input`:

.. code-block:: python

   ipv4 = (
       Pattern().start_of_input()
       .use(octet).exactly(3).group().char(".").use(octet).end()
       .end_of_input()
   )

which emits:

.. code-block:: text

   ^(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}$

Four octets, each 0 to 255
--------------------------

Exactly four dot-separated octets — no more, no fewer — and each runs the full
0–255 range, the all-zero network and the all-ones broadcast included. One past
the top, ``256``, is out; so is the wrong octet count, or an IPv6 address:

.. code-block:: python

   ipv4("192.168.0.1")         # True
   ipv4("0.0.0.0")             # True  — this-network
   ipv4("255.255.255.255")     # True  — limited broadcast
   ipv4("256.0.0.1")           # False — 256 is past the top of the range
   ipv4("1.2.3")               # False — only three octets
   ipv4("1.2.3.4.5")           # False — five octets
   ipv4("2001:db8::1")         # False — that's IPv6; use ipv6

.. edify-playground::
   :tests: 192.168.0.1|0.0.0.0|255.255.255.255|256.0.0.1|1.2.3|2001:db8::1

   from edify.library import ipv4
   ipv4

No leading zeros
----------------

An octet is a bare number: a lone ``0`` is fine, but zero-padded octets like
``01`` are rejected. That matters for correctness *and* security — many parsers
read a leading-zero octet as octal, so treating ``010`` as decimal 10 would be a
classic SSRF-style bug:

.. code-block:: python

   ipv4("10.0.0.1")      # True
   ipv4("010.0.0.1")     # False — 010 has a leading zero
   ipv4("192.168.01.1")  # False — 01 has a leading zero

.. edify-playground::
   :tests: 10.0.0.1|192.168.0.1|010.0.0.1|192.168.01.1

   from edify.library import ipv4
   ipv4

``ipv4`` checks the textual form only — it does not care whether an address is
routable, private, or reserved (``127.0.0.1`` and ``0.0.0.0`` both match). The
octet fragment it is built from is reused across the family: for an address plus a
mask length use :doc:`cidr`, for a ``host:port`` pair :doc:`socket`, and for either
IP family :doc:`ip`.
