"""``git`` — 40-character git SHA-1 hash shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

git = RegexBackedPattern(r"^[a-f0-9]{7,40}$")
"""Callable :class:`Pattern` for a git commit SHA (7-40 hex characters)."""
