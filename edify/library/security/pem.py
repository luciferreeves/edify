"""``pem`` — PEM-armoured artifact shape."""

from __future__ import annotations

from edify import Pattern

_label = Pattern().uppercase().zero_or_more().any_of().uppercase().digit().any_of_chars(" ").end()

_body = Pattern().zero_or_more().any_of().alphanumeric().any_of_chars("+/=").whitespace_char().end()

pem = (
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
"""Callable :class:`Pattern` for a PEM-armoured artifact: a ``-----BEGIN
LABEL-----`` header, a base64 body, and a matching ``-----END LABEL-----``
footer.
"""
