ip
==

``ip`` is the union of :doc:`ipv4` and :doc:`ipv6` — it accepts an address of
either family, for the common case where a field may hold one or the other. It is
built by combining their two bodies with :func:`~edify.any_of`, so it inherits
every rule each of them enforces.

.. edify-playground::
   :tests: 192.168.0.1|8.8.8.8|2001:db8::1|::1|fe80::1%eth0|999.1.1.1|gg::

   from edify.library import ip
   ip

Everything on the IPv4 side is exactly :doc:`ipv4` — four range-checked octets,
``256`` and friends rejected. Everything on the IPv6 side is exactly :doc:`ipv6` —
the full form, ``::`` compression, embedded IPv4, and scoped ``%zone`` addresses.
When you need to pin the family, use those two directly; for a network block, use
:doc:`cidr`. Like both, ``ip`` is a shape check — it says nothing about
reachability.
