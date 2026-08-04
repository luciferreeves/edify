"""The in-browser playground must answer with advice a reader can actually act on.

The alternate engine is a compiled extension, so it can never load in the
playground's WebAssembly sandbox. Edify's own diagnostic for a missing backend
tells the caller to install an extra, which is correct at a terminal and useless
in a browser tab. These tests drive the harness the playground actually ships,
with the module hidden the way WebAssembly hides it.
"""

from __future__ import annotations

import json
import re
import sys
from collections.abc import Callable, Sequence
from importlib.abc import MetaPathFinder
from importlib.machinery import ModuleSpec
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest

_RUNTIME = (
    Path(__file__).parent.parent.parent
    / "docs"
    / "_theme"
    / "edify"
    / "static"
    / "js"
    / "pyodide-runtime.js"
)
_HARNESS = re.compile(r"const HARNESS = String\.raw`(.*?)`;", re.S)


def _harness_source() -> str:
    found = _HARNESS.search(_RUNTIME.read_text())
    assert found is not None, "the playground runtime no longer defines a HARNESS block"
    return found.group(1)


class _Unavailable(MetaPathFinder):
    """Refuse one module the way a WebAssembly runtime refuses a compiled extension."""

    def __init__(self, blocked: str) -> None:
        self._blocked = blocked

    def find_spec(
        self,
        fullname: str,
        path: Sequence[str] | None = None,
        target: ModuleType | None = None,
    ) -> ModuleSpec | None:
        if fullname == self._blocked:
            raise ImportError(f"no module named {fullname!r}")
        return None


@pytest.fixture
def browser_namespace(monkeypatch: pytest.MonkeyPatch) -> dict[str, Any]:
    """The shipped harness, loaded with the alternate engine unimportable."""
    monkeypatch.delitem(sys.modules, "regex", raising=False)
    monkeypatch.setattr(sys, "meta_path", [_Unavailable("regex"), *sys.meta_path])
    namespace: dict[str, Any] = {}
    exec(compile(_harness_source(), "<harness>", "exec"), namespace)
    return namespace


def _run(namespace: dict[str, Any], source: str) -> dict[str, Any]:
    runner: Callable[[str], str] = namespace["edify_run"]
    return json.loads(runner(source))


def test_the_alternate_engine_is_reported_as_unavailable_in_the_browser(
    browser_namespace: dict[str, Any],
):
    outcome = _run(
        browser_namespace, 'RegexBuilder().one_or_more().digit().to_regex(engine="regex")'
    )
    assert "not available in this playground" in outcome["error"]


def test_the_unavailable_engine_message_does_not_tell_the_reader_to_retry(
    browser_namespace: dict[str, Any],
):
    outcome = _run(
        browser_namespace, 'RegexBuilder().one_or_more().digit().to_regex(engine="regex")'
    )
    assert "and retry" not in outcome["error"]


def test_the_unavailable_engine_message_names_a_way_forward(
    browser_namespace: dict[str, Any],
):
    outcome = _run(
        browser_namespace, 'RegexBuilder().one_or_more().digit().to_regex(engine="regex")'
    )
    assert "default engine" in outcome["error"]


def test_the_default_engine_still_compiles_when_the_alternate_one_is_missing(
    browser_namespace: dict[str, Any],
):
    outcome = _run(browser_namespace, "RegexBuilder().one_or_more().digit()")
    assert outcome["regex"] == r"\d+"
    assert outcome.get("error") is None


def test_a_pattern_still_matches_after_the_alternate_engine_is_refused(
    browser_namespace: dict[str, Any],
):
    _run(browser_namespace, "RegexBuilder().one_or_more().digit()")
    tester: Callable[[str], bool] = browser_namespace["edify_test"]
    assert tester("2024") is True
    assert tester("abc") is False
