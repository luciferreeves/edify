Address
=======

:doc:`Library <../index>` › **Address**

Network and location addressing — IP addresses, host and domain names, ports,
subnets, reverse-DNS records, URLs, and postal codes. Each is a callable
:class:`~edify.Pattern`: import it, call it, get a ``bool``.

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

The sixteen address validators:

- :doc:`ipv4` / :doc:`ipv6` / :doc:`ip` — IPv4, IPv6, or either.
- :doc:`cidr` / :doc:`subnet` — CIDR blocks and dotted-decimal masks.
- :doc:`domain` / :doc:`hostname` / :doc:`subdomain` / :doc:`tld` — name shapes.
- :doc:`ptr` — reverse-DNS records.
- :doc:`url` / :doc:`uri` / :doc:`path` — locators and paths.
- :doc:`port` / :doc:`socket` — ports and ``host:port`` pairs.
- :doc:`zip_code` — US postal codes.
