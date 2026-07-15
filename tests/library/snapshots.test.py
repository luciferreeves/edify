"""Snapshot suite for every public library validator.

Each :class:`edify.Pattern` exposed by :mod:`edify.library` has a committed
``.to_regex_string()`` snapshot under ``tests/snapshots/library/<name>.regex``.
Set ``EDIFY_UPDATE_SNAPSHOTS=1`` to regenerate the corpus in one pytest run
after an intentional compile-path change.
"""

from pathlib import Path

import pytest

import edify.library as library_module
from edify import Pattern
from edify.testing import assert_snapshot

_SNAPSHOT_ROOT = Path(__file__).parent.parent / "snapshots" / "library"


def _registered_patterns():
    for name in sorted(dir(library_module)):
        if name.startswith("_"):
            continue
        value = getattr(library_module, name)
        if isinstance(value, Pattern):
            yield name, value


REGISTERED_PATTERNS = list(_registered_patterns())


@pytest.mark.parametrize(("name", "pattern"), REGISTERED_PATTERNS, ids=lambda item: item)
def test_library_pattern_emits_the_snapshotted_regex(name, pattern):
    snapshot_path = _SNAPSHOT_ROOT / f"{name}.regex"
    emitted = pattern.to_regex_string()
    assert_snapshot(emitted, snapshot_path)
