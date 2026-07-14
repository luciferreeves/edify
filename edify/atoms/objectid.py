"""``objectid`` — 24-character hex ObjectId."""

from __future__ import annotations

from edify import Pattern
from edify.atoms.nibble import nibble

objectid = Pattern().exactly(24).use(nibble)
"""Composable :class:`Pattern` fragment for a 24-hex-character ObjectId."""
