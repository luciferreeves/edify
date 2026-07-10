"""The :class:`StackFrame` dataclass."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field, replace

from edify.elements.types.base import BaseElement
from edify.elements.types.union import QuantifierElement
from edify.errors.context import CallerContext

PendingQuantifier = Callable[[BaseElement], QuantifierElement]


@dataclass(frozen=True)
class StackFrame:
    """One frame of the builder's open-construct stack.

    Attributes:
        type_node: The element that anchors this frame.
        quantifier: A callable that wraps the next child element in a
            quantifier, or ``None`` when no quantifier is pending.
        children: The ordered children accumulated in this frame so far.
        call_site: Source-location snapshot of the chain call that opened
            this frame; ``None`` on the root frame or when unavailable.
        last_child_call_site: Source-location snapshot of the chain call
            that appended the most recent child; ``None`` when no child
            has been appended yet or the location is unavailable.
        quantifier_call_site: Source-location snapshot of the chain call
            that set :attr:`quantifier`; ``None`` when no quantifier is
            pending.
        quantifier_name: Human-readable name of the pending quantifier
            (e.g. ``"exactly(3)"``); ``None`` when no quantifier is pending.
    """

    type_node: BaseElement
    quantifier: PendingQuantifier | None = field(default=None, compare=False, hash=False)
    children: tuple[BaseElement, ...] = field(default_factory=tuple)
    call_site: CallerContext | None = field(default=None, compare=False, hash=False)
    last_child_call_site: CallerContext | None = field(default=None, compare=False, hash=False)
    quantifier_call_site: CallerContext | None = field(default=None, compare=False, hash=False)
    quantifier_name: str | None = None

    def with_appended_child(
        self,
        child: BaseElement,
        call_site: CallerContext | None,
    ) -> StackFrame:
        """Return a new frame with ``child`` appended and pending quantifier cleared."""
        appended_children = (*self.children, child)
        return replace(
            self,
            children=appended_children,
            quantifier=None,
            last_child_call_site=call_site,
            quantifier_call_site=None,
            quantifier_name=None,
        )

    def with_quantifier(
        self,
        quantifier: PendingQuantifier,
        call_site: CallerContext | None,
        quantifier_name: str,
    ) -> StackFrame:
        """Return a new frame carrying the pending quantifier and its source location."""
        return replace(
            self,
            quantifier=quantifier,
            quantifier_call_site=call_site,
            quantifier_name=quantifier_name,
        )
