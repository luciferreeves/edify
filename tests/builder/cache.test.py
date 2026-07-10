"""Tests for the lazy :class:`Regex` cache on :class:`BuilderCore`."""

from edify import Pattern, RegexBuilder


def test_repeated_lazy_regex_calls_return_the_same_instance():
    builder = RegexBuilder().digit()
    first = builder._lazy_regex()
    second = builder._lazy_regex()
    third = builder._lazy_regex()
    assert first is second
    assert second is third


def test_repeated_matcher_calls_reuse_the_cached_regex():
    builder = RegexBuilder().digit()
    builder.match("1")
    cached = builder._cached_regex
    builder.search("2")
    builder.findall("3")
    builder.test("4")
    assert builder._cached_regex is cached


def test_pattern_lazy_regex_is_memoised_too():
    pattern = Pattern().word()
    first = pattern._lazy_regex()
    second = pattern._lazy_regex()
    assert first is second


def test_a_forked_builder_gets_a_fresh_cache_slot():
    original = RegexBuilder().digit()
    original.match("1")
    assert original._cached_regex is not None
    forked = original.fork()
    assert forked._cached_regex is None


def test_a_copied_builder_gets_a_fresh_cache_slot():
    original = RegexBuilder().digit()
    original.match("1")
    copied = original.copy()
    assert copied._cached_regex is None


def test_a_chain_extension_gets_a_fresh_cache_slot():
    original = RegexBuilder().digit()
    original.match("1")
    extended = original.word()
    assert extended._cached_regex is None


def test_a_fresh_builder_starts_without_a_cached_regex():
    builder = RegexBuilder()
    assert builder._cached_regex is None


def test_calling_to_regex_directly_does_not_populate_the_cache():
    builder = RegexBuilder().digit()
    _ = builder.to_regex()
    assert builder._cached_regex is None


def test_lazy_regex_produces_a_regex_that_matches_the_pattern():
    builder = RegexBuilder().digit()
    result = builder._lazy_regex()
    assert result.source == "\\d"
    assert result.match("7") is not None
