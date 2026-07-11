"""``emoji`` — one-or-more emoji-character shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

emoji = RegexBackedPattern(r"^[\U0001F300-\U0001FAFF☀-➿]+$")
"""Callable :class:`Pattern` for a run of one or more emoji characters."""
