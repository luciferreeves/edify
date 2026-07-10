"""Exceptions raised for equality / hash operations on unfinished builders."""

from __future__ import annotations

from edify.errors.context import capture_caller_context
from edify.errors.formatting import (
    Problem,
    format_error,
    format_note_line,
    format_pointer_block,
    format_problem,
)
from edify.errors.syntax import EdifySyntaxError


class CannotCompareUnfinishedBuilderError(EdifySyntaxError):
    """Raised by ``==`` when either operand has open frames or a pending quantifier.

    Args:
        problems: One :class:`Problem` per unfinished operand.
    """

    def __init__(self, problems: list[Problem]) -> None:
        caller_context = capture_caller_context()
        trigger_block = ""
        if caller_context is not None:
            trigger_block = format_pointer_block(caller_context, "comparison rejected here")
        note_line = format_note_line(
            "value equality on RegexBuilder is (emitted_pattern, flags); "
            "both operands must render their regex, but edify sees "
            f"{len(problems)} problem{'s' if len(problems) != 1 else ''} below."
        )
        trigger_with_note = trigger_block + "\n" + note_line if trigger_block else note_line
        problem_blocks = [format_problem(problem) for problem in problems]
        message = format_error(
            "cannot compare an unfinished builder",
            trigger_with_note,
            *problem_blocks,
        )
        super().__init__(message)


class CannotHashUnfinishedBuilderError(EdifySyntaxError):
    """Raised by ``hash(...)`` when the builder has open frames or a pending quantifier.

    Args:
        problem: The single :class:`Problem` describing what is unfinished.
    """

    def __init__(self, problem: Problem) -> None:
        caller_context = capture_caller_context()
        trigger_block = ""
        if caller_context is not None:
            trigger_block = format_pointer_block(caller_context, "hash rejected here")
        note_line = format_note_line(
            "the value hash on RegexBuilder is derived from (emitted_pattern, flags); "
            "the builder must be renderable, but edify sees the problem below."
        )
        trigger_with_note = trigger_block + "\n" + note_line if trigger_block else note_line
        problem_block = format_problem(problem)
        message = format_error(
            "cannot hash an unfinished builder",
            trigger_with_note,
            problem_block,
        )
        super().__init__(message)
