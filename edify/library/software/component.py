"""``component`` — versioned software-component identifier (``name@version``)."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
component = RegexBackedPattern(
    r"^(?:@[a-z0-9][a-z0-9-]*/)?[a-z0-9][a-z0-9._-]{0,213}"
    r"@\d+(?:\.\d+){0,3}(?:[-.+][a-zA-Z0-9.\-]+)?$"
)
"""Callable :class:`Pattern` for a versioned component identifier ``name@version``."""
