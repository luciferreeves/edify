"""Discipline test — every ``# pragma: no cover`` carries an inline reason.

The rule: pragmas are allowed only on individual lines, each with an inline
reason after the pragma text. File-level pragmas and bare pragmas without
a reason are banned outright — same discipline as the type-ignore rule.
"""

import io
import re
import tokenize
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).parent.parent.parent
_EDIFY_ROOT = _REPO_ROOT / "edify"
_TESTS_ROOT = _REPO_ROOT / "tests"

_PRAGMA_LINE_PATTERN = re.compile(r"#\s*pragma:\s*no cover\b(.*)$")


def _every_python_file():
    for source_root in (_EDIFY_ROOT, _TESTS_ROOT):
        yield from source_root.rglob("*.py")


def _pragma_comments(python_file):
    source_text = python_file.read_text()
    for token in tokenize.tokenize(io.BytesIO(source_text.encode("utf-8")).readline):
        if token.type != tokenize.COMMENT:
            continue
        matched = _PRAGMA_LINE_PATTERN.search(token.string)
        if matched is None:
            continue
        yield token.start[0], token.string, matched.group(1)


@pytest.mark.parametrize("python_file", sorted(_every_python_file()), ids=lambda path: str(path))
def test_no_bare_pragma_no_cover_without_inline_reason(python_file):
    for line_number, comment_text, reason_suffix in _pragma_comments(python_file):
        stripped_reason = reason_suffix.strip()
        if stripped_reason == "" or stripped_reason[0] not in "—:-":
            pytest.fail(
                f"{python_file.relative_to(_REPO_ROOT)}:{line_number} carries "
                f"{comment_text!r} without an inline reason. The rule is: every pragma "
                "gets an em-dash-separated reason on the same line, e.g. "
                "'# pragma: no cover — <why this branch is unreachable>'."
            )
