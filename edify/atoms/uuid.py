"""``uuid`` — version-4 UUID shape."""

from __future__ import annotations

from edify import Pattern
from edify.atoms.nibble import nibble

uuid = (
    Pattern()
    .exactly(8)
    .use(nibble)
    .char("-")
    .exactly(4)
    .use(nibble)
    .char("-")
    .char("4")
    .exactly(3)
    .use(nibble)
    .char("-")
    .any_of_chars("89ab")
    .exactly(3)
    .use(nibble)
    .char("-")
    .exactly(12)
    .use(nibble)
)
"""Composable :class:`Pattern` fragment for a version-4 UUID."""
