PTR record
==========

A `PTR record <https://en.wikipedia.org/wiki/Reverse_DNS_lookup>`__ is a reverse-DNS
name — the name you look up to turn an address *back* into a hostname. There is one
form per family, and **PTR record** matches either.

Both forms are the branches of an :func:`~edify.any_of`, anchored end to end, and both
allow an :meth:`~edify.RegexBuilder.optional` trailing dot for the fully-qualified
form.

IPv4 — ``in-addr.arpa``
-----------------------

The four octets of the address, **reversed**, followed by the literal
``in-addr.arpa`` (:rfc:`1035`). So a lookup for ``127.0.0.1`` is written
``1.0.0.127.in-addr.arpa``. A forward address is not a PTR name:

.. edify-playground::

   from edify.library import ptr

   ptr("1.0.0.127.in-addr.arpa")   # 127.0.0.1 reversed
   ptr("4.3.2.1.in-addr.arpa.")    # with the trailing dot
   ptr("127.0.0.1")                # that's a forward address

IPv6 — ``ip6.arpa``
-------------------

All 32 hex :doc:`nibbles <../../guide/atoms/network>` of the address, reversed and
dot-separated, followed by ``ip6.arpa`` (:rfc:`3596`) — one nibble per label, 32 of
them, via :meth:`~edify.RegexBuilder.exactly`\ ``(32)``:

.. edify-playground::

   from edify.library import ptr

   ptr("b.a.9.8.7.6.5.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa")   # 32 nibbles
   ptr("example.com")   # an ordinary domain, not a reverse record

**PTR record** checks the reverse-record shape only — it does not verify that the
embedded address is in range; for that, use :doc:`ipv4` and :doc:`ipv6`.
