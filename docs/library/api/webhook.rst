Webhook
=======

A `webhook <https://en.wikipedia.org/wiki/Webhook>`__ is a callback: you hand a
provider a URL, and it delivers events there by HTTP request. **Webhook** validates
that endpoint. Because delivery targets carry
event data across the public internet, the scheme is fixed to ``https`` — an
``http`` endpoint would expose payloads in transit, so it is rejected rather than
merely discouraged.

The shape is ``https://`` with :meth:`~edify.RegexBuilder.string`, a dotted host of
one or more labels, an optional ``:port``, and a path introduced by ``/``. Requiring
a dot in the host is what rules out bare internal names like ``localhost``.

Delivery endpoints
------------------

A path is required, and query strings, ports, and multi-label hosts are all fine:

.. edify-playground::

   from edify.library import webhook

   webhook("https://example.com/hooks/github")
   webhook("https://hooks.example.co.uk/deliver")
   webhook("https://api.example.com:8443/cb?token=abc")
   webhook("https://example.com/")

TLS only, public hosts only
---------------------------

The two rejections that matter most in practice — an insecure scheme, and a host
with no dot, which usually means an internal or loopback target:

.. edify-playground::

   from edify.library import webhook

   webhook("https://example.com/hooks")    # TLS and a dotted host
   webhook("http://example.com/hooks")     # not TLS
   webhook("https://localhost/hooks")      # no dotted host
   webhook("example.com/hooks")            # no scheme
   webhook("hello-world")                   # not a URL

Matching says nothing about whether the endpoint is reachable, who controls it, or
whether it verifies delivery signatures — validate the shape here, then verify the
signature on every request you receive. For a general web address see
:doc:`../address/url`, and for the signing secret itself, :doc:`../auth/hmac`.
