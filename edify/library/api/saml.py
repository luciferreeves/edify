"""``saml`` — SAML 2.0 protocol message shape."""

from __future__ import annotations

from edify import Pattern

_declaration = Pattern().string("<?xml").zero_or_more().any_char()

_prefix = Pattern().one_or_more().any_of().alphanumeric().any_of_chars("-_").end().char(":")

_element = (
    Pattern()
    .char("<")
    .optional()
    .use(_prefix)
    .any_of()
    .string("Response")
    .string("AuthnRequest")
    .string("LogoutRequest")
    .string("LogoutResponse")
    .string("Assertion")
    .string("EntityDescriptor")
    .end()
    .zero_or_more()
    .any_char()
    .string("urn:oasis:names:tc:SAML:2.0:")
)

saml = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .optional()
    .use(_declaration)
    .use(_element)
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a SAML 2.0 message: a protocol or assertion
element carrying a ``urn:oasis:names:tc:SAML:2.0:`` namespace.
"""
