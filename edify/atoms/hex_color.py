"""``hex_color`` — CSS hex-colour shape (``#RGB``, ``#RGBA``, ``#RRGGBB``, ``#RRGGBBAA``)."""

from __future__ import annotations

from edify import Pattern
from edify.atoms.hex_nibble import hex_nibble

hex_color = (
    Pattern()
    .char("#")
    .any_of()
    .exactly(8)
    .use(hex_nibble)
    .exactly(6)
    .use(hex_nibble)
    .exactly(4)
    .use(hex_nibble)
    .exactly(3)
    .use(hex_nibble)
    .end()
)
"""Composable :class:`Pattern` fragment for a CSS hex colour."""
