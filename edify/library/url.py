"""URL-shape validator.

Validates that a string matches a URL shape — either with a protocol prefix
(``https://...``) or without (``example.com/path``). The caller can restrict
which forms are accepted via the ``match`` argument. Shape-only: does not
verify resolvability or RFC-correctness.
"""

from __future__ import annotations

import re

_PROTOCOL_PATTERN = re.compile(
    r"^https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\."
    r"[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)$"
)
_NO_PROTOCOL_PATTERN = re.compile(
    r"^[-a-zA-Z0-9@:%._\+~#=]{1,256}\."
    r"[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)$"
)
_PROTOCOL_MODE = "proto"
_NO_PROTOCOL_MODE = "no_proto"
_DEFAULT_MATCH_MODES = (_PROTOCOL_MODE, _NO_PROTOCOL_MODE)


def url(value: str, match: list[str] | tuple[str, ...] | None = None) -> bool:
    """Return True when ``value`` matches one of the requested URL shapes.

    Args:
        value: The string to check.
        match: Sequence of mode strings naming which URL shapes to accept.
            Use ``"proto"`` for the ``https?://...`` shape and ``"no_proto"``
            for the bare ``example.com/...`` shape. Defaults to accepting both.

    Returns:
        True when ``value`` matches any of the requested mode patterns.

    Raises:
        TypeError: When ``match`` is not a list or tuple.
        ValueError: When ``match`` is empty or contains an unrecognised mode.
    """
    selected_modes = match if match is not None else _DEFAULT_MATCH_MODES
    _ensure_match_is_sequence(selected_modes)
    _ensure_match_non_empty(selected_modes)
    patterns = _patterns_for_modes(selected_modes)
    return _matches_any(value, patterns)


def _ensure_match_is_sequence(match: object) -> None:
    """Raise :class:`TypeError` when ``match`` is not a list or tuple."""
    if isinstance(match, (list, tuple)):
        return
    actual_type_name = type(match).__name__
    raise TypeError(f"match argument must be a list (got {actual_type_name})")


def _ensure_match_non_empty(match: list[str] | tuple[str, ...]) -> None:
    """Raise :class:`ValueError` when ``match`` is empty."""
    if len(match) > 0:
        return
    raise ValueError("match argument must not be empty")


def _patterns_for_modes(match_modes: list[str] | tuple[str, ...]) -> list[re.Pattern[str]]:
    """Return the compiled patterns named by ``match_modes`` (raises on unknown names)."""
    patterns: list[re.Pattern[str]] = []
    for mode in match_modes:
        if mode == _PROTOCOL_MODE:
            patterns.append(_PROTOCOL_PATTERN)
        elif mode == _NO_PROTOCOL_MODE:
            patterns.append(_NO_PROTOCOL_PATTERN)
        else:
            raise ValueError(f"Invalid protocol: {mode}")
    return patterns


def _matches_any(value: str, patterns: list[re.Pattern[str]]) -> bool:
    """Return True when ``value`` matches at least one of ``patterns``."""
    return any(pattern.match(value) is not None for pattern in patterns)
