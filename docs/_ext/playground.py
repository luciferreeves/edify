"""Playground + navigation Sphinx extension.

Provides the ``edify-playground`` directive (a mount point the browser widget
hydrates into a live editor, with optional ``:tests:`` seed strings), the
per-section template overrides, and a computed library sidebar that mirrors the
real ``edify.library`` / ``edify.atoms`` structure.
"""

from __future__ import annotations

import base64
import html
import importlib
import pkgutil
import re
from typing import Any

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.application import Sphinx

_CONTROL = {"\n": "\\n", "\t": "\\t", "\r": "\\r", "\f": "\\f", "\v": "\\v", "\0": "\\0"}


def _display_regex(regex: str) -> str:
    return re.sub(
        r"[\x00-\x1f]",
        lambda m: _CONTROL.get(m.group(), f"\\x{ord(m.group()):02x}"),
        regex,
    )

_STANDALONE = {
    "playground": "wide.html",
    "upgrading/index": "wide.html",
    "upgrading/0.3-to-1.0": "wide.html",
    "deprecation-policy": "wide.html",
    "changelog": "wide.html",
    "contributing": "wide.html",
}

_CATEGORY_TITLES = {
    "address": "Address", "api": "API", "auth": "Auth", "color": "Color",
    "contact": "Contact", "data": "Data", "document": "Documents",
    "financial": "Finance", "geo": "Geo", "grammar": "Grammar",
    "identifier": "Identifiers", "media": "Media", "medical": "Medical",
    "numeric": "Numeric", "product": "Product", "publishing": "Publishing",
    "security": "Security", "software": "Software", "temporal": "Temporal",
    "text": "Text", "transport": "Transport", "web": "Web",
}
_CATEGORY_ORDER = list(_CATEGORY_TITLES)

_sections_cache: list[tuple[str, str, list[str]]] | None = None


def _encode(text: str) -> str:
    return base64.b64encode(text.encode("utf-8")).decode("ascii")


def _library_sections() -> list[tuple[str, str, list[str]]]:
    """(title, dir, [validator names]) for every library category + atoms."""
    global _sections_cache
    if _sections_cache is not None:
        return _sections_cache
    library = importlib.import_module("edify.library")
    by_dir: dict[str, list[str]] = {}
    for module in pkgutil.iter_modules(library.__path__):
        if module.name.startswith("_"):
            continue
        loaded = importlib.import_module(f"edify.library.{module.name}")
        names = sorted(
            name for name in dir(loaded)
            if not name.startswith("_") and hasattr(getattr(loaded, name), "to_regex_string")
        )
        if names:
            by_dir[module.name] = names
    _sections_cache = [
        (_CATEGORY_TITLES[key], key, by_dir[key]) for key in _CATEGORY_ORDER if key in by_dir
    ]
    return _sections_cache


class EdifyPlayground(Directive):
    """``.. edify-playground::`` — a live builder/regex/test widget."""

    has_content = True
    option_spec = {"tests": directives.unchanged}

    def run(self) -> list[nodes.Node]:
        source = "\n".join(self.content).strip()
        attributes = f'data-source="{_encode(source)}"'
        raw_tests = self.options.get("tests", "")
        test_lines = [item.strip() for item in raw_tests.split("|") if item.strip()]
        if test_lines:
            attributes += f' data-tests="{_encode(chr(10).join(test_lines))}"'
        markup = (
            f'<div class="edify-playground" {attributes}>'
            f'<pre class="pg-code pg-fallback">{html.escape(source)}</pre>'
            f"</div>"
        )
        return [nodes.raw("", markup, format="html")]


def _library_nav(app: Sphinx, pagename: str) -> str:
    builder = app.builder
    docs = set(app.env.found_docs)
    current_dir = pagename.split("/")[1] if pagename.count("/") >= 2 else ""
    parts = ['<nav class="lib-nav" aria-label="Library navigation">']
    home = builder.get_relative_uri(pagename, "library/index")
    home_cls = " current" if pagename == "library/index" else ""
    parts.append(f'<a class="lib-nav-home{home_cls}" href="{home}">Library</a>')
    for title, directory, names in _library_sections():
        present = [n for n in names if f"library/{directory}/{n}" in docs]
        if not present or f"library/{directory}/index" not in docs:
            continue
        active = directory == current_dir
        cat_uri = builder.get_relative_uri(pagename, f"library/{directory}/index")
        cat_cls = " open" if active else ""
        parts.append(f'<div class="lib-nav-section{cat_cls}">')
        parts.append(f'<a class="lib-nav-cat" href="{cat_uri}">{html.escape(title)}</a>')
        if active:
            parts.append("<ul>")
            for name in present:
                target = f"library/{directory}/{name}"
                uri = builder.get_relative_uri(pagename, target)
                item_cls = ' class="current"' if pagename == target else ""
                parts.append(f'<li><a href="{uri}"{item_cls}>{html.escape(name)}</a></li>')
            parts.append("</ul>")
        parts.append("</div>")
    parts.append("</nav>")
    return "".join(parts)


class EdifyValidator(Directive):
    """``.. edify-validator:: name`` — a rich header card for a library validator.

    Imports the validator, shows that it is a callable ``Pattern`` returning
    ``bool``, its import line, and its emitted regex in a styled box.
    """

    required_arguments = 1
    option_spec = {"module": directives.unchanged}

    def run(self) -> list[nodes.Node]:
        name = self.arguments[0].strip()
        module = self.options.get("module", "edify.library").strip()
        try:
            loaded = importlib.import_module(module)
            regex = _display_regex(getattr(loaded, name).to_regex_string())
        except Exception:
            regex = ""
        regex_block = (
            f'<div class="val-regex"><span class="val-regex-tag">emits</span>'
            f"<code>{html.escape(regex)}</code></div>"
            if regex
            else ""
        )
        markup = (
            '<div class="val-header">'
            '<div class="val-meta">'
            '<span class="val-kind">callable Pattern</span>'
            '<span class="val-ret">&rarr; bool</span>'
            f'<code class="val-import">from {html.escape(module)} import {html.escape(name)}</code>'
            "</div>"
            f"{regex_block}"
            "</div>"
        )
        return [nodes.raw("", markup, format="html")]


def _select_template(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Any,
) -> str | None:
    if pagename == "index":
        return "home.html"
    if pagename == "library/index" or pagename.startswith("library/"):
        context["library_nav"] = _library_nav(app, pagename)
        return "library.html"
    if pagename.startswith("api/"):
        return "api.html"
    return _STANDALONE.get(pagename)


def setup(app: Sphinx) -> dict[str, object]:
    app.add_directive("edify-playground", EdifyPlayground)
    app.add_directive("edify-validator", EdifyValidator)
    app.connect("html-page-context", _select_template)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
