ipv6
====

:doc:`Library <../index>` › :doc:`Address <index>` › **ipv6**

``ipv6`` matches an IPv6 address in any of its standard textual forms — full
eight-group notation, ``::`` zero-compression, IPv4-mapped tails, and
``fe80::…%zone`` scoped link-local addresses.

.. code-block:: python

   from edify.library import ipv6

   ipv6("2001:db8::1")                       # True — :: compression
   ipv6("fe80::1")                           # True
   ipv6("::1")                               # True — loopback
   ipv6("2001:db8:0:0:0:0:0:1")              # True — full eight groups
   ipv6("1.2.3.4")                           # False — that's IPv4
   ipv6("gg::")                              # False — 'g' isn't a hex digit

What it matches
---------------

- **Full form**: eight colon-separated groups of 1–4 hex digits.
- **Compressed form**: a single ``::`` standing in for one or more all-zero
  groups, anywhere in the address.
- **IPv4-mapped tails**: ``::ffff:192.0.2.1`` and the embedded-IPv4 variants.
- **Scoped link-local**: ``fe80::1%eth0`` with a zone identifier.
- Anchored at both ends.

It does **not** check reachability or reserved-range semantics. For IPv4 use
:doc:`ipv4`; for "either family" use :doc:`ip`.

Try it
------

.. edify-playground::
   :tests: 2001:db8::1|fe80::1|::1|2001:db8:0:0:0:0:0:1|1.2.3.4|gg::

   from edify.library import ipv6
   ipv6

Pattern
-------

The pattern enumerates every legal placement of ``::`` alongside the full and
IPv4-mapped forms; it is long by necessity. Emit it with
``ipv6.to_regex_string()`` to see the whole thing.
