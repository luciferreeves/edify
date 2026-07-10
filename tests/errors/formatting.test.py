"""Tests for the message formatter helpers in :mod:`edify.errors.formatting`."""

from unittest import mock

from edify.errors.context import CallerContext
from edify.errors.formatting import (
    FixInsertion,
    Problem,
    compose_annotated_message,
    format_error,
    format_fix_block,
    format_help_header,
    format_note_line,
    format_pointer_block,
    format_problem,
    format_problem_header,
)


def _context(source_line: str = "    x = do_the_thing(1, 2, 3)", colno: int = 9) -> CallerContext:
    return CallerContext(
        filename="/tmp/user_code.py",
        lineno=42,
        colno=colno,
        end_colno=colno + 15,
        source_line=source_line,
    )


def test_format_error_with_only_summary_returns_bare_header():
    assert format_error("boom") == "error: boom"


def test_format_error_with_summary_and_blocks_joins_them_with_blank_line():
    output = format_error("boom", "first block", "second block")
    assert output == "error: boom\n\nfirst block\n\nsecond block"


def test_format_error_skips_empty_blocks():
    output = format_error("boom", "", "only real block", "")
    assert output == "error: boom\n\nonly real block"


def test_format_pointer_block_draws_caret_at_caller_column():
    context = _context()
    block = format_pointer_block(context, "here")
    lines = block.splitlines()
    assert lines[0] == "  --> /tmp/user_code.py:42:9"
    assert "^^^^^^^^^^^^^^^ here" in block


def test_format_pointer_block_has_at_least_one_caret_when_span_is_empty():
    context = CallerContext(
        filename="/tmp/x.py",
        lineno=1,
        colno=5,
        end_colno=5,
        source_line="abcde",
    )
    block = format_pointer_block(context, "point")
    assert "^ point" in block


def test_format_note_line_prepends_the_note_prefix():
    assert format_note_line("something is off") == "   = note: something is off"


def test_format_problem_header_prepends_problem_prefix():
    assert format_problem_header("stuff") == "problem: stuff"


def test_format_help_header_prepends_help_prefix():
    assert format_help_header("do X") == "help: do X"


def test_format_fix_block_inserts_text_at_the_target_column():
    context = _context(source_line="value = compute()", colno=1)
    insertion = FixInsertion(column=9, text="new_")
    block = format_fix_block(context, insertion)
    assert "value = new_compute()" in block
    assert "++++" in block


def test_format_problem_composes_header_pointer_help_and_fix():
    problem_context = _context(source_line="pattern = build()", colno=11)
    fix_context = _context(source_line="pattern = build()", colno=11)
    fix_insertion = FixInsertion(column=11, text=".digit()")
    problem = Problem(
        description="missing operand",
        problem_context=problem_context,
        problem_hint="no operand added",
        help_summary="add .digit() before .build()",
        fix_context=fix_context,
        fix_insertion=fix_insertion,
    )
    output = format_problem(problem)
    assert "problem: missing operand" in output
    assert "no operand added" in output
    assert "help: add .digit() before .build()" in output
    assert "++++++++" in output


def test_compose_annotated_message_when_caller_context_is_available():
    output = compose_annotated_message(
        summary="bad thing happened",
        trigger_hint="right here",
        note="because reasons",
        help_line="help: do X",
    )
    assert output.startswith("error: bad thing happened")
    assert "-->" in output
    assert "= note: because reasons" in output
    assert output.rstrip().endswith("help: do X")


def test_compose_annotated_message_falls_back_when_caller_context_is_none():
    with mock.patch("edify.errors.formatting.capture_caller_context", return_value=None):
        output = compose_annotated_message(
            summary="bad thing happened",
            trigger_hint="here",
            note="because reasons",
            help_line="help: do X",
        )
    assert output.startswith("error: bad thing happened")
    assert "-->" not in output
    assert "= note: because reasons" in output
    assert output.rstrip().endswith("help: do X")
