ip
==

``ip`` accepts an address of **either** family — it is the union of :doc:`ipv4`
and :doc:`ipv6`, built by combining their two bodies with :func:`~edify.any_of`.
So it inherits every rule each of them enforces, and is the validator to reach for
when a field may legitimately hold one or the other.

An IPv4 address
---------------

Everything :doc:`ipv4` accepts — four dot-separated octets, each range-checked to
0–255, with ``256`` and the wrong octet count rejected:

.. code-block:: python

   ip("192.168.0.1")   # True
   ip("8.8.8.8")       # True
   ip("0.0.0.0")       # True
   ip("999.1.1.1")     # False — octet out of range
   ip("1.2.3")         # False — only three octets

.. edify-playground::
   :tests: 192.168.0.1|8.8.8.8|0.0.0.0|999.1.1.1|1.2.3

   from edify.library import ip
   ip

An IPv6 address
---------------

Everything :doc:`ipv6` accepts — the full eight-group form, ``::`` compression,
the embedded-IPv4 tail, and the scoped ``%zone`` form:

.. code-block:: python

   ip("2001:db8::1")    # True — :: compression
   ip("::1")            # True — loopback
   ip("fe80::1%eth0")   # True — scoped link-local
   ip("gg::")           # False — not valid hex

.. edify-playground::
   :tests: 2001:db8::1|::1|fe80::1%eth0|gg::

   from edify.library import ip
   ip

Because it is a straight union, ``ip`` says nothing more than "valid IPv4 or valid
IPv6" — a textual-form check, with no reachability or allocation semantics. When
you need to pin the family, use :doc:`ipv4` or :doc:`ipv6` directly; for a network
block, :doc:`cidr`.
