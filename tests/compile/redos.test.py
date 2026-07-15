"""Tests for the build-time ReDoS detector."""

import pytest

from edify import RegexBuilder
from edify.compile.redos import ReDoSWarning


def _classic_redos_builder():
    return RegexBuilder().one_or_more().group().one_or_more().digit().end()


def test_classic_nested_unbounded_quantifier_triggers_the_warning():
    with pytest.warns(ReDoSWarning, match="nested unbounded quantifier"):
        _classic_redos_builder().to_regex()


def test_zero_or_more_wrapping_one_or_more_triggers_the_warning():
    builder = RegexBuilder().zero_or_more().group().one_or_more().digit().end()
    with pytest.warns(ReDoSWarning):
        builder.to_regex()


def test_at_least_wrapping_zero_or_more_triggers_the_warning():
    builder = RegexBuilder().at_least(2).group().zero_or_more().word().end()
    with pytest.warns(ReDoSWarning):
        builder.to_regex()


def test_lazy_variants_also_trigger_the_warning():
    builder = RegexBuilder().one_or_more_lazy().group().zero_or_more_lazy().digit().end()
    with pytest.warns(ReDoSWarning):
        builder.to_regex()


def test_warning_message_names_both_quantifiers():
    with pytest.warns(ReDoSWarning) as record:
        _classic_redos_builder().to_regex()
    message_text = str(record[0].message)
    assert "one_or_more()" in message_text
    assert "engine='regex'" in message_text


def test_bounded_quantifier_does_not_trigger_the_warning(recwarn):
    builder = RegexBuilder().exactly(3).group().exactly(2).digit().end()
    builder.to_regex()
    is_redos_flags = [isinstance(warning.message, ReDoSWarning) for warning in recwarn]
    assert not any(is_redos_flags)


def test_grouped_quantifier_over_a_composite_group_does_not_trigger(recwarn):
    builder = RegexBuilder().one_or_more().group().digit().letter().end()
    builder.to_regex()
    is_redos_flags = [isinstance(warning.message, ReDoSWarning) for warning in recwarn]
    assert not any(is_redos_flags)


def test_grouped_quantifier_over_a_single_non_quantifier_child_does_not_trigger(recwarn):
    builder = RegexBuilder().one_or_more().group().digit().end()
    builder.to_regex()
    is_redos_flags = [isinstance(warning.message, ReDoSWarning) for warning in recwarn]
    assert not any(is_redos_flags)


def test_sequential_unbounded_quantifiers_do_not_trigger_the_warning(recwarn):
    builder = RegexBuilder().one_or_more().digit().one_or_more().letter()
    builder.to_regex()
    is_redos_flags = [isinstance(warning.message, ReDoSWarning) for warning in recwarn]
    assert not any(is_redos_flags)


def test_warning_only_fires_once_per_construct_within_a_single_terminal_call():
    with pytest.warns(ReDoSWarning) as record:
        _classic_redos_builder().to_regex()
    redos_records = [w for w in record if isinstance(w.message, ReDoSWarning)]
    assert len(redos_records) == 1


def test_terminal_still_returns_the_compiled_regex_after_warning():
    with pytest.warns(ReDoSWarning):
        compiled = _classic_redos_builder().to_regex()
    assert compiled.source == "(?:\\d+)+"
