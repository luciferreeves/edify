domain
======

:doc:`Library <../index>` › :doc:`Address <index>` › **domain**

``domain`` matches a DNS domain name — one or more dot-separated labels followed
by a letters-only top-level domain.

.. code-block:: python

   from edify.library import domain

   domain("example.com")   # True

Labels
------

A domain is a series of labels joined by dots. Each label is 1–63 characters of
letters, digits, and hyphens, and there is no limit on how many you stack:

.. code-block:: python

   domain("example.com")        # True — one label + TLD
   domain("a.b.example.io")     # True — several labels deep
   domain("xn--nxasmq6b.com")   # True — a Punycode (IDNA) label

The TLD
-------

The final component must be a **letters-only TLD of 2–63 characters** (this is
the :doc:`tld` shape). A bare label with no TLD is not a domain:

.. code-block:: python

   domain("example.com")   # True
   domain("example")       # False — no TLD
   domain("example.123")   # False — a TLD is letters only

Hyphens are interior only
-------------------------

A label may contain hyphens, but may not begin or end with one:

.. code-block:: python

   domain("my-site.org")   # True  — interior hyphen
   domain("-x.com")        # False — label starts with a hyphen
   domain("x-.com")        # False — label ends with a hyphen

What it rejects
---------------

.. code-block:: python

   domain(".com")       # False — empty leading label
   domain("a b.com")    # False — no spaces
   domain("localhost")  # False — no TLD (use hostname for bare labels)

For a name that may be a single bare label such as ``localhost``, use
:doc:`hostname`; for one label on its own, :doc:`subdomain`.

Try it
------

.. edify-playground::
   :tests: example.com|a.b.example.io|my-site.org|example|-x.com|localhost

   from edify.library import domain
   domain
