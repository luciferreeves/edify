ptr
===

:doc:`Library <../index>` › :doc:`Address <index>` › **ptr**

``ptr`` matches a reverse-DNS PTR record name — the ``in-addr.arpa`` form for
IPv4 or the ``ip6.arpa`` nibble form for IPv6.

.. code-block:: python

   from edify.library import ptr

   ptr("1.0.0.127.in-addr.arpa")   # True — IPv4 reverse record
   ptr("127.0.0.1")                # False — that's a forward address

What it matches
---------------

- **IPv4**: four dot-separated numbers followed by ``in-addr.arpa`` (with an
  optional trailing dot for the fully-qualified form).
- **IPv6**: 32 dot-separated hex nibbles followed by ``ip6.arpa``.
- Anchored at both ends.

It checks the *reverse-record shape*, not that the embedded address is itself in
range. For forward addresses use :doc:`ipv4` / :doc:`ipv6`.

Try it
------

.. edify-playground::
   :tests: 1.0.0.127.in-addr.arpa|4.3.2.1.in-addr.arpa.|127.0.0.1|example.com

   from edify.library import ptr
   ptr

Pattern
-------

.. code-block:: text

   ^(?:(?:\d{1,3}\.){4}in\-addr\.arpa\.?|(?:[0-9a-fA-F]\.){32}ip6\.arpa\.?)$
