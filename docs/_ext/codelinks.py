"""Link the symbol names inside highlighted Python blocks to their reference entries.

A construction listing is only half an answer while ``.start_of_input()`` is dead
text: the reader can see the chain but not follow it. This walks the highlighted
HTML after Pygments has run and wraps every name it can resolve in a link to the
entry that documents it.

Resolution is deliberately conservative, because a wrong link costs more than a
missing one. Builder methods, the pattern classes, factory functions, and constants
resolve everywhere -- they cannot mean anything else in a Python block. Atom and
library names resolve only inside a block that imports them, so an example variable
called ``year`` or ``label`` is never mistaken for the fragment of the same name.
"""

from __future__ import annotations

import re
from typing import Any

from sphinx.application import Sphinx

_BLOCK = re.compile(r'<div class="highlight"><pre>(.*?)</pre>', re.S)
_NAME = re.compile(r'<span class="n">([A-Za-z_][A-Za-z0-9_]*)</span>')
_ASSIGNED = re.compile(r'^(?:<span class="w"> </span>|\s)*<span class="o">=</span>')
_IMPORTED = re.compile(
    r'<span class="nn">edify\.(atoms|library)[\w.]*</span>.*?<span class="kn">import</span>'
    r"(?P<names>.*?)(?=\n)",
    re.S,
)
_IMPORTED_NAME = re.compile(r'<span class="n">([A-Za-z_][A-Za-z0-9_]*)</span>')

_ALWAYS = (
    "edify.RegexBuilder.",
    "edify.Pattern.",
    "edify.Regex.",
    "edify.result.Match.",
    "edify.",
)
_SCOPED = ("edify.atoms.", "edify.library.")


def _object_index(app: Sphinx) -> dict[str, dict[str, tuple[str, str]]]:
    """Return {"always": …, "scoped": …} mapping a bare name to its (docname, anchor)."""
    always: dict[str, tuple[str, str]] = {}
    scoped: dict[str, tuple[str, str]] = {}
    entries = app.env.domains["py"].objects
    for group, names in (("always", _ALWAYS), ("scoped", _SCOPED)):
        destination = always if group == "always" else scoped
        for owner in names:
            for fullname, entry in entries.items():
                if not fullname.startswith(owner):
                    continue
                if "." in fullname[len(owner) :]:
                    continue
                destination.setdefault(fullname.rsplit(".", 1)[-1], (entry.docname, entry.node_id))
    return {"always": always, "scoped": scoped}


_INDEX: dict[str, dict[str, tuple[str, str]]] = {}


def _locally_imported(block: str) -> set[str]:
    """Names the block itself pulls in from ``edify.atoms`` or ``edify.library``."""
    names: set[str] = set()
    for match in _IMPORTED.finditer(block):
        names.update(_IMPORTED_NAME.findall(match.group("names")))
    return names


def _link_block(app: Sphinx, pagename: str, block: str) -> str:
    scoped_here = _locally_imported(block)
    always = _INDEX["always"]
    scoped = _INDEX["scoped"]

    def replace(match: re.Match[str]) -> str:
        name = match.group(1)
        if _ASSIGNED.match(block[match.end() :]):
            return match.group(0)
        target = always.get(name)
        if target is None and name in scoped_here:
            target = scoped.get(name)
        if target is None:
            return match.group(0)
        docname, anchor = target
        uri = app.builder.get_relative_uri(pagename, docname)
        return f'<a class="code-ref" href="{uri}#{anchor}">{match.group(0)}</a>'

    return _NAME.sub(replace, block)


def _link_code(app: Sphinx, pagename: str, templatename: str, context: dict, doctree: Any) -> None:
    body = context.get("body")
    if not body or '<div class="highlight"><pre>' not in body:
        return
    if not _INDEX:
        _INDEX.update(_object_index(app))

    def replace(match: re.Match[str]) -> str:
        return match.group(0).replace(match.group(1), _link_block(app, pagename, match.group(1)), 1)

    context["body"] = _BLOCK.sub(replace, body)


def setup(app: Sphinx) -> dict[str, Any]:
    app.connect("html-page-context", _link_code, priority=800)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
