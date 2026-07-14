"""``printable`` — a single printable ASCII character (``0x20``-``0x7E``)."""

from __future__ import annotations

from edify import Pattern

printable = Pattern().range("\x20", "\x7e")
"""Composable :class:`Pattern` fragment for one printable-ASCII character."""
