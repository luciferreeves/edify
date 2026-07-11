"""``unicode`` — Unicode string free of control codes."""

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


unicode = Pattern().start_of_input().one_or_more().subexpression(_not_ctrl()).end_of_input()
"""Callable :class:`Pattern` for any Unicode string containing no control codes."""
