"""Phone-number shape validator.

Validates a permissive international phone-number shape (with optional
``+`` prefix, optional country code, parenthesised area code, and various
separators) plus a short-number fallback for 4-digit service codes.
Shape-only — does not verify dialability.
"""

from __future__ import annotations

import re

_PHONE_PATTERN = re.compile(
    r"^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
)
_SHORT_NUMBER_PATTERN = re.compile(r"^\d{2,4}")


def phone_number(value: str) -> bool:
    """Return True when ``value`` matches the international or short-number shape.

    Args:
        value: The string to check.

    Returns:
        True for permissive international phone shapes and 4-digit service
        numbers; False otherwise.
    """
    matched_international = _PHONE_PATTERN.match(value) is not None
    matched_short_number = _SHORT_NUMBER_PATTERN.match(value) is not None
    return matched_international or matched_short_number
