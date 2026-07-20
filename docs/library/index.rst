Library
=======

Edify ships **228 ready-made validators** across 22 topical categories. Each is a
callable :class:`~edify.Pattern`: import it, call it, get a ``bool``.

.. code-block:: python

   from edify.library import email, semver, iban

   email("a@b.com")                  # True
   semver("1.2.3")                   # True
   iban("GB82WEST12345698765432")    # True

Every validator has its own page with what it matches, each variant covered with
verified examples, a live playground, and the emitted regex. Browse by category
in the sidebar, or start here:

.. toctree::
   :maxdepth: 1

   address/index

Categories
----------

- **Address** — IPs, hosts, domains, ports, URLs, postal codes. *(done)*
- **API, Auth, Color, Contact, Data, Documents, Finance, Geo, Grammar,
  Identifiers, Media, Medical, Numeric, Product, Publishing, Security, Software,
  Temporal, Text, Transport, Web** — being handcrafted, one validator at a time.
