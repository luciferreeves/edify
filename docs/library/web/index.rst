Web
===

Server configuration, site metadata, and the HTTP header values that travel with
every request. Each validator is a callable :class:`~edify.Pattern`: import it, call
it with a string, get a ``bool``.

.. code-block:: python

   from edify.library import robots, cookie, csp

   robots("User-agent: *")            # True
   cookie("sessionid=abc123")         # True
   csp("default-src 'self'")          # True

.. toctree::
   :hidden:

   apache
   captcha
   cookie
   csp
   htaccess
   humans
   manifest
   nginx
   robots
   sitemap
   useragent

Server configuration
--------------------

- :doc:`nginx` and :doc:`apache` — top-level server configuration.
- :doc:`htaccess` — a per-directory override file.

Site metadata
-------------

- :doc:`robots` — a crawler exclusion file; :doc:`sitemap` — an XML sitemap.
- :doc:`humans` — a credits file; :doc:`manifest` — a web app manifest.

HTTP values
-----------

- :doc:`cookie` — a ``name=value`` pair; :doc:`csp` — a Content-Security-Policy.
- :doc:`useragent` — a User-Agent string; :doc:`captcha` — a verification token.
