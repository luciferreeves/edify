Address
=======

Network and location addressing — IP addresses, host and domain names, ports,
subnets, reverse-DNS records, URLs, and postal codes. Each validator is a callable
:class:`~edify.Pattern`: import it, call it with a string, get a ``bool``. Every
method each one is built from is documented in the :doc:`API reference <../../api/index>`.

.. code-block:: python

   from edify.library import ipv4, url, port

   ipv4("192.168.0.1")            # True
   url("https://example.com")     # True
   port("8080")                   # True

.. toctree::
   :hidden:

   cidr
   domain
   hostname
   ip
   ipv4
   ipv6
   path
   port
   ptr
   socket
   subdomain
   subnet
   tld
   uri
   url
   zip_code

Addresses of a machine
----------------------

- :doc:`ip` — an IPv4 or IPv6 address; :doc:`ipv4` and :doc:`ipv6` pin one family.
- :doc:`cidr` — an address plus a ``/prefix`` network block.
- :doc:`subnet` — a dotted-decimal mask such as ``255.255.255.0``.
- :doc:`ptr` — a reverse-DNS ``in-addr.arpa`` / ``ip6.arpa`` record.

Names of a host
---------------

- :doc:`domain` — a dotted name ending in a letters-only :doc:`tld`.
- :doc:`hostname` — the same, but a bare single label like ``localhost`` is allowed.
- :doc:`subdomain` — one label on its own.
- :doc:`tld` — a top-level domain.

Locators, ports, and codes
--------------------------

- :doc:`url` — an HTTP/HTTPS web address; :doc:`uri` — any ``scheme:`` locator.
- :doc:`path` — a POSIX, Windows, or UNC filesystem path.
- :doc:`port` — a 0–65535 port; :doc:`socket` — a ``host:port`` pair.
- :doc:`zip_code` — a US ZIP or ZIP+4 postal code.
