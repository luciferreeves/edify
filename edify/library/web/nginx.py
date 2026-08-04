"""``nginx`` — web-server configuration shape."""

from __future__ import annotations

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
"""Callable :class:`Pattern` for a web-server configuration: a comment, a
``server``/``http``/``location`` block, or a top-level directive.
"""
