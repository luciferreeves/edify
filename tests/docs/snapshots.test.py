"""Snapshot suite for every ``.. code-block:: python`` block shipped in the docs.

Each block is executed in a fresh edify-populated namespace; any ``Regex``
or ``Pattern`` bound to a top-level name has its ``.to_regex_string()``
snapshotted under ``tests/snapshots/docs/<file-stem>/<block-index>.regex``.
The snapshot pins the docs against silent drift: an intentional compile-path
change surfaces every doc example the change touches so their prose stays
truthful.
"""

from pathlib import Path

import pytest

import re

import edify
import edify.library as edify_library
from edify import Pattern
from edify.result import Regex
from edify.testing import assert_snapshot

_REPO_ROOT = Path(__file__).parent.parent.parent
_DOCS_ROOT = _REPO_ROOT / "docs"
_SNAPSHOT_ROOT = _REPO_ROOT / "tests" / "snapshots" / "docs"
_CODE_BLOCK_HEADER = ".. code-block:: python"


def _collect_python_code_blocks(rst_path: Path):
    lines = rst_path.read_text().splitlines()
    line_index = 0
    while line_index < len(lines):
        stripped = lines[line_index].strip()
        if stripped != _CODE_BLOCK_HEADER:
            line_index += 1
            continue
        block_start, block_lines = _consume_indented_block(lines, line_index + 1)
        if block_lines:
            yield block_start, "\n".join(block_lines)
        line_index = block_start + len(block_lines)


def _consume_indented_block(lines, start_index):
    block_lines: list[str] = []
    line_index = start_index
    while line_index < len(lines) and lines[line_index].strip() == "":
        line_index += 1
    if line_index >= len(lines):
        return line_index, block_lines
    indent_prefix = lines[line_index][: len(lines[line_index]) - len(lines[line_index].lstrip())]
    if indent_prefix == "":
        return line_index, block_lines
    while line_index < len(lines):
        current_line = lines[line_index]
        if current_line.strip() == "":
            block_lines.append("")
            line_index += 1
            continue
        if not current_line.startswith(indent_prefix):
            break
        block_lines.append(current_line[len(indent_prefix) :])
        line_index += 1
    return line_index - len(block_lines), block_lines


def _discover_blocks():
    for rst_path in sorted(_DOCS_ROOT.rglob("*.rst")):
        for block_start, block_source in _collect_python_code_blocks(rst_path):
            relative_stem = rst_path.relative_to(_DOCS_ROOT).with_suffix("")
            yield rst_path, block_start, block_source, relative_stem


def _snapshot_bodies_for_block(namespace: dict) -> str:
    interesting_pairs = []
    for identifier, value in namespace.items():
        if identifier.startswith("_") or identifier in {"edify", "Pattern", "Regex"}:
            continue
        if isinstance(value, Regex):
            interesting_pairs.append((identifier, "regex", value.source))
        elif isinstance(value, Pattern):
            interesting_pairs.append((identifier, "pattern", value.to_regex_string()))
    interesting_pairs.sort()
    rendered_lines = [f"{name} :: {kind} :: {body}" for name, kind, body in interesting_pairs]
    return "\n".join(rendered_lines) + ("\n" if rendered_lines else "")


DISCOVERED_BLOCKS = list(_discover_blocks())

_BLOCKS_DEFERRED_TO_DOCS_REWRITE = frozenset(
    {
        ("built-in/index", 46),
        ("built-in/index", 83),
        ("built-in/index", 98),
        ("built-in/index", 142),
        ("built-in/index", 175),
        ("built-in/index", 184),
        ("built-in/index", 936),
        ("regex-builder/builder/index", 396),
    }
)


@pytest.mark.parametrize(
    ("rst_path", "block_start", "block_source", "relative_stem"),
    DISCOVERED_BLOCKS,
    ids=[f"{relative_stem}:{block_start}" for _, block_start, _, relative_stem in DISCOVERED_BLOCKS],
)
def test_doc_code_block_produces_the_snapshotted_regex(
    rst_path, block_start, block_source, relative_stem
):
    stem_string = str(relative_stem)
    if (stem_string, block_start) in _BLOCKS_DEFERRED_TO_DOCS_REWRITE:
        pytest.skip("doc block references validators / kwargs slated for the docs rewrite")
    namespace = _prepared_exec_namespace()
    exec(compile(block_source, str(rst_path), "exec"), namespace)
    rendered = _snapshot_bodies_for_block(namespace)
    snapshot_path = _SNAPSHOT_ROOT / stem_string / f"{block_start:04d}.regex"
    assert_snapshot(rendered, snapshot_path)


def _prepared_exec_namespace() -> dict[str, object]:
    namespace: dict[str, object] = {"edify": edify, "Pattern": Pattern, "Regex": Regex, "re": re}
    for edify_export in dir(edify):
        if edify_export.startswith("_"):
            continue
        namespace[edify_export] = getattr(edify, edify_export)
    for library_export in dir(edify_library):
        if library_export.startswith("_"):
            continue
        namespace[library_export] = getattr(edify_library, library_export)
    return namespace
