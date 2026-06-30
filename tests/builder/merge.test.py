"""Tests that exercise every element kind through the subexpression merge path.

Each subexpression is built with one particular element kind and merged
into a parent; the resulting regex string is asserted byte-for-byte so the
per-type branches in :mod:`edify.builder.merge` all get exercised.
"""

from edify import RegexBuilder


def _merge(sub: RegexBuilder) -> str:
    return RegexBuilder().subexpression(sub).to_regex_string()


def test_subexpression_with_capture():
    sub = RegexBuilder().capture().digit().end()
    assert _merge(sub) == "(\\d)"


def test_subexpression_with_named_capture():
    sub = RegexBuilder().named_capture("token").digit().end()
    assert _merge(sub) == "(?P<token>\\d)"


def test_subexpression_with_back_reference():
    sub = RegexBuilder().capture().digit().end().back_reference(1)
    assert _merge(sub) == "(\\d)\\1"


def test_subexpression_with_named_back_reference():
    sub = RegexBuilder().named_capture("token").digit().end().named_back_reference("token")
    assert _merge(sub) == "(?P<token>\\d)(?P=token)"


def test_subexpression_with_group():
    sub = RegexBuilder().group().digit().end()
    assert _merge(sub) == "(?:\\d)"


def test_subexpression_with_any_of():
    sub = RegexBuilder().any_of().char("a").char("b").end()
    assert _merge(sub) == "[ab]"


def test_subexpression_with_nested_subexpression():
    inner = RegexBuilder().digit()
    middle = RegexBuilder().subexpression(inner)
    assert _merge(middle) == "\\d"


def test_subexpression_with_assert_ahead():
    sub = RegexBuilder().assert_ahead().digit().end()
    assert _merge(sub) == "(?=\\d)"


def test_subexpression_with_assert_not_ahead():
    sub = RegexBuilder().assert_not_ahead().digit().end()
    assert _merge(sub) == "(?!\\d)"


def test_subexpression_with_assert_behind():
    sub = RegexBuilder().assert_behind().digit().end()
    assert _merge(sub) == "(?<=\\d)"


def test_subexpression_with_assert_not_behind():
    sub = RegexBuilder().assert_not_behind().digit().end()
    assert _merge(sub) == "(?<!\\d)"


def test_subexpression_with_optional():
    sub = RegexBuilder().optional().digit()
    assert _merge(sub) == "\\d?"


def test_subexpression_with_zero_or_more():
    sub = RegexBuilder().zero_or_more().digit()
    assert _merge(sub) == "\\d*"


def test_subexpression_with_zero_or_more_lazy():
    sub = RegexBuilder().zero_or_more_lazy().digit()
    assert _merge(sub) == "\\d*?"


def test_subexpression_with_one_or_more():
    sub = RegexBuilder().one_or_more().digit()
    assert _merge(sub) == "\\d+"


def test_subexpression_with_one_or_more_lazy():
    sub = RegexBuilder().one_or_more_lazy().digit()
    assert _merge(sub) == "\\d+?"


def test_subexpression_with_exactly():
    sub = RegexBuilder().exactly(3).digit()
    assert _merge(sub) == "\\d{3}"


def test_subexpression_with_at_least():
    sub = RegexBuilder().at_least(2).digit()
    assert _merge(sub) == "\\d{2,}"


def test_subexpression_with_between():
    sub = RegexBuilder().between(1, 4).digit()
    assert _merge(sub) == "\\d{1,4}"


def test_subexpression_with_between_lazy():
    sub = RegexBuilder().between_lazy(1, 4).digit()
    assert _merge(sub) == "\\d{1,4}?"


def test_subexpression_with_start_of_input_collapses_to_noop():
    sub = RegexBuilder().start_of_input().digit()
    assert _merge(sub) == "\\d"


def test_subexpression_with_end_of_input_collapses_to_noop():
    sub = RegexBuilder().digit().end_of_input()
    assert _merge(sub) == "\\d"
