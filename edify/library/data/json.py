"""``json`` — JSON document shape."""

from __future__ import annotations

from edify import Pattern

_number = (
    Pattern()
    .optional()
    .char("-")
    .one_or_more()
    .digit()
    .optional()
    .group()
    .char(".")
    .one_or_more()
    .digit()
    .end()
    .optional()
    .group()
    .any_of_chars("eE")
    .optional()
    .any_of_chars("+-")
    .one_or_more()
    .digit()
    .end()
)

_object = Pattern().char("{").zero_or_more().any_char().char("}")
_array = Pattern().char("[").zero_or_more().any_char().char("]")
_string = Pattern().char('"').zero_or_more().any_char().char('"')

json = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .any_of()
    .use(_object)
    .use(_array)
    .use(_string)
    .string("true")
    .string("false")
    .string("null")
    .use(_number)
    .end()
    .zero_or_more()
    .whitespace_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a JSON document: an object, array, string,
number, or literal, with optional surrounding whitespace.
"""
