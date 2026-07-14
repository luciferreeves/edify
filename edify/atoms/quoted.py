"""``quoted`` — a double-quoted string with no embedded quotes."""

from __future__ import annotations

from edify import Pattern

quoted = Pattern().char('"').zero_or_more().anything_but_chars('"').char('"')
"""Composable :class:`Pattern` fragment for a ``"..."`` string."""
