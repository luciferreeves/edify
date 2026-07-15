"""Deterministic cold/warm ratio gate for the per-instance lazy compile cache.

Measures the wall-clock cost of the first ``.to_regex()`` call on a fresh
builder (``cold``) against the cost of a repeat call on the same instance
(``warm``). The cache promise from :issue:`141` is that the warm path is
an order of magnitude cheaper than the cold path — a hardware-independent
ratio that gates the cache contract in a way absolute milliseconds cannot.
"""

from __future__ import annotations

import time

from edify import RegexBuilder


def _hex_number_builder():
    builder = (
        RegexBuilder()
        .start_of_input()
        .assert_ahead()
        .any_of("0x", "0o", "0b")
        .end()
        .capture()
        .any_of("0x", "0o", "0b")
        .end()
        .between(1, 16)
        .any_of_chars("0123456789abcdefABCDEF")
        .end_of_input()
    )
    return builder


def _measure_call_wall_clock(action, iterations):
    start = time.perf_counter()
    for _ in range(iterations):
        action()
    return time.perf_counter() - start


def test_warm_to_regex_is_at_least_ten_times_cheaper_than_cold_to_regex():
    warm_iterations = 200
    cold_iterations = 200

    cold_total = 0.0
    for _ in range(cold_iterations):
        builder = _hex_number_builder()
        cold_start = time.perf_counter()
        builder.to_regex()
        cold_total += time.perf_counter() - cold_start

    warm_builder = _hex_number_builder()
    warm_builder.to_regex()
    warm_total = _measure_call_wall_clock(warm_builder.to_regex, warm_iterations)

    average_cold = cold_total / cold_iterations
    average_warm = warm_total / warm_iterations

    assert average_warm * 10 < average_cold, (
        f"cache ratio too weak: warm={average_warm * 1e6:.2f}µs, "
        f"cold={average_cold * 1e6:.2f}µs — warm should be < cold / 10."
    )


def test_repeat_to_regex_returns_the_same_regex_instance():
    warm_builder = _hex_number_builder()
    first = warm_builder.to_regex()
    second = warm_builder.to_regex()
    assert first is second
