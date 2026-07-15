"""String-snapshot helpers for pattern tests.

The default flow compares a produced string against a committed reference
file and raises an AssertionError with a unified diff on mismatch. Setting
``EDIFY_UPDATE_SNAPSHOTS=1`` in the environment switches the helper into
regeneration mode: mismatched or missing snapshots are written to disk
instead of raising, so the reference set can be refreshed in one pytest
run.
"""

from __future__ import annotations

import difflib
import os
from pathlib import Path

_UPDATE_ENVIRONMENT_VARIABLE = "EDIFY_UPDATE_SNAPSHOTS"


class SnapshotMismatchError(AssertionError):
    """Raised when actual output diverges from the committed snapshot."""

    def __init__(self, snapshot_path: Path, actual: str, expected: str) -> None:
        rendered_diff = _render_diff(snapshot_path, expected, actual)
        message = (
            f"snapshot mismatch at {snapshot_path}\n\n"
            f"{rendered_diff}\n\n"
            f"help: re-run pytest with {_UPDATE_ENVIRONMENT_VARIABLE}=1 to accept the new "
            "output as the reference."
        )
        super().__init__(message)


class SnapshotMissingError(AssertionError):
    """Raised when the committed snapshot file does not exist."""

    def __init__(self, snapshot_path: Path) -> None:
        message = (
            f"snapshot file missing at {snapshot_path}\n\n"
            f"help: re-run pytest with {_UPDATE_ENVIRONMENT_VARIABLE}=1 to create it."
        )
        super().__init__(message)


def assert_snapshot(actual: str, snapshot_path: Path) -> None:
    """Compare ``actual`` against the reference at ``snapshot_path``.

    Args:
        actual: The string produced by the code under test.
        snapshot_path: Absolute path to the committed reference file.

    Raises:
        SnapshotMissingError: when the reference file does not exist and
            update-mode is off.
        SnapshotMismatchError: when ``actual`` differs from the reference and
            update-mode is off.
    """
    if _update_mode_enabled():
        _write_snapshot(snapshot_path, actual)
        return
    if not snapshot_path.exists():
        raise SnapshotMissingError(snapshot_path)
    expected = snapshot_path.read_text()
    if actual == expected:
        return
    raise SnapshotMismatchError(snapshot_path, actual, expected)


def _update_mode_enabled() -> bool:
    return os.environ.get(_UPDATE_ENVIRONMENT_VARIABLE) == "1"


def _write_snapshot(snapshot_path: Path, actual: str) -> None:
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_path.write_text(actual)


def _render_diff(snapshot_path: Path, expected: str, actual: str) -> str:
    expected_lines = expected.splitlines(keepends=True)
    actual_lines = actual.splitlines(keepends=True)
    diff_iterator = difflib.unified_diff(
        expected_lines,
        actual_lines,
        fromfile=f"{snapshot_path} (snapshot)",
        tofile=f"{snapshot_path} (actual)",
    )
    return "".join(diff_iterator).rstrip()
