"""``tex`` — LaTeX / TeX source shape."""

from __future__ import annotations

from edify import Pattern

tex = (
    Pattern()
    .start_of_input()
    .string("\\documentclass")
    .optional()
    .group()
    .char("[")
    .zero_or_more()
    .anything_but_chars("]")
    .char("]")
    .end()
    .char("{")
    .one_or_more()
    .anything_but_chars("}")
    .char("}")
    .zero_or_more()
    .any_char()
    .end_of_input()
)
"""Callable :class:`Pattern` for a LaTeX document source (``\\documentclass`` prefix)."""
