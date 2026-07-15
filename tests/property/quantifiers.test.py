"""Property — no chain silently drops a quantifier (count parity)."""

import re

from hypothesis import given
from hypothesis import strategies as strategy

from edify import RegexBuilder

_QUANTIFIER_ELEMENTS = ["digit", "word", "letter", "any_char"]


_ZERO_OR_MORE_METHOD = "zero_or_more"
_ONE_OR_MORE_METHOD = "one_or_more"
_OPTIONAL_METHOD = "optional"


_QUANTIFIER_METHOD_STRATEGY = strategy.sampled_from(
    [_ZERO_OR_MORE_METHOD, _ONE_OR_MORE_METHOD, _OPTIONAL_METHOD]
)


_QUANTIFIER_SUFFIX_PATTERN = re.compile(r"[+*?]|\{[0-9,]+\}")


@given(strategy.lists(_QUANTIFIER_METHOD_STRATEGY, min_size=1, max_size=8))
def test_every_bare_quantifier_call_produces_one_output_quantifier(quantifier_calls):
    builder = RegexBuilder()
    for quantifier_method in quantifier_calls:
        quantifier_bound = getattr(builder, quantifier_method)()
        builder = quantifier_bound.digit()
    emitted = builder.to_regex_string()
    output_quantifier_count = len(_QUANTIFIER_SUFFIX_PATTERN.findall(emitted))
    assert output_quantifier_count == len(quantifier_calls), (
        f"chain declared {len(quantifier_calls)} quantifier calls but emitted "
        f"{output_quantifier_count} quantifier suffixes in {emitted!r}"
    )


@given(
    strategy.lists(
        strategy.tuples(
            strategy.integers(min_value=1, max_value=8),
            strategy.integers(min_value=1, max_value=8),
        ),
        min_size=1,
        max_size=5,
    )
)
def test_between_calls_produce_a_brace_quantifier_per_call(min_max_pairs):
    builder = RegexBuilder()
    expected_quantifiers = 0
    for lower_bound, extra in min_max_pairs:
        upper_bound = lower_bound + extra
        builder = builder.between(lower_bound, upper_bound).digit()
        expected_quantifiers += 1
    emitted = builder.to_regex_string()
    output_quantifier_count = len(_QUANTIFIER_SUFFIX_PATTERN.findall(emitted))
    assert output_quantifier_count == expected_quantifiers
