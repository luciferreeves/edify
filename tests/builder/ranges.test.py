"""Range endpoints must stay literal inside the character class they build.

``]`` would close the class, ``^`` would negate it, ``-`` would be read as a
range operator and ``\\`` would escape whatever follows — so each has to survive
as a literal endpoint, both on its own and when the range sits beside others.
"""

from __future__ import annotations

import pytest

from edify import Pattern

_SYNTACTIC_ENDPOINTS = ["]", "^", "-", "\\"]


@pytest.mark.parametrize("endpoint", _SYNTACTIC_ENDPOINTS)
def test_range_with_a_syntactic_lower_bound_still_matches_that_character(endpoint: str):
    pattern = Pattern().start_of_input().range(endpoint, "\x7f").end_of_input()
    assert pattern(endpoint) is True


@pytest.mark.parametrize("endpoint", _SYNTACTIC_ENDPOINTS)
def test_range_with_a_syntactic_bound_rejects_a_character_below_it(endpoint: str):
    pattern = Pattern().start_of_input().range(endpoint, "\x7f").end_of_input()
    assert pattern("\x01") is False


def test_range_starting_at_caret_does_not_negate_the_class():
    pattern = Pattern().start_of_input().range("^", "~").end_of_input()
    assert pattern("^") is True
    assert pattern("a") is True
    assert pattern("\x01") is False


def test_range_endpoint_does_not_terminate_a_surrounding_class():
    pattern = Pattern().start_of_input().any_of().char("!").range("]", "~").end().end_of_input()
    assert pattern("]") is True
    assert pattern("!") is True
    assert pattern("a") is True
    assert pattern("\x01") is False


def test_negated_range_with_a_syntactic_bound_excludes_that_character():
    pattern = Pattern().start_of_input().anything_but_range("]", "~").end_of_input()
    assert pattern("]") is False
    assert pattern("a") is False
    assert pattern("!") is True


def test_quoted_local_part_is_reachable_in_the_rfc_5322_address_shape():
    from edify.library import email_rfc_5322

    assert email_rfc_5322('"quoted"@example.com') is True
    assert email_rfc_5322("plain@example.com") is True
