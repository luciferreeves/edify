"""``extension`` — a file extension (``.ext``, alphanumeric)."""

from __future__ import annotations

from edify import Pattern

extension = Pattern().char(".").one_or_more().alphanumeric()
"""Composable :class:`Pattern` fragment for a file extension."""
