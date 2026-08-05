"""``from_regex`` must translate every character class and back-reference the builder writes.

Normalisation is allowed to change the emitted text — ``[\\da-z]`` comes back as
``(?:\\d|[a-z])`` — so these assert behaviour, not string equality: the
translation and the original must agree on every probe.
"""

from __future__ import annotations

import re
import string

import pytest

from edify import RegexBuilder
from edify.builder.reverse import UnsupportedReverseParseError

_PROBES = [
    *string.ascii_letters,
    *string.digits,
    *"_-^]\\ .!@#\t\n",
    "",
    "aa",
    "ab",
    "abab",
    "a1",
    "AZ",
    "cat",
    "a-b",
    "]]",
]

_MULTI_MEMBER_CLASSES = [
    r"[a-z0-9]",
    r"[a-z_]",
    r"[0-46-9]",
    r"[a-zA-Z0-9_.-]",
    r"[\da-z]",
    r"[a-]",
    r"[a^]",
    r"[]]",
]

_NEGATED_CLASSES = [
    r"[^abc]",
    r"[^a]",
    r"[^a-z]",
    r"[^a-z0-9]",
    r"[^a-z_]",
    r"[^-a-z]",
    r"[^ \t]",
    r"[^]]",
    r"[^\\]",
]

_BACK_REFERENCES = [
    r"(a)\1",
    r"([abc])\1+",
    r"(a|b)\1",
    r"^(\w)(\d)\2\1$",
    r"(?P<x>a)(?P=x)",
    r"(?P<a>x)(?P<b>y)(?P=b)(?P=a)",
    r"(?P<n>[a-z0-9]+)-(?P=n)",
]


def _agrees_on_every_probe(pattern_text: str) -> bool:
    translated = RegexBuilder.from_regex(pattern_text).to_regex_string()
    return all(
        (re.search(pattern_text, probe) is not None)
        == (re.search(translated, probe) is not None)
        for probe in _PROBES
    )


@pytest.mark.parametrize("pattern_text", _MULTI_MEMBER_CLASSES)
def test_a_multi_member_class_round_trips(pattern_text: str):
    assert _agrees_on_every_probe(pattern_text)


@pytest.mark.parametrize("pattern_text", _NEGATED_CLASSES)
def test_a_negated_class_round_trips(pattern_text: str):
    assert _agrees_on_every_probe(pattern_text)


@pytest.mark.parametrize("pattern_text", _BACK_REFERENCES)
def test_a_back_reference_round_trips(pattern_text: str):
    assert _agrees_on_every_probe(pattern_text)


def test_two_ranges_become_a_single_class():
    assert RegexBuilder.from_regex(r"[a-z0-9]").to_regex_string() == "[a-z0-9]"


def test_a_range_beside_a_literal_becomes_a_single_class():
    assert RegexBuilder.from_regex(r"[a-z_]").to_regex_string() == "[a-z_]"


def test_a_negated_literal_set_uses_the_direct_method():
    assert RegexBuilder.from_regex(r"[^abc]").to_regex_string() == "[^abc]"


def test_a_negated_range_uses_the_direct_method():
    assert RegexBuilder.from_regex(r"[^a-z]").to_regex_string() == "[^a-z]"


def test_a_negated_multi_member_class_uses_the_negated_frame():
    assert RegexBuilder.from_regex(r"[^a-z0-9]").to_regex_string() == "[^a-z0-9]"


def test_a_numbered_back_reference_translates_to_the_numbered_method():
    assert RegexBuilder.from_regex(r"(a)\1").to_regex_string() == r"(a)\1"


def test_a_named_back_reference_keeps_its_name():
    assert RegexBuilder.from_regex(r"(?P<x>a)(?P=x)").to_regex_string() == "(?P<x>a)(?P=x)"


def test_a_back_reference_to_a_later_group_keeps_its_index():
    translated = RegexBuilder.from_regex(r"(a)(b)\2").to_regex_string()
    assert translated == r"(a)(b)\2"


def test_a_back_reference_inside_a_quantified_group_round_trips():
    assert _agrees_on_every_probe(r"(?:([ab])\1)+")


def test_the_translated_chain_is_still_extendable():
    extended = RegexBuilder.from_regex(r"[a-z0-9]").char("-").to_regex_string()
    assert extended == "[a-z0-9]\\-"


_QUANTIFIED_GROUPS = [
    r"^[a-z]+(?:-[a-z]+)*$",
    r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
    r"(?:a[0-9])+",
    r"(?:\d-)*x",
    r"(?:ab|cd){2}",
    r"(?:[a-z]\d)+",
    r"(?:x[0-9]y)*z",
    r"(?:-x)*",
    r"(?:ab)+",
    r"a+",
]


@pytest.mark.parametrize("pattern_text", _QUANTIFIED_GROUPS)
def test_a_quantified_group_round_trips(pattern_text: str):
    assert _agrees_on_every_probe(pattern_text)


def test_a_multi_element_repeat_body_is_grouped_before_quantifying():
    translated = RegexBuilder.from_regex(r"^[a-z]+(?:-[a-z]+)*$").to_regex_string()
    assert translated == r"^[a-z]+(?:\-[a-z]+)*$"


def test_a_single_element_repeat_body_is_not_wrapped():
    assert RegexBuilder.from_regex(r"a+").to_regex_string() == "a+"


def test_the_slug_shape_rejects_a_doubled_separator():
    translated = RegexBuilder.from_regex(r"^[a-z0-9]+(?:-[a-z0-9]+)*$").to_regex_string()
    assert re.search(translated, "a--b") is None
    assert re.search(translated, "a-b") is not None


def test_a_negated_class_holding_a_category_is_still_refused():
    with pytest.raises(UnsupportedReverseParseError) as raised:
        RegexBuilder.from_regex(r"[^\da-z]")
    assert "negated character-class member" in str(raised.value)
