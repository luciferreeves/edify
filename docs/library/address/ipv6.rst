ipv6
====

:doc:`Library <../index>` › :doc:`Address <index>` › **ipv6**

An IPv6 address is, at heart, eight groups of four hexadecimal digits joined by
colons. Almost nobody writes it that way — the notation has a stack of shorthand
rules, and ``ipv6`` accepts all of them: dropped leading zeros, ``::``
zero-compression anywhere in the address, embedded IPv4 tails, and scoped
link-local zones. This page walks every form it takes.

.. code-block:: python

   from edify.library import ipv6

   ipv6("2001:db8::1")   # True

The full form
-------------

Eight colon-separated groups, each **one to four hex digits**. Leading zeros in a
group may be dropped, and a group of all zeros may shrink to a single ``0``:

.. code-block:: python

   ipv6("2001:0db8:0000:0000:0000:ff00:0042:8329")   # True — every digit written out
   ipv6("2001:db8:0:0:0:ff00:42:8329")               # True — leading zeros dropped
   ipv6("2001:DB8:0:0:0:FF00:42:8329")               # True — hex is case-insensitive

A group with more than four digits is not valid:

.. code-block:: python

   ipv6("12345::")   # False — 12345 is five digits

Zero compression with ``::``
----------------------------

A single ``::`` stands in for **one or more consecutive all-zero groups**. It may
appear at the start, the middle, or the end of the address — and the two most
famous IPv6 addresses are nothing but zeros:

.. code-block:: python

   ipv6("2001:db8::ff00:42:8329")   # True — three zero groups collapse in the middle
   ipv6("fe80::")                   # True — trailing zero groups, :: at the end
   ipv6("::1")                      # True — loopback: :: at the start, then 1
   ipv6("::")                       # True — the unspecified address, all zeros

The one rule: ``::`` may appear **at most once**, because two of them would be
ambiguous about how many zero groups each stands for:

.. code-block:: python

   ipv6("1::2::3")   # False — a second :: is ambiguous

.. edify-playground::
   :tests: 2001:db8::ff00:42:8329|fe80::|::1|::|1::2::3

   from edify.library import ipv6
   ipv6

Embedded IPv4
-------------

The last 32 bits may be written as a dotted-quad instead of two hex groups — the
form you see for IPv4-mapped and IPv4-translated addresses:

.. code-block:: python

   ipv6("::ffff:192.0.2.1")       # True — IPv4-mapped
   ipv6("::ffff:0:192.0.2.1")     # True — IPv4-translated
   ipv6("2001:db8::192.0.2.1")    # True — embedded in a routable prefix

Scoped (link-local) addresses
-----------------------------

A link-local address can carry a **zone identifier** after a ``%`` — the
interface it is scoped to, named or numbered:

.. code-block:: python

   ipv6("fe80::1%eth0")   # True — named zone
   ipv6("fe80::1%1")      # True — numeric zone

What it rejects
---------------

.. code-block:: python

   ipv6("gg::")           # False — 'g' is not a hex digit
   ipv6("1.2.3.4")        # False — that's an IPv4 address (use ipv4)
   ipv6("2001:db8::z")    # False — trailing non-hex junk
   ipv6("12345::")        # False — a group may not exceed four digits

``ipv6`` validates the *textual form* only — it says nothing about whether the
address is reachable, allocated, or reserved. For IPv4 use :doc:`ipv4`; to accept
either family use :doc:`ip`; for a network block use :doc:`cidr`.

Pattern
-------

The emitted pattern enumerates every legal placement of ``::`` alongside the full
and embedded-IPv4 forms, so it is long — inspect it with
``ipv6.to_regex_string()`` or render it with ``ipv6.to_regex().explain()``.
