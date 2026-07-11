"""``ref`` — git ref shape (branch, tag, or SHA)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

ref = RegexBackedPattern(
    r"^(?:"
    r"[a-f0-9]{7,40}"
    r"|refs/(?:heads|tags|remotes)/[^\s~^:?*[\\]+"
    r"|[^\s~^:?*[\\/][^\s~^:?*[\\]{0,127}"
    r")$"
)
"""Callable :class:`Pattern` for a git ref: SHA, ``refs/heads/…``, or bare branch/tag name."""
