"""Tests for the ``changes/`` fragment generator in ``tools/changes.py``."""

import importlib.util
from pathlib import Path

_REPO_ROOT = Path(__file__).parent.parent.parent
_GENERATOR_PATH = _REPO_ROOT / "tools" / "changes.py"


def _load_generator():
    spec = importlib.util.spec_from_file_location("edify_changes_tool", _GENERATOR_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_GENERATOR = _load_generator()


def _write_fragment(directory: Path, name: str, body: str) -> Path:
    fragment_path = directory / name
    fragment_path.write_text(body, encoding="utf-8")
    return fragment_path


def test_collect_fragments_returns_files_in_fragment_id_order(tmp_path):
    _write_fragment(tmp_path, "0020-second.rst", "[change]\nanchor=b\nheading=B\ncontext=b")
    _write_fragment(tmp_path, "0010-first.rst", "[change]\nanchor=a\nheading=A\ncontext=a")
    collected = _GENERATOR.collect_fragments(tmp_path)
    assert [path.name for path in collected] == ["0010-first.rst", "0020-second.rst"]


def test_collect_fragments_skips_the_readme(tmp_path):
    _write_fragment(tmp_path, "README.rst", "not a fragment")
    _write_fragment(tmp_path, "0010-only.rst", "[change]\nanchor=a\nheading=A\ncontext=a")
    collected = _GENERATOR.collect_fragments(tmp_path)
    assert [path.name for path in collected] == ["0010-only.rst"]


def test_render_fragment_emits_anchor_heading_and_context(tmp_path):
    fragment_path = _write_fragment(
        tmp_path,
        "0010-example.rst",
        "[change]\nanchor = my-anchor\nheading = My Heading\ncontext = A single sentence.",
    )
    rendered = _GENERATOR.render_fragment(fragment_path)
    assert ".. _my-anchor:" in rendered
    assert "My Heading" in rendered
    assert "-" * len("My Heading") in rendered
    assert "A single sentence." in rendered


def test_render_fragment_collapses_multiline_context_into_one_paragraph(tmp_path):
    fragment_path = _write_fragment(
        tmp_path,
        "0010-multiline.rst",
        "[change]\nanchor = a\nheading = H\ncontext = first line\n    second line",
    )
    rendered = _GENERATOR.render_fragment(fragment_path)
    assert "first line second line" in rendered


def test_render_fragment_includes_before_after_block_when_both_present(tmp_path):
    fragment_path = _write_fragment(
        tmp_path,
        "0010-beforeafter.rst",
        "[change]\nanchor = a\nheading = H\nbefore = old\nafter = new\ncontext = changed",
    )
    rendered = _GENERATOR.render_fragment(fragment_path)
    assert ".. code-block:: text" in rendered
    assert "    old" in rendered
    assert "    new" in rendered


def test_render_fragment_omits_before_after_block_when_absent(tmp_path):
    fragment_path = _write_fragment(
        tmp_path,
        "0010-nofix.rst",
        "[change]\nanchor = a\nheading = H\ncontext = no before/after here",
    )
    rendered = _GENERATOR.render_fragment(fragment_path)
    assert ".. code-block:: text" not in rendered


def test_render_all_concatenates_every_fragment_in_order(tmp_path):
    _write_fragment(tmp_path, "0020-b.rst", "[change]\nanchor=b\nheading=Bravo\ncontext=b")
    _write_fragment(tmp_path, "0010-a.rst", "[change]\nanchor=a\nheading=Alpha\ncontext=a")
    rendered = _GENERATOR.render_all(tmp_path)
    assert rendered.index("Alpha") < rendered.index("Bravo")


def test_main_release_deletes_consumed_fragments(tmp_path, monkeypatch):
    _write_fragment(tmp_path, "0010-a.rst", "[change]\nanchor=a\nheading=A\ncontext=a")
    monkeypatch.setattr(_GENERATOR, "_CHANGES_DIR", tmp_path)
    exit_code = _GENERATOR.main(["--release"])
    assert exit_code == 0
    assert _GENERATOR.collect_fragments(tmp_path) == []


def test_main_without_release_leaves_fragments_in_place(tmp_path, monkeypatch, capsys):
    _write_fragment(tmp_path, "0010-a.rst", "[change]\nanchor=a\nheading=A\ncontext=a")
    monkeypatch.setattr(_GENERATOR, "_CHANGES_DIR", tmp_path)
    exit_code = _GENERATOR.main([])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "A" in captured.out
    assert len(_GENERATOR.collect_fragments(tmp_path)) == 1


def test_committed_changes_directory_fragments_all_parse():
    changes_dir = _REPO_ROOT / "changes"
    for fragment_path in _GENERATOR.collect_fragments(changes_dir):
        rendered = _GENERATOR.render_fragment(fragment_path)
        assert rendered.strip() != ""
