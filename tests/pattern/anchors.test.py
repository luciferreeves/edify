"""Tests for the START and END module-level anchor constants."""

from edify import END, START, Pattern


def test_start_is_a_pattern():
    assert isinstance(START, Pattern)


def test_end_is_a_pattern():
    assert isinstance(END, Pattern)


def test_start_compiles_to_caret():
    assert START.to_regex_string() == "^"


def test_end_compiles_to_dollar_sign():
    assert END.to_regex_string() == "$"


def test_start_matches_start_of_input_element_from_the_fluent_chain():
    assert Pattern().start_of_input() == START


def test_end_matches_end_of_input_element_from_the_fluent_chain():
    assert Pattern().end_of_input() == END
