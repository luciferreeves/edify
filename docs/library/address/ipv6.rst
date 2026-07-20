ipv6
====

An IPv6 address is 128 bits, written as eight groups of four hexadecimal digits
joined by colons — ``2001:0db8:0000:0000:0000:ff00:0042:8329``. Almost nobody
writes the full form, because the notation (RFC 4291, with the canonical
short-form rules of RFC 5952) allows a stack of shorthands. ``ipv6`` accepts every
one of them: dropped leading zeros, ``::`` zero-compression, the embedded-IPv4
tail, and the scoped ``%zone`` suffix.

Under the hood, the base unit is a **hex group** — one to four hex digits, written as
:meth:`~edify.RegexBuilder.between`\ ``(1, 4)`` of a
:doc:`nibble <../../guide/composing>` (a ``0``–``9`` ``a``–``f`` ``A``–``F``
:meth:`~edify.RegexBuilder.range` class). Those groups feed an
:func:`~edify.any_of` alternation whose branches enumerate every legal layout —
the full eight-group form, one branch for each position ``::`` can occupy, the
``fe80::…%zone`` link-local form, and the embedded-IPv4 tail — all anchored with
:meth:`~edify.RegexBuilder.start_of_input` / :meth:`~edify.RegexBuilder.end_of_input`:

.. code-block:: python

   from edify import Pattern, any_of

   nibble = Pattern().any_of().range("0", "9").range("a", "f").range("A", "F").end()
   hex_group = Pattern().between(1, 4).use(nibble)

   ipv6 = (
       Pattern().start_of_input()
       .use(any_of(full_form, *compressed_forms, link_local, ipv4_mapped))
       .end_of_input()
   )

which emits:

.. code-block:: text

   ^(?:(?:(?:[0-9a-fA-F]){1,4}:){7}(?:[0-9a-fA-F]){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,7}:|(?:(?:[0-9a-fA-F]){1,4}:){1,6}:(?:[0-9a-fA-F]){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,5}(?::(?:[0-9a-fA-F]){1,4}){1,2}|(?:(?:[0-9a-fA-F]){1,4}:){1,4}(?::(?:[0-9a-fA-F]){1,4}){1,3}|(?:(?:[0-9a-fA-F]){1,4}:){1,3}(?::(?:[0-9a-fA-F]){1,4}){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,2}(?::(?:[0-9a-fA-F]){1,4}){1,5}|(?:[0-9a-fA-F]){1,4}:(?:(?::(?:[0-9a-fA-F]){1,4}){1,6})|:(?:(?:(?::(?:[0-9a-fA-F]){1,4}){1,7}|[:]))|fe80:(?::(?:[0-9a-fA-F]){0,4}){0,4}%[0-9a-zA-Z]+|::(?:ffff(?::0{1,4})?:)?(?:(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)\.){3}(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)|(?:(?:[0-9a-fA-F]){1,4}:){1,4}:(?:(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)\.){3}(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d))$

The forms it accepts
--------------------

Every textual form of an IPv6 address, at a glance:

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Form
     - Example
     - Notes
   * - Full
     - ``2001:0db8:0000:0000:0000:ff00:0042:8329``
     - eight four-digit groups
   * - Leading zeros dropped
     - ``2001:db8:0:0:0:ff00:42:8329``
     - each group 1–4 digits
   * - Zero-compressed
     - ``2001:db8::ff00:42:8329``
     - one ``::`` for a run of zeros
   * - Loopback
     - ``::1``
     - seven zero groups, then 1
   * - Unspecified
     - ``::``
     - all zeros
   * - Link-local
     - ``fe80::1``
     - the ``fe80::/10`` block
   * - Scoped link-local
     - ``fe80::1%eth0``
     - a ``%zone`` interface suffix
   * - IPv4-mapped
     - ``::ffff:192.0.2.1``
     - a dotted-quad tail
   * - IPv4-embedded
     - ``2001:db8::192.0.2.1``
     - a dotted-quad in a routable prefix

The full form
-------------

Eight colon-separated groups, each one to four hex digits. Leading zeros within a
group may be dropped, an all-zero group may shrink to a single ``0``, and the hex
digits are case-insensitive. A group longer than four digits is invalid:

.. code-block:: python

   ipv6("2001:0db8:0000:0000:0000:ff00:0042:8329")   # True  — written out in full
   ipv6("2001:db8:0:0:0:ff00:42:8329")               # True  — leading zeros dropped
   ipv6("2001:DB8:0:0:0:FF00:42:8329")               # True  — uppercase hex
   ipv6("12345::")                                   # False — a group can't exceed four digits
   ipv6("gg::")                                      # False — 'g' is not a hex digit
   ipv6("1.2.3.4")                                   # False — that's IPv4; use ipv4

.. edify-playground::
   :tests: 2001:db8:0:0:0:ff00:42:8329|2001:DB8:0:0:0:FF00:42:8329|12345::|gg::|1.2.3.4

   from edify.library import ipv6
   ipv6

Zero compression with ``::``
----------------------------

A single ``::`` stands in for one or more consecutive all-zero groups. It can sit
at the start, the middle, or the end, and the two most important addresses — the
loopback ``::1`` and the unspecified ``::`` — are made almost entirely of it. The
one rule: ``::`` may appear **only once**, because a second occurrence would be
ambiguous about how many zero groups each represents:

.. code-block:: python

   ipv6("2001:db8::ff00:42:8329")   # True — three zero groups collapse in the middle
   ipv6("fe80::")                   # True — trailing zeros, :: at the end
   ipv6("::1")                      # True — loopback: :: at the start
   ipv6("::")                       # True — the unspecified address, all zeros
   ipv6("1::2::3")                  # False — a second :: is ambiguous
   ipv6("2001:db8:::1")             # False — ::: is never valid

.. edify-playground::
   :tests: 2001:db8::ff00:42:8329|fe80::|::1|::|1::2::3|2001:db8:::1

   from edify.library import ipv6
   ipv6

Embedded IPv4
-------------

The last 32 bits — the final two hex groups — may instead be written as a
dotted-quad. This is the notation for IPv4-mapped (``::ffff:…``) and
IPv4-translated addresses, and for IPv4 embedded in a routable prefix. The
embedded octets are range-checked like a real :doc:`ipv4` address, so an
out-of-range octet fails:

.. code-block:: python

   ipv6("::ffff:192.0.2.1")       # True — IPv4-mapped
   ipv6("::ffff:0:192.0.2.1")     # True — IPv4-translated
   ipv6("2001:db8::192.0.2.1")    # True — embedded in a routable prefix
   ipv6("::ffff:999.0.0.1")       # False — 999 is not a valid octet

.. edify-playground::
   :tests: ::ffff:192.0.2.1|::ffff:0:192.0.2.1|2001:db8::192.0.2.1|::ffff:999.0.0.1

   from edify.library import ipv6
   ipv6

Scoped (link-local) addresses
-----------------------------

A link-local address can carry a **zone identifier** after a ``%`` — the network
interface it is scoped to, named (``eth0``) or numbered (``1``). Without it, a
``fe80::`` address is ambiguous when a host has more than one interface:

.. code-block:: python

   ipv6("fe80::1%eth0")   # True  — named zone
   ipv6("fe80::1%1")      # True  — numeric zone
   ipv6("fe80::1%")       # False — the zone identifier can't be empty

.. edify-playground::
   :tests: fe80::1%eth0|fe80::1%1|fe80::abcd%wlan0|fe80::1%

   from edify.library import ipv6
   ipv6

.. note::

   ``ipv6`` validates the **textual form** only — it does not check whether an
   address is reachable, allocated, or in a reserved range (``::`` and ``::1``
   both match), and it accepts case-insensitive hex rather than requiring the RFC
   5952 canonical form. The embedded-IPv4 tail reuses the octet range check of
   :doc:`ipv4`; for either family use :doc:`ip`, and for an address plus a
   ``/prefix`` use :doc:`cidr`.
