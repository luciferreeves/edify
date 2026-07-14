"""``signed`` — decimal integer with a required leading sign."""

from __future__ import annotations

from edify import Pattern

signed = Pattern().any_of_chars("+-").one_or_more().digit()
"""Composable :class:`Pattern` fragment for a signed integer with the sign required."""
