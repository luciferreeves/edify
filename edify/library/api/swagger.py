"""``swagger`` — Swagger 2.0 specification document shape."""

from __future__ import annotations

from edify import Pattern

_yaml_form = (
    Pattern()
    .string("swagger")
    .zero_or_more()
    .whitespace_char()
    .char(":")
    .zero_or_more()
    .whitespace_char()
    .optional()
    .any_of_chars("\"'")
    .string("2.0")
)

_json_form = (
    Pattern()
    .char("{")
    .zero_or_more()
    .any_char()
    .char('"')
    .string("swagger")
    .char('"')
    .zero_or_more()
    .whitespace_char()
    .char(":")
    .zero_or_more()
    .whitespace_char()
    .char('"')
    .string("2.0")
)

swagger = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .any_of()
    .use(_json_form)
    .use(_yaml_form)
    .end()
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a Swagger 2.0 document: a ``swagger: "2.0"``
declaration in YAML or JSON form.
"""
