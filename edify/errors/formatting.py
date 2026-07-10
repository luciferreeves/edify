"""Message formatter helpers for the edify error classes."""

from __future__ import annotations

from dataclasses import dataclass

from edify.errors.context import CallerContext, capture_caller_context


@dataclass(frozen=True)
class FixInsertion:
    """A single insertion into a source line.

    Attributes:
        column: 1-indexed column where the insertion begins.
        text: The text to insert; also the width used to draw the ``+`` marks.
    """

    column: int
    text: str


@dataclass(frozen=True)
class Problem:
    """A single named problem with a pointer at its creation site and a suggested fix.

    Attributes:
        description: Full-sentence text that follows the ``problem:`` label.
        problem_context: Source-location snapshot of the offending chain call.
        problem_hint: Inline label rendered next to the problem's caret.
        help_summary: One-line text that follows the ``help:`` label.
        fix_context: Source-location snapshot of the line that should be patched.
        fix_insertion: The text to insert into the source line and where.
    """

    description: str
    problem_context: CallerContext
    problem_hint: str
    help_summary: str
    fix_context: CallerContext
    fix_insertion: FixInsertion


def format_error(summary: str, *blocks: str) -> str:
    """Return the full message: ``error: <summary>`` followed by ``blocks``."""
    non_empty_blocks = [block for block in blocks if block]
    body = "\n\n".join(non_empty_blocks)
    if body:
        return f"error: {summary}\n\n{body}"
    return f"error: {summary}"


def format_pointer_block(context: CallerContext, hint: str) -> str:
    """Return a ``-->`` pointer block underlining the offending call in the source line."""
    lineno_prefix = str(context.lineno)
    left_pad = " " * len(lineno_prefix)
    caret_width = max(1, context.end_colno - context.colno)
    caret_indent = " " * (context.colno - 1)
    caret_line = f"{left_pad} | {caret_indent}{'^' * caret_width} {hint}".rstrip()
    header_line = f"{left_pad}--> {context.filename}:{context.lineno}:{context.colno}"
    bar_line = f"{left_pad} |"
    source_line = f"{lineno_prefix} | {context.source_line}"
    lines = [header_line, bar_line, source_line, caret_line, bar_line]
    return "\n".join(lines)


def format_fix_block(context: CallerContext, insertion: FixInsertion) -> str:
    """Return a pointer-style block that shows the corrected line with ``+`` marks."""
    lineno_prefix = str(context.lineno)
    left_pad = " " * len(lineno_prefix)
    original_line = context.source_line
    insertion_zero_col = insertion.column - 1
    corrected_line = (
        original_line[:insertion_zero_col] + insertion.text + original_line[insertion_zero_col:]
    )
    plus_indent = " " * insertion_zero_col
    plus_marks = "+" * len(insertion.text)
    bar_line = f"{left_pad} |"
    source_line = f"{lineno_prefix} | {corrected_line}"
    marker_line = f"{left_pad} | {plus_indent}{plus_marks}"
    return "\n".join([bar_line, source_line, marker_line, bar_line])


def format_note_line(note: str) -> str:
    """Return an aligned ``= note:`` continuation line."""
    return f"   = note: {note}"


def format_problem_header(description: str) -> str:
    """Return the ``problem: <description>`` header line."""
    return f"problem: {description}"


def format_help_header(help: str) -> str:
    """Return the ``help: <help>`` header line."""
    return f"help: {help}"


def format_problem(problem: Problem) -> str:
    """Return a full problem block: header, pointer, help header, fix pointer."""
    header = format_problem_header(problem.description)
    problem_pointer = format_pointer_block(problem.problem_context, problem.problem_hint)
    help_header = format_help_header(problem.help_summary)
    fix_pointer = format_fix_block(problem.fix_context, problem.fix_insertion)
    return "\n\n".join([header, problem_pointer, help_header, fix_pointer])


def compose_annotated_message(
    summary: str,
    trigger_hint: str,
    note: str,
    help_line: str,
) -> str:
    """Return a full annotated error message.

    Captures the caller context, draws a pointer block with ``trigger_hint`` at the
    caret, adds a ``= note:`` line explaining ``note``, and appends the pre-formatted
    ``help_line`` (which must start with ``help:``).

    Args:
        summary: One-line summary printed after ``error:``.
        trigger_hint: Inline label placed next to the caret in the pointer block.
        note: Sentence explaining why the invariant was violated.
        help_line: Pre-formatted help line, starting with ``help:``.
    """
    caller_context = capture_caller_context()
    note_line = format_note_line(note)
    if caller_context is None:
        body = note_line
    else:
        trigger_block = format_pointer_block(caller_context, trigger_hint)
        body = trigger_block + "\n" + note_line
    return format_error(summary, body, help_line)
