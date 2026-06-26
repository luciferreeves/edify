"""ZIP / postal-code shape validator.

Validates the postal-code shape for a given country (default ``US``). The
per-locale patterns live in :mod:`edify.library._support.zip`; this
module wires the user-supplied ``locale`` to its pattern and runs the match.
"""

from __future__ import annotations

import re

from edify.library._support.zip import ZIP_LOCALES


def zip(value: str, locale: str = "US") -> bool:
    """Return True when ``value`` matches the postal-code shape for ``locale``.

    Args:
        value: The string to check.
        locale: The two-letter country code whose postal pattern to apply.

    Returns:
        True for valid postal codes in the given locale; False otherwise.

    Raises:
        TypeError: When ``locale`` is not a string.
        ValueError: When ``locale`` is empty or not in the supported set.
    """
    _ensure_is_string(locale)
    _ensure_non_empty(locale)
    pattern = _pattern_for_locale(locale)
    return re.match(pattern, value) is not None


def _ensure_is_string(locale: object) -> None:
    """Raise :class:`TypeError` when ``locale`` is not a string."""
    if isinstance(locale, str):
        return
    actual_type_name = type(locale).__name__
    raise TypeError(f"locale must be a string (got {actual_type_name})")


def _ensure_non_empty(locale: str) -> None:
    """Raise :class:`ValueError` when ``locale`` is the empty string."""
    if locale != "":
        return
    raise ValueError("locale cannot be empty")


def _pattern_for_locale(locale: str) -> str:
    """Return the postal-code regex string for ``locale``.

    Raises :class:`ValueError` when ``locale`` is not in the supported set.
    """
    for locale_entry in ZIP_LOCALES:
        if locale_entry.get("abbrev") == locale and "zip" in locale_entry:
            return locale_entry["zip"]
    supported_abbreviations = [
        locale_entry["abbrev"] for locale_entry in ZIP_LOCALES if "zip" in locale_entry
    ]
    raise ValueError(f"locale must be one of {supported_abbreviations}")
