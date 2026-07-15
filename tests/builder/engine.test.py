import pytest

from edify import RegexBuilder
from edify.errors.engine import EngineNotWiredError


def test_engine_defaults_to_re_and_compiles():
    compiled = RegexBuilder().digit().to_regex()
    assert compiled.source == "\\d"


def test_engine_re_explicit_is_accepted():
    compiled = RegexBuilder().digit().to_regex(engine="re")
    assert compiled.source == "\\d"


def test_engine_regex_raises_until_wired():
    with pytest.raises(EngineNotWiredError, match="engine='regex'"):
        RegexBuilder().digit().to_regex(engine="regex")
