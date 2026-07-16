"""Property — ``Pattern.from_dict(pattern.to_dict())`` roundtrips every generated pattern."""

from hypothesis import given
from hypothesis import strategies as strategy

from edify import Pattern

_LITERAL_ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789"


def _string_pattern(text: str) -> Pattern:
    return Pattern().string(text)


def _any_of_chars_pattern(body: str) -> Pattern:
    return Pattern().any_of_chars(body)


def _pattern_strategy() -> strategy.SearchStrategy[Pattern]:
    text_strategy = strategy.text(alphabet=_LITERAL_ALPHABET, min_size=1, max_size=6)
    class_body_strategy = strategy.text(alphabet=_LITERAL_ALPHABET, min_size=1, max_size=4)
    leaves = strategy.one_of(
        text_strategy.map(_string_pattern),
        strategy.builds(lambda: Pattern().digit()),
        strategy.builds(lambda: Pattern().word()),
        strategy.builds(lambda: Pattern().letter()),
        class_body_strategy.map(_any_of_chars_pattern),
    )
    return strategy.recursive(
        leaves,
        lambda children: strategy.one_of(
            children.map(_wrap_in_capture),
            children.map(_wrap_in_group),
            children.map(_wrap_in_one_or_more),
            children.map(_wrap_in_optional),
        ),
        max_leaves=4,
    )


def _wrap_in_capture(inner: Pattern) -> Pattern:
    return Pattern().capture().subexpression(inner).end()


def _wrap_in_group(inner: Pattern) -> Pattern:
    return Pattern().group().subexpression(inner).end()


def _wrap_in_one_or_more(inner: Pattern) -> Pattern:
    return Pattern().one_or_more().subexpression(inner)


def _wrap_in_optional(inner: Pattern) -> Pattern:
    return Pattern().optional().subexpression(inner)


@given(_pattern_strategy())
def test_dict_roundtrip_preserves_the_emitted_regex_string(original_pattern: Pattern):
    document = original_pattern.to_dict()
    reconstructed_pattern = Pattern.from_dict(document)
    assert reconstructed_pattern.to_regex_string() == original_pattern.to_regex_string()


@given(_pattern_strategy())
def test_json_roundtrip_preserves_the_emitted_regex_string(original_pattern: Pattern):
    payload = original_pattern.to_json()
    reconstructed_pattern = Pattern.from_json(payload)
    assert reconstructed_pattern.to_regex_string() == original_pattern.to_regex_string()
