"""Tests for the per-instance lazy compile cache."""

from edify import Pattern, RegexBuilder


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
