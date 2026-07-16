"""Property — ``RegexBuilder.from_regex(source)`` roundtrips behaviorally.

Fuzz the constructs the reverse parser supports and verify that the emitted
pattern from the rebuilt chain matches the same corpus as the original raw
regex string.
"""

import re

from hypothesis import assume, given
from hypothesis import strategies as strategy

from edify import RegexBuilder

_LITERAL_ALPHABET = "abcdef0123"


def _simple_regex_strategy() -> strategy.SearchStrategy[str]:
    literal_strategy = strategy.text(alphabet=_LITERAL_ALPHABET, min_size=1, max_size=4)
    class_strategy = strategy.text(alphabet=_LITERAL_ALPHABET, min_size=1, max_size=4).map(
        lambda body: f"[{body}]"
    )
    return strategy.one_of(
        literal_strategy,
        class_strategy,
        strategy.sampled_from([r"\d", r"\w", r"\s", "."]),
    )


_QUANTIFIER_SUFFIX_STRATEGY = strategy.one_of(
    strategy.just(""),
    strategy.just("+"),
    strategy.just("*"),
    strategy.just("?"),
    strategy.integers(min_value=1, max_value=4).map(lambda n: f"{{{n}}}"),
)


@given(_simple_regex_strategy(), _QUANTIFIER_SUFFIX_STRATEGY)
def test_from_regex_roundtrip_preserves_match_behavior_on_the_source_alphabet(
    atom: str, suffix: str
):
    source_pattern = f"{atom}{suffix}"
    _assume_compilable(source_pattern)
    reconstructed_builder = RegexBuilder.from_regex(source_pattern)
    reconstructed_source = reconstructed_builder.to_regex_string()

    original_compiled = re.compile(source_pattern)
    reconstructed_compiled = re.compile(reconstructed_source)

    for candidate in _corpus():
        assert bool(original_compiled.search(candidate)) == bool(
            reconstructed_compiled.search(candidate)
        )


def _assume_compilable(source_pattern: str) -> None:
    try:
        re.compile(source_pattern)
    except re.error:
        assume(False)


def _corpus() -> list[str]:
    return [
        "",
        "a",
        "abcdef",
        "0123",
        "abc123",
        "abcxyz",
        "z",
        " ",
        "\n",
        "aabbcc",
        "0",
        "9",
    ]
