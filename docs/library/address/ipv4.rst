ipv4
====

``ipv4`` matches an IPv4 address in dotted-decimal form — four octets joined by
dots, each a number from 0 to 255, like ``192.168.0.1``.

Edify composes it from a single reusable **octet** fragment repeated four times.
The octet is where the range check lives: an :func:`~edify.any_of` over five
branches — ``25`` + ``0``–``5`` for 250–255, ``2`` + ``0``–``4`` + a
:meth:`~edify.RegexBuilder.digit` for 200–249, ``1`` + two digits for 100–199,
``1``–``9`` + a digit for 10–99, and a lone digit for 0–9 — which together cover
0–255 *exactly*, so ``256`` has no branch to match. ``ipv4`` joins four of those
:doc:`octets <../../guide/composing>` with dots (via
:meth:`~edify.RegexBuilder.exactly`\ ``(3)`` of a
:meth:`~edify.RegexBuilder.group`) between
:meth:`~edify.RegexBuilder.start_of_input` and
:meth:`~edify.RegexBuilder.end_of_input`. The regex that falls out:

.. code-block:: text

   ^(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}$

Four octets, each 0 to 255
--------------------------

Exactly four dot-separated octets — no more, no fewer — and each runs the full
0–255 range, the all-zero network and the all-ones broadcast included. One past
the top, ``256``, is out; so is the wrong octet count or an IPv6 address:

.. code-block:: python

   ipv4("192.168.0.1")         # True
   ipv4("0.0.0.0")             # True  — this-network
   ipv4("255.255.255.255")     # True  — limited broadcast
   ipv4("256.0.0.1")           # False — 256 is past the top of the range
   ipv4("1.2.3")               # False — only three octets
   ipv4("2001:db8::1")         # False — that's IPv6; use ipv6

.. edify-playground::
   :tests: 192.168.0.1|0.0.0.0|255.255.255.255|256.0.0.1|1.2.3|2001:db8::1

   from edify.library import ipv4
   ipv4

No leading zeros
----------------

An octet is a bare number: a lone ``0`` is fine, but zero-padded octets like
``01`` are rejected — that is how some tools smuggle in octal, and treating
``010`` as decimal 10 would be a security bug:

.. code-block:: python

   ipv4("10.0.0.1")      # True
   ipv4("010.0.0.1")     # False — 010 has a leading zero
   ipv4("192.168.01.1")  # False — 01 has a leading zero

.. edify-playground::
   :tests: 10.0.0.1|192.168.0.1|010.0.0.1|192.168.01.1

   from edify.library import ipv4
   ipv4

``ipv4`` checks the textual form only — it does not care whether an address is
routable, private, or reserved (``127.0.0.1`` and ``0.0.0.0`` both match). The
same octet fragment is reused by :doc:`ip`, :doc:`cidr`, and the IPv4 host of
:doc:`socket`; for IPv6 see :doc:`ipv6`, and for either family :doc:`ip`.
