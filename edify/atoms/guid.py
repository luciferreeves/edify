"""``guid`` — any-version UUID/GUID (8-4-4-4-12 hex)."""

from __future__ import annotations

from edify import Pattern
from edify.atoms.nibble import nibble

guid = (
    Pattern()
    .exactly(8)
    .use(nibble)
    .char("-")
    .exactly(4)
    .use(nibble)
    .char("-")
    .exactly(4)
    .use(nibble)
    .char("-")
    .exactly(4)
    .use(nibble)
    .char("-")
    .exactly(12)
    .use(nibble)
)
"""Composable :class:`Pattern` fragment for an any-version UUID/GUID."""
