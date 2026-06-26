"""GUID-shape validator.

Validates the Microsoft-flavoured GUID form: the 8-4-4-4-12 hex shape,
optionally wrapped in braces, with either case.
"""

from __future__ import annotations

import re

_GUID_PATTERN = re.compile(
    r"^(?:\{?(?:[0-9a-fA-F]){8}-(?:[0-9a-fA-F]){4}-"
    r"(?:[0-9a-fA-F]){4}-(?:[0-9a-fA-F]){4}-(?:[0-9a-fA-F]){12}\}?)$"
)


def guid(value: str) -> bool:
    """Return True when ``value`` matches the Microsoft-flavoured GUID shape.

    Args:
        value: The string to check.

    Returns:
        True for valid braced or bare 8-4-4-4-12 hex strings (either case);
        False otherwise.
    """
    return _GUID_PATTERN.match(value) is not None
