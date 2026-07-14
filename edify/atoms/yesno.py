"""``yesno`` — ``yes``/``no`` boolean value in common English forms."""

from __future__ import annotations

from edify import Pattern, any_of

yesno = any_of(
    Pattern().string("yes"),
    Pattern().string("no"),
    Pattern().string("Yes"),
    Pattern().string("No"),
    Pattern().string("YES"),
    Pattern().string("NO"),
    Pattern().string("y"),
    Pattern().string("n"),
    Pattern().string("Y"),
    Pattern().string("N"),
)
"""Composable :class:`Pattern` fragment for a yes/no boolean."""
