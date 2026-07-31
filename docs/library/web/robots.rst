Robots
======

A `robots.txt <https://datatracker.ietf.org/doc/html/rfc9309>`__ file (:rfc:`9309`)
tells crawlers which parts of a site they may fetch. It is a list of ``Field: value``
lines from a small vocabulary, and **Robots** matches how such a file opens.

The known fields are an :func:`~edify.any_of` — ``user-agent``, ``disallow``,
``allow``, ``sitemap``, ``crawl-delay``, ``host`` — followed by a colon, or a ``#``
comment. The pattern carries :meth:`~edify.RegexBuilder.ignore_case`, since the
specification treats field names case-insensitively.

Directive lines
---------------

.. edify-playground::

   from edify.library import robots

   robots("User-agent: *\nDisallow: /admin")
   robots("User-agent: Googlebot\nAllow: /public")
   robots("Sitemap: https://example.com/sitemap.xml")
   robots("user-agent: *")               # field names are case-insensitive
   robots("# a comment\nUser-agent: *")  # a leading comment

A known field is required
-------------------------

Arbitrary text is not a robots file:

.. edify-playground::

   from edify.library import robots

   robots("Disallow: /private")   # a known field
   robots("hello-world")          # no directive
   robots('{"a": 1}')             # JSON
   robots("")                     # empty

Two things worth remembering: robots.txt is advisory — it asks well-behaved crawlers
to stay away and stops nobody else, so never use it to protect anything sensitive.
And listing a path under ``Disallow`` publishes that path to anyone who reads the
file. For the sitemap it often references see :doc:`sitemap`.
