User-Agent
==========

A `User-Agent <https://datatracker.ietf.org/doc/html/rfc9110#field.user-agent>`__
string identifies the client making a request. Its grammar is famously loose —
decades of compatibility spoofing left it a jumble of product tokens and parenthesised
comments — so **User-Agent** validates the *character set and length* rather than
pretending there is a structure to parse.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(4, 1024)`` over an
:meth:`~edify.RegexBuilder.any_of` class of alphanumerics and the punctuation these
strings use: ``/`` ``.`` ``-`` ``(`` ``)`` space ``;`` ``+`` ``_`` ``,`` ``:``.

Real user agents
----------------

.. edify-playground::

   from edify.library import useragent

   useragent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36")
   useragent("curl/8.4.0")                       # a command-line client
   useragent("python-requests/2.31.0")           # a library
   useragent("Googlebot/2.1 (+http://www.google.com/bot.html)")   # a crawler

Length and alphabet
-------------------

Four characters is the floor, and characters outside the set — such as a quote or a
newline — are rejected:

.. edify-playground::

   from edify.library import useragent

   useragent("curl/8.4.0")     # valid
   useragent("abc")            # too short
   useragent("a" * 1025)       # too long
   useragent('bad"quote')      # a quote
   useragent("")               # empty

A User-Agent is client-supplied and trivially forged, so never use it for access
control or security decisions — treat it as a hint for analytics and compatibility
only. Because it is attacker-controlled, validating the character set here is
worthwhile before the value reaches a log file or a template.
