ip
==

:doc:`Library <../index>` › :doc:`Address <index>` › **ip**

``ip`` matches an IP address of **either** family — an IPv4 dotted-quad or any
IPv6 form. It is the union of :doc:`ipv4` and :doc:`ipv6`.

.. code-block:: python

   from edify.library import ip

   ip("192.168.0.1")   # True — IPv4
   ip("2001:db8::1")   # True — IPv6
   ip("::1")           # True — IPv6 loopback
   ip("999.1.1.1")     # False — octet out of range
   ip("gg::")          # False — not hex

What it matches
---------------

- Everything :doc:`ipv4` matches (four octets, each 0–255), **or**
- Everything :doc:`ipv6` matches (full, compressed, IPv4-mapped, scoped).
- Anchored at both ends.

It does **not** check reachability, allocation, or reserved-range semantics.
Reach for :doc:`ipv4` or :doc:`ipv6` directly when you need to pin the family.

Try it
------

.. edify-playground::
   :tests: 192.168.0.1|8.8.8.8|2001:db8::1|::1|999.1.1.1|gg::

   from edify.library import ip
   ip
