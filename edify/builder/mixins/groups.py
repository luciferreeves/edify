"""The :class:`GroupsMixin` — chain methods that open non-capturing groups.

Both methods push a new frame onto the builder's stack; the frame closes
when the user calls ``.end()`` later. The accumulated children are wrapped
in the appropriate element class at close time.
"""

from __future__ import annotations

from typing import Self

from edify.builder.types.frame import StackFrame
from edify.builder.types.protocol import BuilderProtocol
from edify.elements.types.groups import AnyOfElement, GroupElement


class GroupsMixin(BuilderProtocol):
    """Provides the ``any_of`` and ``group`` frame-opening chain methods."""

    def any_of(self) -> Self:
        """Return a new builder with an alternation frame opened."""
        new_frame = StackFrame(type_node=AnyOfElement())
        new_state = self._state.with_frame_pushed(new_frame)
        return self._with_state(new_state)

    def group(self) -> Self:
        """Return a new builder with a non-capturing-group frame opened."""
        new_frame = StackFrame(type_node=GroupElement())
        new_state = self._state.with_frame_pushed(new_frame)
        return self._with_state(new_state)
