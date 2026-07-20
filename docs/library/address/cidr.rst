cidr
====

``cidr`` matches a network block in CIDR notation — an address, a ``/``, and a
prefix length — for both IP families, with the prefix bound checked per family.

Under the hood edify builds two branches and joins them with
:func:`~edify.any_of`: an IPv4 dotted-quad (each octet range-checked, reusing the
same octet as :doc:`ipv4`) followed by ``/`` and a ``0``–``32`` prefix, or a run
of colon-separated hex groups followed by ``/`` and a ``0``–``128`` prefix. The
prefix bounds are enforced digit by digit, and the whole thing is anchored with
:meth:`~edify.RegexBuilder.start_of_input` / :meth:`~edify.RegexBuilder.end_of_input`:

.. code-block:: python

   from edify import Pattern, any_of

   cidr = (
       Pattern().start_of_input()
       .use(any_of(ipv4_address_slash_prefix, ipv6_groups_slash_prefix))
       .end_of_input()
   )

which emits:

.. code-block:: text

   ^(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}/(?:3[0-2]|[12]?\d)|(?:[0-9a-fA-F]{1,4}:){0,7}[0-9a-fA-F]{1,4}/(?:12[0-8]|1[01]\d|[1-9]?\d))$

IPv4 blocks
-----------

A dotted-quad, then ``/`` and a prefix from 0 to 32. The prefix is validated, so
``/33`` fails, and so does an address with an out-of-range octet:

.. code-block:: python

   cidr("10.0.0.0/8")       # True
   cidr("192.168.1.0/24")   # True
   cidr("1.2.3.4/32")       # True  — a single host
   cidr("0.0.0.0/0")        # True  — the default route
   cidr("10.0.0.0/33")      # False — prefix above the IPv4 maximum
   cidr("256.0.0.0/8")      # False — octet out of range
   cidr("10.0.0.0")         # False — no prefix

.. edify-playground::
   :tests: 10.0.0.0/8|192.168.1.0/24|1.2.3.4/32|0.0.0.0/0|10.0.0.0/33|10.0.0.0

   from edify.library import cidr
   cidr

IPv6 blocks
-----------

Colon-separated hex groups, then ``/`` and a prefix from 0 to 128. The address
portion must be written **in full** here — ``::`` zero-compression is not accepted
on the IPv6 side of ``cidr`` (unlike the standalone :doc:`ipv6`):

.. code-block:: python

   cidr("2001:db8:0:0:0:0:0:0/64")    # True
   cidr("2001:db8:0:0:0:0:0:1/128")   # True  — a single IPv6 host
   cidr("2001:db8::/32")              # False — :: compression on the address side

.. edify-playground::
   :tests: 2001:db8:0:0:0:0:0:0/64|2001:db8:0:0:0:0:0:1/128|2001:db8::/32

   from edify.library import cidr
   cidr

Notes
-----

- The prefix bound is per family: ``/0``–``/32`` for IPv4, ``/0``–``/128`` for
  IPv6, both enforced exactly.
- For an address without a prefix use :doc:`ipv4`, :doc:`ipv6`, or :doc:`ip`; for
  a dotted-decimal mask instead of a prefix length use :doc:`subnet`.
