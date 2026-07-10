"""The :class:`BuilderState` dataclass."""

from __future__ import annotations

from dataclasses import dataclass, field, replace

from edify.builder.types.flags import Flags
from edify.builder.types.frame import StackFrame
from edify.elements.types.base import BaseElement
from edify.elements.types.root import RootElement
from edify.errors.context import CallerContext, capture_caller_context


def _initial_stack() -> tuple[StackFrame, ...]:
    """Return the one-element stack a fresh builder starts with."""
    root_frame = StackFrame(type_node=RootElement())
    return (root_frame,)


@dataclass(frozen=True)
class BuilderState:
    """The full immutable state carried by a builder instance.

    Attributes:
        has_defined_start: True once ``start_of_input`` has been added.
        has_defined_end: True once ``end_of_input`` has been added.
        flags: The current pattern-global flag snapshot.
        stack: Ordered frames; the root frame is always at index 0.
        named_groups: Names declared by ``named_capture`` so far.
        total_capture_groups: Total number of capture groups declared so far.
    """

    has_defined_start: bool = False
    has_defined_end: bool = False
    flags: Flags = field(default_factory=Flags)
    stack: tuple[StackFrame, ...] = field(default_factory=_initial_stack)
    named_groups: tuple[str, ...] = field(default_factory=tuple)
    total_capture_groups: int = 0

    @property
    def top_frame(self) -> StackFrame:
        """Return the frame currently being built into (the last on the stack)."""
        return self.stack[-1]

    def with_start_defined(self) -> BuilderState:
        """Return a new state with ``has_defined_start`` set to True."""
        return replace(self, has_defined_start=True)

    def with_end_defined(self) -> BuilderState:
        """Return a new state with ``has_defined_end`` set to True."""
        return replace(self, has_defined_end=True)

    def with_flags(self, new_flags: Flags) -> BuilderState:
        """Return a new state carrying the given flags snapshot."""
        return replace(self, flags=new_flags)

    def with_top_frame_replaced(self, new_top_frame: StackFrame) -> BuilderState:
        """Return a new state whose top frame is replaced by ``new_top_frame``."""
        all_but_top = self.stack[:-1]
        new_stack = (*all_but_top, new_top_frame)
        return replace(self, stack=new_stack)

    def with_frame_pushed(self, frame: StackFrame) -> BuilderState:
        """Return a new state with ``frame`` pushed onto the top of the stack.

        When ``frame.call_site`` is ``None`` this helper captures the caller's
        source location automatically so error messages can point at the chain
        method that opened the frame.
        """
        stamped_frame = (
            frame
            if frame.call_site is not None
            else replace(frame, call_site=capture_caller_context())
        )
        new_stack = (*self.stack, stamped_frame)
        return replace(self, stack=new_stack)

    def with_top_frame_popped(self) -> tuple[BuilderState, StackFrame]:
        """Return ``(new_state, popped_top_frame)`` after popping the top frame."""
        popped_frame = self.stack[-1]
        all_but_top = self.stack[:-1]
        new_state = replace(self, stack=all_but_top)
        return new_state, popped_frame

    def with_named_group_added(self, name: str) -> BuilderState:
        """Return a new state with ``name`` appended to the declared named-groups list."""
        appended = (*self.named_groups, name)
        return replace(self, named_groups=appended)

    def with_capture_group_count_incremented(self) -> BuilderState:
        """Return a new state with ``total_capture_groups`` incremented by one."""
        incremented = self.total_capture_groups + 1
        return replace(self, total_capture_groups=incremented)

    def with_capture_groups_added(self, count: int) -> BuilderState:
        """Return a new state with ``count`` added to ``total_capture_groups``."""
        new_total = self.total_capture_groups + count
        return replace(self, total_capture_groups=new_total)

    def with_element_added_to_top(
        self,
        element: BaseElement,
        call_site: CallerContext | None = None,
    ) -> BuilderState:
        """Return a new state with ``element`` added to the top frame's children.

        If the top frame carries a pending quantifier, it wraps ``element``
        before appending and the quantifier slot is cleared.

        Args:
            element: The element to append to the top frame's children.
            call_site: The source location of the chain call responsible for
                appending ``element``. When ``None`` this helper captures the
                caller's source location automatically.
        """
        effective_call_site = call_site if call_site is not None else capture_caller_context()
        top = self.top_frame
        if top.quantifier is not None:
            wrapped_element = top.quantifier(element)
            new_top_frame = top.with_appended_child(wrapped_element, effective_call_site)
        else:
            new_top_frame = top.with_appended_child(element, effective_call_site)
        return self.with_top_frame_replaced(new_top_frame)
