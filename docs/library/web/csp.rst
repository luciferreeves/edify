CSP
===

A `Content-Security-Policy <https://www.w3.org/TR/CSP3/>`__ header is a list of
directives separated by semicolons, each naming a resource type and the sources
allowed for it. **CSP** matches that structure.

The construction is a lowercase hyphenated directive name, whitespace, then a value
made of :meth:`~edify.RegexBuilder.assert_not_ahead` over ``;`` — "any character
that is not the separator". That group repeats for each further
semicolon-separated directive, with an :meth:`~edify.RegexBuilder.optional`
trailing semicolon.

Policy strings
--------------

.. edify-playground::

   from edify.library import csp

   csp("default-src 'self'")                                    # a single directive
   csp("script-src 'self' https://cdn.example.com; object-src 'none'")
   csp("default-src 'self'; img-src * data:; frame-ancestors 'none'")
   csp("default-src 'self';")                                    # a trailing semicolon

Directive names are lowercase
-----------------------------

A name must be lowercase letters and hyphens, and a value is required:

.. edify-playground::

   from edify.library import csp

   csp("frame-ancestors 'none'")   # a hyphenated name
   csp("Default-Src 'self'")       # uppercase is rejected
   csp("default-src")              # no value
   csp("hello")                    # not a policy

This checks the header's syntax, not its security value. A policy can be perfectly
well formed and still be useless — ``default-src *`` matches here, as does a
``script-src`` containing ``'unsafe-inline'``, which defeats the main protection CSP
offers. Review the sources themselves, and prefer nonces (see
:doc:`../security/nonce`) or hashes over blanket allowances.
