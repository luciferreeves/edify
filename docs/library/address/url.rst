url
===

``url`` matches a permissive HTTP/HTTPS web-URL shape. Everything except the
dotted host and its short TLD is optional, so it accepts the many ways people
write a link — with or without a scheme, with or without ``www.``.

Under the hood edify chains an :meth:`~edify.RegexBuilder.optional`
``http[s]://`` scheme, an optional ``www.`` prefix, a run of host characters, a
dot, a 1–6 character TLD, and an optional path/query/fragment tail — anchored with
:meth:`~edify.RegexBuilder.start_of_input` / :meth:`~edify.RegexBuilder.end_of_input`:

.. code-block:: python

   from edify import Pattern

   url = (
       Pattern().start_of_input()
       .optional().group().string("http").optional().char("s").string("://").end()
       .optional().group().string("www.").end()
       .between(1, 256).use(host_chars).char(".").between(1, 6).use(tld_chars)
       .word_boundary().zero_or_more().use(path_chars)
       .end_of_input()
   )

which emits:

.. code-block:: text

   ^(?:https?://)?(?:www\.)?[\-a-zA-Z0-9@:%\._\+\~\#=]{1,256}\.[a-zA-Z0-9\(\)]{1,6}\b[\-a-zA-Z0-9\(\)@:%_\+\.\~\#\?\&/=]*$

The scheme is optional
----------------------

An ``http://`` or ``https://`` prefix is accepted but not required, and a bare
``www.`` host works too. The one required part is a dotted host ending in a short
TLD, so a bare word fails:

.. code-block:: python

   url("https://example.com")   # True
   url("http://example.com")    # True
   url("example.com")           # True — no scheme
   url("www.example.com")       # True — www prefix, no scheme
   url("notaurl")               # False — no dotted host + TLD

.. edify-playground::
   :tests: https://example.com|http://example.com|example.com|www.example.com|notaurl

   from edify.library import url
   url

Paths, queries, and fragments
-----------------------------

Anything after the host — a path, a ``?`` query, a ``#`` fragment, or an explicit
port — is matched as an optional tail, while a ``//``-style non-HTTP scheme is
rejected because ``/`` is not a host character:

.. code-block:: python

   url("https://a.io/x/y")          # True — path
   url("https://a.io/s?q=1&r=2")    # True — query string
   url("https://a.io/p#top")        # True — fragment
   url("https://a.io:8443/x")       # True — explicit port
   url("ftp://x.com")               # False — the // scheme separator isn't a host char

.. edify-playground::
   :tests: https://a.io/x/y|https://a.io/s?q=1&r=2|https://a.io/p#top|https://a.io:8443/x|ftp://x.com

   from edify.library import url
   url

Notes
-----

- ``url`` keys on a dotted host ending in a short TLD, and its host characters
  include ``:`` — so a colon-prefixed string that still ends in a dotted TLD, like
  ``mailto:a@b.com``, *does* match. If you need strict scheme handling use
  :doc:`uri` or check the scheme yourself.
- It guarantees the shape only — not reachability, TLS validity, or DNS
  resolution.
