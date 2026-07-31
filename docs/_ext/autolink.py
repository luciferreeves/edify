"""Turn inline literals naming a public API symbol into links to its reference.

Writing ``.between(1, 4)`` or ``any_of`` in prose is far more natural than the
equivalent cross-reference role, but a plain literal is dead text. This extension
walks every literal node after parsing and, when its text names a builder method,
factory function, constant, or class, replaces it with a pending cross-reference
that Sphinx resolves exactly as if the author had written the role by hand.

Literals already inside a reference, a signature, or a code block are left alone.
"""

from __future__ import annotations

import re
from typing import Any

from docutils import nodes
from sphinx.addnodes import pending_xref
from sphinx.application import Sphinx

_CALL = re.compile(r"^\.?([A-Za-z_][A-Za-z0-9_]*)\s*(?:\(.*\))?$")


def _symbol_index() -> dict[str, tuple[str, str]]:
    """Map a bare symbol name to the (role, target) that documents it."""
    import inspect

    import edify

    index: dict[str, tuple[str, str]] = {}
    for name in dir(edify.RegexBuilder):
        if not name.startswith("_"):
            index[name] = ("meth", f"edify.RegexBuilder.{name}")
    for name in dir(edify):
        if name.startswith("_"):
            continue
        value = getattr(edify, name)
        if name in index:
            continue
        if inspect.isclass(value):
            index[name] = ("class", f"edify.{name}")
        elif inspect.isfunction(value):
            index[name] = ("func", f"edify.{name}")
    return index


_SYMBOLS: dict[str, tuple[str, str]] = {}


def _skip(node: nodes.Node) -> bool:
    parent = node.parent
    while parent is not None:
        if isinstance(parent, nodes.reference | pending_xref | nodes.literal_block):
            return True
        if parent.get("desc_signature") or parent.tagname in {"desc_signature", "desc_name"}:
            return True
        parent = parent.parent
    return False


def _link_literals(app: Sphinx, doctree: nodes.document) -> None:
    docname = app.env.docname
    if not _SYMBOLS:
        _SYMBOLS.update(_symbol_index())
    if docname.startswith(("api/", "_modules")):
        return
    for literal in list(doctree.findall(nodes.literal)):
        if _skip(literal):
            continue
        if "xref" in literal.get("classes", []):
            continue
        match = _CALL.match(literal.astext().strip())
        if match is None:
            continue
        entry = _SYMBOLS.get(match.group(1))
        if entry is None:
            continue
        role, target = entry
        reference = pending_xref(
            "",
            literal.deepcopy(),
            refdomain="py",
            reftype=role,
            reftarget=target,
            refexplicit=True,
            refwarn=False,
        )
        literal.replace_self(reference)


def setup(app: Sphinx) -> dict[str, Any]:
    app.connect("doctree-read", _link_literals, priority=900)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
