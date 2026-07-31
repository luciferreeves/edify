"""``certificate`` — PEM certificate shape."""

from __future__ import annotations

from edify import Pattern

_label = Pattern().optional().string("TRUSTED ").string("CERTIFICATE")

_body = Pattern().zero_or_more().any_of().alphanumeric().any_of_chars("+/=").whitespace_char().end()

certificate = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .string("-----BEGIN ")
    .use(_label)
    .string("-----")
    .use(_body)
    .string("-----END ")
    .use(_label)
    .string("-----")
    .zero_or_more()
    .whitespace_char()
    .end_of_input()
)
"""Callable :class:`Pattern` for a PEM certificate: a ``CERTIFICATE`` or
``TRUSTED CERTIFICATE`` armoured block.
"""
