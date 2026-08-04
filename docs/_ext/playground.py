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
from typing import Any, ClassVar

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.application import Sphinx

_STANDALONE = {
    "playground": "wide.html",
    "upgrading/index": "wide.html",
    "upgrading/0.3-to-1.0": "wide.html",
    "deprecation-policy": "wide.html",
    "changelog": "wide.html",
    "contributing": "wide.html",
}

_CATEGORY_ORDER = [
    "address",
    "api",
    "auth",
    "color",
    "contact",
    "data",
    "document",
    "financial",
    "geo",
    "grammar",
    "identifier",
    "media",
    "medical",
    "numeric",
    "product",
    "publishing",
    "security",
    "software",
    "temporal",
    "text",
    "transport",
    "web",
]

_NESTING: dict[str, dict[str, list[str]]] = {
    "address": {
        "ip": ["ipv4", "ipv6"],
        "subnet": ["cidr"],
        "domain": ["subdomain", "hostname", "tld"],
    },
}


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
            name
            for name in dir(loaded)
            if not name.startswith("_") and hasattr(getattr(loaded, name), "to_regex_string")
        )
        if names:
            by_dir[module.name] = names
    _sections_cache = [(key, key, by_dir[key]) for key in _CATEGORY_ORDER if key in by_dir]
    return _sections_cache


class EdifyPlayground(Directive):
    """``.. edify-playground::`` — a live builder/regex/test widget."""

    has_content = True
    option_spec: ClassVar[dict[str, object]] = {"tests": directives.unchanged}

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


def _library_link(builder: Any, pagename: str, target: str, label: str) -> str:
    uri = builder.get_relative_uri(pagename, target)
    current = ' class="current"' if pagename == target else ""
    return f'<a href="{uri}"{current}>{html.escape(label)}</a>'


def _library_items(app: Sphinx, pagename: str, directory: str, present: list[str]) -> str:
    builder = app.builder
    nesting = _NESTING.get(directory, {})
    present_set = set(present)
    child_parent = {child: parent for parent, children in nesting.items() for child in children}
    out = ["<ul>"]
    for name in present:
        parent = child_parent.get(name)
        if parent and parent in present_set:
            continue
        target = f"library/{directory}/{name}"
        link = _library_link(builder, pagename, target, _page_title(app, target))
        children = [child for child in nesting.get(name, []) if child in present_set]
        if not children:
            out.append(f"<li>{link}</li>")
            continue
        out.append(f'<li class="has-children">{link}<ul>')
        for child in children:
            child_target = f"library/{directory}/{child}"
            child_link = _library_link(
                builder, pagename, child_target, _page_title(app, child_target)
            )
            out.append(f"<li>{child_link}</li>")
        out.append("</ul></li>")
    out.append("</ul>")
    return "".join(out)


_GUIDE_SECTIONS = [
    ("start", "Get started", ["getting-started", "thinking-in-edify"]),
    (
        "builder",
        "The builder",
        ["anchors", "characters", "quantifiers", "groups", "captures", "lookaround", "flags"],
    ),
    (
        "atoms",
        "Atoms",
        ["network", "numbers", "text", "encodings", "datetime", "web", "finance", "grouping"],
    ),
    (
        "beyond",
        "Beyond the chain",
        [
            "composing",
            "from-regex",
            "matching",
            "errors",
            "testing",
            "seeing",
            "serialization",
            "integrations",
        ],
    ),
    ("practice", "In practice", ["recipes", "performance", "debugging", "unicode"]),
]


def _page_title(app: Sphinx, docname: str) -> str:
    title = app.env.titles.get(docname)
    return title.astext() if title is not None else docname.rsplit("/", 1)[-1]


def _guide_nav(app: Sphinx, pagename: str) -> str:
    builder = app.builder
    docs = set(app.env.found_docs)
    parts = ['<nav class="lib-nav" aria-label="Guide navigation">']
    home = builder.get_relative_uri(pagename, "guide/index")
    home_cls = " current" if pagename == "guide/index" else ""
    parts.append(f'<a class="lib-nav-home{home_cls}" href="{home}">Guide</a>')
    for directory, title, pages in _GUIDE_SECTIONS:
        index_doc = f"guide/{directory}/index"
        present = [name for name in pages if f"guide/{directory}/{name}" in docs]
        if index_doc not in docs or not present:
            continue
        active = pagename.startswith(f"guide/{directory}/")
        section_cls = " open" if active else ""
        current_cls = " current" if pagename == index_doc else ""
        uri = builder.get_relative_uri(pagename, index_doc)
        parts.append(f'<div class="lib-nav-section{section_cls}">')
        parts.append(f'<a class="lib-nav-cat{current_cls}" href="{uri}">{html.escape(title)}</a>')
        parts.append("<ul>")
        for name in present:
            target = f"guide/{directory}/{name}"
            page_uri = builder.get_relative_uri(pagename, target)
            item_cls = ' class="current"' if pagename == target else ""
            label = html.escape(_page_title(app, target))
            parts.append(f'<li><a href="{page_uri}"{item_cls}>{label}</a></li>')
        parts.append("</ul>")
        parts.append("</div>")
    parts.append("</nav>")
    return "".join(parts)


def _library_nav(app: Sphinx, pagename: str) -> str:
    builder = app.builder
    docs = set(app.env.found_docs)
    current_dir = pagename.split("/")[1] if pagename.count("/") >= 2 else ""
    parts = ['<nav class="lib-nav" aria-label="Library navigation">']
    home = builder.get_relative_uri(pagename, "library/index")
    home_cls = " current" if pagename == "library/index" else ""
    parts.append(f'<a class="lib-nav-home{home_cls}" href="{home}">Library</a>')
    for _title, directory, names in _library_sections():
        present = [n for n in names if f"library/{directory}/{n}" in docs]
        index_doc = f"library/{directory}/index"
        if not present or index_doc not in docs:
            continue
        active = directory == current_dir
        cat_uri = builder.get_relative_uri(pagename, index_doc)
        cat_cls = " open" if active else ""
        cat_current = " current" if pagename == index_doc else ""
        parts.append(f'<div class="lib-nav-section{cat_cls}">')
        cat_label = html.escape(_page_title(app, index_doc))
        parts.append(f'<a class="lib-nav-cat{cat_current}" href="{cat_uri}">{cat_label}</a>')
        parts.append(_library_items(app, pagename, directory, present))
        parts.append("</div>")
    parts.append("</nav>")
    return "".join(parts)


def _select_template(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Any,
) -> str | None:
    if pagename == "index":
        return "home.html"
    if pagename.startswith("_modules/"):
        return "wide.html"
    if pagename == "library/index" or pagename.startswith("library/"):
        context["library_nav"] = _library_nav(app, pagename)
        return "library.html"
    if pagename == "guide/index" or pagename.startswith("guide/"):
        context["library_nav"] = _guide_nav(app, pagename)
        return "guide.html"
    if pagename.startswith("api/"):
        context["api_page_toc"] = _inner_toc(context.get("toc", ""))
        return "api.html"
    return _STANDALONE.get(pagename)


_QUALIFIER = re.compile(r'(<span class="pre">)(?:[A-Za-z_][\w.]*\.)(?=\w)')


def _inner_toc(rendered_toc: str) -> str:
    """Return the section list from ``toc``, dropping the wrapper that repeats the page title."""
    opening = rendered_toc.find("<ul>", rendered_toc.find("</a>"))
    closing = rendered_toc.rfind("</ul>", 0, rendered_toc.rfind("</ul>"))
    if opening == -1 or closing <= opening:
        return ""
    return _QUALIFIER.sub(r"\1", rendered_toc[opening : closing + len("</ul>")])


def setup(app: Sphinx) -> dict[str, object]:
    app.add_directive("edify-playground", EdifyPlayground)
    app.connect("html-page-context", _select_template)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
