"""Helper to freeze a :class:`RegexBuilder` chain into an exported :class:`Pattern`.

The library validators build their regex via ``RegexBuilder()`` chains at
import time and expose the result at module level as a :class:`Pattern`
instance so ``isinstance(uuid, Pattern) is True`` and ``uuid(value)`` works.
This helper copies the immutable builder state into a fresh :class:`Pattern`
instance without recompiling or reparsing the emitted regex.
"""

from __future__ import annotations

from edify.builder.core import BuilderCore
from edify.pattern.composition import Pattern


def as_pattern(builder: BuilderCore) -> Pattern:
    """Return a fresh :class:`Pattern` carrying ``builder``'s immutable state."""
    pattern_instance = Pattern()
    pattern_instance._state = builder._state
    return pattern_instance