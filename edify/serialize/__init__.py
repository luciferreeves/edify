"""Canonical dict/JSON serialization for :class:`edify.Pattern`.

The wire format is versioned under the ``"edify"`` key and uses public,
stable ``kind`` strings for every AST element. See :data:`SCHEMA_VERSION`
for the current experimental version.
"""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

from edify.serialize.dump import state_to_dict
from edify.serialize.load import dict_to_pattern
from edify.serialize.version import SCHEMA_VERSION

if TYPE_CHECKING:
    from edify.pattern.composition import Pattern

__all__ = [
    "SCHEMA_VERSION",
    "pattern_from_dict",
    "pattern_from_json",
    "pattern_to_dict",
    "pattern_to_json",
]


def pattern_to_dict(pattern: Pattern) -> dict[str, Any]:
    """Return the canonical dict for ``pattern`` (with schema version header)."""
    return state_to_dict(pattern._state)


def pattern_from_dict(document: dict[str, Any]) -> Pattern:
    """Reconstruct a :class:`Pattern` from a canonical dict."""
    return dict_to_pattern(document)


def pattern_to_json(pattern: Pattern) -> str:
    """Return the canonical JSON string for ``pattern`` (compact, sorted keys)."""
    return json.dumps(pattern_to_dict(pattern), sort_keys=True, separators=(",", ":"))


def pattern_from_json(blob: str) -> Pattern:
    """Reconstruct a :class:`Pattern` from a canonical JSON string."""
    return pattern_from_dict(json.loads(blob))
