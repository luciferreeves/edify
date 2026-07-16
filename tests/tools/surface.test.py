"""Tests for the public-surface snapshot tool in ``tools/surface.py``."""

from pathlib import Path

import pytest

from tools import surface

_REPO_ROOT = Path(__file__).parent.parent.parent
_SURFACE_PATH = _REPO_ROOT / ".public-surface"


def test_committed_surface_file_exists_and_is_non_empty() -> None:
    assert _SURFACE_PATH.exists()
    assert _SURFACE_PATH.read_text(encoding="utf-8").strip() != ""


def test_computed_surface_matches_the_committed_snapshot() -> None:
    computed = surface.compute_surface()
    committed = _SURFACE_PATH.read_text(encoding="utf-8")
    assert computed == committed, (
        "public surface drift: run `python tools/surface.py --write` and commit "
        ".public-surface with a changes/ fragment describing the change."
    )


def test_surface_lists_the_core_public_symbols() -> None:
    computed = surface.compute_surface()
    assert "edify.Pattern" in computed
    assert "edify.RegexBuilder" in computed
    assert "edify.Regex" in computed
    assert "edify.EdifyError" in computed


def test_surface_excludes_private_module_paths() -> None:
    computed = surface.compute_surface()
    for line in computed.splitlines():
        dotted = line.split("(")[0]
        parts = dotted.split(".")
        assert not any(part.startswith("_") for part in parts[:-1]), (
            f"surface line leaks a private module path: {line!r}"
        )


def test_surface_is_sorted_and_deduplicated() -> None:
    computed = surface.compute_surface()
    lines = computed.splitlines()
    assert lines == sorted(lines)
    assert len(lines) == len(set(lines))


def test_check_returns_zero_when_surface_matches() -> None:
    exit_code = surface.main(["--check"])
    assert exit_code == 0


def test_check_returns_one_when_surface_drifts(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    drifted_snapshot = tmp_path / ".public-surface"
    drifted_snapshot.write_text("edify.SomethingRemoved\n", encoding="utf-8")
    monkeypatch.setattr(surface, "_SURFACE_PATH", drifted_snapshot)
    exit_code = surface.main(["--check"])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "public surface drift" in captured.err


def test_write_overwrites_the_snapshot_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    target = tmp_path / ".public-surface"
    monkeypatch.setattr(surface, "_SURFACE_PATH", target)
    exit_code = surface.main(["--write"])
    assert exit_code == 0
    assert target.read_text(encoding="utf-8") == surface.compute_surface()


def test_bare_invocation_prints_the_surface_to_stdout(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = surface.main([])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "edify.Pattern" in captured.out
