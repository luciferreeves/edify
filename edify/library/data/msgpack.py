"""``msgpack`` — msgpack data-format / file-marker shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

msgpack = RegexBackedPattern(r"^[A-Za-z0-9_.\-/+]{2,256}$")
"""Callable :class:`Pattern` for msgpack data-format identifier or content marker."""
