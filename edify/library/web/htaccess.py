"""``htaccess`` — per-directory Apache override shape."""

from __future__ import annotations

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
"""Callable :class:`Pattern` for a per-directory Apache override: a comment, an
``<IfModule>``-style section, or a rewrite/access directive.
"""
