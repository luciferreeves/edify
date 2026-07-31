"""Rejected arguments must be named as the caller wrote them.

An annotated diagnostic points at the call that caused it, so the summary has to
use the parameter's real name; a placeholder such as ``x`` or ``Y`` leaves the
reader hunting for an argument that does not appear in any signature.
"""

from __future__ import annotations

import pytest

from edify import EdifySyntaxError, Pattern, between, between_lazy

_PLACEHOLDER_LABELS = ["x", "y", "X", "Y", "a", "b", "Value"]


def _summary_of(callable_under_test) -> str:
    with pytest.raises(EdifySyntaxError) as raised:
        callable_under_test()
    return str(raised.value).splitlines()[0]


@pytest.mark.parametrize(
    "callable_under_test",
    [
        lambda: Pattern().between(-1, 3),
        lambda: Pattern().between_lazy(-1, 3),
        lambda: between(-1, 3, Pattern().digit()),
        lambda: between_lazy(-1, 3, Pattern().digit()),
    ],
)
def test_a_negative_lower_bound_is_reported_as_lower(callable_under_test):
    assert "lower" in _summary_of(callable_under_test)


@pytest.mark.parametrize(
    "callable_under_test",
    [
        lambda: Pattern().between(1, 0),
        lambda: Pattern().between_lazy(1, 0),
        lambda: between(1, 0, Pattern().digit()),
        lambda: between_lazy(1, 0, Pattern().digit()),
    ],
)
def test_a_non_positive_upper_bound_is_reported_as_upper(callable_under_test):
    assert "upper" in _summary_of(callable_under_test)


@pytest.mark.parametrize(
    "callable_under_test",
    [
        lambda: Pattern().between(5, 2),
        lambda: Pattern().between_lazy(5, 2),
        lambda: between(5, 2, Pattern().digit()),
        lambda: between_lazy(5, 2, Pattern().digit()),
    ],
)
def test_inverted_bounds_are_reported_as_lower_and_upper(callable_under_test):
    summary = _summary_of(callable_under_test)
    assert "lower" in summary
    assert "upper" in summary


@pytest.mark.parametrize(
    ("callable_under_test", "expected_name"),
    [
        (lambda: Pattern().range("ab", "z"), "start_character"),
        (lambda: Pattern().range("a", "yz"), "end_character"),
        (lambda: Pattern().anything_but_range("ab", "z"), "start_character"),
        (lambda: Pattern().anything_but_range("a", "yz"), "end_character"),
        (lambda: Pattern().char("ab"), "value"),
        (lambda: Pattern().string(""), "value"),
        (lambda: Pattern().anything_but_string(""), "value"),
        (lambda: Pattern().anything_but_chars(""), "characters"),
    ],
)
def test_a_rejected_character_argument_is_reported_by_its_parameter_name(
    callable_under_test, expected_name: str
):
    assert expected_name in _summary_of(callable_under_test)


_REJECTING_CALLS = [
    lambda: Pattern().between(-1, 3),
    lambda: Pattern().between(1, 0),
    lambda: Pattern().between(5, 2),
    lambda: Pattern().range("ab", "z"),
    lambda: Pattern().range("a", "yz"),
    lambda: Pattern().anything_but_range("ab", "z"),
    lambda: Pattern().char("ab"),
    lambda: Pattern().string(""),
    lambda: Pattern().anything_but_chars(""),
]


@pytest.mark.parametrize("rejecting_call", _REJECTING_CALLS)
def test_no_diagnostic_names_a_placeholder_as_its_subject(rejecting_call):
    subject = _summary_of(rejecting_call).removeprefix("error: ").split(" ", 1)[0]
    assert subject not in _PLACEHOLDER_LABELS
