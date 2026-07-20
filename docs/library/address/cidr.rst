cidr
====

:doc:`Library <../index>` › :doc:`Address <index>` › **cidr**

``cidr`` matches a network block in CIDR notation — an address followed by a
``/`` and a prefix length. IPv4 with ``/0``–``/32``, or IPv6 with ``/0``–``/128``.

.. code-block:: python

   from edify.library import cidr

   cidr("10.0.0.0/8")                    # True
   cidr("192.168.1.0/24")                # True
   cidr("2001:db8:0:0:0:0:0:0/32")       # True — IPv6, full form
   cidr("10.0.0.0")                      # False — no prefix
   cidr("10.0.0.0/33")                   # False — prefix above 32

What it matches
---------------

- **IPv4**: a dotted-quad (each octet 0–255) + ``/`` + a prefix ``0``–``32``.
- **IPv6**: colon-separated hex groups + ``/`` + a prefix ``0``–``128``.
- The prefix bound is enforced per family — ``/33`` is rejected for IPv4,
  ``/129`` for IPv6.
- Anchored at both ends.

.. note::

   The IPv6 side accepts the **explicit** eight-group form; it does not accept
   ``::`` zero-compression on the address portion (``2001:db8::/32`` is rejected —
   write ``2001:db8:0:0:0:0:0:0/32``). The prefix range itself is fully
   validated.

Try it
------

.. edify-playground::
   :tests: 10.0.0.0/8|192.168.1.0/24|2001:db8:0:0:0:0:0:0/32|10.0.0.0|10.0.0.0/33

   from edify.library import cidr
   cidr
