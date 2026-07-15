"""Tests for the :class:`Match` wrapper — attribute-access for named captures."""

import pytest

from edify import Pattern, RegexBuilder
from edify.result import Match, NamedCaptures


def _username_pattern():
    return RegexBuilder().string("@").named_capture("username").one_or_more().letter().end()


def test_search_returns_a_wrapped_match():
    result = _username_pattern().search("hi @alice")
    assert isinstance(result, Match)


def test_search_returns_none_when_no_match():
    result = RegexBuilder().string("zzz").search("hi @alice")
    assert result is None


def test_match_attribute_access_returns_named_group_substring():
    result = _username_pattern().search("hi @alice")
    assert result is not None
    assert result.username == "alice"


def test_captures_namespace_returns_named_group_substring():
    result = _username_pattern().search("hi @bob")
    assert result is not None
    assert result.captures.username == "bob"


def test_captures_namespace_dir_lists_every_declared_group():
    result = _username_pattern().search("hi @carol")
    assert result is not None
    assert dir(result.captures) == ["username"]


def test_captures_namespace_attribute_error_names_valid_groups():
    result = _username_pattern().search("hi @dave")
    assert result is not None
    with pytest.raises(AttributeError, match="does not exist"):
        _ = result.captures.nonexistent


def test_match_delegates_re_match_methods_via_getattr():
    result = _username_pattern().search("hi @erin")
    assert result is not None
    assert result.group() == "@erin"
    assert result.group("username") == "erin"
    assert result.groupdict() == {"username": "erin"}
    assert result.span("username") == (4, 8)


def test_match_wrapped_property_returns_the_underlying_re_match():
    result = _username_pattern().search("hi @frank")
    assert result is not None
    wrapped = result.wrapped
    assert wrapped.group("username") == "frank"


def test_match_repr_contains_span_and_text():
    result = _username_pattern().search("hi @greta")
    assert result is not None
    assert "greta" in repr(result)


def test_finditer_yields_wrapped_matches():
    pattern = _username_pattern().to_regex()
    hits = list(pattern.finditer("hi @heidi and @ivan"))
    assert all(isinstance(item, Match) for item in hits)
    assert [item.captures.username for item in hits] == ["heidi", "ivan"]


def test_sub_callable_receives_wrapped_match():
    pattern = _username_pattern().to_regex()
    result = pattern.sub(lambda m: m.captures.username.upper(), "hi @jane")
    assert result == "hi JANE"


def test_subn_callable_receives_wrapped_match():
    pattern = _username_pattern().to_regex()
    result, count = pattern.subn(lambda m: m.captures.username.upper(), "hi @jane and @jim")
    assert result == "hi JANE and JIM"
    assert count == 2


def test_sub_still_accepts_a_plain_string_replacement():
    pattern = _username_pattern().to_regex()
    assert pattern.sub("[X]", "hi @jane") == "hi [X]"


def test_named_captures_instance_is_a_namespace():
    pattern = _username_pattern().to_regex()
    result = pattern.search("hi @karen")
    assert result is not None
    assert isinstance(result.captures, NamedCaptures)


def test_pattern_match_via_pattern_class_returns_wrapped_match():
    pattern = Pattern().named_capture("word").one_or_more().letter().end()
    assert pattern.match("hello") is not None
    assert pattern.match("hello").captures.word == "hello"


def test_fullmatch_returns_wrapped_match_when_full_input_matches():
    pattern = _username_pattern().to_regex()
    result = pattern.fullmatch("@leo")
    assert result is not None
    assert result.captures.username == "leo"


def test_fullmatch_returns_none_when_input_is_only_partial():
    pattern = _username_pattern().to_regex()
    assert pattern.fullmatch("hi @leo") is None
