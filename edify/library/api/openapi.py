"""``openapi`` — OpenAPI specification document shape."""

from __future__ import annotations

from edify import Pattern

_version = (
    Pattern()
    .char("3")
    .char(".")
    .one_or_more()
    .digit()
    .zero_or_more()
    .any_of()
    .digit()
    .char(".")
    .end()
)

_yaml_form = (
    Pattern()
    .string("openapi")
    .zero_or_more()
    .whitespace_char()
    .char(":")
    .zero_or_more()
    .whitespace_char()
    .optional()
    .any_of_chars("\"'")
    .use(_version)
)

_json_form = (
    Pattern()
    .char("{")
    .zero_or_more()
    .any_char()
    .char('"')
    .string("openapi")
    .char('"')
    .zero_or_more()
    .whitespace_char()
    .char(":")
    .zero_or_more()
    .whitespace_char()
    .char('"')
    .use(_version)
)

openapi = (
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
"""Callable :class:`Pattern` for an OpenAPI 3 document: an ``openapi: 3.x``
declaration in YAML or JSON form.
"""
