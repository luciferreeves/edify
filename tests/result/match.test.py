"""Tests for the :class:`Match` wrapper — attribute-access for named captures."""

import pytest

from edify import Pattern, RegexBuilder
from edify.result import Match, NamedCaptures


def _username_pattern():
    return RegexBuilder().string("@").named_capture("username").one_or_more().letter().end()


def _uppercase_username(match: Match) -> str:
    username = match.captures.username
    assert username is not None
    return username.upper()


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
    assert [item.captures.username for item in hits] == ["heidi", "ivan"]


def test_sub_callable_receives_wrapped_match():
    pattern = _username_pattern().to_regex()
    result = pattern.sub(_uppercase_username, "hi @jane")
    assert result == "hi JANE"


def test_subn_callable_receives_wrapped_match():
    pattern = _username_pattern().to_regex()
    result, count = pattern.subn(_uppercase_username, "hi @jane and @jim")
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
    result = pattern.match("hello")
    assert result is not None
    assert result.captures.word == "hello"


def test_fullmatch_returns_wrapped_match_when_full_input_matches():
    pattern = _username_pattern().to_regex()
    result = pattern.fullmatch("@leo")
    assert result is not None
    assert result.captures.username == "leo"


def test_fullmatch_returns_none_when_input_is_only_partial():
    pattern = _username_pattern().to_regex()
    assert pattern.fullmatch("hi @leo") is None


def test_match_forwarded_group_accepts_named_and_positional_selectors():
    result = _username_pattern().search("hi @meg")
    assert result is not None
    assert result.group() == "@meg"
    assert result.group(0) == "@meg"
    assert result.group(1) == "meg"


def test_match_forwarded_groups_returns_the_positional_group_tuple():
    result = _username_pattern().search("hi @nora")
    assert result is not None
    assert result.groups() == ("nora",)


def test_match_forwarded_groups_uses_default_for_unmatched_groups():
    optional_capture = (
        RegexBuilder()
        .start_of_input()
        .capture()
        .string("hi")
        .end()
        .optional()
        .capture()
        .string("bye")
        .end()
        .end_of_input()
    )
    result = optional_capture.match("hi")
    assert result is not None
    assert result.groups(default="missing") == ("hi", "missing")


def test_match_forwarded_groupdict_defaults_to_none_for_absent_named_groups():
    result = _username_pattern().search("hi @olive")
    assert result is not None
    assert result.groupdict() == {"username": "olive"}


def test_match_forwarded_groupdict_accepts_a_default_string():
    optional_named = (
        RegexBuilder()
        .start_of_input()
        .string("hi")
        .optional()
        .named_capture("nick")
        .one_or_more()
        .letter()
        .end()
        .end_of_input()
    )
    result = optional_named.match("hi")
    assert result is not None
    assert result.groupdict(default="none") == {"nick": "none"}


def test_match_forwarded_start_end_span_and_expand_return_the_expected_values():
    result = _username_pattern().search("hi @pete")
    assert result is not None
    assert result.start() == 3
    assert result.end() == 8
    assert result.span() == (3, 8)
    assert result.expand(r"\g<username>") == "pete"


def test_match_forwarded_re_pos_endpos_string_lastindex_lastgroup_reflect_the_compiled_pattern():
    pattern = _username_pattern().to_regex()
    result = pattern.search("hi @quinn there")
    assert result is not None
    assert result.re is pattern.compiled
    assert result.string == "hi @quinn there"
    assert result.pos == 0
    assert result.endpos > 0
    assert result.lastindex == 1
    assert result.lastgroup == "username"


def test_match_fallback_getattr_raises_attribute_error_on_unknown_name():
    result = _username_pattern().search("hi @rita")
    assert result is not None
    with pytest.raises(AttributeError, match="no attribute"):
        _ = result.nonexistent
