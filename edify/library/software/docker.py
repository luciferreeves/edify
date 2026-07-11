"""``docker`` — Docker image reference shape."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
docker = RegexBackedPattern(
    r"^(?:(?:[a-z0-9.\-]+(?::\d+)?/)?[a-z0-9]+(?:[._\-][a-z0-9]+)*)"
    r"(?:/[a-z0-9]+(?:[._\-][a-z0-9]+)*)*"
    r"(?::[a-zA-Z0-9_][a-zA-Z0-9._\-]{0,127})?"
    r"(?:@sha256:[a-f0-9]{64})?$"
)
"""Callable :class:`Pattern` for a Docker image reference."""
