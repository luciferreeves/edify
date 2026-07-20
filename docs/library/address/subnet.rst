subnet
======

.. edify-validator:: subnet

``subnet`` matches a dotted-decimal IPv4 subnet mask — four octets, each one of
the nine byte values a mask can legally take.

Under the hood a **mask octet** is an :func:`~edify.any_of` over the nine literal
values a run-of-ones-then-zeros byte can hold; ``subnet`` joins four of them with
dots, anchored with :meth:`~edify.RegexBuilder.start_of_input` /
:meth:`~edify.RegexBuilder.end_of_input`:

.. code-block:: python

   from edify import Pattern, any_of

   mask_octet = any_of(*[Pattern().string(v) for v in
       ("255", "254", "252", "248", "240", "224", "192", "128")], Pattern().char("0"))

   subnet = (
       Pattern().start_of_input()
       .use(mask_octet).char(".").use(mask_octet).char(".")
       .use(mask_octet).char(".").use(mask_octet)
       .end_of_input()
   )

The nine mask bytes
-------------------

Each octet must be one of ``255``, ``254``, ``252``, ``248``, ``240``, ``224``,
``192``, ``128``, or ``0`` — the only bytes with a leading run of one-bits. An
ordinary address byte like ``1`` or ``168`` fails:

.. code-block:: python

   subnet("255.255.255.0")     # True — a /24
   subnet("255.255.0.0")       # True — a /16
   subnet("255.255.255.128")   # True — a /25 (128 is a legal mask byte)
   subnet("0.0.0.0")           # True — the all-zero mask
   subnet("255.255.255.1")     # False — 1 is not a mask byte
   subnet("192.168.0.0")       # False — 168 is not a mask byte

.. edify-playground::
   :tests: 255.255.255.0|255.255.0.0|255.255.255.128|0.0.0.0|255.255.255.1|192.168.0.0

   from edify.library import subnet
   subnet

Notes
-----

- ``subnet`` validates each octet **independently**; it does not check that the
  mask is *contiguous* (all one-bits leading). A discontiguous but byte-legal mask
  like ``255.0.255.0`` matches even though it is not a valid netmask.
- For a network block with a prefix length instead, use :doc:`cidr`.
