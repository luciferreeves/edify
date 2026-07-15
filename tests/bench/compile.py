"""Benchmark: compile-path wall clock across the simple/medium/complex cases."""

from __future__ import annotations

import pytest

from tests.bench.cases import BUILDER_FACTORIES


@pytest.mark.parametrize("case_name", list(BUILDER_FACTORIES))
def test_compile_bench(case_name, benchmark):
    factory = BUILDER_FACTORIES[case_name]
    benchmark(lambda: factory().to_regex())


@pytest.mark.parametrize("case_name", list(BUILDER_FACTORIES))
def test_to_regex_string_bench(case_name, benchmark):
    factory = BUILDER_FACTORIES[case_name]
    benchmark(lambda: factory().to_regex_string())
