URI
===

Where :doc:`url` is fussy about the HTTP web-address shape, **URI** is deliberately
broad: a **scheme**, a **colon**, and a **non-empty remainder**, with the scheme free
to be anything (the generic syntax of :rfc:`3986`).

It starts with a :meth:`~edify.RegexBuilder.letter`, then
:meth:`~edify.RegexBuilder.zero_or_more` of a scheme
:meth:`~edify.RegexBuilder.any_of` class (letters, digits, ``+``, ``.``, ``-``), a
``:``, then :meth:`~edify.RegexBuilder.one_or_more`
:meth:`~edify.RegexBuilder.non_whitespace_char`. Three parts, three things to know.

Any scheme
----------

Web (``https:``), email (``mailto:``), telephone (``tel:``), names (``urn:``), file
transfer (``ftp:``) — **URI** does not care which, only that there is one:

.. edify-playground::

   from edify.library import uri

   uri("https://example.com")       # web
   uri("mailto:jane@example.com")   # email
   uri("tel:+15551234567")          # telephone
   uri("urn:isbn:0451450523")       # a URN
   uri("ftp://host/f")              # file transfer

The scheme has a shape
----------------------

It must start with a :meth:`~edify.RegexBuilder.letter`, then letters, digits, ``+``,
``.``, ``-``. Whitespace breaks it, and so does a missing scheme:

.. edify-playground::

   from edify.library import uri

   uri("git+ssh://host/repo")   # + is a legal scheme character
   uri("ht tp://x")             # a space in the scheme
   uri("no scheme")             # no scheme and colon

The remainder can't be empty
----------------------------

After the ``:`` there must be at least one
:meth:`~edify.RegexBuilder.non_whitespace_char`, so a bare ``http:`` fails:

.. edify-playground::

   from edify.library import uri

   uri("http:x")   # one character is enough
   uri("http:")    # nothing after the colon

Reach for :doc:`url` when you specifically want the HTTP/HTTPS web-address shape with
a dotted host — otherwise **URI** accepts the whole family.
