"""Validate the shape of a named-capture-group identifier.

Named groups (``(?P<name>...)``) accept identifier-style names: letters,
digits, and underscores, starting with a letter. This module owns that
single check.
"""

from __future__ import annotations

import re

_NAMED_GROUP_PATTERN = re.compile(r"^[a-z]+\w*$", re.IGNORECASE)


def is_valid_group_name(name: str) -> bool:
    """Return True when ``name`` is a syntactically valid named-group identifier.

    Args:
        name: The candidate name to check.

    Returns:
        True if ``name`` matches ``^[a-z]+\\w*$`` case-insensitively, False otherwise.
    """
    match_result = _NAMED_GROUP_PATTERN.match(name)
    return match_result is not None
