"""Cross-cutting invariants that must hold for every registered library Pattern."""

import pytest

import edify.library as library_module
from edify import Pattern


def _registered_patterns():
    for name in sorted(dir(library_module)):
        if name.startswith("_"):
            continue
        value = getattr(library_module, name)
        if isinstance(value, Pattern):
            yield name, value


REGISTERED_PATTERNS = list(_registered_patterns())


@pytest.mark.parametrize(("name", "pattern"), REGISTERED_PATTERNS, ids=lambda item: item)
def test_to_regex_string_matches_the_compiled_pattern_source(name, pattern):
    emitted_source = pattern.to_regex_string()
    compiled_source = pattern.to_regex().source
    assert emitted_source == compiled_source, (
        f"library pattern {name!r} emits {emitted_source!r} but its compiled Regex reports "
        f"{compiled_source!r} — the terminals have drifted apart."
    )
