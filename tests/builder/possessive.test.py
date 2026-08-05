"""Atomic groups and possessive quantifiers — the constructs the ReDoS warning recommends.

Both reached stdlib ``re`` in Python 3.11, which edify already requires, so these
need no alternate engine. What matters is the behaviour, not the emitted text:
a possessive or atomic construct matches as much as it can and then refuses to
give any of it back, which is invisible in the pattern string and only shows up
in what matches.
"""

from __future__ import annotations

import warnings
from collections.abc import Callable

import pytest

from edify import (
    Pattern,
    RegexBuilder,
    at_least_possessive,
    at_most_possessive,
    atomic,
    between_possessive,
    one_or_more_possessive,
    optional_possessive,
    zero_or_more_possessive,
)
from edify.compile.redos import ReDoSWarning
from edify.errors import EdifySyntaxError
from edify.introspect import verbose_elements, visualize_elements
from edify.serialize import dict_to_state, state_to_dict

_POSSESSIVE_EMISSIONS = [
    ("optional_possessive", (), "[a-zA-Z]?+"),
    ("zero_or_more_possessive", (), "[a-zA-Z]*+"),
    ("one_or_more_possessive", (), "[a-zA-Z]++"),
    ("at_least_possessive", (2,), "[a-zA-Z]{2,}+"),
    ("at_most_possessive", (3,), "[a-zA-Z]{0,3}+"),
    ("between_possessive", (2, 4), "[a-zA-Z]{2,4}+"),
]


def _warns_redos(builder: RegexBuilder) -> bool:
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        builder.to_regex()
        return any(issubclass(warning.category, ReDoSWarning) for warning in caught)


@pytest.mark.parametrize(("method_name", "arguments", "expected"), _POSSESSIVE_EMISSIONS)
def test_each_possessive_quantifier_emits_its_suffix(
    method_name: str, arguments: tuple[int, ...], expected: str
):
    builder = getattr(RegexBuilder(), method_name)(*arguments).letter()
    assert builder.to_regex_string() == expected


def test_atomic_emits_a_non_backtracking_group():
    assert RegexBuilder().atomic().one_or_more().letter().end().to_regex_string() == "(?>[a-zA-Z]+)"


def test_a_greedy_quantifier_gives_back_so_the_trailing_character_can_match():
    greedy = Pattern().start_of_input().one_or_more().char("a").char("a").end_of_input()
    assert greedy("aa") is True


def test_a_possessive_quantifier_refuses_to_give_back():
    possessive = (
        Pattern().start_of_input().one_or_more_possessive().char("a").char("a").end_of_input()
    )
    assert possessive.to_regex_string() == "^a++a$"
    assert possessive("aa") is False


def test_an_atomic_group_refuses_to_give_back():
    atomic_pattern = (
        Pattern().start_of_input().atomic().one_or_more().char("a").end().char("a").end_of_input()
    )
    assert atomic_pattern.to_regex_string() == "^(?>a+)a$"
    assert atomic_pattern("aa") is False


def test_a_possessive_quantifier_still_matches_when_nothing_must_be_given_back():
    possessive = Pattern().start_of_input().one_or_more_possessive().char("a").end_of_input()
    assert possessive("aaa") is True


def test_optional_possessive_matches_zero_or_one():
    pattern = Pattern().start_of_input().optional_possessive().char("a").end_of_input()
    assert pattern("") is True
    assert pattern("a") is True
    assert pattern("aa") is False


def test_at_most_possessive_bounds_the_upper_end():
    pattern = Pattern().start_of_input().at_most_possessive(2).char("a").end_of_input()
    assert pattern("") is True
    assert pattern("aa") is True
    assert pattern("aaa") is False


def test_between_possessive_bounds_both_ends():
    pattern = Pattern().start_of_input().between_possessive(2, 3).char("a").end_of_input()
    assert pattern("a") is False
    assert pattern("aa") is True
    assert pattern("aaa") is True
    assert pattern("aaaa") is False


def test_at_least_possessive_bounds_the_lower_end():
    pattern = Pattern().start_of_input().at_least_possessive(2).char("a").end_of_input()
    assert pattern("a") is False
    assert pattern("aaaa") is True


def test_an_atomic_group_composes_inside_a_larger_pattern():
    inner = Pattern().atomic().one_or_more().letter().end()
    outer = Pattern().start_of_input().string("x=").use(inner).end_of_input()
    assert outer.to_regex_string() == "^x=(?>[a-zA-Z]+)$"
    assert outer("x=abc") is True


def test_the_factories_match_the_chain_methods():
    assert atomic(Pattern().one_or_more().letter()).to_regex_string() == "(?>[a-zA-Z]+)"
    assert one_or_more_possessive(Pattern().letter()).to_regex_string() == "[a-zA-Z]++"
    assert zero_or_more_possessive(Pattern().letter()).to_regex_string() == "[a-zA-Z]*+"
    assert optional_possessive(Pattern().letter()).to_regex_string() == "[a-zA-Z]?+"
    assert at_least_possessive(2, Pattern().letter()).to_regex_string() == "[a-zA-Z]{2,}+"
    assert at_most_possessive(3, Pattern().letter()).to_regex_string() == "[a-zA-Z]{0,3}+"
    assert between_possessive(2, 4, Pattern().letter()).to_regex_string() == "[a-zA-Z]{2,4}+"


def test_the_possessive_factories_validate_their_bounds():
    with pytest.raises(EdifySyntaxError):
        at_least_possessive(0, Pattern().letter())
    with pytest.raises(EdifySyntaxError):
        at_most_possessive(0, Pattern().letter())
    with pytest.raises(EdifySyntaxError):
        between_possessive(4, 2, Pattern().letter())


def test_the_possessive_methods_validate_their_bounds():
    with pytest.raises(EdifySyntaxError):
        RegexBuilder().at_least_possessive(0)
    with pytest.raises(EdifySyntaxError):
        RegexBuilder().at_most_possessive(0)
    with pytest.raises(EdifySyntaxError):
        RegexBuilder().between_possessive(4, 2)
    with pytest.raises(EdifySyntaxError):
        RegexBuilder().between_possessive(-1, 2)


def test_the_classic_vulnerable_shape_still_warns():
    assert _warns_redos(RegexBuilder().one_or_more().group().one_or_more().letter().end()) is True


@pytest.mark.parametrize(
    "builder_factory",
    [
        lambda: RegexBuilder().one_or_more_possessive().group().one_or_more().letter().end(),
        lambda: RegexBuilder().one_or_more().group().one_or_more_possessive().letter().end(),
        lambda: RegexBuilder().one_or_more().atomic().one_or_more().letter().end(),
        lambda: RegexBuilder().zero_or_more_possessive().group().zero_or_more().letter().end(),
    ],
)
def test_a_shape_that_cannot_backtrack_does_not_warn(
    builder_factory: Callable[[], RegexBuilder],
):
    assert _warns_redos(builder_factory()) is False


def test_the_warning_names_the_methods_that_fix_it():
    with pytest.warns(ReDoSWarning) as record:
        RegexBuilder().one_or_more().group().one_or_more().letter().end().to_regex()
    message = str(record[0].message)
    assert ".atomic()" in message
    assert ".one_or_more_possessive()" in message
    assert "engine=" not in message


def test_an_unclosed_atomic_frame_names_the_method_that_opened_it():
    with pytest.raises(EdifySyntaxError) as raised:
        RegexBuilder().atomic().one_or_more().letter().to_regex_string()
    assert "atomic()" in str(raised.value)


@pytest.mark.parametrize(("method_name", "arguments", "_expected"), _POSSESSIVE_EMISSIONS)
def test_each_possessive_quantifier_survives_a_serialization_round_trip(
    method_name: str, arguments: tuple[int, ...], _expected: str
):
    original = getattr(RegexBuilder(), method_name)(*arguments).letter()
    restored = RegexBuilder().with_state(dict_to_state(state_to_dict(original.state)))
    assert restored.to_regex_string() == original.to_regex_string()


def test_an_atomic_group_survives_a_serialization_round_trip():
    original = RegexBuilder().atomic().one_or_more().letter().end()
    restored = RegexBuilder().with_state(dict_to_state(state_to_dict(original.state)))
    assert restored.to_regex_string() == original.to_regex_string()


@pytest.mark.parametrize(("method_name", "arguments", "_expected"), _POSSESSIVE_EMISSIONS)
def test_each_possessive_quantifier_is_explained_without_leaking_its_class(
    method_name: str, arguments: tuple[int, ...], _expected: str
):
    builder = getattr(RegexBuilder(), method_name)(*arguments).letter()
    explanation = builder.to_regex().explain()
    assert "never given back" in explanation
    assert "Element" not in explanation


def test_an_atomic_group_is_explained_without_leaking_its_class():
    explanation = RegexBuilder().atomic().one_or_more().letter().end().to_regex().explain()
    assert "never given back" in explanation
    assert "Element" not in explanation


@pytest.mark.parametrize(("method_name", "arguments", "_expected"), _POSSESSIVE_EMISSIONS)
def test_each_possessive_quantifier_is_annotated_in_the_verbose_form(
    method_name: str, arguments: tuple[int, ...], _expected: str
):
    builder = getattr(RegexBuilder(), method_name)(*arguments).letter()
    rendered = verbose_elements(builder.state.stack[0].children)
    assert "(possessive)" in rendered
    assert "unrecognized" not in rendered


def test_the_atomic_group_is_annotated_in_the_verbose_form():
    builder = RegexBuilder().atomic().one_or_more().letter().end()
    rendered = verbose_elements(builder.state.stack[0].children)
    assert "begin atomic group (never gives back)" in rendered
    assert "unrecognized" not in rendered


@pytest.mark.parametrize(("method_name", "arguments", "_expected"), _POSSESSIVE_EMISSIONS)
def test_each_possessive_quantifier_is_labelled_in_the_diagram(
    method_name: str, arguments: tuple[int, ...], _expected: str
):
    builder = getattr(RegexBuilder(), method_name)(*arguments).letter()
    diagram = visualize_elements(builder.state.stack[0].children)
    assert "(possessive)" in diagram
    assert "Element" not in diagram


def test_the_atomic_group_is_labelled_in_the_diagram():
    builder = RegexBuilder().atomic().one_or_more().letter().end()
    diagram = visualize_elements(builder.state.stack[0].children)
    assert "atomic" in diagram
    assert "Element" not in diagram


@pytest.mark.parametrize(("method_name", "arguments", "_expected"), _POSSESSIVE_EMISSIONS)
def test_a_nested_possessive_quantifier_is_described_inline(
    method_name: str, arguments: tuple[int, ...], _expected: str
):
    builder = getattr(RegexBuilder().capture(), method_name)(*arguments).letter().end()
    explanation = builder.to_regex().explain()
    assert "Element" not in explanation


def test_a_nested_atomic_group_is_described_inline():
    builder = RegexBuilder().capture().atomic().one_or_more().letter().end().end()
    assert "Element" not in builder.to_regex().explain()


@pytest.mark.parametrize(("method_name", "arguments", "_expected"), _POSSESSIVE_EMISSIONS)
def test_each_possessive_quantifier_is_labelled_in_the_graph_diagram(
    method_name: str, arguments: tuple[int, ...], _expected: str
):
    builder = getattr(RegexBuilder(), method_name)(*arguments).group().letter().end()
    rendered = visualize_elements(builder.state.stack[0].children, format="svg", engine="graphviz")
    assert "possessive" in rendered


def test_the_atomic_group_is_labelled_in_the_graph_diagram():
    builder = RegexBuilder().atomic().one_or_more().letter().end()
    rendered = visualize_elements(builder.state.stack[0].children, format="svg", engine="graphviz")
    assert "atomic" in rendered
