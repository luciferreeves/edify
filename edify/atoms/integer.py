"""``integer`` — signed decimal integer."""

from __future__ import annotations

from edify import Pattern

integer = Pattern().optional().any_of_chars("+-").one_or_more().digit()
"""Composable :class:`Pattern` fragment for a signed decimal integer."""
