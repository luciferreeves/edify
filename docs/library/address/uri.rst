uri
===

Where :doc:`url` is fussy about the HTTP web-URL shape, ``uri`` is deliberately
broad. A URI is a **scheme**, a **colon**, and a **non-empty remainder** — and the
scheme can be anything, so the whole family of identifiers passes.

.. edify-playground::
   :tests: https://example.com|mailto:jane@example.com|tel:+15551234567|urn:isbn:0451450523|ftp://host/f|no scheme|http:|ht tp://x

   from edify.library import uri
   uri

**Any scheme.** Web (``https:``), email (``mailto:``), telephone (``tel:``),
names (``urn:``), file transfer (``ftp:``) — ``uri`` doesn't care which, only that
there is one:

.. code-block:: python

   uri("https://example.com")       # True — web
   uri("mailto:jane@example.com")   # True — email
   uri("tel:+15551234567")          # True — telephone
   uri("urn:isbn:0451450523")       # True — a URN

**The scheme has a shape.** It must start with a :meth:`~edify.RegexBuilder.letter`,
then letters, digits, ``+``, ``.``, ``-``. A space breaks it:

.. code-block:: python

   uri("ht tp://x")   # False — whitespace in the scheme

**The remainder can't be empty.** After the ``:`` there must be at least one
:meth:`~edify.RegexBuilder.non_whitespace_char`, which is why a bare ``http:`` and
a string with no colon at all both fail:

.. code-block:: python

   uri("http:")      # False — nothing after the colon
   uri("no scheme")  # False — no scheme and colon

The emitted pattern is a tidy ``^[a-zA-Z][a-zA-Z0-9\+\.\-]*:\S+$``. Reach for
:doc:`url` instead when you specifically want the HTTP/HTTPS web-URL shape with a
validated TLD.
