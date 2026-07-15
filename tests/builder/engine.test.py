import sys

import pytest

from edify import RegexBuilder
from edify.errors.backend import MissingRegexBackendError


def test_engine_defaults_to_re_and_compiles():
    compiled = RegexBuilder().digit().to_regex()
    assert compiled.source == "\\d"
    assert compiled.engine == "re"


def test_engine_re_explicit_compiles_via_stdlib():
    compiled = RegexBuilder().digit().to_regex(engine="re")
    assert compiled.source == "\\d"
    assert compiled.engine == "re"
    assert compiled.compiled.__class__.__module__ == "re"


def test_engine_regex_compiles_via_third_party_module():
    compiled = RegexBuilder().digit().to_regex(engine="regex")
    assert compiled.source == "\\d"
    assert compiled.engine == "regex"
    assert compiled.compiled.__class__.__module__.endswith("regex")


def test_engine_regex_and_engine_re_are_not_equal_for_the_same_source():
    left = RegexBuilder().digit().to_regex(engine="re")
    right = RegexBuilder().digit().to_regex(engine="regex")
    assert left != right


def test_engine_regex_raises_clean_import_error_without_the_extra(monkeypatch):
    monkeypatch.setitem(sys.modules, "regex", None)
    with pytest.raises(MissingRegexBackendError, match="engine='regex'") as excinfo:
        RegexBuilder().digit().to_regex(engine="regex")
    text = str(excinfo.value)
    assert "pip install edify[regex]" in text
    assert "= note:" in text


def test_missing_regex_backend_error_chains_from_underlying_import_error(monkeypatch):
    monkeypatch.setitem(sys.modules, "regex", None)
    with pytest.raises(MissingRegexBackendError) as excinfo:
        RegexBuilder().digit().to_regex(engine="regex")
    assert isinstance(excinfo.value.__cause__, ImportError)


def test_regex_engine_flags_propagate():
    compiled = RegexBuilder().string("ABC").to_regex(engine="regex", ignore_case=True)
    assert bool(compiled.search("abc"))
