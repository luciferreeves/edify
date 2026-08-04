IPv6
====

An IPv6 address is 128 bits, written as eight groups of four hexadecimal digits
joined by colons — ``2001:0db8:0000:0000:0000:ff00:0042:8329``. Almost nobody writes
the full form: the notation (:rfc:`4291`, with the canonical short-form rules of
:rfc:`5952`) allows a stack of shorthands, and **IPv6** accepts every one — dropped
leading zeros, ``::`` zero-compression, the embedded-IPv4 tail, and the scoped
``%zone`` suffix. It checks the *textual form* only: it says nothing about whether an
address is reachable or allocated, and it accepts case-insensitive hex, so ``::``,
``::1``, and ``2001:DB8::1`` all match.

The base unit edify composes it from is a :doc:`hex group <../../guide/atoms/network>` —
one to four hex digits, written as :meth:`~edify.RegexBuilder.between`\ ``(1, 4)`` of
a :doc:`nibble <../../guide/atoms/network>` (a ``0``–``9`` ``a``–``f`` ``A``–``F``
:meth:`~edify.RegexBuilder.range` class). Those groups feed an :func:`~edify.any_of`
alternation whose branches enumerate every legal layout — the full eight-group form,
one branch for each position ``::`` can occupy, the
`link-local <https://en.wikipedia.org/wiki/Link-local_address>`__ ``fe80::…%zone``
form, and the embedded-IPv4 tail — all anchored with
:meth:`~edify.RegexBuilder.start_of_input` / :meth:`~edify.RegexBuilder.end_of_input`.

The forms it accepts
--------------------

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Form
     - Example
     - What it is
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

.. edify-playground::

   from edify.library import ipv6

   ipv6("2001:0db8:0000:0000:0000:ff00:0042:8329")   # written out in full
   ipv6("2001:db8:0:0:0:ff00:42:8329")               # leading zeros dropped
   ipv6("2001:DB8:0:0:0:FF00:42:8329")               # uppercase hex
   ipv6("12345::")                                   # a group can't exceed four digits
   ipv6("gg::")                                      # 'g' is not a hex digit
   ipv6("1.2.3.4")                                   # that is IPv4

Zero compression with ``::``
----------------------------

A single ``::`` stands in for one or more consecutive all-zero groups. It can sit at
the start, the middle, or the end, and the two most important addresses — the
loopback ``::1`` and the unspecified ``::`` — are made almost entirely of it. The one
rule is that ``::`` may appear **only once**, because a second occurrence would be
ambiguous about how many zero groups each represents:

.. edify-playground::

   from edify.library import ipv6

   ipv6("2001:db8::ff00:42:8329")   # three zero groups collapse in the middle
   ipv6("fe80::")                   # trailing zeros, :: at the end
   ipv6("::1")                      # loopback: :: at the start
   ipv6("::")                       # the unspecified address, all zeros
   ipv6("1::2::3")                  # a second :: is ambiguous
   ipv6("2001:db8:::1")             # ::: is never valid

Embedded IPv4
-------------

The last 32 bits — the final two hex groups — may instead be written as a
dotted-quad. This is the notation for
`IPv4-mapped <https://en.wikipedia.org/wiki/IPv6_address>`__
(``::ffff:…``) and IPv4-translated addresses, and for IPv4 embedded in a routable
prefix. The embedded octets are range-checked like a real :doc:`ipv4` address, so an
out-of-range octet fails:

.. edify-playground::

   from edify.library import ipv6

   ipv6("::ffff:192.0.2.1")     # IPv4-mapped
   ipv6("::ffff:0:192.0.2.1")   # IPv4-translated
   ipv6("2001:db8::192.0.2.1")  # embedded in a routable prefix
   ipv6("::ffff:999.0.0.1")     # 999 is not a valid octet

Scoped (link-local) addresses
-----------------------------

A link-local address can carry a **zone identifier** after a ``%`` — the network
interface it is scoped to, named (``eth0``) or numbered (``1``). Without one, a
``fe80::`` address is ambiguous when a host has more than one interface:

.. edify-playground::

   from edify.library import ipv6

   ipv6("fe80::1%eth0")     # named zone
   ipv6("fe80::1%1")        # numeric zone
   ipv6("fe80::abcd%wlan0") # another named zone
   ipv6("fe80::1%")         # the zone identifier can't be empty

The embedded-IPv4 tail reuses the :doc:`octet <../../guide/atoms/network>` range check of
:doc:`ipv4`. To accept either address family with one validator use :doc:`ip`, and
for an IPv6 network block — an address plus a ``/prefix`` — use :doc:`cidr`.
