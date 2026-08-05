"""Every atom the API reference documents must emit what the page says it emits.

Snapshotting a doc block only proves the block is self-consistent. What
``docs/api/atoms.rst`` actually promises is stronger: that each entry describes
*that* atom and the regex it really produces. These tests assert that directly,
so a construction can never drift from the fragment it claims to build.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from edify import atoms

_ATOMS_PAGE = Path(__file__).resolve().parent.parent.parent / "docs" / "api" / "atoms.rst"
_ENTRY = re.compile(r"\.\. py:data:: edify\.atoms\.(\w+)\n(.*?)(?=\n\.\. py:data::|\Z)", re.S)
_EMITS = re.compile(r"\*\*Emits\*\* ``(.*)``", re.S)

_CONTROL_ESCAPES = {0x00: "\\x00", 0x09: "\\t", 0x0A: "\\n", 0x0D: "\\r"}


def _documented_entries() -> list[tuple[str, str]]:
    page_text = _ATOMS_PAGE.read_text(encoding="utf-8")
    return [(name, body) for name, body in _ENTRY.findall(page_text)]


DOCUMENTED_ENTRIES = _documented_entries()


def test_the_page_documents_every_exported_atom():
    documented = {name for name, _ in DOCUMENTED_ENTRIES}
    exported = set(atoms.__all__)
    assert documented == exported


@pytest.mark.parametrize(
    ("atom_name", "entry_body"), DOCUMENTED_ENTRIES, ids=[name for name, _ in DOCUMENTED_ENTRIES]
)
def test_each_entry_documents_the_regex_its_atom_emits(atom_name: str, entry_body: str):
    documented = _EMITS.search(entry_body)
    assert documented is not None, f"{atom_name} has no **Emits** line"
    emitted = getattr(atoms, atom_name).to_regex_string()
    assert documented.group(1) == emitted.translate(_CONTROL_ESCAPES)


def test_the_page_carries_no_raw_control_characters():
    raw_bytes = _ATOMS_PAGE.read_bytes()
    assert b"\x00" not in raw_bytes
