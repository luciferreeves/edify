"""``captcha`` — CAPTCHA verification token shape."""

from __future__ import annotations

from edify import Pattern

captcha = (
    Pattern()
    .start_of_input()
    .between(20, 2048)
    .any_of()
    .alphanumeric()
    .any_of_chars("-_")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a CAPTCHA verification token: a long
URL-safe base64 response string.
"""
