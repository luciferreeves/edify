"""``mac`` — MAC address (six hex pairs separated by ``:`` or ``-``)."""

from __future__ import annotations

from edify import Pattern
from edify.atoms.nibble import nibble

mac = (
    Pattern()
    .exactly(2)
    .use(nibble)
    .exactly(5)
    .group()
    .any_of_chars(":-")
    .exactly(2)
    .use(nibble)
    .end()
)
"""Composable :class:`Pattern` fragment for a MAC address."""
