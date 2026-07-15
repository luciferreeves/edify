"""Snapshot suite for the compile-path edge-case fixtures.

Each fixture builds a small, intentionally-tricky pattern and pins the
emitted regex string. The fixtures are the ones most likely to silently
drift when the compile path is refactored: deeply nested alternation,
combined lookaround, item-4 named backreferences, and constructs that
:mod:`edify` flags for ReDoS.
"""

from pathlib import Path

import pytest

from edify import Pattern, RegexBuilder
from edify.testing import assert_snapshot

_SNAPSHOT_ROOT = Path(__file__).parent.parent / "snapshots" / "fixtures"


def _deeply_nested_alternation():
    inner_alt = RegexBuilder().any_of("abc", "def", "ghi")
    outer_alt = RegexBuilder().any_of("first", "second", "third")
    return (
        RegexBuilder()
        .start_of_input()
        .subexpression(inner_alt)
        .string("-")
        .subexpression(outer_alt)
        .end_of_input()
    )


def _combined_lookaround_positive_and_negative():
    return (
        RegexBuilder()
        .assert_ahead()
        .digit()
        .end()
        .assert_not_ahead()
        .string("0")
        .end()
        .assert_behind()
        .string("$")
        .end()
        .digit()
        .digit()
        .digit()
    )


def _named_backreference_pair():
    return (
        RegexBuilder()
        .named_capture("open")
        .any_of("[", "(", "{")
        .end()
        .zero_or_more()
        .word()
        .named_back_reference("open")
    )


def _nested_unbounded_quantifier_redos():
    return RegexBuilder().one_or_more().group().one_or_more().digit().end()


def _alternation_with_overlapping_prefixes_redos():
    return RegexBuilder().one_or_more().any_of("aa", "aaa", "aaaa")


def _hex_color_pattern():
    return (
        RegexBuilder()
        .start_of_input()
        .string("#")
        .any_of_chars("0123456789abcdefABCDEF")
        .exactly(6)
        .word()
        .end_of_input()
    )


def _email_shape_pattern():
    return (
        RegexBuilder()
        .start_of_input()
        .one_or_more()
        .any_of_chars("a-zA-Z0-9._%+-")
        .string("@")
        .one_or_more()
        .any_of_chars("a-zA-Z0-9.-")
        .string(".")
        .at_least(2)
        .letter()
        .end_of_input()
    )


def _pattern_composition_via_use():
    reusable = Pattern().at_least(2).letter()
    return RegexBuilder().start_of_input().subexpression(reusable).end_of_input()


_FIXTURES = [
    ("deeply_nested_alternation", _deeply_nested_alternation),
    ("combined_lookaround", _combined_lookaround_positive_and_negative),
    ("named_backreference_pair", _named_backreference_pair),
    ("nested_unbounded_quantifier_redos", _nested_unbounded_quantifier_redos),
    ("alternation_with_overlapping_prefixes_redos", _alternation_with_overlapping_prefixes_redos),
    ("hex_color_pattern", _hex_color_pattern),
    ("email_shape_pattern", _email_shape_pattern),
    ("pattern_composition_via_use", _pattern_composition_via_use),
]


@pytest.mark.parametrize(
    ("fixture_name", "builder_factory"), _FIXTURES, ids=[name for name, _ in _FIXTURES]
)
def test_edge_case_fixture_emits_the_snapshotted_regex(fixture_name, builder_factory):
    builder = builder_factory()
    emitted = builder.to_regex_string()
    snapshot_path = _SNAPSHOT_ROOT / f"{fixture_name}.regex"
    assert_snapshot(emitted, snapshot_path)


def test_nested_unbounded_quantifier_fixture_raises_the_redos_warning():
    from edify.compile.redos import ReDoSWarning

    with pytest.warns(ReDoSWarning):
        _nested_unbounded_quantifier_redos().to_regex()
