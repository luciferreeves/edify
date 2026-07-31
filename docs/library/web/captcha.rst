CAPTCHA
=======

A `CAPTCHA <https://en.wikipedia.org/wiki/CAPTCHA>`__ widget hands the browser a
long opaque token, which your server then submits to the provider for verification.
**CAPTCHA** matches that response token: 20 to 2048 URL-safe characters.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(20, 2048)`` over an
:meth:`~edify.RegexBuilder.any_of` class of alphanumerics plus ``-`` and ``_``. The
wide ceiling accommodates the long tokens the major providers issue.

Response tokens
---------------

.. edify-playground::

   from edify.library import captcha

   captcha("03AGdBq26" + "a" * 40)   # a provider-style token
   captcha("a" * 20)                  # at the minimum
   captcha("token-with_safe-chars12") # the URL-safe marks
   captcha("a" * 2048)                # at the maximum

Length and alphabet
-------------------

.. edify-playground::

   from edify.library import captcha

   captcha("a" * 20)      # at the minimum
   captcha("short")       # too short
   captcha("a" * 2049)    # too long
   captcha("has spaces here too")   # outside the alphabet

The token is meaningless until you verify it server-side with the provider's secret
key — a client can send any well-formed string, so treating a shape match as "human
verified" defeats the entire mechanism. Verify once, and reject reused tokens.
