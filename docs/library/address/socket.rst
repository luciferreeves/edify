socket
======

:doc:`Library <../index>` › :doc:`Address <index>` › **socket**

``socket`` matches a ``host:port`` socket address. The host may take three forms —
an IPv4 address, a bracketed IPv6 address, or a hostname — each followed by a
colon and a port.

.. code-block:: python

   from edify.library import socket

   socket("127.0.0.1:8080")   # True

An IPv4 host
------------

A dotted-quad host, colon, and port:

.. code-block:: python

   socket("127.0.0.1:8080")   # True
   socket("0.0.0.0:80")       # True — bind-any address

A hostname host
---------------

A dotted hostname (or a single label) works in the host position:

.. code-block:: python

   socket("localhost:80")        # True
   socket("db.internal:5432")    # True
   socket("api.example.com:443") # True

A bracketed IPv6 host
---------------------

Because IPv6 addresses already contain colons, they are wrapped in ``[…]`` so the
port colon stays unambiguous:

.. code-block:: python

   socket("[2001:db8::1]:443")   # True
   socket("[::1]:8080")          # True — bracketed loopback

What it rejects
---------------

.. code-block:: python

   socket("127.0.0.1")       # False — no port
   socket("localhost")       # False — no port
   socket("2001:db8::1:443") # False — bare IPv6 host must be bracketed

The port here is a 1–5 digit field; for the exact 0–65535 bound on its own see
:doc:`port`, and for the host on its own see :doc:`hostname` or :doc:`ipv4`.

Try it
------

.. edify-playground::
   :tests: 127.0.0.1:8080|localhost:80|[2001:db8::1]:443|db.internal:5432|127.0.0.1

   from edify.library import socket
   socket
