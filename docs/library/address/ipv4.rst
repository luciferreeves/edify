ipv4
====

:doc:`Library <../index>` › :doc:`Address <index>` › **ipv4**

``ipv4`` matches an IPv4 address in dotted-decimal form: four octets separated by
dots, each octet a number from 0 to 255.

.. code-block:: python

   from edify.library import ipv4

   ipv4("192.168.0.1")   # True
   ipv4("8.8.8.8")       # True
   ipv4("0.0.0.0")       # True
   ipv4("256.1.1.1")     # False — 256 is above the 0–255 range
   ipv4("1.2.3")         # False — only three octets

What it matches
---------------

- **Exactly four octets** separated by dots.
- Each octet ranges **0–255**, with the range enforced digit-by-digit
  (``250`` matches, ``256`` does not).
- No leading-zero padding beyond a single ``0`` — ``01`` in an octet is rejected.
- Anchored at both ends, so the whole string must be the address.

It does **not** check whether the address is routable, allocated, or in a
reserved range (``0.0.0.0``, ``127.0.0.1``, and ``255.255.255.255`` all match).
For "IPv4 or IPv6" use :doc:`ip`; for a network block use :doc:`cidr`.

Try it
------

.. edify-playground::
   :tests: 192.168.0.1|8.8.8.8|0.0.0.0|255.255.255.255|256.1.1.1|1.2.3

   from edify.library import ipv4
   ipv4

Pattern
-------

.. code-block:: text

   ^(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}$
