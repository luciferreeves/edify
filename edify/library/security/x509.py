"""``x509`` — X.509 certificate shape in either encoding."""

from __future__ import annotations

from edify import Pattern

_body = Pattern().zero_or_more().any_of().alphanumeric().any_of_chars("+/=").whitespace_char().end()

_armoured = (
    Pattern()
    .zero_or_more()
    .whitespace_char()
    .string("-----BEGIN ")
    .optional()
    .string("TRUSTED ")
    .string("CERTIFICATE-----")
    .use(_body)
    .string("-----END ")
    .optional()
    .string("TRUSTED ")
    .string("CERTIFICATE-----")
    .zero_or_more()
    .whitespace_char()
)

_binary = Pattern().char("\x30").range("\x80", "\x84").zero_or_more().any_char()

x509 = (
    Pattern().start_of_input().any_of().use(_armoured).use(_binary).end().end_of_input().dot_all()
)
"""Callable :class:`Pattern` for an X.509 certificate: a PEM ``CERTIFICATE``
block or a DER ``SEQUENCE`` payload.
"""
