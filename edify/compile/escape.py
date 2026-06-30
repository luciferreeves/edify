"""Escape user-provided string fragments for safe insertion into a regex pattern.

Single-purpose wrapper around :func:`re.escape` so the builder never embeds
user input directly into a compiled pattern.
"""

from __future__ import annotations

import re


def escape_special(value: str) -> str:
    """Return ``value`` with all regex metacharacters backslash-escaped.

    Args:
        value: A literal fragment supplied by the user.

    Returns:
        The fragment with every regex metacharacter escaped, safe to embed
        directly into a compiled pattern.
    """
    return re.escape(value)
