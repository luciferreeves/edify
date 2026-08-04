IPv4
====

An IPv4 address is 32 bits, written as four decimal octets joined by dots —
``192.168.0.1`` (:rfc:`791`). Each octet is 0 to 255, and **IPv4** enforces that range
exactly: it is a shape check on the dotted-quad, not a lookup of what the address
means, so ``127.0.0.1`` and ``0.0.0.0`` both match regardless of whether they are
routable.

The range check lives in one reusable :doc:`octet <../../guide/atoms/network>` fragment —
an :func:`~edify.any_of` over five branches that between them cover 0–255 with no
overlap and no gap (``250``–``255``, ``200``–``249``, ``100``–``199``, ``10``–``99``,
and ``0``–``9``), which is why ``256`` has no branch to match. **IPv4** joins four of
those octets with dots — :meth:`~edify.RegexBuilder.exactly`\ ``(3)`` of a
``.``-plus-octet :meth:`~edify.RegexBuilder.group` after the first — between
:meth:`~edify.RegexBuilder.start_of_input` and :meth:`~edify.RegexBuilder.end_of_input`.

Four octets, each 0 to 255
--------------------------

Exactly four dot-separated octets — no more, no fewer — and each runs the full 0–255
range, the all-zero network and the all-ones broadcast included. One past the top,
``256``, is out; so is the wrong octet count, or an IPv6 address:

.. edify-playground::

   from edify.library import ipv4

   ipv4("192.168.0.1")       # a private address
   ipv4("0.0.0.0")           # this-network
   ipv4("255.255.255.255")   # limited broadcast
   ipv4("256.0.0.1")         # 256 is past the top of the range
   ipv4("1.2.3")             # only three octets
   ipv4("1.2.3.4.5")         # five octets
   ipv4("2001:db8::1")       # that is IPv6

No leading zeros
----------------

An octet is a bare number: a lone ``0`` is fine, but zero-padded octets like ``01``
are rejected. That matters for correctness *and* security — many parsers read a
leading-zero octet as octal, so treating ``010`` as decimal 10 is a classic
`SSRF <https://owasp.org/www-community/attacks/Server_Side_Request_Forgery>`__-style
bug that this no-leading-zero rule closes off:

.. edify-playground::

   from edify.library import ipv4

   ipv4("10.0.0.1")       # a bare octet
   ipv4("192.168.0.1")    # another
   ipv4("010.0.0.1")      # 010 has a leading zero
   ipv4("192.168.01.1")   # 01 has a leading zero

The :doc:`octet <../../guide/atoms/network>` fragment is reused across the family: for an
address plus a mask length use :doc:`cidr`, for a ``host:port`` pair :doc:`socket`,
and to accept either IP family with one validator, :doc:`ip`.
