cidr
====

CIDR notation is an address, a slash, and a prefix length — ``192.168.1.0/24``.
``cidr`` handles both families, and the only real subtlety is that each family
caps the prefix differently, so it is worth taking them one at a time.

IPv4 blocks
-----------

A dotted-quad — each octet range-checked exactly as in :doc:`ipv4` — then ``/``
and a prefix from **0 to 32**. Because the prefix is validated (not just "one or
two digits"), ``/33`` is rejected, and so is an address with a bad octet:

.. code-block:: python

   cidr("10.0.0.0/8")       # True
   cidr("1.2.3.4/32")       # True  — a single host
   cidr("0.0.0.0/0")        # True  — the default route
   cidr("10.0.0.0/33")      # False — prefix above the IPv4 maximum
   cidr("256.0.0.0/8")      # False — octet out of range
   cidr("10.0.0.0")         # False — no prefix at all

.. edify-playground::
   :tests: 10.0.0.0/8|192.168.1.0/24|1.2.3.4/32|0.0.0.0/0|10.0.0.0/33|10.0.0.0

   from edify.library import cidr
   cidr

IPv6 blocks
-----------

Colon-separated hex groups, then ``/`` and a prefix from **0 to 128**. One catch:
here the address must be written **in full** — ``::`` zero-compression is *not*
accepted on the IPv6 side of ``cidr`` (it is on the standalone :doc:`ipv6`):

.. code-block:: python

   cidr("2001:db8:0:0:0:0:0:0/64")    # True
   cidr("2001:db8:0:0:0:0:0:1/128")   # True  — a single IPv6 host
   cidr("2001:db8::/32")              # False — :: compression on the address side

.. edify-playground::
   :tests: 2001:db8:0:0:0:0:0:0/64|2001:db8:0:0:0:0:0:1/128|2001:db8::/32

   from edify.library import cidr
   cidr

Internally the two are just an :func:`~edify.any_of` of "address ``/`` prefix",
one branch per family, with the prefix bounds enforced digit by digit. For an
address with no prefix use :doc:`ipv4`, :doc:`ipv6`, or :doc:`ip`; for a
dotted-decimal mask instead of a prefix, :doc:`subnet`.
