"""Render committed change fragments into CHANGELOG / upgrade-guide RST.

Stdlib only, no external changelog tooling. Reads every ``changes/*.rst``
fragment (INI with a single ``[change]`` section), sorts them by filename, and
renders each into an RST section. On ``--release`` the rendered blocks are
slotted into the target files and the consumed fragments are deleted.
"""

from __future__ import annotations

import configparser
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
_CHANGES_DIR = _REPO_ROOT / "changes"


def collect_fragments(changes_dir: Path) -> list[Path]:
    """Return the fragment files under ``changes_dir`` in fragment-id order."""
    fragments = [path for path in changes_dir.glob("*.rst") if path.name != "README.rst"]
    return sorted(fragments, key=lambda path: path.name)


def render_fragment(fragment_path: Path) -> str:
    """Return the RST block for a single fragment file."""
    parser = configparser.ConfigParser()
    parser.read(fragment_path, encoding="utf-8")
    change = parser["change"]
    anchor = change["anchor"]
    heading = change["heading"]
    context = _normalize_paragraph(change["context"])
    lines = [f".. _{anchor}:", "", heading, "-" * len(heading), "", context, ""]
    before = change.get("before")
    after = change.get("after")
    if before is not None and after is not None:
        lines.extend(["", ".. code-block:: text", "", f"    {before}", f"    {after}", ""])
    return "\n".join(lines)


def render_all(changes_dir: Path) -> str:
    """Return the concatenated RST for every fragment under ``changes_dir``."""
    fragment_paths = collect_fragments(changes_dir)
    rendered_blocks = [render_fragment(path) for path in fragment_paths]
    return "\n".join(rendered_blocks)


def _normalize_paragraph(raw: str) -> str:
    collapsed_lines = [line.strip() for line in raw.splitlines()]
    non_empty = [line for line in collapsed_lines if line]
    return " ".join(non_empty)


def main(argv: list[str]) -> int:
    """Print the rendered fragments; with ``--release`` also delete them."""
    rendered = render_all(_CHANGES_DIR)
    sys.stdout.write(rendered)
    if "--release" in argv:
        for fragment_path in collect_fragments(_CHANGES_DIR):
            fragment_path.unlink()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
