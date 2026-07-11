"""``postal`` — postal / ZIP code shape (accepts any known locale)."""

from __future__ import annotations

import re

from edify.library._support.regex import RegexBackedPattern
from edify.library._support.zip import ZIP_LOCALES

_alternatives: list[str] = []
for _entry in ZIP_LOCALES:
    _raw = _entry.get("zip")
    if not _raw:
        continue
    _stripped = _raw.strip("^$")
    _alternatives.append(f"(?:{_stripped})")

postal = RegexBackedPattern(rf"^(?:{'|'.join(_alternatives)})$")
"""Callable :class:`Pattern` that accepts any known postal/ZIP shape by locale."""

del re, _alternatives, _entry, _raw, _stripped
