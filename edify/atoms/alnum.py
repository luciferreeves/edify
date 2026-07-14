"""``alnum`` — a single alphanumeric ASCII character."""

from __future__ import annotations

from edify import Pattern

alnum = Pattern().alphanumeric()
"""Composable :class:`Pattern` fragment for one alphanumeric char ``[a-zA-Z0-9]``."""
