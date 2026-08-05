"""``anything_but_any_of`` is the negated counterpart of the ``any_of`` class frame.

Negation previously covered a set of literal characters or a single range and
nothing that mixed or repeated them, so ``[^a-z0-9]`` had no chain that built it.
"""

from __future__ import annotations

import pytest

from edify import Pattern, RegexBuilder, anything_but_any_of
from edify.errors import EdifySyntaxError

_SYNTACTIC_MEMBERS = ["]", "^", "-", "\\"]


def test_two_ranges_emit_one_negated_class():
    pattern = RegexBuilder().anything_but_any_of().range("a", "z").range("0", "9").end()
    assert pattern.to_regex_string() == "[^a-z0-9]"


def test_a_range_beside_a_literal_emits_one_negated_class():
    pattern = RegexBuilder().anything_but_any_of().range("a", "z").char("_").end()
    assert pattern.to_regex_string() == "[^a-z_]"


def test_a_character_set_emits_one_negated_class():
    pattern = RegexBuilder().anything_but_any_of().any_of_chars("abc").end()
    assert pattern.to_regex_string() == "[^abc]"


def test_a_single_member_still_emits_a_well_formed_class():
    pattern = RegexBuilder().anything_but_any_of().char("a").end()
    assert pattern.to_regex_string() == "[^a]"


def test_the_class_rejects_its_members_and_accepts_everything_else():
    pattern = (
        Pattern()
        .start_of_input()
        .one_or_more()
        .anything_but_any_of()
        .range("a", "z")
        .range("0", "9")
        .end()
        .end_of_input()
    )
    assert pattern("ABC") is True
    assert pattern("!!!") is True
    assert pattern("abc") is False
    assert pattern("a1") is False
    assert pattern("XY9") is False


def test_it_matches_exactly_one_character_at_a_time():
    pattern = Pattern().start_of_input().anything_but_any_of().range("a", "z").end().end_of_input()
    assert pattern("A") is True
    assert pattern("AB") is False


@pytest.mark.parametrize("member", _SYNTACTIC_MEMBERS)
def test_a_syntactic_member_is_excluded_rather_than_changing_the_class(member: str):
    pattern = Pattern().start_of_input().anything_but_any_of().char(member).end().end_of_input()
    assert pattern(member) is False
    assert pattern("q") is True


def test_a_syntactic_member_beside_a_range_keeps_both_meanings():
    pattern = (
        Pattern()
        .start_of_input()
        .anything_but_any_of()
        .range("a", "z")
        .char("^")
        .end()
        .end_of_input()
    )
    assert pattern("^") is False
    assert pattern("m") is False
    assert pattern("!") is True


def test_the_frame_composes_into_a_larger_pattern():
    inner = Pattern().one_or_more().anything_but_any_of().range("a", "z").char("_").end()
    outer = Pattern().start_of_input().string("x=").use(inner).end_of_input()
    assert outer.to_regex_string() == "^x=[^a-z_]+$"
    assert outer("x=ABC") is True
    assert outer("x=a_") is False


def test_the_factory_builds_the_same_class_as_the_chain():
    from_factory = anything_but_any_of(Pattern().range("a", "z"), Pattern().range("0", "9"))
    from_chain = RegexBuilder().anything_but_any_of().range("a", "z").range("0", "9").end()
    assert from_factory.to_regex_string() == from_chain.to_regex_string()


def test_the_factory_rejects_an_empty_member_list():
    with pytest.raises(EdifySyntaxError) as raised:
        anything_but_any_of()
    assert "requires at least one operand" in str(raised.value)


def test_a_multi_character_member_is_refused_with_an_actionable_error():
    with pytest.raises(EdifySyntaxError) as raised:
        RegexBuilder().anything_but_any_of().string("ab").end().to_regex_string()
    message = str(raised.value)
    assert "cannot negate the multi-character string 'ab'" in message
    assert "anything_but_string" in message


def test_an_empty_frame_is_refused_rather_than_emitting_an_invalid_class():
    with pytest.raises(EdifySyntaxError) as raised:
        RegexBuilder().anything_but_any_of().end().to_regex_string()
    assert "requires at least one operand" in str(raised.value)


def test_a_token_that_is_not_one_character_wide_is_refused():
    with pytest.raises(EdifySyntaxError) as raised:
        RegexBuilder().anything_but_any_of().digit().end().to_regex_string()
    assert "cannot negate a digit member" in str(raised.value)


def test_a_single_member_explanation_names_just_that_member():
    explanation = (
        Pattern()
        .start_of_input()
        .anything_but_any_of()
        .char("q")
        .end()
        .end_of_input()
        .to_regex()
        .explain()
    )
    assert 'one character NOT from "q"' in explanation


def test_a_character_set_member_is_named_as_a_set():
    explanation = (
        Pattern()
        .start_of_input()
        .anything_but_any_of()
        .any_of_chars("abc")
        .end()
        .end_of_input()
        .to_regex()
        .explain()
    )
    assert 'the set "abc"' in explanation


def test_the_example_avoids_every_kind_of_member():
    pattern = (
        Pattern()
        .start_of_input()
        .anything_but_any_of()
        .range("a", "y")
        .any_of_chars("z")
        .char("0")
        .end()
        .end_of_input()
    )
    explanation = pattern.to_regex().explain()
    examples = [line.strip() for line in explanation.splitlines() if line.startswith("    ")]
    assert examples
    for example in examples:
        assert pattern(example) is True


def test_the_diagram_labels_a_character_set_member():
    from edify.introspect import visualize_elements

    builder = RegexBuilder().anything_but_any_of().any_of_chars("abc").end()
    assert '"abc"' in visualize_elements(builder.state.stack[0].children)


def test_an_unclosed_frame_names_the_method_that_opened_it():
    with pytest.raises(EdifySyntaxError) as raised:
        RegexBuilder().anything_but_any_of().range("a", "z").to_regex_string()
    assert "anything_but_any_of()" in str(raised.value)


def test_the_class_survives_a_serialization_round_trip():
    from edify.serialize import dict_to_state, state_to_dict

    original = RegexBuilder().one_or_more().anything_but_any_of().range("a", "z").end()
    restored = RegexBuilder().with_state(dict_to_state(state_to_dict(original.state)))
    assert restored.to_regex_string() == original.to_regex_string()


def test_the_explanation_names_the_rejected_members_and_offers_an_example():
    explanation = (
        RegexBuilder()
        .start_of_input()
        .one_or_more()
        .anything_but_any_of()
        .range("a", "z")
        .range("0", "9")
        .end()
        .end_of_input()
        .to_regex()
        .explain()
    )
    assert 'characters NOT from "a" through "z" or "0" through "9"' in explanation
    assert "AnythingButAnyOf" not in explanation


def test_the_explanation_example_is_a_string_the_pattern_accepts():
    pattern = (
        Pattern()
        .start_of_input()
        .anything_but_any_of()
        .range("a", "z")
        .char("_")
        .end()
        .end_of_input()
    )
    explanation = pattern.to_regex().explain()
    examples = [line.strip() for line in explanation.splitlines() if line.startswith("    ")]
    assert examples
    for example in examples:
        assert pattern(example) is True


def test_the_diagram_labels_the_class_without_leaking_the_element_name():
    from edify.introspect import visualize_elements

    builder = RegexBuilder().anything_but_any_of().range("a", "z").char("_").end()
    diagram = visualize_elements(builder.state.stack[0].children)
    assert 'anything except "a"-"z", "_"' in diagram
    assert "AnythingButAnyOf" not in diagram


def test_the_verbose_form_renders_the_negated_class():
    from edify.introspect import verbose_elements

    builder = RegexBuilder().one_or_more().anything_but_any_of().range("a", "z").end()
    assert "[^a-z]" in verbose_elements(builder.state.stack[0].children)
