"""``httpstatus`` — three-digit HTTP status code (1xx-5xx)."""

from __future__ import annotations

from edify import Pattern

httpstatus = Pattern().range("1", "5").exactly(2).digit()
"""Composable :class:`Pattern` fragment for a three-digit HTTP status code."""
