IP
==

**IP** accepts an address of *either* family: it is the union of :doc:`ipv4`
(:rfc:`791`) and :doc:`ipv6` (:rfc:`4291`), so it inherits every rule each of them
enforces. Reach for it when a field may legitimately hold one or the other; to pin a
single family, use the specific validator.

It adds no grammar of its own. It takes the whole un-anchored body of each family
validator and offers them as the two branches of a single :func:`~edify.any_of`,
anchored with :meth:`~edify.RegexBuilder.start_of_input` /
:meth:`~edify.RegexBuilder.end_of_input` — the :doc:`octet <../../guide/atoms/network>`
range check of :doc:`ipv4` and the :doc:`hex group <../../guide/atoms/network>` layouts of
:doc:`ipv6`, side by side.

An IPv4 address
---------------

Everything :doc:`ipv4` accepts — four dot-separated octets, each range-checked to
0–255, with an out-of-range octet or the wrong octet count rejected:

.. edify-playground::

   from edify.library import ip

   ip("192.168.0.1")   # a private address
   ip("8.8.8.8")       # a public resolver
   ip("0.0.0.0")       # this-network
   ip("999.1.1.1")     # octet out of range
   ip("1.2.3")         # only three octets

An IPv6 address
---------------

Everything :doc:`ipv6` accepts — the full eight-group form, ``::`` compression, the
embedded-IPv4 tail, and the scoped ``%zone`` form:

.. edify-playground::

   from edify.library import ip

   ip("2001:db8::1")    # :: compression
   ip("::1")            # loopback
   ip("fe80::1%eth0")   # scoped link-local
   ip("gg::")           # not valid hex

Because it is a straight union, **IP** says nothing more than "valid IPv4 or valid
IPv6" — a textual-form check, with no reachability or allocation semantics. When you
need the family pinned, use :doc:`ipv4` or :doc:`ipv6` directly; for a network block,
:doc:`cidr`; for a ``host:port`` pair, :doc:`socket`.
