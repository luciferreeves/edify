ipv4
====

:doc:`Library <../index>` › :doc:`Address <index>` › **ipv4**

``ipv4`` matches an IPv4 address in dotted-decimal form: four octets joined by
dots, each octet a number the pattern range-checks digit by digit so ``255``
passes and ``256`` does not.

.. code-block:: python

   from edify.library import ipv4

   ipv4("192.168.0.1")   # True

Four octets, each 0–255
-----------------------

Exactly four dot-separated octets, no more and no fewer:

.. code-block:: python

   ipv4("192.168.0.1")   # True
   ipv4("8.8.8.8")       # True — single-digit octets are fine
   ipv4("1.2.3")         # False — only three octets
   ipv4("1.2.3.4.5")     # False — five octets
   ipv4("1.2.3.4.")      # False — a trailing dot leaves an empty fifth octet

.. edify-playground::
   :tests: 192.168.0.1|8.8.8.8|1.2.3|1.2.3.4.5

   from edify.library import ipv4
   ipv4

The boundaries
--------------

Every octet runs the full 0–255 range, and the two edge addresses — the
all-zero network and the all-ones broadcast — both match:

.. code-block:: python

   ipv4("0.0.0.0")             # True — this-network
   ipv4("255.255.255.255")     # True — limited broadcast
   ipv4("255.0.0.255")         # True — mixing the extremes is fine
   ipv4("256.0.0.1")           # False — 256 is one past the top of the range

.. edify-playground::
   :tests: 0.0.0.0|255.255.255.255|255.0.0.255|256.0.0.1

   from edify.library import ipv4
   ipv4

No leading zeros
----------------

An octet is a bare number: a lone ``0`` is fine, but zero-padded octets like
``01`` or ``001`` are rejected (they are how some tools smuggle in octal):

.. code-block:: python

   ipv4("192.168.0.1")    # True
   ipv4("192.168.01.1")   # False — 01 has a leading zero

.. edify-playground::
   :tests: 10.0.0.1|192.168.0.1|010.0.0.1|192.168.01.1

   from edify.library import ipv4
   ipv4

What it rejects
---------------

.. code-block:: python

   ipv4("2001:db8::1")   # False — that's IPv6 (use ipv6)
   ipv4("1.2.3")         # False — wrong octet count
   ipv4("999.1.1.1")     # False — octet out of range
   ipv4("abc")           # False — not numeric

.. edify-playground::
   :tests: 192.168.0.1|2001:db8::1|999.1.1.1|abc

   from edify.library import ipv4
   ipv4

``ipv4`` checks the textual form only — it does not care whether an address is
routable, private, or reserved (``127.0.0.1`` and ``0.0.0.0`` both match). Use
:doc:`ipv6` for IPv6, :doc:`ip` for "either family", or :doc:`cidr` for a network
block.

How it's created
----------------

The heart of ``ipv4`` is a single **octet** — an :func:`~edify.any_of` over five
range branches that together cover 0–255 exactly, which is why ``256`` fails
where ``255`` passes. ``ipv4`` anchors that octet with
:meth:`~edify.RegexBuilder.start_of_input` / :meth:`~edify.RegexBuilder.end_of_input`
and repeats it four times, joined by dots via :meth:`~edify.RegexBuilder.exactly`
and :meth:`~edify.RegexBuilder.group`:

.. code-block:: python

   from edify import Pattern, any_of

   octet = any_of(
       Pattern().string("25").any_of().range("0", "5").end(),   # 250–255
       Pattern().char("2").any_of().range("0", "4").end().digit(),  # 200–249
       Pattern().char("1").digit().digit(),                     # 100–199
       Pattern().any_of().range("1", "9").end().digit(),        # 10–99
       Pattern().digit(),                                       # 0–9
   )
   ipv4 = (
       Pattern().start_of_input()
       .use(octet).exactly(3).group().char(".").use(octet).end()
       .end_of_input()
   )

That same octet construction is reused by :doc:`ip`, :doc:`cidr`, and the IPv4
host of :doc:`socket`.

Pattern
-------

.. code-block:: text

   ^(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}$
