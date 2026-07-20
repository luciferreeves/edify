ptr
===

.. edify-validator:: ptr

``ptr`` matches a reverse-DNS PTR record name — the ``in-addr.arpa`` form for
IPv4 or the ``ip6.arpa`` nibble form for IPv6. These are the names you look up to
turn an address back into a hostname.

Under the hood it is an :func:`~edify.any_of` of two shapes: four
:meth:`~edify.RegexBuilder.between`\ ``(1, 3)``-digit groups followed by the
literal ``in-addr.arpa``, or 32 single hex nibbles followed by ``ip6.arpa`` — each
with an optional trailing dot for the fully-qualified form, anchored with
:meth:`~edify.RegexBuilder.start_of_input` / :meth:`~edify.RegexBuilder.end_of_input`:

.. code-block:: python

   from edify import Pattern, any_of

   ptr = (
       Pattern().start_of_input()
       .use(any_of(ipv4_in_addr_arpa, ipv6_ip6_arpa))
       .end_of_input()
   )

IPv4 reverse records
--------------------

The four octets of an IPv4 address, reversed, then ``in-addr.arpa`` — with an
optional trailing dot. A forward address is not a PTR name:

.. code-block:: python

   ptr("1.0.0.127.in-addr.arpa")    # True — 127.0.0.1 reversed
   ptr("4.3.2.1.in-addr.arpa.")     # True — the fully-qualified form
   ptr("127.0.0.1")                 # False — that's a forward address

.. edify-playground::
   :tests: 1.0.0.127.in-addr.arpa|4.3.2.1.in-addr.arpa.|127.0.0.1

   from edify.library import ptr
   ptr

IPv6 reverse records
--------------------

All 32 hex nibbles of an IPv6 address, reversed and dot-separated, then
``ip6.arpa``:

.. code-block:: python

   ptr("b.a.9.8.7.6.5.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa")   # True
   ptr("example.com")   # False — an ordinary domain, not a reverse record

.. edify-playground::
   :tests: b.a.9.8.7.6.5.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa|example.com

   from edify.library import ptr
   ptr

Notes
-----

- ``ptr`` checks the reverse-record *shape*; it does not verify that the embedded
  address is itself in range. For forward addresses use :doc:`ipv4` / :doc:`ipv6`.
