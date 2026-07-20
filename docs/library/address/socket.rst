socket
======

A socket address is a host and a port, ``host:port``. What makes ``socket`` more
than "something, a colon, a number" is that the host can be three different
things — and one of them needs special handling because it already contains
colons.

.. edify-playground::
   :tests: 127.0.0.1:8080|localhost:80|[2001:db8::1]:443|db.internal:5432|127.0.0.1

   from edify.library import socket
   socket

**An IPv4 host** is a dotted-quad, reusing the octet range check of :doc:`ipv4` —
``127.0.0.1:8080``, ``0.0.0.0:80``.

**A hostname host** is a dotted name or a single label, following the grammar of
:doc:`hostname` — ``localhost:80``, ``db.internal:5432``, ``api.example.com:443``.

**An IPv6 host** must be wrapped in ``[...]`` so its colons don't collide with the
port colon — ``[2001:db8::1]:443``, ``[::1]:8080``. A bare IPv6 host like
``2001:db8::1:443`` is ambiguous and therefore rejected.

Those three are an :func:`~edify.any_of`, joined by ``:`` to a 1–5 digit port. For
the exact 0–65535 port bound on its own, see :doc:`port`; for the host alone, see
:doc:`hostname`, :doc:`ipv4`, or :doc:`ipv6`.
