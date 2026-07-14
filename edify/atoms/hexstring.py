"""``hexstring`` — one or more hexadecimal characters."""

from __future__ import annotations

from edify import Pattern
from edify.atoms.nibble import nibble

hexstring = Pattern().one_or_more().use(nibble)
"""Composable :class:`Pattern` fragment for a hex character string."""
