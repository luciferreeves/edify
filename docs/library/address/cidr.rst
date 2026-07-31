CIDR
====

`CIDR <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__ notation
(:rfc:`4632`) is an address, a slash, and a prefix length — ``192.168.1.0/24``.
**CIDR** handles both families, and the only real subtlety is that each family caps
the prefix differently, so it is worth taking them one at a time.

Each family is one branch of an :func:`~edify.any_of`: an address, a ``/``, and a
prefix. The prefix is not "one or two digits" — it is its own :func:`~edify.any_of` of
range branches that stops at the family maximum, the same value-checked technique
:doc:`port` uses. On the IPv4 side the address is the range-checked
:doc:`octet <../../guide/composing>` quad from :doc:`ipv4`; on the IPv6 side it is the
plain full-form :doc:`hex group <../../guide/composing>` chain — which is exactly why
``::`` compression is *not* accepted here.

IPv4 blocks
-----------

A dotted-quad — each octet range-checked exactly as in :doc:`ipv4` — then ``/`` and a
prefix from **0 to 32**. Because the prefix is validated rather than merely counted,
``/33`` is rejected, and so is an address with a bad octet:

.. edify-playground::

   from edify.library import cidr

   cidr("10.0.0.0/8")     # a class-A sized block
   cidr("1.2.3.4/32")     # a single host
   cidr("0.0.0.0/0")      # the default route
   cidr("10.0.0.0/33")    # prefix above the IPv4 maximum
   cidr("256.0.0.0/8")    # octet out of range
   cidr("10.0.0.0")       # no prefix at all

IPv6 blocks
-----------

Colon-separated hex groups, then ``/`` and a prefix from **0 to 128**. One catch: here
the address must be written **in full** — ``::`` zero-compression is not accepted on
the IPv6 side of **CIDR**, though it is on the standalone :doc:`ipv6`:

.. edify-playground::

   from edify.library import cidr

   cidr("2001:db8:0:0:0:0:0:0/64")    # a routable block, written out
   cidr("2001:db8:0:0:0:0:0:1/128")   # a single IPv6 host
   cidr("2001:db8::/32")              # :: compression on the address side

For an address with no prefix use :doc:`ipv4`, :doc:`ipv6`, or :doc:`ip`; for a
dotted-decimal mask instead of a prefix length, :doc:`subnet`.
