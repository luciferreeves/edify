"""``uuid_v4`` — version-4 UUID shape."""

from __future__ import annotations

from edify import Pattern
from edify.atoms.hex_nibble import hex_nibble

uuid_v4 = (
    Pattern()
    .exactly(8)
    .use(hex_nibble)
    .char("-")
    .exactly(4)
    .use(hex_nibble)
    .char("-")
    .char("4")
    .exactly(3)
    .use(hex_nibble)
    .char("-")
    .any_of_chars("89ab")
    .exactly(3)
    .use(hex_nibble)
    .char("-")
    .exactly(12)
    .use(hex_nibble)
)
"""Composable :class:`Pattern` fragment for a version-4 UUID."""
