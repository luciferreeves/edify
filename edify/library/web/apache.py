"""``apache`` — Apache server configuration shape."""

from __future__ import annotations

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
"""Callable :class:`Pattern` for an Apache server configuration: a comment, a
``<VirtualHost>``-style section, or a top-level directive.
"""
