"""``scientific`` — scientific-notation number shape."""

from __future__ import annotations

from edify import Pattern

scientific = (
    Pattern()
    .start_of_input()
    .optional()
    .any_of_chars("+-")
    .one_or_more()
    .digit()
    .optional()
    .group()
    .char(".")
    .one_or_more()
    .digit()
    .end()
    .any_of_chars("eE")
    .optional()
    .any_of_chars("+-")
    .one_or_more()
    .digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for scientific-notation shape."""
