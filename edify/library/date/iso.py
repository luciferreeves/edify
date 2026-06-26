"""ISO-8601 date-time shape validator.

Validates the ``YYYY-MM-DDTHH:MM:SS[.frac][Z|±HH:MM]`` shape used by ISO
8601 timestamps. Shape-only — does not verify calendar correctness.
"""

from __future__ import annotations

import re

_ISO_DATE_PATTERN = re.compile(
    r"^(?:\d{4})-(?:\d{2})-(?:\d{2})T(?:\d{2}):(?:\d{2}):"
    r"(?:\d{2}(?:\.\d*)?)(?:(?:-(?:\d{2}):(?:\d{2})|Z)?)$"
)


def iso_date(value: str) -> bool:
    """Return True when ``value`` matches the ISO 8601 date-time shape.

    Args:
        value: The string to check.

    Returns:
        True for valid ISO 8601 date-time strings; False otherwise.
    """
    return _ISO_DATE_PATTERN.match(value) is not None
