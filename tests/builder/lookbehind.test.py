"""Tests for lookbehind width behavior across the ``re`` and ``regex`` engines."""

import re

import pytest

from edify import RegexBuilder
from edify.errors.backend import VariableWidthLookbehindNotSupportedError


def _variable_width_lookbehind_builder():
    return RegexBuilder().assert_behind().between(1, 3).string("foo").end().string("bar")


def _fixed_width_lookbehind_builder():
    return RegexBuilder().assert_behind().string("foo").end().string("bar")


def test_variable_width_lookbehind_under_re_raises_annotated_error():
    with pytest.raises(VariableWidthLookbehindNotSupportedError) as excinfo:
        _variable_width_lookbehind_builder().to_regex(engine="re")
    text = str(excinfo.value)
    assert "assert_behind" in text
    assert "engine='regex'" in text
    assert "= note:" in text
    assert "help:" in text


def test_variable_width_lookbehind_under_regex_compiles_and_matches():
    compiled = _variable_width_lookbehind_builder().to_regex(engine="regex")
    assert compiled.engine == "regex"
    assert compiled.search("foobar") is not None
    assert compiled.search("foofoobar") is not None
    assert compiled.search("foofoofoobar") is not None
    assert compiled.search("bar") is None


def test_fixed_width_lookbehind_still_works_under_re():
    compiled = _fixed_width_lookbehind_builder().to_regex(engine="re")
    assert compiled.search("foobar") is not None
    assert compiled.search("bar") is None


def test_variable_width_lookbehind_error_chains_the_underlying_pattern_error():
    with pytest.raises(VariableWidthLookbehindNotSupportedError) as excinfo:
        _variable_width_lookbehind_builder().to_regex(engine="re")
    assert isinstance(excinfo.value.__cause__, re.error)


def test_re_engine_still_surfaces_other_pattern_errors_unchanged(monkeypatch: pytest.MonkeyPatch):
    def raise_other_error(_pattern: str, flags: int = 0) -> re.Pattern[str]:
        raise re.error("some other syntax error")

    monkeypatch.setattr(re, "compile", raise_other_error)
    with pytest.raises(re.error) as excinfo:
        RegexBuilder().digit().to_regex(engine="re")
    assert "some other syntax error" in str(excinfo.value)
