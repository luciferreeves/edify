Apache
======

An `Apache <https://httpd.apache.org/docs/current/configuring.html>`__ configuration
uses XML-style sections and capitalised directives — a different dialect from
:doc:`nginx`'s braces. **Apache** recognises a ``<Section>`` opening, a known
top-level directive, or a ``#`` comment.

Those are the branches of an :func:`~edify.any_of`. The section branch is ``<``
followed by a container name — ``VirtualHost``, ``Directory``, ``Location``,
``Files``, ``IfModule``, ``Limit``, ``Proxy``. The directive branch is a known
setting followed by whitespace.

Sections
--------

.. edify-playground::

   from edify.library import apache

   apache("<VirtualHost *:80>\n  ServerName example.com\n</VirtualHost>")
   apache("<Directory /var/www>\n  Require all granted\n</Directory>")
   apache("<IfModule mod_ssl.c>\n</IfModule>")

Directives and comments
-----------------------

.. edify-playground::

   from edify.library import apache

   apache("ServerName example.com\n")
   apache("Listen 80")
   apache("LoadModule ssl_module modules/mod_ssl.so")
   apache("# a comment\nListen 80")

Not a configuration
-------------------

.. edify-playground::

   from edify.library import apache

   apache("Listen 80")     # a directive
   apache("hello-world")   # plain text
   apache('{"a": 1}')      # JSON
   apache("")              # empty

As with :doc:`nginx`, this matches the opening rather than validating the whole file
— run ``apachectl configtest`` for that. For per-directory overrides see
:doc:`htaccess`.
