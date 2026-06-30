"""The :class:`ChainMixin` — the ``.end()`` method that closes the top frame.

Pops the top frame off the stack, constructs the corresponding container
element from the frame's accumulated children, and appends that element to
the new top frame (applying any pending quantifier on the way).
"""

from __future__ import annotations

from typing import Self

from edify.builder.types.frame import StackFrame
from edify.builder.types.protocol import BuilderProtocol
from edify.elements.types.base import BaseElement
from edify.elements.types.captures import CaptureElement, NamedCaptureElement
from edify.elements.types.groups import (
    AnyOfElement,
    AssertAheadElement,
    AssertBehindElement,
    AssertNotAheadElement,
    AssertNotBehindElement,
    GroupElement,
)
from edify.errors.internal import UnexpectedFrameTypeError
from edify.errors.structure import CannotEndWhileBuildingRootExpressionError


class ChainMixin(BuilderProtocol):
    """Provides the ``.end()`` method that closes the current frame."""

    def end(self) -> Self:
        """Return a new builder with the top frame closed and merged into its parent."""
        _ensure_non_root_frame_open(self._state.stack)
        state_with_popped, popped_frame = self._state.with_top_frame_popped()
        closed_element = _close_frame(popped_frame)
        new_state = state_with_popped.with_element_added_to_top(closed_element)
        return self._with_state(new_state)


def _ensure_non_root_frame_open(stack: tuple[StackFrame, ...]) -> None:
    """Raise :class:`CannotEndWhileBuildingRootExpressionError` when the root is the only frame."""
    if len(stack) > 1:
        return
    raise CannotEndWhileBuildingRootExpressionError()


def _close_frame(frame: StackFrame) -> BaseElement:
    """Construct the container element that wraps the frame's accumulated children."""
    type_node = frame.type_node
    children = frame.children
    match type_node:
        case CaptureElement():
            return CaptureElement(children=children)
        case NamedCaptureElement(name=capture_name):
            return NamedCaptureElement(name=capture_name, children=children)
        case GroupElement():
            return GroupElement(children=children)
        case AnyOfElement():
            return AnyOfElement(children=children)
        case AssertAheadElement():
            return AssertAheadElement(children=children)
        case AssertNotAheadElement():
            return AssertNotAheadElement(children=children)
        case AssertBehindElement():
            return AssertBehindElement(children=children)
        case AssertNotBehindElement():
            return AssertNotBehindElement(children=children)
        case _:
            element_type_name = type(type_node).__name__
            raise UnexpectedFrameTypeError(element_type_name)
