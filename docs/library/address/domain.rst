domain
======

.. edify-validator:: domain

``domain`` matches a DNS domain name — one or more dot-separated labels ending in
a letters-only top-level domain, like ``example.com``.

Under the hood edify repeats a **label** — an :meth:`~edify.RegexBuilder.alphanumeric`
start, up to 61 interior letters/digits/hyphens, an alphanumeric end — with
:meth:`~edify.RegexBuilder.one_or_more`, each followed by a dot, and finishes with
a :doc:`tld` of 2–63 :meth:`~edify.RegexBuilder.letter`\ s, anchored with
:meth:`~edify.RegexBuilder.start_of_input` / :meth:`~edify.RegexBuilder.end_of_input`:

.. code-block:: python

   from edify import Pattern

   domain = (
       Pattern().start_of_input()
       .one_or_more().group().use(label).char(".").end()
       .between(2, 63).letter()
       .end_of_input()
   )

Labels and the TLD
------------------

One or more labels joined by dots, ending in a letters-only TLD. A bare label with
no TLD is not a domain, and the TLD may not be numeric:

.. code-block:: python

   domain("example.com")        # True — one label + TLD
   domain("a.b.example.io")     # True — several labels deep
   domain("xn--nxasmq6b.com")   # True — a Punycode (IDNA) label
   domain("example")            # False — no TLD
   domain("example.123")        # False — a TLD is letters only

.. edify-playground::
   :tests: example.com|a.b.example.io|xn--nxasmq6b.com|example|example.123

   from edify.library import domain
   domain

Interior hyphens only
---------------------

A label may contain hyphens, but may not begin or end with one:

.. code-block:: python

   domain("my-site.org")   # True  — interior hyphen
   domain("-x.com")        # False — label starts with a hyphen
   domain("x-.com")        # False — label ends with a hyphen

.. edify-playground::
   :tests: my-site.org|sub-domain.example.com|-x.com|x-.com

   from edify.library import domain
   domain

Notes
-----

- For a name that may be a single bare label such as ``localhost``, use
  :doc:`hostname`; for one label on its own, :doc:`subdomain`; for the trailing
  component alone, :doc:`tld`.
