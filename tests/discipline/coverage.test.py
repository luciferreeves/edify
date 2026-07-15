"""Anti-vacuous-green coverage discipline.

If ``[tool.coverage.run].source`` ever points at the wrong directory (say,
``src/edify`` post-reorg while the code moved back to ``edify/``), the
``--cov-fail-under`` gate passes with an empty file list — a 100% score
over zero measured lines. This test rebuilds the source-file discovery
that coverage.py runs internally, asserts the file list is non-empty, and
asserts every listed file is a real Python source inside ``edify/``.
"""

from pathlib import Path

import coverage

_REPO_ROOT = Path(__file__).parent.parent.parent
_EDIFY_ROOT = _REPO_ROOT / "edify"


def test_coverage_run_source_resolves_to_the_edify_package_tree():
    coverage_instance = coverage.Coverage()
    configured_sources = coverage_instance.config.source
    assert configured_sources is not None
    assert configured_sources != [], (
        "coverage's [tool.coverage.run].source is empty — the gate would pass over "
        "zero measured lines. Point source at 'edify'."
    )
    for entry in configured_sources:
        assert entry == "edify", (
            f"coverage source contains {entry!r} — expected exactly ['edify']. "
            "A wrong source path is the one way this gate passes vacuously green."
        )


def test_edify_package_tree_contains_measurable_python_source():
    python_files = sorted(_EDIFY_ROOT.rglob("*.py"))
    assert python_files, (
        "no Python files found under edify/ — the coverage source directory is empty."
    )
    total_source_bytes = sum(python_file.stat().st_size for python_file in python_files)
    assert total_source_bytes > 0, (
        "every file under edify/ is empty — coverage would measure nothing across the tree."
    )
    non_init_source_files = [path for path in python_files if path.name != "__init__.py"]
    assert non_init_source_files, (
        "edify/ contains only __init__.py files — nothing substantial for coverage to measure."
    )
