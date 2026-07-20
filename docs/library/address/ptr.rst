ptr
===

A PTR record is a reverse-DNS name — the name you look up to turn an address
*back* into a hostname. There is one form per family, and ``ptr`` matches either;
both allow an optional trailing dot for the fully-qualified form.

IPv4 — ``in-addr.arpa``
-----------------------

The four octets of the address, **reversed**, followed by the literal
``in-addr.arpa``. So a lookup for ``127.0.0.1`` is written
``1.0.0.127.in-addr.arpa``. A forward address is not a PTR name:

.. code-block:: python

   ptr("1.0.0.127.in-addr.arpa")    # True  — 127.0.0.1 reversed
   ptr("4.3.2.1.in-addr.arpa.")     # True  — with the trailing dot
   ptr("127.0.0.1")                 # False — that's a forward address

.. edify-playground::
   :tests: 1.0.0.127.in-addr.arpa|4.3.2.1.in-addr.arpa.|127.0.0.1

   from edify.library import ptr
   ptr

IPv6 — ``ip6.arpa``
-------------------

All 32 hex nibbles of the address, reversed and dot-separated, followed by
``ip6.arpa`` — one nibble per label, 32 of them:

.. code-block:: python

   ptr("b.a.9.8.7.6.5.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa")   # True
   ptr("example.com")   # False — an ordinary domain, not a reverse record

.. edify-playground::
   :tests: b.a.9.8.7.6.5.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa|example.com

   from edify.library import ptr
   ptr

The two forms are an :func:`~edify.any_of`, anchored at both ends. ``ptr`` checks
the reverse-record shape only — it does not verify that the embedded address is in
range; for that, use :doc:`ipv4` and :doc:`ipv6`.
