"""Tests for the public-surface snapshot tool in ``tools/surface.py``."""

import importlib.util
from pathlib import Path

_REPO_ROOT = Path(__file__).parent.parent.parent
_TOOL_PATH = _REPO_ROOT / "tools" / "surface.py"
_SURFACE_PATH = _REPO_ROOT / ".public-surface"


def _load_tool():
    spec = importlib.util.spec_from_file_location("edify_surface_tool", _TOOL_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_TOOL = _load_tool()


def test_committed_surface_file_exists_and_is_non_empty():
    assert _SURFACE_PATH.exists()
    assert _SURFACE_PATH.read_text(encoding="utf-8").strip() != ""


def test_computed_surface_matches_the_committed_snapshot():
    computed = _TOOL.compute_surface()
    committed = _SURFACE_PATH.read_text(encoding="utf-8")
    assert computed == committed, (
        "public surface drift: run `python tools/surface.py --write` and commit "
        ".public-surface with a changes/ fragment describing the change."
    )


def test_surface_lists_the_core_public_symbols():
    computed = _TOOL.compute_surface()
    assert "edify.Pattern" in computed
    assert "edify.RegexBuilder" in computed
    assert "edify.Regex" in computed
    assert "edify.EdifyError" in computed


def test_surface_excludes_private_module_paths():
    computed = _TOOL.compute_surface()
    for line in computed.splitlines():
        dotted = line.split("(")[0]
        parts = dotted.split(".")
        assert not any(part.startswith("_") for part in parts[:-1]), (
            f"surface line leaks a private module path: {line!r}"
        )


def test_surface_is_sorted_and_deduplicated():
    computed = _TOOL.compute_surface()
    lines = computed.splitlines()
    assert lines == sorted(lines)
    assert len(lines) == len(set(lines))


def test_check_returns_zero_when_surface_matches(capsys):
    exit_code = _TOOL.main(["--check"])
    assert exit_code == 0


def test_check_returns_one_when_surface_drifts(tmp_path, monkeypatch, capsys):
    drifted_snapshot = tmp_path / ".public-surface"
    drifted_snapshot.write_text("edify.SomethingRemoved\n", encoding="utf-8")
    monkeypatch.setattr(_TOOL, "_SURFACE_PATH", drifted_snapshot)
    exit_code = _TOOL.main(["--check"])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "public surface drift" in captured.err


def test_write_overwrites_the_snapshot_file(tmp_path, monkeypatch):
    target = tmp_path / ".public-surface"
    monkeypatch.setattr(_TOOL, "_SURFACE_PATH", target)
    exit_code = _TOOL.main(["--write"])
    assert exit_code == 0
    assert target.read_text(encoding="utf-8") == _TOOL.compute_surface()


def test_bare_invocation_prints_the_surface_to_stdout(capsys):
    exit_code = _TOOL.main([])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "edify.Pattern" in captured.out
