"""Tests for :mod:`edify.integrations.fastapi`."""

import sys

import pytest

from edify import Pattern
from edify.errors.integration import MissingIntegrationDependencyError
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
    fastapi_module = _fastapi()
    assert type(query_default).__name__ == "Query" or isinstance(
        query_default, fastapi_module.params.Query
    )


def test_pattern_query_forwards_extra_kwargs_to_fastapi_query():
    query_with_description = pattern_query(_UUID_PATTERN, description="prefix")
    assert query_with_description.description == "prefix"


def test_pattern_query_default_differs_from_an_explicit_default():
    without_default = pattern_query(_UUID_PATTERN)
    with_default = pattern_query(_UUID_PATTERN, default="deadbeef")
    assert without_default.default != with_default.default


def test_pattern_query_respects_an_explicit_default_kwarg():
    query_with_default = pattern_query(_UUID_PATTERN, default="deadbeef")
    assert query_with_default.default == "deadbeef"


def test_pattern_path_returns_a_fastapi_path_pinned_to_the_pattern_regex():
    path_default = pattern_path(_UUID_PATTERN)
    fastapi_module = _fastapi()
    assert isinstance(path_default, fastapi_module.params.Path)


def test_pattern_query_raises_missing_integration_when_fastapi_absent(monkeypatch):
    monkeypatch.setitem(sys.modules, "fastapi", None)
    with pytest.raises(MissingIntegrationDependencyError, match="fastapi"):
        pattern_query(_UUID_PATTERN)


def test_pattern_path_raises_missing_integration_when_fastapi_absent(monkeypatch):
    monkeypatch.setitem(sys.modules, "fastapi", None)
    with pytest.raises(MissingIntegrationDependencyError, match="fastapi"):
        pattern_path(_UUID_PATTERN)


def test_missing_integration_error_carries_the_actionable_install_hint(monkeypatch):
    monkeypatch.setitem(sys.modules, "fastapi", None)
    with pytest.raises(MissingIntegrationDependencyError) as excinfo:
        pattern_query(_UUID_PATTERN)
    assert "pip install edify[fastapi]" in str(excinfo.value)


def _fastapi():
    import fastapi

    return fastapi
