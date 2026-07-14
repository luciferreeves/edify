"""``ascii`` — a single ASCII character (``0x00``-``0x7F``)."""

from __future__ import annotations

from edify import Pattern

ascii = Pattern().range("\x00", "\x7f")
"""Composable :class:`Pattern` fragment for any ASCII code point."""
