"""Shared immutable-state plumbing for :class:`RegexBuilder` and :class:`Pattern`.

Both fluent surfaces carry the same :class:`BuilderState` and use the same
clone-and-replace pattern for chain methods. :class:`BuilderCore` provides
the state attribute, the constructor, and the ``_with_state`` helper that
mixins call to produce new instances; concrete classes compose it with
their mixin set.
"""

from __future__ import annotations

from typing import Self

from edify.builder.types.state import BuilderState


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
