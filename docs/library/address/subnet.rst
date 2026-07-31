Subnet mask
===========

A `subnet mask <https://en.wikipedia.org/wiki/Subnetwork>`__ is four dotted decimal
octets that, read as bits, are a run of ones followed by a run of zeros —
``255.255.255.0``. **Subnet mask** accepts only the byte values a mask boundary can
produce, so ``255.255.255.1`` — a hole in the run of ones — is rejected.

A mask byte is a run of one-bits followed by zero-bits, which leaves exactly nine
legal values per octet: ``255``, ``254``, ``252``, ``248``, ``240``, ``224``, ``192``,
``128``, and ``0``. Under the hood that is an :func:`~edify.any_of` over those nine
literals, and **Subnet mask** joins four of them with
:meth:`~edify.RegexBuilder.char`\ ``(".")`` between
:meth:`~edify.RegexBuilder.start_of_input` and :meth:`~edify.RegexBuilder.end_of_input`.

The nine mask octets
--------------------

Each octet must be one of the nine, so common prefixes all pass while ordinary
address bytes do not:

.. edify-playground::

   from edify.library import subnet

   subnet("255.255.255.0")     # a /24
   subnet("255.255.0.0")       # a /16
   subnet("255.255.255.128")   # a /25 — 128 is a legal mask byte
   subnet("0.0.0.0")           # the all-zero mask
   subnet("255.255.255.1")     # 1 is not a mask byte
   subnet("192.168.0.0")       # 192 is legal, but 168 is not
   subnet("255.255.255")       # only three octets

Each octet is checked on its own
--------------------------------

One caveat worth knowing: **Subnet mask** does not verify that the mask is
*contiguous* across octets. A byte-legal but nonsensical mask still matches, because
every octet on its own is one of the nine:

.. edify-playground::

   from edify.library import subnet

   subnet("255.0.255.0")       # byte-legal, though not a real netmask
   subnet("255.255.240.0")     # a genuine /20
   subnet("255.255.255.255")   # a /32

When you would rather express the mask as a prefix length — ``/24`` instead of
``255.255.255.0`` — use :doc:`cidr`.
