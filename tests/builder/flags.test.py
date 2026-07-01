"""Tests for the flag keyword arguments on :meth:`TerminalsMixin.to_regex`."""

import re

from edify import Pattern, RegexBuilder


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
