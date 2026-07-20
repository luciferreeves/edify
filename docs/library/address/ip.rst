ip
==

``ip`` matches an IP address of **either** family — an IPv4 dotted-quad or any
IPv6 form. It is the union of :doc:`ipv4` and :doc:`ipv6`, for the common case
where a field may legitimately hold either.

Under the hood it is exactly that union: edify takes the body of :doc:`ipv4`
(four range-checked octets) and the body of :doc:`ipv6` (the hex-group
alternation) and combines them with the :func:`~edify.any_of` factory, anchored
with :meth:`~edify.RegexBuilder.start_of_input` /
:meth:`~edify.RegexBuilder.end_of_input`:

.. code-block:: python

   from edify import Pattern, any_of

   ip = (
       Pattern().start_of_input()
       .use(any_of(ipv4_body, ipv6_body))
       .end_of_input()
   )

which emits:

.. code-block:: text

   ^(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}|<the full IPv6 alternation>)$

An IPv4 address
---------------

Everything :doc:`ipv4` accepts — four dot-separated octets, each range-checked to
0–255:

.. code-block:: python

   ip("192.168.0.1")   # True
   ip("8.8.8.8")       # True
   ip("0.0.0.0")       # True
   ip("999.1.1.1")     # False — octet out of range

.. edify-playground::
   :tests: 192.168.0.1|8.8.8.8|0.0.0.0|999.1.1.1

   from edify.library import ip
   ip

An IPv6 address
---------------

Everything :doc:`ipv6` accepts — the full form, ``::`` compression, embedded
IPv4, and scoped ``%zone`` addresses:

.. code-block:: python

   ip("2001:db8::1")    # True
   ip("::1")            # True — loopback
   ip("fe80::1%eth0")   # True — scoped link-local
   ip("gg::")           # False — not valid hex

.. edify-playground::
   :tests: 2001:db8::1|::1|fe80::1%eth0|gg::

   from edify.library import ip
   ip

Notes
-----

- ``ip`` checks the **textual form** only, of either family — not reachability or
  allocation.
- When you need to pin the family, reach for :doc:`ipv4` or :doc:`ipv6` directly;
  for a network block use :doc:`cidr`.
