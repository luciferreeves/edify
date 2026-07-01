"""Tests for value-based ``__eq__`` and ``__hash__`` on :class:`BuilderCore`."""

from edify import Pattern, RegexBuilder


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
