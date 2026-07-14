"""``tld`` — top-level domain (2 to 63 letters)."""

from __future__ import annotations

from edify import Pattern

tld = Pattern().between(2, 63).letter()
"""Composable :class:`Pattern` fragment for a top-level domain."""
