"""Benchmark: match hot path across matches, near-matches, and non-matches."""

from __future__ import annotations

import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from edify.result import Regex
from tests.bench.cases import BUILDER_FACTORIES, MATCH_SCENARIOS

_MATCH_KINDS = ("matches", "near_matches", "non_matches")


@pytest.mark.parametrize("case_name", list(BUILDER_FACTORIES))
@pytest.mark.parametrize("match_kind", _MATCH_KINDS)
def test_match_bench(case_name: str, match_kind: str, benchmark: BenchmarkFixture):
    factory = BUILDER_FACTORIES[case_name]
    compiled = factory().to_regex()
    inputs = MATCH_SCENARIOS[case_name][match_kind]
    benchmark(_match_all_inputs, compiled, inputs)


def _match_all_inputs(compiled: Regex, inputs: list[str]) -> None:
    for candidate in inputs:
        compiled.search(candidate)
