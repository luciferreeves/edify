"""``hexnum`` — hexadecimal integer literal (``0x`` or ``0X`` prefix)."""

from __future__ import annotations

from edify import Pattern
from edify.atoms.nibble import nibble

hexnum = Pattern().char("0").any_of_chars("xX").one_or_more().use(nibble)
"""Composable :class:`Pattern` fragment for a ``0xNN``-shaped hexadecimal literal."""
