uri
===

Where :doc:`url` is fussy about the HTTP web-URL shape, ``uri`` is deliberately
broad: **a scheme, a colon, and a non-empty remainder** — any scheme at all.

.. edify-playground::
   :tests: https://example.com|mailto:jane@example.com|tel:+15551234567|urn:isbn:0451450523|ftp://host/f|no scheme|http:

   from edify.library import uri
   uri

So the whole family passes — ``https:`` for the web, ``mailto:`` for email,
``tel:`` for phone numbers, ``urn:`` for names, ``ftp:`` for transfers. The scheme
must start with a :meth:`~edify.RegexBuilder.letter` (then letters, digits, ``+``,
``.``, ``-``), and after the ``:`` there must be at least one
:meth:`~edify.RegexBuilder.non_whitespace_char` — which is why ``no scheme`` (no
colon) and ``http:`` (nothing after it) both fail. The emitted pattern is a tidy
``^[a-zA-Z][a-zA-Z0-9\+\.\-]*:\S+$``.

Reach for :doc:`url` instead when you specifically want the HTTP/HTTPS web-URL
shape with a validated TLD.
