url
===

``url`` matches an HTTP/HTTPS web URL, and the thing to understand about it is how
much is **optional**. The scheme is optional, ``www.`` is optional, the path and
query and fragment are optional. The one part it insists on is a **dotted host
ending in a short TLD** — that is what makes something a URL to ``url``.

.. edify-playground::
   :tests: https://example.com|www.example.com|example.com|a.io/x?q=1|https://a.io:8443/p#top|ftp://x.com|notaurl

   from edify.library import url
   url

So ``example.com`` matches with no scheme at all, and ``https://a.io/s?q=1#top``
matches with everything attached, but ``notaurl`` (no dotted host) does not. A
``//``-style scheme like ``ftp://`` is rejected — not because edify checks the
scheme, but because ``/`` isn't one of the host's allowed characters.

.. note::

   ``url`` keys on that dotted host, and its host characters include ``:``, so a
   colon-prefixed string that still ends in a dotted TLD — ``mailto:a@b.com`` —
   *does* slip through. If you need strict scheme handling, use :doc:`uri` or
   check the scheme yourself. ``url`` guarantees the shape, not reachability, TLS,
   or DNS.
