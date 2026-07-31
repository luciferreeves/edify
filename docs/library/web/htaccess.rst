htaccess
========

An `.htaccess <https://httpd.apache.org/docs/current/howto/htaccess.html>`__ file
applies Apache configuration to a single directory. Its vocabulary is narrower than
a server-wide config — mostly rewriting, access control, and content-type overrides —
and **htaccess** recognises that vocabulary.

The branches of the :func:`~edify.any_of` are a ``<Section>`` opening from the
per-directory containers, one of the rewrite/access directives, or a ``#`` comment.

Rewriting
---------

.. edify-playground::

   from edify.library import htaccess

   htaccess("RewriteEngine On\nRewriteRule ^old$ /new [R=301]")
   htaccess("RewriteCond %{HTTPS} off\nRewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI}")
   htaccess("RewriteBase /")

Access and content
------------------

.. edify-playground::

   from edify.library import htaccess

   htaccess("Options -Indexes")
   htaccess("ErrorDocument 404 /404.html")
   htaccess("Require all granted")
   htaccess("<IfModule mod_rewrite.c>\n  RewriteEngine On\n</IfModule>")
   htaccess("# a comment\nOptions -Indexes")

Not a configuration
-------------------

.. edify-playground::

   from edify.library import htaccess

   htaccess("RewriteEngine On")   # a directive
   htaccess("hello-world")        # plain text
   htaccess('{"a": 1}')           # JSON, not a directive
   htaccess("")                   # empty

Per-directory files are read on every request and can weaken server settings, so
their contents deserve review rather than a shape check alone. For server-wide
configuration see :doc:`apache`.
