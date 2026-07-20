ipv6
====

:doc:`Library <../index>` › :doc:`Address <index>` › **ipv6**

An IPv6 address is, at heart, eight groups of four hexadecimal digits joined by
colons. Almost nobody writes it that way — the notation has a stack of shorthand
rules, and ``ipv6`` accepts all of them. This page walks every form it takes,
with a playground for each so you can push on the edges yourself.

The full form
-------------

Eight colon-separated groups, each **one to four hex digits**. Leading zeros in a
group may be dropped, a group of all zeros may shrink to a single ``0``, and hex
is case-insensitive:

.. code-block:: python

   ipv6("2001:0db8:0000:0000:0000:ff00:0042:8329")   # True — every digit written out
   ipv6("2001:db8:0:0:0:ff00:42:8329")               # True — leading zeros dropped
   ipv6("2001:DB8:0:0:0:FF00:42:8329")               # True — uppercase hex
   ipv6("12345::")                                   # False — a group can't exceed four digits

.. edify-playground::
   :tests: 2001:0db8:0000:0000:0000:ff00:0042:8329|2001:db8:0:0:0:ff00:42:8329|2001:DB8:0:0:0:FF00:42:8329|12345::

   from edify.library import ipv6
   ipv6

Zero compression with ``::``
----------------------------

A single ``::`` stands in for **one or more consecutive all-zero groups**, at the
start, middle, or end — and the two most famous IPv6 addresses are nothing but
zeros. Only **one** ``::`` is allowed, since two would be ambiguous:

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

The last 32 bits may be written as a dotted-quad — the IPv4-mapped and
IPv4-translated forms:

.. code-block:: python

   ipv6("::ffff:192.0.2.1")       # True — IPv4-mapped
   ipv6("::ffff:0:192.0.2.1")     # True — IPv4-translated
   ipv6("2001:db8::192.0.2.1")    # True — embedded in a routable prefix

.. edify-playground::
   :tests: ::ffff:192.0.2.1|::ffff:0:192.0.2.1|2001:db8::192.0.2.1|::ffff:999.0.0.1

   from edify.library import ipv6
   ipv6

Scoped (link-local) addresses
-----------------------------

A link-local address may carry a **zone identifier** after a ``%`` — the
interface it is scoped to, named or numbered:

.. code-block:: python

   ipv6("fe80::1%eth0")   # True — named zone
   ipv6("fe80::1%1")      # True — numeric zone

.. edify-playground::
   :tests: fe80::1%eth0|fe80::1%1|fe80::abcd%wlan0|2001:db8::1%eth0

   from edify.library import ipv6
   ipv6

What it rejects
---------------

.. code-block:: python

   ipv6("gg::")           # False — 'g' is not a hex digit
   ipv6("1.2.3.4")        # False — that's IPv4 (use ipv4)
   ipv6("2001:db8::z")    # False — trailing non-hex junk
   ipv6("12345::")        # False — a group may not exceed four digits

.. edify-playground::
   :tests: gg::|1.2.3.4|2001:db8::z|12345::|2001:db8::1

   from edify.library import ipv6
   ipv6

How it's created
----------------

``ipv6`` is assembled with edify's own builder — you could rebuild it yourself
from the same pieces. The base unit is a **hex group**:
:meth:`~edify.RegexBuilder.between`\ ``(1, 4)`` of a hex-digit class, itself an
:meth:`~edify.RegexBuilder.any_of` over three :meth:`~edify.RegexBuilder.range`
spans (``0``–``9``, ``a``–``f``, ``A``–``F``):

.. code-block:: python

   from edify import Pattern, any_of

   hex_group = (
       Pattern().between(1, 4)
       .any_of().range("0", "9").range("a", "f").range("A", "F").end()
   )

Those groups are then combined by the :func:`~edify.any_of` factory across a dozen
branches — one for the full eight-group form, one for **each placement of** ``::``
(embedded with :meth:`~edify.RegexBuilder.subexpression`), one for the
``fe80::…%zone`` link-local form, and one for the embedded-IPv4 tail. The whole
alternation is anchored with :meth:`~edify.RegexBuilder.start_of_input` and
:meth:`~edify.RegexBuilder.end_of_input`:

.. code-block:: python

   ipv6 = (
       Pattern().start_of_input()
       .subexpression(any_of(full_form, *compressed_forms, link_local, ipv4_mapped))
       .end_of_input()
   )

Every method above is a link into the :doc:`builder reference <../../api/builder>`.
The same hex-group construction underpins :doc:`ip` on its IPv6 side, and its
reversed-nibble form is what :doc:`ptr` matches under ``ip6.arpa``.

Pattern
-------

.. code-block:: text

   ^(?:(?:(?:[0-9a-fA-F]){1,4}:){7}(?:[0-9a-fA-F]){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,7}:|(?:(?:[0-9a-fA-F]){1,4}:){1,6}:(?:[0-9a-fA-F]){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,5}(?::(?:[0-9a-fA-F]){1,4}){1,2}|(?:(?:[0-9a-fA-F]){1,4}:){1,4}(?::(?:[0-9a-fA-F]){1,4}){1,3}|(?:(?:[0-9a-fA-F]){1,4}:){1,3}(?::(?:[0-9a-fA-F]){1,4}){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,2}(?::(?:[0-9a-fA-F]){1,4}){1,5}|(?:[0-9a-fA-F]){1,4}:(?:(?::(?:[0-9a-fA-F]){1,4}){1,6})|:(?:(?:(?::(?:[0-9a-fA-F]){1,4}){1,7}|[:]))|fe80:(?::(?:[0-9a-fA-F]){0,4}){0,4}%[0-9a-zA-Z]+|::(?:ffff(?::0{1,4})?:)?(?:(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)\.){3}(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)|(?:(?:[0-9a-fA-F]){1,4}:){1,4}:(?:(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)\.){3}(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d))$

Read it aloud with ``ipv6.to_regex().explain()``.
