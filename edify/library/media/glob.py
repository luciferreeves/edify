"""``glob`` — Unix glob shape (must contain a wildcard)."""

from __future__ import annotations

from edify import Pattern


def _not_ctrl() -> Pattern:
    return Pattern().assert_not_ahead().any_of().range("\x00", "\x1f").end().end().any_char()


glob = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .subexpression(_not_ctrl())
    .any_of_chars("*?[]")
    .zero_or_more()
    .subexpression(_not_ctrl())
    .end_of_input()
)
"""Callable :class:`Pattern` for a Unix glob (must contain at least one wildcard)."""
