"""``hexcolor`` — CSS hex-colour shape (``#RGB``, ``#RGBA``, ``#RRGGBB``, ``#RRGGBBAA``)."""

from __future__ import annotations

from edify import Pattern
from edify.atoms.nibble import nibble

hexcolor = (
    Pattern()
    .char("#")
    .any_of()
    .exactly(8)
    .use(nibble)
    .exactly(6)
    .use(nibble)
    .exactly(4)
    .use(nibble)
    .exactly(3)
    .use(nibble)
    .end()
)
"""Composable :class:`Pattern` fragment for a CSS hex colour."""
