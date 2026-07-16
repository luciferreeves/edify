"""Tests for the per-instance lazy compile cache — semantics and cold/warm ratio."""

import time

from edify import Pattern, RegexBuilder


def _hex_number_builder():
    return (
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


def _measure_call_wall_clock(action, iterations):
    start = time.perf_counter()
    for _ in range(iterations):
        action()
    return time.perf_counter() - start


def test_two_no_kwargs_to_regex_calls_return_the_same_instance():
    builder = RegexBuilder().one_or_more().digit()
    first = builder.to_regex()
    second = builder.to_regex()
    assert first is second


def test_matcher_call_shares_the_cache_with_to_regex():
    builder = RegexBuilder().one_or_more().digit()
    first = builder.to_regex()
    builder.test("42")
    assert builder.to_regex() is first


def test_kwarg_call_bypasses_the_cache_and_never_populates_it():
    builder = RegexBuilder().string("ABC")
    with_kwargs = builder.to_regex(ignore_case=True)
    default = builder.to_regex()
    assert with_kwargs is not default
    assert builder.to_regex() is default


def test_regex_engine_kwarg_bypasses_the_cache():
    builder = RegexBuilder().digit()
    default = builder.to_regex()
    via_regex = builder.to_regex(engine="regex")
    assert default is not via_regex
    assert default.engine == "re"
    assert via_regex.engine == "regex"


def test_kwarg_call_first_still_leaves_a_default_no_kwargs_call_cacheable():
    builder = RegexBuilder().string("hi")
    builder.to_regex(ignore_case=True)
    first_default = builder.to_regex()
    second_default = builder.to_regex()
    assert first_default is second_default


def test_forked_builder_gets_its_own_empty_cache():
    parent = RegexBuilder().digit()
    parent.to_regex()
    child = parent.fork()
    assert child.to_regex() is child.to_regex()
    assert parent.to_regex() is not child.to_regex()


def test_chain_step_yields_a_fresh_cache_slot():
    root = RegexBuilder().digit()
    original = root.to_regex()
    extended = root.word()
    extended_regex = extended.to_regex()
    assert extended_regex is not original


def test_pattern_also_caches_across_repeat_to_regex_calls():
    pattern = Pattern().string("hi")
    assert pattern.to_regex() is pattern.to_regex()


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
