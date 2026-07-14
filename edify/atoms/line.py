"""``line`` — one non-empty line of text (no CR/LF)."""

from __future__ import annotations

from edify import Pattern

line = Pattern().one_or_more().anything_but_chars("\r\n")
"""Composable :class:`Pattern` fragment for one line of text."""
