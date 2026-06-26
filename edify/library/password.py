"""Password-strength validator.

Validates that a string meets all four configurable thresholds: length
window, minimum uppercase count, minimum lowercase count, minimum digit
count, and minimum special-character count. The special-character set is
itself configurable. Shape and class-count only — does not check entropy,
breach databases, or anything beyond what's spelled out in the signature.
"""

from __future__ import annotations

import re

_UPPERCASE_PATTERN = re.compile("[A-Z]")
_LOWERCASE_PATTERN = re.compile("[a-z]")
_DIGIT_PATTERN = re.compile("[0-9]")
_DEFAULT_SPECIAL_CHARS = "!@#$%^&*()_+-=[]{}|;':\",./<>?"


def password(
    password: str,
    min_length: int = 8,
    max_length: int = 64,
    min_upper: int = 1,
    min_lower: int = 1,
    min_digit: int = 1,
    min_special: int = 1,
    special_chars: str = _DEFAULT_SPECIAL_CHARS,
) -> bool:
    """Return True when ``password`` meets every configured strength threshold.

    Args:
        password: The candidate password to check.
        min_length: Minimum allowed length (inclusive).
        max_length: Maximum allowed length (inclusive).
        min_upper: Minimum number of uppercase letters required.
        min_lower: Minimum number of lowercase letters required.
        min_digit: Minimum number of decimal digits required.
        min_special: Minimum number of special characters required.
        special_chars: The set of characters counted toward ``min_special``.

    Returns:
        True when every threshold is satisfied; False as soon as one fails.
    """
    return (
        _length_in_range(password, min_length, max_length)
        and _meets_threshold(password, _UPPERCASE_PATTERN, min_upper)
        and _meets_threshold(password, _LOWERCASE_PATTERN, min_lower)
        and _meets_threshold(password, _DIGIT_PATTERN, min_digit)
        and _meets_special_threshold(password, special_chars, min_special)
    )


def _length_in_range(value: str, min_length: int, max_length: int) -> bool:
    """Return True when ``len(value)`` is within the inclusive length window."""
    value_length = len(value)
    return min_length <= value_length <= max_length


def _meets_threshold(value: str, character_pattern: re.Pattern[str], required_count: int) -> bool:
    """Return True when ``value`` has at least ``required_count`` ``character_pattern`` matches."""
    matches = character_pattern.findall(value)
    return len(matches) >= required_count


def _meets_special_threshold(value: str, special_chars: str, required_count: int) -> bool:
    """Return True when ``value`` contains at least ``required_count`` special characters."""
    special_match_count = sum(1 for character in value if character in special_chars)
    return special_match_count >= required_count
