"""Tests for value-based ``__eq__`` and ``__hash__`` on :class:`BuilderCore`."""

import pytest

from edify import Pattern, RegexBuilder
from edify.errors.comparison import (
    CannotCompareUnfinishedBuilderError,
    CannotHashUnfinishedBuilderError,
)


def test_two_builders_with_the_same_chain_are_equal():
    assert RegexBuilder().digit() == RegexBuilder().digit()


def test_two_patterns_with_the_same_chain_are_equal():
    assert Pattern().digit() == Pattern().digit()


def test_builders_with_different_chains_are_not_equal():
    assert RegexBuilder().digit() != RegexBuilder().word()


def test_equal_builders_produce_equal_hashes():
    assert hash(RegexBuilder().digit()) == hash(RegexBuilder().digit())


def test_a_builder_is_usable_as_a_dict_key():
    lookup = {RegexBuilder().digit(): "digit-key"}
    assert lookup[RegexBuilder().digit()] == "digit-key"


def test_a_builder_can_be_deduplicated_in_a_set():
    dedup = {RegexBuilder().digit(), RegexBuilder().digit(), RegexBuilder().word()}
    assert len(dedup) == 2


def test_a_pattern_and_a_regex_builder_with_the_same_state_compare_equal():
    assert Pattern().digit() == RegexBuilder().digit()


def test_a_builder_compared_to_a_non_builder_is_not_equal():
    assert (RegexBuilder().digit() == "foo") is False
    assert (RegexBuilder().digit() == 42) is False


def test_a_builder_compared_to_a_non_builder_returns_not_implemented_from_the_dunder():
    result = RegexBuilder().digit().__eq__("foo")
    assert result is NotImplemented


def test_hash_of_two_flags_that_differ_are_distinct():
    a = RegexBuilder().ignore_case().digit()
    b = RegexBuilder().digit()
    assert a != b
    assert hash(a) != hash(b)


def test_equality_uses_emitted_pattern_not_underlying_state():
    from_chain = RegexBuilder().string("hi")
    from_string_kwarg = RegexBuilder().string("hi")
    assert from_chain.to_regex_string() == from_string_kwarg.to_regex_string()
    assert from_chain == from_string_kwarg


def test_hash_uses_emitted_pattern_and_flags_tuple():
    a = RegexBuilder().string("hi")
    b = RegexBuilder().string("hi")
    assert hash(a) == hash((a.to_regex_string(), a._state.flags))
    assert hash(a) == hash(b)


def test_equality_raises_when_left_operand_has_open_frames():
    left = RegexBuilder().any_of()
    right = RegexBuilder().digit()
    with pytest.raises(CannotCompareUnfinishedBuilderError):
        _ = left == right


def test_equality_raises_when_right_operand_has_open_frames():
    left = RegexBuilder().digit()
    right = RegexBuilder().any_of()
    with pytest.raises(CannotCompareUnfinishedBuilderError):
        _ = left == right


def test_equality_raises_when_both_operands_are_unfinished():
    left = RegexBuilder().any_of()
    right = RegexBuilder().exactly(3)
    with pytest.raises(CannotCompareUnfinishedBuilderError):
        _ = left == right


def test_hash_raises_when_frames_are_open():
    with pytest.raises(CannotHashUnfinishedBuilderError):
        hash(RegexBuilder().any_of())


def test_equality_raises_when_a_quantifier_is_dangling():
    left = RegexBuilder().exactly(3)
    right = RegexBuilder().digit()
    with pytest.raises(CannotCompareUnfinishedBuilderError):
        _ = left == right


def test_hash_raises_when_a_quantifier_is_dangling():
    with pytest.raises(CannotHashUnfinishedBuilderError):
        hash(RegexBuilder().exactly(3))


def test_compare_error_message_names_the_open_frame():
    with pytest.raises(CannotCompareUnfinishedBuilderError) as excinfo:
        _ = RegexBuilder().named_capture("domain") == RegexBuilder().digit()
    assert 'named_capture("domain")' in str(excinfo.value)
    assert "frame opened here" in str(excinfo.value)
    assert ".end()" in str(excinfo.value)


def test_compare_error_message_names_the_dangling_quantifier():
    with pytest.raises(CannotCompareUnfinishedBuilderError) as excinfo:
        _ = RegexBuilder().digit() == RegexBuilder().exactly(4)
    assert "exactly(4)" in str(excinfo.value)
    assert "no element follows" in str(excinfo.value)
    assert ".digit()" in str(excinfo.value)


def test_hash_error_message_names_the_specific_problem():
    with pytest.raises(CannotHashUnfinishedBuilderError) as excinfo:
        hash(RegexBuilder().at_least(2))
    assert "at_least(2)" in str(excinfo.value)


def test_error_message_shows_a_source_pointer_when_called_from_user_code():
    with pytest.raises(CannotHashUnfinishedBuilderError) as excinfo:
        hash(RegexBuilder().any_of())
    assert "-->" in str(excinfo.value)
    assert __file__ in str(excinfo.value)
