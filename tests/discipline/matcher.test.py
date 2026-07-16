"""Discipline test — the builder exposes exactly the five closed match verbs."""

import pytest

from edify import Pattern, RegexBuilder

_ALLOWED_MATCH_VERBS = frozenset({"test", "match", "search", "findall", "sub"})
_FORBIDDEN_MATCH_VERBS = frozenset({"fullmatch", "finditer", "subn", "split"})
_FORBIDDEN_RE_PATTERN_ATTRS = frozenset({"groups", "groupindex", "pattern", "flags"})


@pytest.mark.parametrize("factory", [RegexBuilder, Pattern])
def test_builder_exposes_every_allowed_match_verb(factory: type[RegexBuilder | Pattern]):
    builder = factory()
    for verb in _ALLOWED_MATCH_VERBS:
        assert callable(getattr(builder, verb)), f"missing verb: {verb}"


@pytest.mark.parametrize("factory", [RegexBuilder, Pattern])
def test_builder_does_not_expose_any_forbidden_match_verb(factory: type[RegexBuilder | Pattern]):
    builder = factory()
    for verb in _FORBIDDEN_MATCH_VERBS:
        assert not hasattr(builder, verb), (
            f"builder must not expose re.Pattern verb {verb!r}; "
            "use .to_regex() and call it on the Regex wrapper instead"
        )


@pytest.mark.parametrize("factory", [RegexBuilder, Pattern])
def test_builder_does_not_expose_re_pattern_metadata_attributes(
    factory: type[RegexBuilder | Pattern],
):
    builder = factory()
    for attribute in _FORBIDDEN_RE_PATTERN_ATTRS:
        assert not hasattr(builder, attribute), (
            f"builder must not expose re.Pattern attribute {attribute!r}"
        )


def test_regex_wrapper_exposes_every_re_pattern_verb():
    regex = RegexBuilder().string("a").to_regex()
    re_pattern_verbs = (_ALLOWED_MATCH_VERBS | _FORBIDDEN_MATCH_VERBS) - {"test"}
    for verb in re_pattern_verbs:
        assert callable(getattr(regex, verb)), f"Regex wrapper missing verb: {verb}"
