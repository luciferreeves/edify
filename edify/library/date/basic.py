"""Basic date-shape validator.

Validates the ``M/D/YYYY`` or ``MM/DD/YYYY`` shape. Shape-only — does not
verify calendar correctness (Feb 30 passes).
"""

from __future__ import annotations

import re

_DATE_PATTERN = re.compile(r"^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$")


def date(value: str) -> bool:
    """Return True when ``value`` matches the slash-separated date shape.

    Args:
        value: The string to check.

    Returns:
        True for valid ``M/D/YYYY`` shapes; False otherwise.
    """
    return _DATE_PATTERN.match(value) is not None
