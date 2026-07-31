Socket address
==============

A `socket address <https://en.wikipedia.org/wiki/Network_socket>`__ is a host and a
port, ``host:port``. What makes **Socket address** more than "something, a colon, a
number" is that the host can be three different things — and one of them, IPv6,
already contains colons and so needs special handling.

The three host shapes are the branches of an :func:`~edify.any_of`; whichever one
matches, a single ``:`` and a :meth:`~edify.RegexBuilder.between`\ ``(1, 5)``
:meth:`~edify.RegexBuilder.digit` port follow.

An IPv4 host
------------

A dotted-quad, reusing the :doc:`octet <../../guide/composing>` range check of
:doc:`ipv4`, then a colon and a port. Without the port the whole thing fails:

.. edify-playground::

   from edify.library import socket

   socket("127.0.0.1:8080")   # loopback and a port
   socket("0.0.0.0:80")       # bind-any address
   socket("127.0.0.1")        # no port

A hostname host
---------------

A dotted name or a single label, following the grammar of :doc:`hostname`:

.. edify-playground::

   from edify.library import socket

   socket("localhost:80")          # a single label
   socket("db.internal:5432")      # an internal name
   socket("api.example.com:443")   # a public name

A bracketed IPv6 host
---------------------

Because an IPv6 address is full of colons, it is wrapped in ``[...]`` so the port colon
stays unambiguous. A bare IPv6 host is rejected — you can't tell where the address
ends and the port begins:

.. edify-playground::

   from edify.library import socket

   socket("[2001:db8::1]:443")   # bracketed, then the port
   socket("[::1]:8080")          # bracketed loopback
   socket("2001:db8::1:443")     # a bare IPv6 host must be bracketed

For the exact 0–65535 port bound on its own see :doc:`port`; for the host alone,
:doc:`hostname`, :doc:`ipv4`, or :doc:`ipv6`.
