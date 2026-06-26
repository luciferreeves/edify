"""The :class:`AssertionsMixin` — chain methods for lookaround assertions.

Each method pushes a new frame onto the builder's stack; the frame closes
when the user calls ``.end()`` later. The accumulated children are wrapped
in the appropriate ``Assert*Element`` class at close time.
"""

from __future__ import annotations

from typing import Self

from edify.builder.types.frame import StackFrame
from edify.builder.types.protocol import BuilderProtocol
from edify.elements.types.groups import (
    AssertAheadElement,
    AssertBehindElement,
    AssertNotAheadElement,
    AssertNotBehindElement,
)


class AssertionsMixin(BuilderProtocol):
    """Provides the four lookaround-assertion frame-opening chain methods."""

    def assert_ahead(self) -> Self:
        """Return a new builder with a positive-lookahead ``(?=...)`` frame opened."""
        new_frame = StackFrame(type_node=AssertAheadElement())
        new_state = self._state.with_frame_pushed(new_frame)
        return self._with_state(new_state)

    def assert_not_ahead(self) -> Self:
        """Return a new builder with a negative-lookahead ``(?!...)`` frame opened."""
        new_frame = StackFrame(type_node=AssertNotAheadElement())
        new_state = self._state.with_frame_pushed(new_frame)
        return self._with_state(new_state)

    def assert_behind(self) -> Self:
        """Return a new builder with a positive-lookbehind ``(?<=...)`` frame opened."""
        new_frame = StackFrame(type_node=AssertBehindElement())
        new_state = self._state.with_frame_pushed(new_frame)
        return self._with_state(new_state)

    def assert_not_behind(self) -> Self:
        """Return a new builder with a negative-lookbehind ``(?<!...)`` frame opened."""
        new_frame = StackFrame(type_node=AssertNotBehindElement())
        new_state = self._state.with_frame_pushed(new_frame)
        return self._with_state(new_state)
