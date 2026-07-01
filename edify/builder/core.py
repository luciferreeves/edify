"""Shared immutable-state plumbing for :class:`RegexBuilder` and :class:`Pattern`.

Both fluent surfaces carry the same :class:`BuilderState` and use the same
clone-and-replace pattern for chain methods. :class:`BuilderCore` provides
the state attribute, the constructor, the ``_with_state`` helper that
mixins call to produce new instances, and the interactive ``__repr__``
that shows the pattern-so-far.
"""

from __future__ import annotations

from typing import Self

from edify.builder.types.state import BuilderState
from edify.errors.structure import CannotCallSubexpressionError

_UNCLOSED_FRAME_MARKER = "<unclosed>"


class BuilderCore:
    """Holds the immutable :class:`BuilderState` and clones it on chain steps."""

    _state: BuilderState

    def __init__(self) -> None:
        self._state = BuilderState()

    def _with_state(self, new_state: BuilderState) -> Self:
        """Return a fresh instance of the same concrete type carrying ``new_state``."""
        concrete_class = type(self)
        new_instance = concrete_class.__new__(concrete_class)
        new_instance._state = new_state
        return new_instance

    def __repr__(self) -> str:
        """Return ``<ClassName 'pattern-so-far'>`` for interactive display."""
        rendered = _render_or_marker(self)
        return f"<{type(self).__name__} {rendered!r}>"


def _render_or_marker(builder: BuilderCore) -> str:
    """Return the emitted regex string, or a placeholder when frames are unclosed."""
    to_regex_string = getattr(builder, "to_regex_string", None)
    if to_regex_string is None:
        return _UNCLOSED_FRAME_MARKER
    try:
        return to_regex_string()
    except CannotCallSubexpressionError:
        return _UNCLOSED_FRAME_MARKER
