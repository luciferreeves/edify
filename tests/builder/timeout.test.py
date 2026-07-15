"""Tests for the per-call ``timeout=`` kwarg on match methods."""

import pytest

from edify import RegexBuilder
from edify.errors.backend import TimeoutNotSupportedByEngineError


def _regex_pattern():
    return RegexBuilder().string("a").to_regex(engine="regex")


def _re_pattern():
    return RegexBuilder().string("a").to_regex(engine="re")


def test_timeout_flows_through_search_under_regex_engine():
    assert _regex_pattern().search("aaa", timeout=1.0) is not None


def test_timeout_flows_through_match_under_regex_engine():
    assert _regex_pattern().match("aaa", timeout=1.0) is not None


def test_timeout_flows_through_fullmatch_under_regex_engine():
    assert _regex_pattern().fullmatch("a", timeout=1.0) is not None


def test_timeout_flows_through_findall_under_regex_engine():
    assert _regex_pattern().findall("aaa", timeout=1.0) == ["a", "a", "a"]


def test_timeout_flows_through_finditer_under_regex_engine():
    matches = list(_regex_pattern().finditer("aaa", timeout=1.0))
    assert len(matches) == 3


def test_timeout_flows_through_sub_under_regex_engine():
    assert _regex_pattern().sub("b", "aaa", timeout=1.0) == "bbb"


def test_timeout_flows_through_subn_under_regex_engine():
    assert _regex_pattern().subn("b", "aaa", timeout=1.0) == ("bbb", 3)


def test_timeout_flows_through_split_under_regex_engine():
    assert _regex_pattern().split("a1a2a3", timeout=1.0) == ["", "1", "2", "3"]


def test_timeout_under_re_engine_raises_annotated_error():
    with pytest.raises(TimeoutNotSupportedByEngineError) as excinfo:
        _re_pattern().search("aaa", timeout=1.0)
    text = str(excinfo.value)
    assert "timeout=" in text
    assert "engine='regex'" in text
    assert "= note:" in text


def test_matcher_search_forwards_timeout_to_the_cached_regex():
    builder = RegexBuilder().string("a")
    with pytest.raises(TimeoutNotSupportedByEngineError):
        builder.search("aaa", timeout=1.0)


def test_matcher_match_forwards_timeout_to_the_cached_regex():
    builder = RegexBuilder().string("a")
    with pytest.raises(TimeoutNotSupportedByEngineError):
        builder.match("aaa", timeout=1.0)


def test_matcher_fullmatch_forwards_timeout_to_the_cached_regex():
    builder = RegexBuilder().string("a")
    with pytest.raises(TimeoutNotSupportedByEngineError):
        builder.fullmatch("a", timeout=1.0)


def test_matcher_findall_forwards_timeout_to_the_cached_regex():
    builder = RegexBuilder().string("a")
    with pytest.raises(TimeoutNotSupportedByEngineError):
        builder.findall("aaa", timeout=1.0)


def test_matcher_finditer_forwards_timeout_to_the_cached_regex():
    builder = RegexBuilder().string("a")
    with pytest.raises(TimeoutNotSupportedByEngineError):
        list(builder.finditer("aaa", timeout=1.0))


def test_matcher_sub_forwards_timeout_to_the_cached_regex():
    builder = RegexBuilder().string("a")
    with pytest.raises(TimeoutNotSupportedByEngineError):
        builder.sub("b", "aaa", timeout=1.0)


def test_matcher_subn_forwards_timeout_to_the_cached_regex():
    builder = RegexBuilder().string("a")
    with pytest.raises(TimeoutNotSupportedByEngineError):
        builder.subn("b", "aaa", timeout=1.0)


def test_matcher_split_forwards_timeout_to_the_cached_regex():
    builder = RegexBuilder().string("a")
    with pytest.raises(TimeoutNotSupportedByEngineError):
        builder.split("aaa", timeout=1.0)


def test_no_timeout_kwarg_never_raises_on_either_engine():
    assert _regex_pattern().search("aaa") is not None
    assert _re_pattern().search("aaa") is not None
