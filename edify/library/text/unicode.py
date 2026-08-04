"""``unicode`` — string carrying at least one non-ASCII character."""

from __future__ import annotations

from edify import Pattern


def _not_ctrl() -> Pattern:
    return (
        Pattern()
        .assert_not_ahead()
        .any_of()
        .range("\x00", "\x1f")
        .char("\x7f")
        .end()
        .end()
        .any_char()
    )


_non_ascii = Pattern().range("\x80", "\U0010ffff")

unicode = (
    Pattern()
    .start_of_input()
    .assert_ahead()
    .zero_or_more()
    .subexpression(_not_ctrl())
    .use(_non_ascii)
    .end()
    .one_or_more()
    .subexpression(_not_ctrl())
    .end_of_input()
)
"""Callable :class:`Pattern` for a string that uses characters beyond ASCII and
contains no control codes.
"""
