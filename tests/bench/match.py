"""Benchmark: match hot path across matches, near-matches, and non-matches."""

from __future__ import annotations

import pytest

from tests.bench.cases import BUILDER_FACTORIES, MATCH_SCENARIOS

_MATCH_KINDS = ("matches", "near_matches", "non_matches")


@pytest.mark.parametrize("case_name", list(BUILDER_FACTORIES))
@pytest.mark.parametrize("match_kind", _MATCH_KINDS)
def test_match_bench(case_name, match_kind, benchmark):
    factory = BUILDER_FACTORIES[case_name]
    compiled = factory().to_regex()
    inputs = MATCH_SCENARIOS[case_name][match_kind]
    benchmark(_match_all_inputs, compiled, inputs)


def _match_all_inputs(compiled, inputs):
    for candidate in inputs:
        compiled.search(candidate)
