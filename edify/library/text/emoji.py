"""``emoji`` — Unicode-emoji run shape."""

from __future__ import annotations

from edify import Pattern

emoji = (
    Pattern()
    .start_of_input()
    .one_or_more()
    .any_of()
    .range("\U0001f300", "\U0001faff")
    .range("☀", "➿")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a run of one or more emoji characters."""
