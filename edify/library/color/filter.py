"""``filter`` — CSS filter function shape."""

from __future__ import annotations

from edify import Pattern

filter = (
    Pattern()
    .start_of_input()
    .any_of(
        "blur",
        "brightness",
        "contrast",
        "grayscale",
        "hue-rotate",
        "invert",
        "opacity",
        "saturate",
        "sepia",
        "drop-shadow",
    )
    .char("(")
    .one_or_more()
    .anything_but_chars(")")
    .char(")")
    .end_of_input()
)
"""Callable :class:`Pattern` for a CSS filter function call."""
