"""Unicode-aware character classes — saying "any letter" and meaning it.

``letter()`` emits ``[a-zA-Z]``, so a name field built on it silently rejects a
large fraction of the world's names, and ``word()`` admits digits and underscore.
These four classes emit ``\\p{...}`` property escapes, which stdlib ``re`` does
not implement at all, so they require the third-party engine and say so loudly
rather than emitting something other than what the method name promises.
"""

from __future__ import annotations

import pytest

from edify import Pattern, RegexBuilder
from edify.errors import EdifySyntaxError
from edify.introspect import verbose_elements, visualize_elements
from edify.serialize import dict_to_state, state_to_dict

_EMISSIONS = [
    ("unicode_letter", "\\p{L}"),
    ("unicode_uppercase", "\\p{Lu}"),
    ("unicode_lowercase", "\\p{Ll}"),
    ("unicode_alphanumeric", "[\\p{L}\\p{N}]"),
]

_ACCEPTED = {
    "unicode_letter": ["café", "日本語", "hello", "Ω", "мир"],
    "unicode_uppercase": ["ÉÑ", "ΛΔ", "ABC"],
    "unicode_lowercase": ["café", "λδ", "abc"],
    "unicode_alphanumeric": ["café1", "日本語2", "abc123"],
}

_REJECTED = {
    "unicode_letter": ["abc123", "a b", "", "_"],
    "unicode_uppercase": ["abc", "É1", ""],
    "unicode_lowercase": ["ABC", "é1", ""],
    "unicode_alphanumeric": ["abc_123", "a b", ""],
}


def _anchored(method_name: str) -> Pattern:
    builder = Pattern().start_of_input().one_or_more()
    return getattr(builder, method_name)().end_of_input()


@pytest.mark.parametrize(("method_name", "expected"), _EMISSIONS)
def test_each_class_emits_its_property_escape(method_name: str, expected: str):
    assert getattr(RegexBuilder(), method_name)().to_regex_string() == expected


@pytest.mark.parametrize("method_name", list(_ACCEPTED))
def test_each_class_accepts_letters_from_several_scripts(method_name: str):
    compiled = _anchored(method_name).to_regex(engine="regex")
    for candidate in _ACCEPTED[method_name]:
        assert compiled.match(candidate) is not None, candidate


@pytest.mark.parametrize("method_name", list(_REJECTED))
def test_each_class_rejects_what_it_should(method_name: str):
    compiled = _anchored(method_name).to_regex(engine="regex")
    for candidate in _REJECTED[method_name]:
        assert compiled.match(candidate) is None, candidate


def test_the_ascii_letter_class_is_the_bug_these_fix():
    ascii_only = Pattern().start_of_input().one_or_more().letter().end_of_input()
    assert ascii_only("café") is False
    assert _anchored("unicode_letter").to_regex(engine="regex").match("café") is not None


def test_unicode_alphanumeric_excludes_the_underscore_that_word_admits():
    with_word = Pattern().start_of_input().one_or_more().word().end_of_input()
    assert with_word("abc_123") is True
    compiled = _anchored("unicode_alphanumeric").to_regex(engine="regex")
    assert compiled.match("abc_123") is None


def test_case_folding_that_is_not_one_to_one_is_still_lowercase():
    compiled = _anchored("unicode_lowercase").to_regex(engine="regex")
    assert compiled.match("ß") is not None


@pytest.mark.parametrize(("method_name", "_expected"), _EMISSIONS)
def test_the_chain_is_constructible_without_choosing_an_engine(method_name: str, _expected: str):
    builder = getattr(RegexBuilder(), method_name)()
    assert builder.to_regex_string()


@pytest.mark.parametrize(("method_name", "_expected"), _EMISSIONS)
def test_compiling_under_the_stdlib_engine_raises(method_name: str, _expected: str):
    with pytest.raises(EdifySyntaxError):
        getattr(RegexBuilder(), method_name)().to_regex(engine="re")


def test_the_stdlib_error_names_the_extra_and_the_method():
    with pytest.raises(EdifySyntaxError) as raised:
        RegexBuilder().unicode_letter().to_regex(engine="re")
    message = str(raised.value)
    assert "pip install edify[regex]" in message
    assert "unicode_letter" in message


def test_the_default_engine_is_the_one_that_raises():
    with pytest.raises(EdifySyntaxError):
        RegexBuilder().unicode_letter().to_regex()


def test_the_emitted_pattern_does_not_depend_on_the_engine():
    builder = RegexBuilder().unicode_letter()
    assert builder.to_regex_string() == builder.to_regex(engine="regex").source


@pytest.mark.parametrize(("method_name", "_expected"), _EMISSIONS)
def test_each_class_survives_a_serialization_round_trip(method_name: str, _expected: str):
    original = getattr(RegexBuilder(), method_name)()
    restored = RegexBuilder().with_state(dict_to_state(state_to_dict(original.state)))
    assert restored.to_regex_string() == original.to_regex_string()


@pytest.mark.parametrize(("method_name", "_expected"), _EMISSIONS)
def test_each_class_is_explained_without_leaking_its_element_name(method_name: str, _expected: str):
    explanation = _anchored(method_name).to_regex(engine="regex").explain()
    assert "in any script" in explanation
    assert "Element" not in explanation


@pytest.mark.parametrize(("method_name", "_expected"), _EMISSIONS)
def test_the_explanation_examples_are_strings_the_pattern_accepts(method_name: str, _expected: str):
    compiled = _anchored(method_name).to_regex(engine="regex")
    explanation = compiled.explain()
    examples = [line.strip() for line in explanation.splitlines() if line.startswith("    ")]
    assert examples
    for example in examples:
        assert compiled.match(example) is not None, example


@pytest.mark.parametrize(("method_name", "_expected"), _EMISSIONS)
def test_each_class_is_annotated_in_the_verbose_form(method_name: str, _expected: str):
    builder = getattr(RegexBuilder(), method_name)()
    rendered = verbose_elements(builder.state.stack[0].children)
    assert "in any script" in rendered
    assert "unrecognized" not in rendered


@pytest.mark.parametrize(("method_name", "_expected"), _EMISSIONS)
def test_each_class_is_labelled_in_the_diagram(method_name: str, _expected: str):
    builder = getattr(RegexBuilder(), method_name)()
    diagram = visualize_elements(builder.state.stack[0].children)
    assert "Unicode" in diagram
    assert "Element" not in diagram


@pytest.mark.parametrize(("method_name", "_expected"), _EMISSIONS)
def test_each_class_is_described_inline_when_nested(method_name: str, _expected: str):
    builder = getattr(RegexBuilder().capture(), method_name)().end()
    explanation = builder.to_regex(engine="regex").explain()
    assert "Element" not in explanation
