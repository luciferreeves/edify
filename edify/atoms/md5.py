"""``md5`` — 32-character hexadecimal MD5 digest."""

from __future__ import annotations

from edify import Pattern
from edify.atoms.nibble import nibble

md5 = Pattern().exactly(32).use(nibble)
"""Composable :class:`Pattern` fragment for an MD5 hex digest."""
