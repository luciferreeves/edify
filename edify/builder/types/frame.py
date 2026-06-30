"""The :class:`StackFrame` dataclass — one entry on the builder's frame stack.

A frame represents an in-progress grouping construct. It carries the element
class that will wrap its children once the frame closes (the ``type_node``),
an optional pending quantifier that will be applied to the next element to
land, and the ordered list of children accumulated so far.

The whole frame is frozen; chain methods produce new frames with
:func:`dataclasses.replace` rather than mutating in place.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field, replace

from edify.elements.types.base import BaseElement
from edify.elements.types.union import QuantifierElement

PendingQuantifier = Callable[[BaseElement], QuantifierElement]


@dataclass(frozen=True)
class StackFrame:
    """One frame of the builder's open-construct stack.

    Attributes:
        type_node: The element that anchors this frame (root, capture, group, etc.).
        quantifier: A callable that wraps the next child element in a
            quantifier, or ``None`` when no quantifier is pending.
        children: The ordered children accumulated in this frame so far.
    """

    type_node: BaseElement
    quantifier: PendingQuantifier | None = None
    children: tuple[BaseElement, ...] = field(default_factory=tuple)

    def with_appended_child(self, child: BaseElement) -> StackFrame:
        """Return a new frame whose ``children`` includes ``child`` at the end."""
        appended_children = (*self.children, child)
        return replace(self, children=appended_children, quantifier=None)

    def with_quantifier(self, quantifier: PendingQuantifier) -> StackFrame:
        """Return a new frame with the given pending quantifier set."""
        return replace(self, quantifier=quantifier)
