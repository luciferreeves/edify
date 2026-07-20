socket
======

.. edify-validator:: socket

``socket`` matches a ``host:port`` socket address. The host may take three forms
— an IPv4 address, a bracketed IPv6 address, or a hostname — each followed by a
colon and a port.

Under the hood the host is an :func:`~edify.any_of` over those three shapes (the
IPv4 branch reusing the octet range check of :doc:`ipv4`, the hostname branch the
label grammar of :doc:`hostname`), joined by a ``:`` to a 1–5 digit port and
anchored with :meth:`~edify.RegexBuilder.start_of_input` /
:meth:`~edify.RegexBuilder.end_of_input`:

.. code-block:: python

   from edify import Pattern, any_of

   socket = (
       Pattern().start_of_input()
       .use(any_of(ipv4_host, bracketed_ipv6_host, hostname_host))
       .char(":").between(1, 5).digit()
       .end_of_input()
   )

An IPv4 host
------------

A dotted-quad host, a colon, and a port. Without the port the whole thing fails:

.. code-block:: python

   socket("127.0.0.1:8080")   # True
   socket("0.0.0.0:80")       # True — bind-any address
   socket("127.0.0.1")        # False — no port

.. edify-playground::
   :tests: 127.0.0.1:8080|0.0.0.0:80|127.0.0.1

   from edify.library import socket
   socket

A hostname host
---------------

A dotted hostname (or a single label) works in the host position:

.. code-block:: python

   socket("localhost:80")          # True
   socket("db.internal:5432")      # True
   socket("api.example.com:443")   # True

.. edify-playground::
   :tests: localhost:80|db.internal:5432|api.example.com:443

   from edify.library import socket
   socket

A bracketed IPv6 host
---------------------

Because IPv6 addresses already contain colons, they are wrapped in ``[…]`` so the
port colon stays unambiguous — a bare IPv6 host is rejected:

.. code-block:: python

   socket("[2001:db8::1]:443")   # True
   socket("[::1]:8080")          # True — bracketed loopback
   socket("2001:db8::1:443")     # False — a bare IPv6 host must be bracketed

.. edify-playground::
   :tests: [2001:db8::1]:443|[::1]:8080|2001:db8::1:443

   from edify.library import socket
   socket

Notes
-----

- The port here is a 1–5 digit field; for the exact 0–65535 bound on its own see
  :doc:`port`, and for the host on its own see :doc:`hostname`, :doc:`ipv4`, or
  :doc:`ipv6`.
