Web
===

Every validator in the :doc:`web <../../library/web/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/web/index>`.

.. py:function:: edify.library.apache(value: str) -> bool

   Apache. See :doc:`../../library/web/apache` for the full description.

   Emits ``^\s*(?:\#|<(?:VirtualHost|Directory|Location|Files|IfModule|Limit|Proxy)|(?:ServerName|ServerRoot|ServerAdmin|DocumentRoot|Listen|LoadModule|ErrorLog|CustomLog|Include)\s+).*$``

.. py:function:: edify.library.captcha(value: str) -> bool

   CAPTCHA. See :doc:`../../library/web/captcha` for the full description.

   Emits ``^(?:[a-zA-Z0-9]|[-_]){20,2048}$``

.. py:function:: edify.library.cookie(value: str) -> bool

   Cookie. See :doc:`../../library/web/cookie` for the full description.

   Emits ``^[a-zA-Z0-9_\-]+=(?:(?!(?:\s|[;])).)+$``

.. py:function:: edify.library.csp(value: str) -> bool

   CSP. See :doc:`../../library/web/csp` for the full description.

   Emits ``^[a-z\-]+\s+(?:(?!;).)+(?:;\s*[a-z\-]+\s+(?:(?!;).)+)*;?$``

.. py:function:: edify.library.htaccess(value: str) -> bool

   htaccess. See :doc:`../../library/web/htaccess` for the full description.

   Emits ``^\s*(?:\#|<(?:IfModule|Files|FilesMatch|Limit|RequireAll)|(?:RewriteEngine|RewriteRule|RewriteCond|RewriteBase|Redirect|RedirectMatch|Options|AddType|AddHandler|ErrorDocument|Header|Require|Order|Deny|Allow|AuthType|DirectoryIndex)\s+).*$``

.. py:function:: edify.library.humans(value: str) -> bool

   humans.txt. See :doc:`../../library/web/humans` for the full description.

   Emits ``^\s*(?:\#|/\*(?:[a-zA-Z0-9]|[ \-_])*\*/|(?:[a-zA-Z0-9]|[ \-_])+:\s*).*$``

.. py:function:: edify.library.manifest(value: str) -> bool

   Manifest. See :doc:`../../library/web/manifest` for the full description.

   Emits ``^\s*\{.*"(?:start_url|display|icons|short_name|theme_color)"\s*:.*\}\s*$``

.. py:function:: edify.library.nginx(value: str) -> bool

   nginx. See :doc:`../../library/web/nginx` for the full description.

   Emits ``^\s*(?:\#|(?:http|server|events|location|upstream|stream|map).*\{|(?:worker_processes|worker_connections|include|user|pid|error_log|access_log)\s+).*$``

.. py:function:: edify.library.robots(value: str) -> bool

   Robots. See :doc:`../../library/web/robots` for the full description.

   Emits ``^\s*(?:\#|(?:user\-agent|disallow|allow|sitemap|crawl\-delay|host)\s*:).*$``

.. py:function:: edify.library.sitemap(value: str) -> bool

   Sitemap. See :doc:`../../library/web/sitemap` for the full description.

   Emits ``^\s*(?:<\?xml.*)?<(?:urlset|sitemapindex).*http://www\.sitemaps\.org/schemas/sitemap/.*$``

.. py:function:: edify.library.useragent(value: str) -> bool

   User-Agent. See :doc:`../../library/web/useragent` for the full description.

   Emits ``^[A-Za-z0-9/\.\-\(\) ;\+_,:]{4,1024}$``

