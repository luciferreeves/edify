uri
===

``uri`` matches the generic URI shape — a scheme, a colon, and a non-empty
remainder. Unlike :doc:`url`, it accepts *any* scheme, not just HTTP.

Under the hood it is a :meth:`~edify.RegexBuilder.letter` (the scheme's required
first character), then any run of letters, digits, ``+``, ``.``, ``-``, a ``:``,
and one or more :meth:`~edify.RegexBuilder.non_whitespace_char` — anchored with
:meth:`~edify.RegexBuilder.start_of_input` / :meth:`~edify.RegexBuilder.end_of_input`:

.. code-block:: python

   from edify import Pattern

   uri = (
       Pattern().start_of_input()
       .letter().zero_or_more().any_of().range("a", "z").range("A", "Z").range("0", "9").char("+").char(".").char("-").end()
       .char(":").one_or_more().non_whitespace_char()
       .end_of_input()
   )

which emits:

.. code-block:: text

   ^[a-zA-Z][a-zA-Z0-9\+\.\-]*:\S+$

Any scheme
----------

Because it accepts any scheme, the whole URI family passes — web, email,
telephone, URN, file transfer. What fails is a string with no scheme and colon,
or whitespace where the scheme should be:

.. code-block:: python

   uri("https://example.com")        # True — web
   uri("mailto:jane@example.com")    # True — email
   uri("tel:+15551234567")           # True — telephone
   uri("urn:isbn:0451450523")        # True — a URN
   uri("no scheme")                  # False — no scheme + colon
   uri("http:")                      # False — the part after the colon is empty

.. edify-playground::
   :tests: https://example.com|mailto:jane@example.com|tel:+15551234567|urn:isbn:0451450523|no scheme|http:

   from edify.library import uri
   uri

Notes
-----

- For the narrower HTTP/HTTPS web-URL shape — with an optional scheme, a ``www.``
  prefix, and a validated short TLD — use :doc:`url`.
