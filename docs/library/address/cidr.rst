cidr
====

:doc:`Library <../index>` › :doc:`Address <index>` › **cidr**

``cidr`` matches a network block in CIDR notation — an address, a ``/``, and a
prefix length — for both IP families, with the prefix bound checked per family.

.. code-block:: python

   from edify.library import cidr

   cidr("192.168.1.0/24")   # True

IPv4 blocks
-----------

A dotted-quad (each octet range-checked exactly like :doc:`ipv4`) followed by a
prefix from ``/0`` to ``/32``:

.. code-block:: python

   cidr("10.0.0.0/8")        # True
   cidr("192.168.1.0/24")    # True
   cidr("1.2.3.4/32")        # True — a single host
   cidr("0.0.0.0/0")         # True — the default route, the whole address space

IPv6 blocks
-----------

Colon-separated hex groups followed by a prefix from ``/0`` to ``/128``:

.. code-block:: python

   cidr("2001:db8:0:0:0:0:0:0/64")    # True
   cidr("2001:db8:0:0:0:0:0:1/128")   # True — a single IPv6 host

.. note::

   The IPv6 **address** portion must be written out in full — ``::``
   zero-compression is not accepted here, so ``2001:db8::/32`` is rejected; write
   ``2001:db8:0:0:0:0:0:0/32``. (The standalone :doc:`ipv6` validator *does*
   accept ``::``.)

The prefix is bounded per family
--------------------------------

The prefix length is validated against the family maximum — 32 for IPv4, 128 for
IPv6 — digit by digit:

.. code-block:: python

   cidr("10.0.0.0/32")     # True  — /32 is the IPv4 maximum
   cidr("10.0.0.0/33")     # False — one past the IPv4 maximum
   cidr("2001:db8:0:0:0:0:0:0/128")   # True  — /128 is the IPv6 maximum

What it rejects
---------------

.. code-block:: python

   cidr("10.0.0.0")        # False — no prefix at all
   cidr("2001:db8::/32")   # False — :: compression on the address side
   cidr("10.0.0/8")        # False — the IPv4 address is incomplete
   cidr("256.0.0.0/8")     # False — an octet is out of range

Try it
------

.. edify-playground::
   :tests: 10.0.0.0/8|192.168.1.0/24|1.2.3.4/32|0.0.0.0/0|10.0.0.0/33|2001:db8::/32

   from edify.library import cidr
   cidr

Pattern
-------

.. code-block:: text

   ^(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}/(?:3[0-2]|[12]?\d)|(?:[0-9a-fA-F]{1,4}:){0,7}[0-9a-fA-F]{1,4}/(?:12[0-8]|1[01]\d|[1-9]?\d))$
