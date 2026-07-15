"""Tests for :mod:`edify.integrations.fastapi`."""

import fastapi.params

from edify import Pattern
from edify.integrations.fastapi import pattern_path, pattern_query

_UUID_PATTERN = (
    Pattern()
    .start_of_input()
    .exactly(8)
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .end()
    .end_of_input()
)


def test_pattern_query_returns_a_fastapi_query_pinned_to_the_pattern_regex():
    query_default = pattern_query(_UUID_PATTERN)
    assert isinstance(query_default, fastapi.params.Query)


def test_pattern_query_forwards_the_description_to_fastapi_query():
    query_with_description = pattern_query(_UUID_PATTERN, description="prefix")
    assert query_with_description.description == "prefix"


def test_pattern_query_default_differs_from_an_explicit_default():
    without_default = pattern_query(_UUID_PATTERN)
    with_default = pattern_query(_UUID_PATTERN, default="deadbeef")
    assert without_default.default != with_default.default


def test_pattern_path_returns_a_fastapi_path_pinned_to_the_pattern_regex():
    path_default = pattern_path(_UUID_PATTERN)
    assert isinstance(path_default, fastapi.params.Path)


def test_pattern_path_forwards_the_description_to_fastapi_path():
    path_with_description = pattern_path(_UUID_PATTERN, description="prefix")
    assert path_with_description.description == "prefix"
