ip
==

:doc:`Library <../index>` › :doc:`Address <index>` › **ip**

``ip`` matches an IP address of **either** family — it is the union of
:doc:`ipv4` and :doc:`ipv6`, useful when a field may hold either.

.. code-block:: python

   from edify.library import ip

   ip("192.168.0.1")   # True

An IPv4 address
---------------

Everything :doc:`ipv4` accepts — four range-checked octets:

.. code-block:: python

   ip("192.168.0.1")   # True
   ip("8.8.8.8")       # True
   ip("0.0.0.0")       # True

An IPv6 address
---------------

Everything :doc:`ipv6` accepts — full form, ``::`` compression, embedded IPv4,
and scoped zones:

.. code-block:: python

   ip("2001:db8::1")   # True
   ip("::1")           # True — loopback
   ip("fe80::1%eth0")  # True — scoped link-local

What it rejects
---------------

.. code-block:: python

   ip("999.1.1.1")   # False — IPv4 octet out of range
   ip("gg::")        # False — not valid hex

When you need to pin the family, reach for :doc:`ipv4` or :doc:`ipv6` directly.
``ip`` checks the textual form only, not reachability or allocation.

Try it
------

.. edify-playground::
   :tests: 192.168.0.1|8.8.8.8|2001:db8::1|::1|999.1.1.1|gg::

   from edify.library import ip
   ip
