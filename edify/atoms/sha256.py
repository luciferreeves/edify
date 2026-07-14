"""``sha256`` — 64-character hexadecimal SHA-256 digest."""

from __future__ import annotations

from edify import Pattern
from edify.atoms.nibble import nibble

sha256 = Pattern().exactly(64).use(nibble)
"""Composable :class:`Pattern` fragment for a SHA-256 hex digest."""
