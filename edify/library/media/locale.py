"""``locale`` — POSIX/BCP-47 locale-tag shape."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
locale = RegexBackedPattern(r"^[a-z]{2,3}(?:[_-][A-Z]{2})?(?:\.[a-zA-Z0-9-]+)?(?:@[a-zA-Z0-9]+)?$")
"""Callable :class:`Pattern` for a POSIX/BCP-47 locale tag (``en``, ``en_US``, ``en-US.UTF-8``)."""
