socket
======

:doc:`Library <../index>` › :doc:`Address <index>` › **socket**

``socket`` matches a ``host:port`` socket address — an IPv4 address, a
bracketed IPv6 address, or a hostname, followed by ``:`` and a port number.

.. code-block:: python

   from edify.library import socket

   socket("127.0.0.1:8080")       # True — IPv4 host
   socket("localhost:80")         # True — hostname
   socket("[2001:db8::1]:443")    # True — bracketed IPv6
   socket("127.0.0.1")            # False — no port

What it matches
---------------

- A **host**: an IPv4 dotted-quad, a ``[…]``-bracketed IPv6 address, or a
  dotted hostname.
- A ``:`` separator followed by a **1–5 digit port**.
- Anchored at both ends.

The port field here is a 1–5 digit number; for the exact 0–65535 bound on its
own, see :doc:`port`, and for the host on its own see :doc:`hostname` or
:doc:`ipv4`.

Try it
------

.. edify-playground::
   :tests: 127.0.0.1:8080|localhost:80|[2001:db8::1]:443|db.internal:5432|127.0.0.1

   from edify.library import socket
   socket

Pattern
-------

.. code-block:: text

   ^(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}|\[[0-9a-fA-F:]+\]|[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*):\d{1,5}$
