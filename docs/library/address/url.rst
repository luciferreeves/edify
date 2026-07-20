url
===

:doc:`Library <../index>` › :doc:`Address <index>` › **url**

``url`` matches a permissive HTTP/HTTPS web-URL shape. Everything except the
dotted host and its short TLD is optional, so it accepts the many ways people
write a link — with or without a scheme, with or without ``www.``, bare host or
host-plus-path.

.. code-block:: python

   from edify.library import url

   url("https://example.com")   # True

The scheme is optional
----------------------

An ``http://`` or ``https://`` prefix is accepted but not required, and a bare
``www.`` host works too:

.. code-block:: python

   url("https://example.com")   # True
   url("http://example.com")    # True
   url("example.com")           # True — no scheme
   url("www.example.com")       # True — www prefix, no scheme

The host and its TLD
--------------------

The host is a dot-separated authority ending in a **1–6 character** TLD; that
trailing dotted TLD is the one non-optional part:

.. code-block:: python

   url("example.com")     # True
   url("a.io")            # True — two-letter TLD
   url("notaurl")         # False — no dotted host + TLD

Paths, queries, and fragments
-----------------------------

Anything after the host — a path, a ``?`` query, a ``#`` fragment, or an explicit
port — is matched as an optional tail:

.. code-block:: python

   url("https://a.io/x/y")          # True — path
   url("https://a.io/s?q=1&r=2")    # True — query string
   url("https://a.io/p#top")        # True — fragment
   url("https://a.io:8443/x")       # True — explicit port

What it rejects
---------------

.. code-block:: python

   url("ftp://x.com")   # False — the // scheme separator isn't a host character
   url("notaurl")       # False — no dotted host + TLD
   url("just text")     # False — no host

.. note::

   ``url`` keys on a **dotted host ending in a short TLD**, and its host character
   set includes ``:``. So while ``//``-style schemes like ``ftp://`` are rejected,
   a colon-prefixed string that still ends in a dotted TLD — ``mailto:a@b.com`` —
   *does* match, because it fits the host shape. If you need strict scheme
   handling, validate the scheme yourself or use :doc:`uri`. ``url`` guarantees
   the shape only, not reachability, TLS validity, or DNS resolution.

Try it
------

.. edify-playground::
   :tests: https://example.com|www.example.com|a.io/x?q=1|https://a.io:8443/p#top|ftp://x.com|notaurl

   from edify.library import url
   url
