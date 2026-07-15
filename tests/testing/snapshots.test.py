"""Tests for the snapshot helper in :mod:`edify.testing.snapshots`."""

from pathlib import Path

import pytest

from edify.testing import SnapshotMismatchError, SnapshotMissingError, assert_snapshot

_UPDATE_ENVIRONMENT_VARIABLE = "EDIFY_UPDATE_SNAPSHOTS"


def test_assert_snapshot_passes_when_actual_matches_committed_reference(tmp_path, monkeypatch):
    monkeypatch.delenv(_UPDATE_ENVIRONMENT_VARIABLE, raising=False)
    snapshot_path = tmp_path / "identical.snapshot"
    snapshot_path.write_text("hello\n")
    assert_snapshot("hello\n", snapshot_path)


def test_assert_snapshot_raises_snapshot_mismatch_when_content_differs(tmp_path, monkeypatch):
    monkeypatch.delenv(_UPDATE_ENVIRONMENT_VARIABLE, raising=False)
    snapshot_path = tmp_path / "drift.snapshot"
    snapshot_path.write_text("expected\n")
    with pytest.raises(SnapshotMismatchError) as excinfo:
        assert_snapshot("actual\n", snapshot_path)
    text = str(excinfo.value)
    assert "snapshot mismatch" in text
    assert "-expected" in text
    assert "+actual" in text
    assert "EDIFY_UPDATE_SNAPSHOTS=1" in text


def test_assert_snapshot_raises_snapshot_missing_when_reference_absent(tmp_path, monkeypatch):
    monkeypatch.delenv(_UPDATE_ENVIRONMENT_VARIABLE, raising=False)
    absent_snapshot = tmp_path / "never_written.snapshot"
    with pytest.raises(SnapshotMissingError, match="snapshot file missing"):
        assert_snapshot("any actual value", absent_snapshot)


def test_update_mode_writes_the_snapshot_when_the_file_is_missing(tmp_path, monkeypatch):
    monkeypatch.setenv(_UPDATE_ENVIRONMENT_VARIABLE, "1")
    snapshot_path = tmp_path / "created.snapshot"
    assert_snapshot("fresh content\n", snapshot_path)
    assert snapshot_path.read_text() == "fresh content\n"


def test_update_mode_overwrites_the_snapshot_on_drift(tmp_path, monkeypatch):
    monkeypatch.setenv(_UPDATE_ENVIRONMENT_VARIABLE, "1")
    snapshot_path = tmp_path / "regenerated.snapshot"
    snapshot_path.write_text("stale\n")
    assert_snapshot("current\n", snapshot_path)
    assert snapshot_path.read_text() == "current\n"


def test_update_mode_is_off_when_env_variable_is_set_to_other_value(tmp_path, monkeypatch):
    monkeypatch.setenv(_UPDATE_ENVIRONMENT_VARIABLE, "0")
    snapshot_path = tmp_path / "no_write.snapshot"
    with pytest.raises(SnapshotMissingError):
        assert_snapshot("actual", snapshot_path)


def test_update_mode_creates_missing_parent_directories(tmp_path, monkeypatch):
    monkeypatch.setenv(_UPDATE_ENVIRONMENT_VARIABLE, "1")
    snapshot_path = tmp_path / "nested" / "dir" / "leaf.snapshot"
    assert_snapshot("value", snapshot_path)
    assert snapshot_path.read_text() == "value"


def test_snapshot_mismatch_error_names_the_snapshot_path(tmp_path, monkeypatch):
    monkeypatch.delenv(_UPDATE_ENVIRONMENT_VARIABLE, raising=False)
    snapshot_path = tmp_path / "named.snapshot"
    snapshot_path.write_text("was")
    with pytest.raises(SnapshotMismatchError) as excinfo:
        assert_snapshot("is", snapshot_path)
    assert str(snapshot_path) in str(excinfo.value)


def test_snapshot_missing_error_is_an_assertion_error_subclass():
    assert issubclass(SnapshotMissingError, AssertionError)


def test_snapshot_mismatch_error_is_an_assertion_error_subclass():
    assert issubclass(SnapshotMismatchError, AssertionError)


def test_snapshot_helper_is_reachable_via_edify_testing_namespace(tmp_path):
    from edify import testing

    snapshot_path: Path = tmp_path / "namespace.snapshot"
    snapshot_path.write_text("ok\n")
    testing.assert_snapshot("ok\n", snapshot_path)
