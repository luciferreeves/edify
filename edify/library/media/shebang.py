"""``shebang`` — script shebang line shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

shebang = RegexBackedPattern(r"^#!/(?:usr/)?(?:bin|sbin|local)/(?:env\s+)?[a-zA-Z0-9._+/-]+$")
"""Callable :class:`Pattern` for a shebang line at the top of a script."""
