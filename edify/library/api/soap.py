"""``soap`` — SOAP envelope document shape."""

from __future__ import annotations

from edify import Pattern

_declaration = Pattern().string("<?xml").zero_or_more().any_char()

_prefix = Pattern().one_or_more().any_of().alphanumeric().any_of_chars("-_").end().char(":")

soap = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .optional()
    .use(_declaration)
    .char("<")
    .optional()
    .use(_prefix)
    .string("Envelope")
    .zero_or_more()
    .any_char()
    .string("http://schemas.xmlsoap.org/soap/envelope/")
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a SOAP 1.1 message: an ``Envelope`` root
element carrying the SOAP envelope namespace.
"""
