"""``braces`` — a curly-brace group with no nested braces."""

from __future__ import annotations

from edify import Pattern

braces = Pattern().char("{").zero_or_more().anything_but_chars("}").char("}")
"""Composable :class:`Pattern` fragment for a ``{...}`` group."""
