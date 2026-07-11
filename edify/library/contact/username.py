"""``username`` — social-handle / login-name shape (3–30 chars alphanumeric + underscore/dot/hyphen)."""

from __future__ import annotations

from edify import Pattern

username = (
    Pattern()
    .start_of_input()
    .any_of().range("a", "z").range("A", "Z").range("0", "9").end()
    .between(2, 29)
    .any_of().range("a", "z").range("A", "Z").range("0", "9").any_of_chars("_.-").end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a permissive username/handle shape:
starts with a letter or digit, 3–30 characters total, remaining characters
alphanumeric plus ``_``, ``.``, or ``-``.
"""
