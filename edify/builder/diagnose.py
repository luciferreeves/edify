"""Diagnostic helpers that describe why a builder is unfinished."""

from __future__ import annotations

from edify.builder.types.frame import StackFrame
from edify.builder.types.state import BuilderState
from edify.elements.types.captures import CaptureElement, NamedCaptureElement
from edify.elements.types.groups import (
    AnyOfElement,
    AssertAheadElement,
    AssertBehindElement,
    AssertNotAheadElement,
    AssertNotBehindElement,
    GroupElement,
)
from edify.errors.context import CallerContext
from edify.errors.formatting import FixInsertion, Problem

_END_INSERTION_TEXT = ".end()"
_DANGLING_INSERTION_TEXT = ".digit()"


def diagnose_unfinished(state: BuilderState, subject: str) -> Problem | None:
    """Return a :class:`Problem` for the first unfinished thing in ``state``, or ``None``."""
    if len(state.stack) > 1:
        return _diagnose_open_frame(state.top_frame, subject)
    for frame in state.stack:
        if frame.quantifier is not None:
            return _diagnose_dangling_quantifier(frame, subject)
    return None


def _diagnose_open_frame(frame: StackFrame, subject: str) -> Problem:
    """Return a :class:`Problem` describing an unclosed frame."""
    frame_name = _frame_display_name(frame)
    problem_context = _fallback(frame.call_site)
    fix_context = _fallback(frame.last_child_call_site or frame.call_site)
    fix_insertion = FixInsertion(
        column=fix_context.end_colno,
        text=_END_INSERTION_TEXT,
    )
    return Problem(
        description=f"`{subject}` has an open `{frame_name}` frame",
        problem_context=problem_context,
        problem_hint="frame opened here, never closed",
        help_summary=f"close the frame with `{_END_INSERTION_TEXT}`",
        fix_context=fix_context,
        fix_insertion=fix_insertion,
    )


def _diagnose_dangling_quantifier(frame: StackFrame, subject: str) -> Problem:
    """Return a :class:`Problem` describing a pending quantifier with no operand."""
    quantifier_name = frame.quantifier_name or "quantifier"
    problem_context = _fallback(frame.quantifier_call_site)
    fix_context = _fallback(frame.quantifier_call_site)
    fix_insertion = FixInsertion(
        column=fix_context.end_colno,
        text=_DANGLING_INSERTION_TEXT,
    )
    return Problem(
        description=f"`{subject}` has a pending `.{quantifier_name}` quantifier",
        problem_context=problem_context,
        problem_hint="quantifier set here — no element follows",
        help_summary=(
            f"append an element to repeat, e.g. `{_DANGLING_INSERTION_TEXT}` "
            '(or `.word()`, `.char("x")`)'
        ),
        fix_context=fix_context,
        fix_insertion=fix_insertion,
    )


def _frame_display_name(frame: StackFrame) -> str:
    """Return the human-facing name of the chain call that opened ``frame``."""
    type_node = frame.type_node
    if isinstance(type_node, AnyOfElement):
        return "any_of()"
    if isinstance(type_node, GroupElement):
        return "group()"
    if isinstance(type_node, AssertAheadElement):
        return "assert_ahead()"
    if isinstance(type_node, AssertNotAheadElement):
        return "assert_not_ahead()"
    if isinstance(type_node, AssertBehindElement):
        return "assert_behind()"
    if isinstance(type_node, AssertNotBehindElement):
        return "assert_not_behind()"
    if isinstance(type_node, CaptureElement):
        return "capture()"
    if isinstance(type_node, NamedCaptureElement):
        return f'named_capture("{type_node.name}")'
    return type(type_node).__name__


def _fallback(context: CallerContext | None) -> CallerContext:
    """Return ``context`` if not ``None``, else a placeholder context marking unknown location."""
    if context is not None:
        return context
    return CallerContext(
        filename="<unknown>",
        lineno=0,
        colno=1,
        end_colno=1,
        source_line="",
    )
