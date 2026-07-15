"""Orphan detection — every committed snapshot must trace back to a live source.

Runs three checks, one per snapshot root:

* ``tests/snapshots/library/<name>.regex`` — must correspond to a
  :class:`edify.Pattern` exported from :mod:`edify.library`.
* ``tests/snapshots/fixtures/<name>.regex`` — must correspond to a fixture
  registered in ``tests/fixtures/fixtures.test.py``.
* ``tests/snapshots/docs/<file>/<block>.regex`` — must correspond to a
  ``.. code-block:: python`` block at that line in that RST.

The reverse direction (a source without a snapshot) is caught by
``SnapshotMissingError`` inside the per-source test; adding a new source
without generating its snapshot fails the direct test, not this one.
"""

from pathlib import Path

import edify.library as library_module
from edify import Pattern

_REPO_ROOT = Path(__file__).parent.parent.parent
_SNAPSHOT_ROOT = _REPO_ROOT / "tests" / "snapshots"
_LIBRARY_SNAPSHOT_ROOT = _SNAPSHOT_ROOT / "library"
_FIXTURES_SNAPSHOT_ROOT = _SNAPSHOT_ROOT / "fixtures"
_DOCS_SNAPSHOT_ROOT = _SNAPSHOT_ROOT / "docs"
_DOCS_SOURCE_ROOT = _REPO_ROOT / "docs"
_CODE_BLOCK_HEADER = ".. code-block:: python"


def test_every_library_snapshot_has_a_registered_pattern():
    snapshot_stems = {path.stem for path in _LIBRARY_SNAPSHOT_ROOT.glob("*.regex")}
    pattern_names = _library_pattern_names()
    orphaned_snapshots = snapshot_stems - pattern_names
    assert orphaned_snapshots == set(), (
        f"library snapshot files without a registered Pattern in edify.library: "
        f"{sorted(orphaned_snapshots)}"
    )


def test_every_fixture_snapshot_has_a_registered_fixture():
    snapshot_stems = {path.stem for path in _FIXTURES_SNAPSHOT_ROOT.glob("*.regex")}
    fixture_names = _registered_fixture_names()
    orphaned_snapshots = snapshot_stems - fixture_names
    assert orphaned_snapshots == set(), (
        f"fixture snapshot files without a registered fixture in "
        f"tests/fixtures/fixtures.test.py: {sorted(orphaned_snapshots)}"
    )


def test_every_doc_snapshot_has_a_matching_rst_code_block():
    snapshot_pairs = _collect_doc_snapshot_pairs()
    doc_block_pairs = _collect_doc_code_block_pairs()
    orphaned_snapshots = snapshot_pairs - doc_block_pairs
    assert orphaned_snapshots == set(), (
        f"doc snapshot files without a matching .. code-block:: python: "
        f"{sorted(orphaned_snapshots)}"
    )


def _library_pattern_names() -> set[str]:
    names: set[str] = set()
    for export_name in dir(library_module):
        if export_name.startswith("_"):
            continue
        value = getattr(library_module, export_name)
        if isinstance(value, Pattern):
            names.add(export_name)
    return names


def _registered_fixture_names() -> set[str]:
    fixture_source = (_REPO_ROOT / "tests" / "fixtures" / "fixtures.test.py").read_text()
    return _fixture_names_from_source(fixture_source)


def _fixture_names_from_source(source: str) -> set[str]:
    names: set[str] = set()
    for line in source.splitlines():
        stripped = line.strip()
        if not stripped.startswith('("'):
            continue
        closing_quote_index = stripped.find('"', 2)
        if closing_quote_index == -1:
            continue
        names.add(stripped[2:closing_quote_index])
    return names


def _collect_doc_snapshot_pairs() -> set[tuple[str, int]]:
    pairs: set[tuple[str, int]] = set()
    for snapshot in _DOCS_SNAPSHOT_ROOT.rglob("*.regex"):
        relative_stem = snapshot.parent.relative_to(_DOCS_SNAPSHOT_ROOT).as_posix()
        block_start = int(snapshot.stem)
        pairs.add((relative_stem, block_start))
    return pairs


def _collect_doc_code_block_pairs() -> set[tuple[str, int]]:
    pairs: set[tuple[str, int]] = set()
    for rst_path in _DOCS_SOURCE_ROOT.rglob("*.rst"):
        relative_stem = rst_path.relative_to(_DOCS_SOURCE_ROOT).with_suffix("").as_posix()
        for block_start in _code_block_start_lines(rst_path):
            pairs.add((relative_stem, block_start))
    return pairs


def _code_block_start_lines(rst_path: Path) -> list[int]:
    starts: list[int] = []
    lines = rst_path.read_text().splitlines()
    line_index = 0
    while line_index < len(lines):
        if lines[line_index].strip() != _CODE_BLOCK_HEADER:
            line_index += 1
            continue
        body_start = _first_content_line(lines, line_index + 1)
        if body_start is not None:
            starts.append(body_start)
        line_index += 1
    return starts


def _first_content_line(lines: list[str], from_index: int) -> int | None:
    line_index = from_index
    while line_index < len(lines) and lines[line_index].strip() == "":
        line_index += 1
    if line_index >= len(lines):
        return None
    if lines[line_index].startswith(" ") or lines[line_index].startswith("\t"):
        return line_index
    return None
