nginx
=====

An `nginx <https://nginx.org/en/docs/beginners_guide.html>`__ configuration is built
from directives and brace-delimited blocks. **Nginx** recognises the three ways such
a file opens: a block keyword, a top-level directive, or a ``#`` comment.

Those are the branches of an :func:`~edify.any_of`. The block branch is a context
name — ``http``, ``server``, ``events``, ``location``, ``upstream``, ``stream``,
``map`` — followed by anything and then ``{``. The directive branch is a known
top-level setting followed by whitespace.

Blocks
------

.. edify-playground::

   from edify.library import nginx

   nginx("server {\n  listen 80;\n  server_name example.com;\n}")
   nginx("http {\n  include mime.types;\n}")
   nginx("events {\n  worker_connections 1024;\n}")
   nginx("location /api {\n  proxy_pass http://backend;\n}")

Directives and comments
-----------------------

.. edify-playground::

   from edify.library import nginx

   nginx("worker_processes 4;")
   nginx("user www-data;")
   nginx("# a comment\nserver {}")

Not a configuration
-------------------

.. edify-playground::

   from edify.library import nginx

   nginx("server {}")    # a block
   nginx("hello-world")  # plain text
   nginx('{"a": 1}')     # JSON, not a directive
   nginx("")             # empty

This matches how a file opens, not that the whole configuration is valid — brace
balance, directive arguments, and context nesting all need ``nginx -t``. For the
other server see :doc:`apache`.
