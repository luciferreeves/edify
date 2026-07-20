url
===

``url`` matches an HTTP/HTTPS web URL, and the key to it is how much is
**optional**. The scheme, ``www.``, and the whole path/query/fragment tail are all
optional; the one thing it insists on is a **dotted host ending in a short TLD**.

.. edify-playground::
   :tests: https://example.com|www.example.com|example.com|a.io/x?q=1|https://a.io:8443/p#top|ftp://x.com|notaurl|mailto:a@b.com

   from edify.library import url
   url

**Almost everything is optional.** A scheme is accepted but not required, and so
is ``www.`` — so a bare host matches, and so does a fully dressed URL:

.. code-block:: python

   url("https://example.com")   # True
   url("www.example.com")       # True — www, no scheme
   url("example.com")           # True — nothing but the host
   url("notaurl")               # False — no dotted host + TLD

**The tail is free-form.** A path, a ``?`` query, a ``#`` fragment, or an explicit
port are all matched as an optional tail:

.. code-block:: python

   url("https://a.io/x/y")          # True — path
   url("https://a.io/s?q=1&r=2")    # True — query string
   url("https://a.io:8443/p#top")   # True — port and fragment

**Why ``ftp://`` fails but ``mailto:`` slips through.** A ``//``-style scheme is
rejected — not because edify checks the scheme, but because ``/`` isn't one of the
host's allowed characters. The host characters *do* include ``:``, though, so a
colon-prefixed string that still ends in a dotted TLD sneaks in:

.. code-block:: python

   url("ftp://x.com")      # False — the // isn't a host character
   url("mailto:a@b.com")   # True  — a colon + a dotted TLD fits the host shape

If you need strict scheme handling, use :doc:`uri` or check the scheme yourself.
``url`` guarantees the shape only — not reachability, TLS, or DNS.
