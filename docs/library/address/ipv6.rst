ipv6
====

An IPv6 address is eight groups of four hexadecimal digits joined by colons —
``2001:0db8:0000:0000:0000:ff00:0042:8329`` — but almost nobody writes the full
form. The notation has a stack of shorthands, and ``ipv6`` accepts every one:
dropped leading zeros, ``::`` zero-compression, embedded IPv4 tails, and scoped
link-local zones.

Edify composes it from a single **hex group** — one to four hex digits, written
as :meth:`~edify.RegexBuilder.between`\ ``(1, 4)`` of a
:doc:`nibble <../../guide/composing>` (a ``0``–``9`` ``a``–``f`` ``A``–``F``
character class). Those groups feed an :func:`~edify.any_of` alternation with one
branch for the full eight-group form, one for **each placement of** ``::`` (the
start, the end, and every interior split), one for the ``fe80::…%zone`` link-local
form, and one for the embedded-IPv4 tail — the whole alternation anchored between
:meth:`~edify.RegexBuilder.start_of_input` and
:meth:`~edify.RegexBuilder.end_of_input`. The regex that falls out:

.. code-block:: text

   ^(?:(?:(?:[0-9a-fA-F]){1,4}:){7}(?:[0-9a-fA-F]){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,7}:|(?:(?:[0-9a-fA-F]){1,4}:){1,6}:(?:[0-9a-fA-F]){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,5}(?::(?:[0-9a-fA-F]){1,4}){1,2}|(?:(?:[0-9a-fA-F]){1,4}:){1,4}(?::(?:[0-9a-fA-F]){1,4}){1,3}|(?:(?:[0-9a-fA-F]){1,4}:){1,3}(?::(?:[0-9a-fA-F]){1,4}){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,2}(?::(?:[0-9a-fA-F]){1,4}){1,5}|(?:[0-9a-fA-F]){1,4}:(?:(?::(?:[0-9a-fA-F]){1,4}){1,6})|:(?:(?:(?::(?:[0-9a-fA-F]){1,4}){1,7}|[:]))|fe80:(?::(?:[0-9a-fA-F]){0,4}){0,4}%[0-9a-zA-Z]+|::(?:ffff(?::0{1,4})?:)?(?:(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)\.){3}(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)|(?:(?:[0-9a-fA-F]){1,4}:){1,4}:(?:(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)\.){3}(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d))$

The full form
-------------

Eight colon-separated groups, each one to four hex digits. Leading zeros in a
group may be dropped, an all-zero group may shrink to a single ``0``, and hex is
case-insensitive. A group of more than four digits, though, is not valid:

.. code-block:: python

   ipv6("2001:0db8:0000:0000:0000:ff00:0042:8329")   # True — written out in full
   ipv6("2001:db8:0:0:0:ff00:42:8329")               # True — leading zeros dropped
   ipv6("2001:DB8:0:0:0:FF00:42:8329")               # True — uppercase hex
   ipv6("12345::")                                   # False — a group can't exceed four digits

.. edify-playground::
   :tests: 2001:0db8:0000:0000:0000:ff00:0042:8329|2001:db8:0:0:0:ff00:42:8329|2001:DB8:0:0:0:FF00:42:8329|12345::

   from edify.library import ipv6
   ipv6

Zero compression with ``::``
----------------------------

A single ``::`` stands in for one or more consecutive all-zero groups — at the
start, the middle, or the end. The two most famous IPv6 addresses are nothing but
zeros. The one rule: ``::`` may appear only **once**, because a second would be
ambiguous about how many zero groups each stands for:

.. code-block:: python

   ipv6("2001:db8::ff00:42:8329")   # True — three zero groups collapse in the middle
   ipv6("fe80::")                   # True — trailing zeros, :: at the end
   ipv6("::1")                      # True — loopback: :: at the start
   ipv6("::")                       # True — the unspecified address, all zeros
   ipv6("1::2::3")                  # False — a second :: is ambiguous

.. edify-playground::
   :tests: 2001:db8::ff00:42:8329|fe80::|::1|::|1::2::3

   from edify.library import ipv6
   ipv6

Embedded IPv4
-------------

The last 32 bits may be written as a dotted-quad instead of two hex groups — the
IPv4-mapped and IPv4-translated forms you see when IPv4 rides inside IPv6:

.. code-block:: python

   ipv6("::ffff:192.0.2.1")       # True — IPv4-mapped
   ipv6("::ffff:0:192.0.2.1")     # True — IPv4-translated
   ipv6("2001:db8::192.0.2.1")    # True — embedded in a routable prefix
   ipv6("::ffff:999.0.0.1")       # False — the embedded octet is out of range

.. edify-playground::
   :tests: ::ffff:192.0.2.1|::ffff:0:192.0.2.1|2001:db8::192.0.2.1|::ffff:999.0.0.1

   from edify.library import ipv6
   ipv6

Scoped (link-local) addresses
-----------------------------

A link-local address can carry a **zone identifier** after a ``%`` — the
interface it is scoped to, named or numbered — which is how ``fe80::`` addresses
are disambiguated across interfaces:

.. code-block:: python

   ipv6("fe80::1%eth0")   # True — named zone
   ipv6("fe80::1%1")      # True — numeric zone
   ipv6("gg::")           # False — 'g' is not a hex digit
   ipv6("1.2.3.4")        # False — that's an IPv4 address

.. edify-playground::
   :tests: fe80::1%eth0|fe80::1%1|gg::|1.2.3.4

   from edify.library import ipv6
   ipv6

``ipv6`` validates the textual form only — it says nothing about reachability or
reserved-range semantics. For IPv4 reach for :doc:`ipv4`, for "either family"
:doc:`ip`, and for a network block :doc:`cidr`; the reversed-nibble form of this
same grammar is what :doc:`ptr` matches under ``ip6.arpa``.
