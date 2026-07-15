"""Property — ``Pattern.from_dict(pattern.to_dict())`` roundtrips every generated pattern."""

from hypothesis import given
from hypothesis import strategies as strategy

from edify import Pattern

_LITERAL_ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789"


def _pattern_strategy():
    return strategy.recursive(
        strategy.one_of(
            strategy.builds(
                lambda text: Pattern().string(text),
                strategy.text(alphabet=_LITERAL_ALPHABET, min_size=1, max_size=6),
            ),
            strategy.builds(lambda: Pattern().digit()),
            strategy.builds(lambda: Pattern().word()),
            strategy.builds(lambda: Pattern().letter()),
            strategy.builds(
                lambda body: Pattern().any_of_chars(body),
                strategy.text(alphabet=_LITERAL_ALPHABET, min_size=1, max_size=4),
            ),
        ),
        lambda children: strategy.one_of(
            strategy.builds(_wrap_in_capture, children),
            strategy.builds(_wrap_in_group, children),
            strategy.builds(_wrap_in_one_or_more, children),
            strategy.builds(_wrap_in_optional, children),
        ),
        max_leaves=4,
    )


def _wrap_in_capture(inner):
    return Pattern().capture().subexpression(inner).end()


def _wrap_in_group(inner):
    return Pattern().group().subexpression(inner).end()


def _wrap_in_one_or_more(inner):
    return Pattern().one_or_more().subexpression(inner)


def _wrap_in_optional(inner):
    return Pattern().optional().subexpression(inner)


@given(_pattern_strategy())
def test_dict_roundtrip_preserves_the_emitted_regex_string(original_pattern):
    document = original_pattern.to_dict()
    reconstructed_pattern = Pattern.from_dict(document)
    assert reconstructed_pattern.to_regex_string() == original_pattern.to_regex_string()


@given(_pattern_strategy())
def test_json_roundtrip_preserves_the_emitted_regex_string(original_pattern):
    payload = original_pattern.to_json()
    reconstructed_pattern = Pattern.from_json(payload)
    assert reconstructed_pattern.to_regex_string() == original_pattern.to_regex_string()
