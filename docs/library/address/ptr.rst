ptr
===

A PTR record is a reverse-DNS name — the thing you look up to turn an address
*back* into a hostname. There are two, one per family, and ``ptr`` matches either:

.. edify-playground::
   :tests: 1.0.0.127.in-addr.arpa|4.3.2.1.in-addr.arpa.|b.a.9.8.7.6.5.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa|127.0.0.1

   from edify.library import ptr
   ptr

For **IPv4**, the four octets of the address are reversed and followed by
``in-addr.arpa`` — ``127.0.0.1`` becomes ``1.0.0.127.in-addr.arpa``. For **IPv6**,
all 32 hex nibbles are reversed, dot-separated, and followed by ``ip6.arpa``. Both
allow an optional trailing dot for the fully-qualified form.

A forward address (``127.0.0.1``) or an ordinary domain is not a PTR name, so both
are rejected. ``ptr`` matches the reverse-record shape only — it doesn't check that
the embedded address is in range; for that, :doc:`ipv4` and :doc:`ipv6`.
