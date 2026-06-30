"""The :class:`BuilderProtocol` — the contract every mixin assumes about ``self``.

Each mixin defines methods that read ``self._state`` and return a new builder
via ``self._with_state(new_state)``. Typing ``self`` against this protocol
gives both type checkers a complete picture of the cross-mixin attribute
surface even when individual mixin files are inspected in isolation.
"""

from __future__ import annotations

from typing import Protocol, Self, runtime_checkable

from edify.builder.types.state import BuilderState


@runtime_checkable
class BuilderProtocol(Protocol):
    """The shared shape that every builder mixin assumes about ``self``."""

    _state: BuilderState

    def _with_state(self, new_state: BuilderState) -> Self:
        """Return a new builder carrying the given state, leaving ``self`` untouched."""
        ...
