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

The boundaries
--------------

Every octet runs the full 0–255 range, and the two edge addresses — the
all-zero network and the all-ones broadcast — both match:

.. code-block:: python

   ipv4("0.0.0.0")             # True — this-network
   ipv4("255.255.255.255")     # True — limited broadcast
   ipv4("255.0.0.255")         # True — mixing the extremes is fine
   ipv4("256.0.0.1")           # False — 256 is one past the top of the range

No leading zeros
----------------

An octet is a bare number: a lone ``0`` is fine, but zero-padded octets like
``01`` or ``001`` are rejected (they are how some tools smuggle in octal):

.. code-block:: python

   ipv4("192.168.0.1")    # True
   ipv4("192.168.01.1")   # False — 01 has a leading zero

What it rejects
---------------

.. code-block:: python

   ipv4("2001:db8::1")   # False — that's IPv6 (use ipv6)
   ipv4("1.2.3")         # False — wrong octet count
   ipv4("999.1.1.1")     # False — octet out of range
   ipv4("abc")           # False — not numeric

``ipv4`` checks the textual form only — it does not care whether an address is
routable, private, or reserved (``127.0.0.1`` and ``0.0.0.0`` both match). Use
:doc:`ipv6` for IPv6, :doc:`ip` for "either family", or :doc:`cidr` for a network
block.

Pattern
-------

.. code-block:: text

   ^(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}$
