"""``hex_nibble`` — one hexadecimal nibble ``[0-9a-fA-F]``."""

from __future__ import annotations

from edify import Pattern

hex_nibble = Pattern().any_of().range("0", "9").range("a", "f").range("A", "F").end()
"""Composable :class:`Pattern` fragment for one mixed-case hex nibble."""
