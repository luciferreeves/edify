"""``readme`` — README file name shape."""

from __future__ import annotations

from edify import Pattern

readme = (
    Pattern()
    .start_of_input()
    .string("readme")
    .optional()
    .group()
    .char(".")
    .any_of()
    .string("md")
    .string("markdown")
    .string("rst")
    .string("txt")
    .string("adoc")
    .string("org")
    .end()
    .end()
    .end_of_input()
    .ignore_case()
)
"""Callable :class:`Pattern` for a README file name, with or without a common
documentation extension.
"""
