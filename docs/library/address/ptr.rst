ptr
===

:doc:`Library <../index>` › :doc:`Address <index>` › **ptr**

``ptr`` matches a reverse-DNS PTR record name — the ``in-addr.arpa`` form for
IPv4 or the ``ip6.arpa`` nibble form for IPv6. These are the names you look up to
turn an address back into a hostname.

.. code-block:: python

   from edify.library import ptr

   ptr("1.0.0.127.in-addr.arpa")   # True

IPv4 reverse records
--------------------

The four octets of an IPv4 address, reversed, followed by ``in-addr.arpa``. A
trailing dot (the fully-qualified form) is optional:

.. code-block:: python

   ptr("1.0.0.127.in-addr.arpa")    # True — 127.0.0.1 reversed
   ptr("4.3.2.1.in-addr.arpa.")     # True — with the trailing dot

IPv6 reverse records
--------------------

All 32 hex nibbles of an IPv6 address, reversed and dot-separated, followed by
``ip6.arpa``:

.. code-block:: python

   ptr("b.a.9.8.7.6.5.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa")   # True

What it rejects
---------------

.. code-block:: python

   ptr("127.0.0.1")     # False — that's a forward address, not a PTR name
   ptr("example.com")   # False — an ordinary domain, not a reverse record

``ptr`` checks the reverse-record *shape*; it does not verify that the embedded
address is itself in range. For forward addresses use :doc:`ipv4` / :doc:`ipv6`.

Try it
------

.. edify-playground::
   :tests: 1.0.0.127.in-addr.arpa|4.3.2.1.in-addr.arpa.|127.0.0.1|example.com

   from edify.library import ptr
   ptr
