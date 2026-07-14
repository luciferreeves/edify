"""``truefalse`` — ``true``/``false`` boolean value in common English forms."""

from __future__ import annotations

from edify import Pattern, any_of

truefalse = any_of(
    Pattern().string("true"),
    Pattern().string("false"),
    Pattern().string("True"),
    Pattern().string("False"),
    Pattern().string("TRUE"),
    Pattern().string("FALSE"),
)
"""Composable :class:`Pattern` fragment for a true/false boolean."""
