socket
======

A socket address is a host and a port, ``host:port``. What makes ``socket`` more
than "something, a colon, a number" is that the host can be three different things
— and one of them, IPv6, already contains colons and so needs special handling.

An IPv4 host
------------

A dotted-quad, reusing the octet range check of :doc:`ipv4`, then a colon and a
port. Without the port the whole thing fails:

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

A dotted name or a single label, following the grammar of :doc:`hostname`:

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

Because an IPv6 address is full of colons, it is wrapped in ``[...]`` so the port
colon stays unambiguous. A bare IPv6 host is rejected — you can't tell where the
address ends and the port begins:

.. code-block:: python

   socket("[2001:db8::1]:443")   # True
   socket("[::1]:8080")          # True — bracketed loopback
   socket("2001:db8::1:443")     # False — a bare IPv6 host must be bracketed

.. edify-playground::
   :tests: [2001:db8::1]:443|[::1]:8080|2001:db8::1:443

   from edify.library import socket
   socket

The three host shapes are an :func:`~edify.any_of`, joined by ``:`` to a 1–5 digit
port. For the exact 0–65535 port bound on its own see :doc:`port`; for the host
alone, :doc:`hostname`, :doc:`ipv4`, or :doc:`ipv6`.
