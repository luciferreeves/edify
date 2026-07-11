"""``otp`` — one-time password shape (6-8 digits or 6-8 alphanumerics)."""

from __future__ import annotations

from edify import Pattern, any_of

otp = any_of(
    Pattern().start_of_input().between(6, 8).digit().end_of_input(),
    Pattern()
    .start_of_input()
    .between(6, 8)
    .any_of()
    .range("A", "Z")
    .range("0", "9")
    .end()
    .end_of_input(),
)
"""Callable :class:`Pattern` for the one-time-password shape: 6-8 digits or
6-8 uppercase-alphanumerics.
"""
