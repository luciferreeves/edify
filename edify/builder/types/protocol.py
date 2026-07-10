"""The :class:`BuilderProtocol` — the contract every mixin assumes about ``self``.

Each mixin defines methods that read ``self._state`` and return a new builder
via ``self._with_state(new_state)``. Typing ``self`` against this protocol
gives both type checkers a complete picture of the cross-mixin attribute
surface even when individual mixin files are inspected in isolation.
"""

from __future__ import annotations

from typing import Protocol, Self, runtime_checkable

from edify.builder.types.state import BuilderState
from edify.result.regex import Regex


@runtime_checkable
class BuilderProtocol(Protocol):
    """The shared shape that every builder mixin assumes about ``self``."""

    _state: BuilderState

    def _with_state(self, new_state: BuilderState) -> Self:
        """Return a new builder carrying the given state, leaving ``self`` untouched."""
        ...

    def _lazy_regex(self) -> Regex:
        """Return the memoised :class:`Regex` produced from ``self``, compiling once."""
        ...

    def to_regex_string(self) -> str:
        """Return the emitted regex string for ``self``."""
        ...

    def to_regex(self) -> Regex:
        """Compile ``self`` into a :class:`Regex` wrapper."""
        ...
