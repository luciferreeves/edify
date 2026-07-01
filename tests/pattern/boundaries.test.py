"""Tests for the WORD_BOUNDARY and NON_WORD_BOUNDARY module-level constants."""

from edify import NON_WORD_BOUNDARY, WORD_BOUNDARY, Pattern


def test_word_boundary_is_a_pattern():
    assert isinstance(WORD_BOUNDARY, Pattern)


def test_non_word_boundary_is_a_pattern():
    assert isinstance(NON_WORD_BOUNDARY, Pattern)


def test_word_boundary_compiles_to_backslash_b():
    assert WORD_BOUNDARY.to_regex_string() == "\\b"


def test_non_word_boundary_compiles_to_backslash_capital_b():
    assert NON_WORD_BOUNDARY.to_regex_string() == "\\B"


def test_word_boundary_matches_fluent_chain_output():
    assert WORD_BOUNDARY._state == Pattern().word_boundary()._state


def test_non_word_boundary_matches_fluent_chain_output():
    assert NON_WORD_BOUNDARY._state == Pattern().non_word_boundary()._state
