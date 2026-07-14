"""``filename`` — a filename with no path separators or reserved characters."""

from __future__ import annotations

from edify import Pattern

filename = Pattern().one_or_more().anything_but_chars('/\\<>:"|?*\x00')
"""Composable :class:`Pattern` fragment for a filename with no path separators."""
