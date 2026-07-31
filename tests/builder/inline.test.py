"""Inline flags declared in a source regex must survive ``from_regex``.

``(?i)`` and its siblings change what a pattern matches, so dropping them during
reverse parsing produces a builder that silently disagrees with the regex it was
built from.
"""

from __future__ import annotations

import re

import pytest

from edify import RegexBuilder

_FLAGGED_PATTERNS = [
    ("(?i)abc", "ABC"),
    ("(?m)^x", "y\nx"),
    ("(?s).", "\n"),
    (r"(?a)\w", "é"),
    ("(?im)^x", "Y\nX"),
]


@pytest.mark.parametrize(("source", "probe"), _FLAGGED_PATTERNS)
def test_a_reverse_parsed_pattern_agrees_with_the_regex_it_came_from(source: str, probe: str):
    reverse_parsed = RegexBuilder.from_regex(source).to_regex()
    assert bool(reverse_parsed.search(probe)) == bool(re.search(source, probe))


@pytest.mark.parametrize(
    ("source", "flag"),
    [
        ("(?i)abc", re.IGNORECASE),
        ("(?m)^x", re.MULTILINE),
        ("(?s).", re.DOTALL),
        (r"(?a)\w", re.ASCII),
        ("(?x) a b", re.VERBOSE),
    ],
)
def test_each_inline_flag_reaches_the_compiled_pattern(source: str, flag: re.RegexFlag):
    reverse_parsed = RegexBuilder.from_regex(source).to_regex()
    assert reverse_parsed.compiled.flags & flag


@pytest.mark.parametrize(("source", "probe"), [("abc", "ABC"), (r"^\d{4}$", "2024")])
def test_a_pattern_without_inline_flags_gains_none(source: str, probe: str):
    reverse_parsed = RegexBuilder.from_regex(source).to_regex()
    assert bool(reverse_parsed.search(probe)) == bool(re.search(source, probe))
    assert not reverse_parsed.compiled.flags & re.IGNORECASE


def test_two_inline_flags_both_survive_together():
    reverse_parsed = RegexBuilder.from_regex("(?im)^x").to_regex()
    assert reverse_parsed.compiled.flags & re.IGNORECASE
    assert reverse_parsed.compiled.flags & re.MULTILINE
