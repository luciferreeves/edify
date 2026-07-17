"""Cross-cutting invariants that must hold for every registered library Pattern."""

from collections.abc import Iterator

import pytest

import edify.library as library_module
from edify import Pattern


def _registered_patterns() -> Iterator[tuple[str, Pattern]]:
    for name in sorted(dir(library_module)):
        if name.startswith("_"):
            continue
        value = getattr(library_module, name)
        if isinstance(value, Pattern):
            yield name, value


REGISTERED_PATTERNS: list[tuple[str, Pattern]] = list(_registered_patterns())
_IDS = [registered_name for registered_name, _ in REGISTERED_PATTERNS]


@pytest.mark.parametrize(("name", "pattern"), REGISTERED_PATTERNS, ids=_IDS)
def test_to_regex_string_matches_the_compiled_pattern_source(name: str, pattern: Pattern):
    emitted_source = pattern.to_regex_string()
    compiled_source = pattern.to_regex().source
    assert emitted_source == compiled_source, (
        f"library pattern {name!r} emits {emitted_source!r} but its compiled Regex reports "
        f"{compiled_source!r} — the terminals have drifted apart."
    )


@pytest.mark.parametrize(("name", "pattern"), REGISTERED_PATTERNS, ids=_IDS)
def test_dict_round_trip_preserves_the_emitted_regex(name: str, pattern: Pattern):
    restored = Pattern.from_dict(pattern.to_dict())
    assert restored.to_regex_string() == pattern.to_regex_string(), (
        f"library pattern {name!r} does not survive a to_dict/from_dict round trip."
    )


@pytest.mark.parametrize(("name", "pattern"), REGISTERED_PATTERNS, ids=_IDS)
def test_json_round_trip_preserves_the_emitted_regex(name: str, pattern: Pattern):
    restored = Pattern.from_json(pattern.to_json())
    assert restored.to_regex_string() == pattern.to_regex_string(), (
        f"library pattern {name!r} does not survive a to_json/from_json round trip."
    )
