"""Pre-built :class:`Pattern` constants for the two word-boundary zero-width assertions."""

from __future__ import annotations

from edify.pattern.composition import Pattern

WORD_BOUNDARY: Pattern = Pattern().word_boundary()
NON_WORD_BOUNDARY: Pattern = Pattern().non_word_boundary()
