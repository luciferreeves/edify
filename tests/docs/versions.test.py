"""The version switcher must stay ours, and stay absent when there is nothing to switch.

Read the Docs injects its own flyout into every published page. The theme hides
it and renders the version list in the navbar instead, from the data the addons
script publishes. These tests pin the pieces that make that work: drop the script
tag or the hide rule and the Read the Docs chrome silently comes back.
"""

from __future__ import annotations

from pathlib import Path

import pytest

_THEME = Path(__file__).parent.parent.parent / "docs" / "_theme" / "edify"
_LAYOUT = (_THEME / "layout.html").read_text(encoding="utf-8")
_BASE_CSS = (_THEME / "static" / "css" / "base.css").read_text(encoding="utf-8")
_VERSIONS_JS = (_THEME / "static" / "js" / "versions.js").read_text(encoding="utf-8")

_REQUIRED_HOOKS = [
    "version-switcher",
    "version-button",
    "version-name",
    "version-menu",
    "version-list",
]


@pytest.mark.parametrize("hook", _REQUIRED_HOOKS)
def test_the_layout_provides_every_hook_the_script_looks_up(hook: str):
    assert f'"{hook}"' in _VERSIONS_JS or f".{hook}" in _VERSIONS_JS
    assert hook in _LAYOUT


def test_the_layout_loads_the_version_script():
    assert "versions.js" in _LAYOUT


def test_the_switcher_starts_hidden_so_a_local_build_shows_nothing():
    assert '<div class="version-switcher" hidden>' in _LAYOUT
    assert 'class="footer-rtd"' in _LAYOUT
    assert "hidden>Hosted by Read the Docs</a>" in _LAYOUT


def test_the_default_read_the_docs_flyout_is_hidden():
    assert "readthedocs-flyout { display: none; }" in _BASE_CSS


def test_the_script_reads_the_read_the_docs_addons_event():
    assert "readthedocs-addons-data-ready" in _VERSIONS_JS
    assert "event.detail.data()" in _VERSIONS_JS


def test_the_script_links_each_version_to_its_documentation_url():
    assert "version.urls.documentation" in _VERSIONS_JS


def test_latest_is_displayed_capitalised_without_changing_its_slug():
    assert 'DISPLAY_NAMES = { latest: "Latest" }' in _VERSIONS_JS
    assert "link.href = version.urls.documentation;" in _VERSIONS_JS
    assert "link.textContent = displayName(version.slug);" in _VERSIONS_JS


def test_the_menu_can_be_dismissed_with_the_keyboard():
    assert "Escape" in _VERSIONS_JS
    assert "aria-expanded" in _VERSIONS_JS


def test_the_switcher_is_styled_from_the_theme_tokens_so_dark_mode_follows():
    switcher_block = _BASE_CSS[_BASE_CSS.index("readthedocs-flyout") :]
    switcher_block = switcher_block[: switcher_block.index("/* ---- docs two-column layout")]
    for token in ["var(--border)", "var(--muted)", "var(--fg)", "var(--accent)", "var(--bg)"]:
        assert token in switcher_block
    assert "#fff" not in switcher_block.lower()
