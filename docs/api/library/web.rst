Web
===

Every validator in the :doc:`Web <../../library/web/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/web/index>`.

.. py:data:: edify.library.apache

   Callable :class:`Pattern` for an Apache server configuration: a comment, a
   ``<VirtualHost>``-style section, or a top-level directive.

   Full description: :doc:`Apache <../../library/web/apache>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _section = (
          Pattern()
          .char("<")
          .any_of()
          .string("VirtualHost")
          .string("Directory")
          .string("Location")
          .string("Files")
          .string("IfModule")
          .string("Limit")
          .string("Proxy")
          .end()
      )

      _directive = (
          Pattern()
          .any_of()
          .string("ServerName")
          .string("ServerRoot")
          .string("ServerAdmin")
          .string("DocumentRoot")
          .string("Listen")
          .string("LoadModule")
          .string("ErrorLog")
          .string("CustomLog")
          .string("Include")
          .end()
          .one_or_more()
          .whitespace_char()
      )

      _comment = Pattern().char("#")

      apache = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_comment)
          .use(_section)
          .use(_directive)
          .end()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:\#|<(?:VirtualHost|Directory|Location|Files|IfModule|Limit|Proxy)|(?:ServerName|ServerRoot|ServerAdmin|DocumentRoot|Listen|LoadModule|ErrorLog|CustomLog|Include)\s+).*$``

.. py:data:: edify.library.captcha

   Callable :class:`Pattern` for a CAPTCHA verification token: a long
   URL-safe base64 response string.

   Full description: :doc:`CAPTCHA <../../library/web/captcha>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      captcha = (
          Pattern()
          .start_of_input()
          .between(20, 2048)
          .any_of()
          .alphanumeric()
          .any_of_chars("-_")
          .end()
          .end_of_input()
      )

   **Emits** ``^(?:[a-zA-Z0-9]|[-_]){20,2048}$``

.. py:data:: edify.library.cookie

   Callable :class:`Pattern` for an HTTP ``name=value`` cookie pair.

   Full description: :doc:`Cookie <../../library/web/cookie>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern


      def _value_char() -> Pattern:
          return Pattern().assert_not_ahead().any_of().whitespace_char().char(";").end().end().any_char()


      cookie = (
          Pattern()
          .start_of_input()
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char("_")
          .char("-")
          .end()
          .char("=")
          .one_or_more()
          .subexpression(_value_char())
          .end_of_input()
      )

   **Emits** ``^[a-zA-Z0-9_\-]+=(?:(?!(?:\s|[;])).)+$``

.. py:data:: edify.library.csp

   Callable :class:`Pattern` for a Content-Security-Policy directive shape.

   Full description: :doc:`CSP <../../library/web/csp>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern


      def _directive_value() -> Pattern:
          return Pattern().assert_not_ahead().char(";").end().any_char()


      csp = (
          Pattern()
          .start_of_input()
          .one_or_more()
          .any_of()
          .range("a", "z")
          .char("-")
          .end()
          .one_or_more()
          .whitespace_char()
          .one_or_more()
          .subexpression(_directive_value())
          .zero_or_more()
          .group()
          .char(";")
          .zero_or_more()
          .whitespace_char()
          .one_or_more()
          .any_of()
          .range("a", "z")
          .char("-")
          .end()
          .one_or_more()
          .whitespace_char()
          .one_or_more()
          .subexpression(_directive_value())
          .end()
          .optional()
          .char(";")
          .end_of_input()
      )

   **Emits** ``^[a-z\-]+\s+(?:(?!;).)+(?:;\s*[a-z\-]+\s+(?:(?!;).)+)*;?$``

.. py:data:: edify.library.htaccess

   Callable :class:`Pattern` for a per-directory Apache override: a comment, an
   ``<IfModule>``-style section, or a rewrite/access directive.

   Full description: :doc:`htaccess <../../library/web/htaccess>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _section = (
          Pattern()
          .char("<")
          .any_of()
          .string("IfModule")
          .string("Files")
          .string("FilesMatch")
          .string("Limit")
          .string("RequireAll")
          .end()
      )

      _directive = (
          Pattern()
          .any_of()
          .string("RewriteEngine")
          .string("RewriteRule")
          .string("RewriteCond")
          .string("RewriteBase")
          .string("Redirect")
          .string("RedirectMatch")
          .string("Options")
          .string("AddType")
          .string("AddHandler")
          .string("ErrorDocument")
          .string("Header")
          .string("Require")
          .string("Order")
          .string("Deny")
          .string("Allow")
          .string("AuthType")
          .string("DirectoryIndex")
          .end()
          .one_or_more()
          .whitespace_char()
      )

      _comment = Pattern().char("#")

      htaccess = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_comment)
          .use(_section)
          .use(_directive)
          .end()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:\#|<(?:IfModule|Files|FilesMatch|Limit|RequireAll)|(?:RewriteEngine|RewriteRule|RewriteCond|RewriteBase|Redirect|RedirectMatch|Options|AddType|AddHandler|ErrorDocument|Header|Require|Order|Deny|Allow|AuthType|DirectoryIndex)\s+).*$``

.. py:data:: edify.library.humans

   Callable :class:`Pattern` for a humans.txt credits file: a comment, a
   ``/* TEAM */`` style section marker, or a ``Field: value`` line.

   Full description: :doc:`humans.txt <../../library/web/humans>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _section = (
          Pattern()
          .string("/*")
          .zero_or_more()
          .any_of()
          .alphanumeric()
          .any_of_chars(" -_")
          .end()
          .string("*/")
      )

      _field = (
          Pattern()
          .one_or_more()
          .any_of()
          .alphanumeric()
          .any_of_chars(" -_")
          .end()
          .char(":")
          .zero_or_more()
          .whitespace_char()
      )

      _comment = Pattern().char("#")

      humans = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_comment)
          .use(_section)
          .use(_field)
          .end()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:\#|/\*(?:[a-zA-Z0-9]|[ \-_])*\*/|(?:[a-zA-Z0-9]|[ \-_])+:\s*).*$``

.. py:data:: edify.library.manifest

   Callable :class:`Pattern` for a web application manifest: a JSON object
   carrying a ``start_url``, ``display``, ``icons``, ``short_name``, or
   ``theme_color`` member.

   Full description: :doc:`Manifest <../../library/web/manifest>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      manifest = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .char("{")
          .zero_or_more()
          .any_char()
          .char('"')
          .any_of()
          .string("start_url")
          .string("display")
          .string("icons")
          .string("short_name")
          .string("theme_color")
          .end()
          .char('"')
          .zero_or_more()
          .whitespace_char()
          .char(":")
          .zero_or_more()
          .any_char()
          .char("}")
          .zero_or_more()
          .whitespace_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*\{.*"(?:start_url|display|icons|short_name|theme_color)"\s*:.*\}\s*$``

.. py:data:: edify.library.nginx

   Callable :class:`Pattern` for a web-server configuration: a comment, a
   ``server``/``http``/``location`` block, or a top-level directive.

   Full description: :doc:`nginx <../../library/web/nginx>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _block = (
          Pattern()
          .any_of()
          .string("http")
          .string("server")
          .string("events")
          .string("location")
          .string("upstream")
          .string("stream")
          .string("map")
          .end()
          .zero_or_more()
          .any_char()
          .char("{")
      )

      _directive = (
          Pattern()
          .any_of()
          .string("worker_processes")
          .string("worker_connections")
          .string("include")
          .string("user")
          .string("pid")
          .string("error_log")
          .string("access_log")
          .end()
          .one_or_more()
          .whitespace_char()
      )

      _comment = Pattern().char("#")

      nginx = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_comment)
          .use(_block)
          .use(_directive)
          .end()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:\#|(?:http|server|events|location|upstream|stream|map).*\{|(?:worker_processes|worker_connections|include|user|pid|error_log|access_log)\s+).*$``

.. py:data:: edify.library.robots

   Callable :class:`Pattern` for a robots exclusion file: a comment or a
   ``User-agent``/``Disallow``/``Allow``/``Sitemap`` directive.

   Full description: :doc:`Robots <../../library/web/robots>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _directive = (
          Pattern()
          .any_of()
          .string("user-agent")
          .string("disallow")
          .string("allow")
          .string("sitemap")
          .string("crawl-delay")
          .string("host")
          .end()
          .zero_or_more()
          .whitespace_char()
          .char(":")
      )

      _comment = Pattern().char("#")

      robots = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_comment)
          .use(_directive)
          .end()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
          .ignore_case()
      )

   **Emits** ``^\s*(?:\#|(?:user\-agent|disallow|allow|sitemap|crawl\-delay|host)\s*:).*$``

.. py:data:: edify.library.sitemap

   Callable :class:`Pattern` for an XML sitemap: a ``<urlset`` or
   ``<sitemapindex`` root carrying the sitemap schema namespace.

   Full description: :doc:`Sitemap <../../library/web/sitemap>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _declaration = Pattern().string("<?xml").zero_or_more().any_char()

      sitemap = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .optional()
          .use(_declaration)
          .char("<")
          .any_of()
          .string("urlset")
          .string("sitemapindex")
          .end()
          .zero_or_more()
          .any_char()
          .string("http://www.sitemaps.org/schemas/sitemap/")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:<\?xml.*)?<(?:urlset|sitemapindex).*http://www\.sitemaps\.org/schemas/sitemap/.*$``

.. py:data:: edify.library.useragent

   Callable :class:`Pattern` for a permissive User-Agent string.

   Full description: :doc:`User-Agent <../../library/web/useragent>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      useragent = (
          Pattern()
          .start_of_input()
          .between(4, 1024)
          .any_of()
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .char("/")
          .char(".")
          .char("-")
          .char("(")
          .char(")")
          .char(" ")
          .char(";")
          .char("+")
          .char("_")
          .char(",")
          .char(":")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Za-z0-9/\.\-\(\) ;\+_,:]{4,1024}$``

