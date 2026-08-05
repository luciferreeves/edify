"""Navigation has to survive a phone-sized screen.

Below the layout breakpoint there is no room for the nav links or the whole
sidebar tree, so both collapse behind a control. These tests pin the pieces that
make that work — every template that renders a sidebar needs the toggle, and the
footer must not be left in a column that also wraps.
"""

from __future__ import annotations

from pathlib import Path

import pytest

_THEME = Path(__file__).parent.parent.parent / "docs" / "_theme" / "edify"
_BASE_CSS = (_THEME / "static" / "css" / "base.css").read_text(encoding="utf-8")
_CONTENT_CSS = (_THEME / "static" / "css" / "content.css").read_text(encoding="utf-8")
_PLAYGROUND_CSS = (_THEME / "static" / "css" / "playground.css").read_text(encoding="utf-8")
_LAYOUT = (_THEME / "layout.html").read_text(encoding="utf-8")
_MOBILE_JS = (_THEME / "static" / "js" / "mobilenav.js").read_text(encoding="utf-8")

_SIDEBAR_TEMPLATES = ["page.html", "guide.html", "library.html", "api.html"]


def _mobile_block() -> str:
    start = _BASE_CSS.index("@media (max-width: 860px)")
    return _BASE_CSS[start:]


def test_the_layout_loads_the_mobile_navigation_script():
    assert "mobilenav.js" in _LAYOUT


def test_the_header_carries_a_control_for_the_hidden_nav_links():
    assert 'class="nav-toggle"' in _LAYOUT
    assert 'aria-controls="navlinks"' in _LAYOUT
    assert 'id="navlinks"' in _LAYOUT


@pytest.mark.parametrize("template", _SIDEBAR_TEMPLATES)
def test_every_template_with_a_sidebar_can_collapse_it(template: str):
    markup = (_THEME / template).read_text(encoding="utf-8")
    assert 'class="sidenav-toggle"' in markup
    assert 'class="sidenav-inner"' in markup
    assert 'aria-controls="sidenav-tree"' in markup


def test_the_nav_links_become_a_panel_below_the_breakpoint():
    block = _mobile_block()
    assert ".navlinks.navlinks-open { display: flex; }" in block
    assert ".nav-toggle {" in block


def test_the_sidebar_tree_is_collapsed_and_scrollable_below_the_breakpoint():
    block = _mobile_block()
    assert ".sidenav-inner { display: none;" in block
    assert "overflow-y: auto" in block
    assert ".sidenav-open .sidenav-inner { display: block; }" in block


def test_the_toggle_is_labelled_with_the_page_you_are_on():
    assert 'sidenav.querySelector("a.current")' in _MOBILE_JS
    assert "toggleLabel.textContent = currentEntry.textContent.trim();" in _MOBILE_JS


def test_a_column_footer_does_not_also_wrap_into_a_second_column():
    block = _mobile_block()
    assert "flex-direction: column; flex-wrap: nowrap;" in block


def test_the_footer_links_wrap_onto_more_than_one_row():
    assert ".footer-links { flex-wrap: wrap;" in _mobile_block()


def test_a_wide_table_scrolls_instead_of_widening_the_page():
    assert "display: block; width: max-content; max-width: 100%; overflow-x: auto;" in _CONTENT_CSS


def test_the_playground_editor_cannot_push_the_page_wider_than_the_screen():
    assert ".pg-editor { flex: 1; display: flex; min-height: 0; min-width: 0; }" in _PLAYGROUND_CSS
    assert ".pg-builder { flex: 1; min-width: 0; }" in _PLAYGROUND_CSS


def test_the_version_menu_is_bounded_by_the_screen_it_opens_on():
    assert "max-height: min(320px, 55vh)" in _BASE_CSS


def test_the_menus_close_on_escape():
    assert '"Escape"' in _MOBILE_JS
