Domain
======

A DNS domain name (:rfc:`1035`) is a run of dot-separated **labels** ending in a
letters-only :doc:`tld` — ``example.com``, ``a.b.example.io``. That trailing TLD is
what distinguishes **Domain** from :doc:`hostname`, where a bare ``localhost`` is
allowed.

Each :doc:`label <../../guide/atoms/network>` is an :meth:`~edify.RegexBuilder.alphanumeric`
start and end around up to 61 interior letters/digits/hyphens; that group,
dot-terminated, repeats with :meth:`~edify.RegexBuilder.one_or_more`, and the name
closes with :meth:`~edify.RegexBuilder.between`\ ``(2, 63)`` letters for the TLD.

Labels
------

One or more, joined by dots. Each label is 1–63 characters of letters, digits, and
hyphens, and you can stack as many as you like. A
`Punycode <https://en.wikipedia.org/wiki/Punycode>`__ (IDNA) label such as
``xn--nxasmq6b`` is just letters, digits, and hyphens, so it passes:

.. edify-playground::

   from edify.library import domain

   domain("example.com")        # one label + TLD
   domain("a.b.example.io")     # several labels deep
   domain("xn--nxasmq6b.com")   # a Punycode label

Interior hyphens only
---------------------

A label may contain hyphens but may not begin or end with one — the rule that most
often surprises people:

.. edify-playground::

   from edify.library import domain

   domain("my-site.org")   # interior hyphen
   domain("-x.com")        # starts with a hyphen
   domain("x-.com")        # ends with a hyphen

The TLD is letters only
-----------------------

The final component must be a :doc:`tld` of 2–63 letters, so a name with no TLD or a
numeric one fails:

.. edify-playground::

   from edify.library import domain

   domain("example.io")    # a short letters-only TLD
   domain("example")       # no TLD
   domain("example.123")   # a numeric TLD

For a name that may be a bare single label use :doc:`hostname`; for one label on its
own, :doc:`subdomain`.
