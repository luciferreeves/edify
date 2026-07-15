"""Tests for the flag keyword arguments on :meth:`TerminalsMixin.to_regex`."""

import re
import sys

import pytest

from edify import Pattern, RegexBuilder

_ON_PYPY = hasattr(sys, "pypy_version_info")


def test_no_kwargs_uses_only_the_chain_flag_snapshot():
    compiled = RegexBuilder().string("hi").to_regex()
    assert compiled.compiled.flags & re.I == 0


def test_ignore_case_kwarg_enables_the_ignore_case_flag():
    compiled = RegexBuilder().string("hi").to_regex(ignore_case=True)
    assert compiled.compiled.flags & re.I == re.I


def test_multiline_kwarg_enables_the_multiline_flag():
    compiled = RegexBuilder().string("hi").to_regex(multiline=True)
    assert compiled.compiled.flags & re.M == re.M


def test_dotall_kwarg_enables_the_dotall_flag():
    compiled = RegexBuilder().string("hi").to_regex(dotall=True)
    assert compiled.compiled.flags & re.S == re.S


def test_ascii_only_kwarg_enables_the_ascii_flag():
    compiled = RegexBuilder().string("hi").to_regex(ascii_only=True)
    assert compiled.compiled.flags & re.A == re.A


def test_verbose_kwarg_enables_the_verbose_flag():
    compiled = RegexBuilder().string("hi").to_regex(verbose=True)
    assert compiled.compiled.flags & re.X == re.X


@pytest.mark.skipif(
    _ON_PYPY,
    reason="PyPy's re.DEBUG opcode disassembler has an upstream IndexError bug",
)
def test_debug_kwarg_compiles_without_error():
    compiled = RegexBuilder().string("hi").to_regex(debug=True)
    assert compiled.source == "hi"


def test_kwargs_or_merge_with_chain_flags():
    compiled = RegexBuilder().ignore_case().string("hi").to_regex(multiline=True)
    assert compiled.compiled.flags & re.I == re.I
    assert compiled.compiled.flags & re.M == re.M


def test_kwargs_never_turn_off_a_chain_flag():
    compiled = RegexBuilder().ignore_case().string("hi").to_regex(ignore_case=False)
    assert compiled.compiled.flags & re.I == re.I


def test_kwargs_work_on_pattern_too():
    compiled = Pattern().string("hi").to_regex(ignore_case=True)
    assert compiled.compiled.flags & re.I == re.I


def test_multiple_kwargs_combine():
    compiled = RegexBuilder().string("hi").to_regex(ignore_case=True, multiline=True, dotall=True)
    assert compiled.compiled.flags & re.I == re.I
    assert compiled.compiled.flags & re.M == re.M
    assert compiled.compiled.flags & re.S == re.S


def _regex_module():
    import regex

    return regex


def test_regex_engine_ignore_case_kwarg_enables_the_flag():
    regex = _regex_module()
    compiled = RegexBuilder().string("hi").to_regex(engine="regex", ignore_case=True)
    assert compiled.compiled.flags & regex.I == regex.I


def test_regex_engine_multiline_kwarg_enables_the_flag():
    regex = _regex_module()
    compiled = RegexBuilder().string("hi").to_regex(engine="regex", multiline=True)
    assert compiled.compiled.flags & regex.M == regex.M


def test_regex_engine_dotall_kwarg_enables_the_flag():
    regex = _regex_module()
    compiled = RegexBuilder().string("hi").to_regex(engine="regex", dotall=True)
    assert compiled.compiled.flags & regex.S == regex.S


def test_regex_engine_ascii_only_kwarg_enables_the_flag():
    regex = _regex_module()
    compiled = RegexBuilder().string("hi").to_regex(engine="regex", ascii_only=True)
    assert compiled.compiled.flags & regex.A == regex.A


def test_regex_engine_verbose_kwarg_enables_the_flag():
    regex = _regex_module()
    compiled = RegexBuilder().string("hi").to_regex(engine="regex", verbose=True)
    assert compiled.compiled.flags & regex.X == regex.X


@pytest.mark.skipif(
    _ON_PYPY,
    reason="PyPy's regex.DEBUG opcode disassembler shares the same upstream disassembler bug",
)
def test_regex_engine_debug_kwarg_compiles_without_error():
    compiled = RegexBuilder().string("hi").to_regex(engine="regex", debug=True)
    assert compiled.source == "hi"
