"""Discipline: every type-checker suppression must carry a rule code AND an inline reason.

The well-formed shape is ``# type: ignore[<code>]  # <reason>`` (mypy) or
``# pyright: ignore[<code>]  # <reason>`` (pyright). The check recognises both
forms and rejects any bare suppression that lacks a rule code or an inline
rationale.
"""

import re
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
_EDIFY_ROOT = _REPO_ROOT / "edify"

_WELL_FORMED = re.compile(
    r"#\s*(?:type|pyright):\s*ignore\[[^\]]+\]\s+#\s*\S+.*$",
)

_ANY_SUPPRESSION = re.compile(r"#\s*(?:type|pyright):\s*ignore\b")


def _collect_python_sources(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.py") if "__pycache__" not in p.parts)


def test_every_suppression_carries_a_rule_code_and_a_reason():
    offenders: list[str] = []
    for path in _collect_python_sources(_EDIFY_ROOT):
        for lineno, line in enumerate(path.read_text().splitlines(), start=1):
            if _ANY_SUPPRESSION.search(line) and not _WELL_FORMED.search(line):
                offenders.append(f"{path.relative_to(_REPO_ROOT)}:{lineno}  {line.rstrip()}")
    assert not offenders, (
        "type-checker suppressions must include both a rule code and an inline reason.\n"
        + "\n".join(offenders)
    )
