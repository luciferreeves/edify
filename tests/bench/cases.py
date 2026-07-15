"""Benchmark case suite — simple, medium, and complex builder shapes.

Each factory returns a fresh builder chain. Benchmarks that measure the
compile/match hot paths reuse these factories so the cost of building the
chain is separable from the cost of terminal + match.
"""

from __future__ import annotations

from collections.abc import Callable

from edify import RegexBuilder


def simple_digit_builder() -> RegexBuilder:
    """Simple: ``digit().one_or_more()`` — the smallest realistic chain."""
    return RegexBuilder().one_or_more().digit()


def medium_hex_number_builder() -> RegexBuilder:
    """Medium: hex-number-class pattern with anchors and a bounded quantifier."""
    return (
        RegexBuilder()
        .start_of_input()
        .string("0x")
        .between(1, 8)
        .any_of_chars("0123456789abcdefABCDEF")
        .end_of_input()
    )


def complex_composed_url_shape_builder() -> RegexBuilder:
    """Complex: multiple nested groups + lookaround + alternation over multi-char literals."""
    return (
        RegexBuilder()
        .start_of_input()
        .assert_ahead()
        .any_of("http", "https", "ftp")
        .end()
        .capture()
        .any_of("http", "https", "ftp")
        .end()
        .string("://")
        .one_or_more()
        .any_of_chars("abcdefghijklmnopqrstuvwxyz0123456789.-")
        .string("/")
        .zero_or_more()
        .any_of_chars("abcdefghijklmnopqrstuvwxyz0123456789/._-")
        .end_of_input()
    )


BUILDER_FACTORIES: dict[str, Callable[[], RegexBuilder]] = {
    "simple": simple_digit_builder,
    "medium": medium_hex_number_builder,
    "complex": complex_composed_url_shape_builder,
}


MATCH_SCENARIOS: dict[str, dict[str, list[str]]] = {
    "simple": {
        "matches": ["1", "42", "9876543210"],
        "near_matches": ["a", "1a", " 12 "],
        "non_matches": ["", "abc", "----"],
    },
    "medium": {
        "matches": ["0x1", "0x123", "0xabcdef12"],
        "near_matches": ["0X1", "0x", "0xxg"],
        "non_matches": ["", "abc", "1234", "0xghijkl"],
    },
    "complex": {
        "matches": ["http://a.b/", "https://example.com/path/to.txt", "ftp://ftp.example.org/"],
        "near_matches": ["gopher://a/", "http:/a/", "http://"],
        "non_matches": ["", "example.com", "just a sentence", "0x123"],
    },
}
