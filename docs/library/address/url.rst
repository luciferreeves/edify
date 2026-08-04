URL
===

**URL** matches an HTTP/HTTPS web address, and the key to it is how much is
*optional*. The scheme, the ``www.``, and the whole path/query/fragment tail are all
optional (loosely following :rfc:`3986`); the one thing it insists on is a **dotted
host ending in a short suffix**.

A scheme is accepted but not required via an :meth:`~edify.RegexBuilder.optional`
``https?://``, likewise ``www.``, then a run of host characters, a dot, a 1–6
character suffix, and one more :meth:`~edify.RegexBuilder.optional` group for the
tail.

Almost everything is optional
-----------------------------

A bare host matches, and so does a fully dressed URL — only the dotted host and its
suffix are mandatory:

.. edify-playground::

   from edify.library import url

   url("https://example.com")   # scheme and host
   url("www.example.com")       # www, no scheme
   url("example.com")           # nothing but the host
   url("notaurl")               # no dotted host + suffix

The tail is free-form
---------------------

A path, a ``?`` query, a ``#`` fragment, or an explicit port are all matched as an
optional tail:

.. edify-playground::

   from edify.library import url

   url("https://a.io/x/y")         # path
   url("https://a.io/s?q=1&r=2")   # query string
   url("https://a.io:8443/p#top")  # port and fragment

Why ``ftp://`` fails but ``mailto:`` slips through
--------------------------------------------------

A ``//``-style scheme is rejected — not because **URL** checks the scheme, but because
``/`` is not one of the host's allowed characters. The host characters *do* include
``:``, though, so a colon-prefixed string that still ends in a dotted suffix sneaks
in:

.. edify-playground::

   from edify.library import url

   url("ftp://x.com")      # the // is not a host character
   url("mailto:a@b.com")   # a colon + a dotted suffix fits the host shape

If you need strict scheme handling, use :doc:`uri` or check the scheme yourself.
**URL** guarantees the shape only — not reachability, TLS, or DNS.
