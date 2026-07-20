subnet
======

``subnet`` matches a dotted-decimal IPv4 subnet mask. A mask byte isn't any old
number — it is a run of one-bits followed by a run of zero-bits — which leaves
exactly **nine** legal values per octet:

   ``255`` · ``254`` · ``252`` · ``248`` · ``240`` · ``224`` · ``192`` · ``128`` · ``0``

.. edify-playground::
   :tests: 255.255.255.0|255.255.0.0|255.0.0.0|255.255.255.128|0.0.0.0|255.255.255.1|192.168.0.0|255.255.255

   from edify.library import subnet
   subnet

**Only those nine, four times over.** Each octet must be one of the values above,
so common prefixes all pass and ordinary address bytes do not:

.. code-block:: python

   subnet("255.255.255.0")     # True  — a /24
   subnet("255.255.0.0")       # True  — a /16
   subnet("255.255.255.128")   # True  — a /25 (128 is a legal mask byte)
   subnet("0.0.0.0")           # True  — the all-zero mask
   subnet("255.255.255.1")     # False — 1 is not a mask byte
   subnet("192.168.0.0")       # False — 192 is legal, but 168 is not
   subnet("255.255.255")       # False — only three octets

**Each octet is checked independently.** This is the one caveat worth knowing:
``subnet`` does not verify that the mask is *contiguous* (all its one-bits
leading). A byte-legal but nonsensical mask like ``255.0.255.0`` still matches,
because every octet on its own is one of the nine values:

.. code-block:: python

   subnet("255.0.255.0")   # True — byte-legal, though not a real netmask

In edify a mask octet is an :func:`~edify.any_of` over those nine literals, and
``subnet`` joins four of them with dots. When you'd rather express the mask as a
prefix length, use :doc:`cidr`.
