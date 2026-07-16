"""Property — builder emitted-pattern equivalence against a hand-rolled reference impl."""

import re

from hypothesis import given
from hypothesis import strategies as strategy

from edify import RegexBuilder

_LITERAL_ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789-_"


@given(
    strategy.lists(
        strategy.text(alphabet=_LITERAL_ALPHABET, min_size=1, max_size=8), min_size=1, max_size=6
    )
)
def test_concatenated_string_calls_emit_the_re_escape_concatenation(literal_segments: list[str]):
    builder = RegexBuilder()
    for literal in literal_segments:
        builder = builder.string(literal)
    emitted = builder.to_regex_string()
    escaped_segments = [re.escape(literal) for literal in literal_segments]
    reference = "".join(escaped_segments)
    assert emitted == reference


@given(strategy.text(alphabet=_LITERAL_ALPHABET, min_size=1, max_size=32))
def test_string_terminal_matches_the_reference_re_escape_output(literal_value: str):
    emitted = RegexBuilder().string(literal_value).to_regex_string()
    reference = re.escape(literal_value)
    assert emitted == reference


@given(strategy.lists(strategy.sampled_from("abcdef012"), min_size=1, max_size=6, unique=True))
def test_any_of_chars_emits_a_char_class_containing_every_input_character(class_members: list[str]):
    body = "".join(class_members)
    emitted = RegexBuilder().any_of_chars(body).to_regex_string()
    reference = f"[{body}]"
    assert emitted == reference


@given(
    strategy.integers(min_value=1, max_value=8),
    strategy.sampled_from(["digit", "word", "letter"]),
)
def test_exactly_n_of_a_class_emits_class_with_brace_quantifier(count: int, class_name: str):
    builder = getattr(RegexBuilder().exactly(count), class_name)()
    emitted = builder.to_regex_string()
    class_source = {"digit": r"\d", "word": r"\w", "letter": r"[a-zA-Z]"}[class_name]
    assert emitted == f"{class_source}{{{count}}}"
