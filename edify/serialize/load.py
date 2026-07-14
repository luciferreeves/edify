"""Deserialize a canonical dict back into a :class:`Pattern`.

The load path validates the schema version, walks the ``pattern`` tree
rebuilding the element AST, and derives the auxiliary state fields
(``has_defined_start``, ``named_groups``, ``total_capture_groups``) from
the tree so the resulting :class:`Pattern` behaves exactly like one built
through the fluent chain.
"""

from __future__ import annotations

from dataclasses import fields
from typing import TYPE_CHECKING, Any

from edify.builder.types.flags import Flags
from edify.builder.types.frame import StackFrame
from edify.builder.types.state import BuilderState
from edify.elements.types.captures import CaptureElement, NamedCaptureElement
from edify.elements.types.leaves import EndOfInputElement, StartOfInputElement
from edify.elements.types.root import RootElement
from edify.errors.serialize import (
    IncompatibleSchemaVersionError,
    MissingSchemaKeyError,
    UnknownElementKindError,
)
from edify.serialize.kinds import class_for
from edify.serialize.version import SCHEMA_VERSION

if TYPE_CHECKING:
    from edify.elements.types.base import BaseElement
    from edify.pattern.composition import Pattern


def dict_to_element(tree: dict[str, Any]) -> BaseElement:
    """Return the AST element described by ``tree``."""
    kind = tree.get("kind")
    if kind is None:
        raise MissingSchemaKeyError("kind")
    try:
        element_class = class_for(kind)
    except KeyError as reason:
        raise UnknownElementKindError(kind) from reason
    field_specs = {spec.name: spec for spec in fields(element_class)}
    constructor_kwargs: dict[str, Any] = {}
    for name, raw_value in tree.items():
        if name == "kind":
            continue
        if name not in field_specs:
            continue
        constructor_kwargs[name] = _deserialize_field_value(raw_value)
    return element_class(**constructor_kwargs)


def _deserialize_field_value(value: Any) -> Any:
    if isinstance(value, list):
        return tuple(dict_to_element(item) for item in value)
    if isinstance(value, dict) and "kind" in value:
        return dict_to_element(value)
    return value


def dict_to_pattern(document: dict[str, Any]) -> Pattern:
    """Return the :class:`Pattern` described by ``document`` (canonical shape)."""
    from edify.pattern.composition import Pattern

    _require_schema_version(document)
    pattern_tree = document.get("pattern")
    if pattern_tree is None:
        raise MissingSchemaKeyError("pattern")
    root_element = dict_to_element(pattern_tree)
    root_children = tuple(root_element.children) if isinstance(root_element, RootElement) else ()
    flag_map = document.get("flags") or {}
    reconstructed_flags = _flags_from_dict(flag_map)
    named_groups = _collect_named_groups(root_children)
    total_captures = _count_capture_groups(root_children)
    has_start = any(isinstance(child, StartOfInputElement) for child in root_children)
    has_end = any(isinstance(child, EndOfInputElement) for child in root_children)
    root_frame = StackFrame(type_node=RootElement(), children=root_children)
    state = BuilderState(
        has_defined_start=has_start,
        has_defined_end=has_end,
        flags=reconstructed_flags,
        stack=(root_frame,),
        named_groups=named_groups,
        total_capture_groups=total_captures,
    )
    empty_pattern = Pattern()
    return empty_pattern._with_state(state)


def _require_schema_version(document: dict[str, Any]) -> None:
    if "edify" not in document:
        raise MissingSchemaKeyError("edify")
    seen_version = document["edify"]
    if seen_version != SCHEMA_VERSION:
        raise IncompatibleSchemaVersionError(seen_version, SCHEMA_VERSION)


def _flags_from_dict(flag_map: dict[str, Any]) -> Flags:
    known_flag_names = {spec.name for spec in fields(Flags)}
    kwargs = {name: bool(value) for name, value in flag_map.items() if name in known_flag_names}
    return Flags(**kwargs)


def _collect_named_groups(children: tuple[BaseElement, ...]) -> tuple[str, ...]:
    return tuple(
        element.name
        for element in _walk_elements(children)
        if isinstance(element, NamedCaptureElement)
    )


def _count_capture_groups(children: tuple[BaseElement, ...]) -> int:
    count = 0
    for element in _walk_elements(children):
        if isinstance(element, CaptureElement | NamedCaptureElement):
            count += 1
    return count


def _walk_elements(children: tuple[BaseElement, ...]):
    from edify.elements.types.base import BaseElement as _BaseElement

    for element in children:
        yield element
        for spec in fields(element):
            value = getattr(element, spec.name)
            if isinstance(value, tuple):
                yield from _walk_elements(value)
            elif isinstance(value, _BaseElement):
                yield from _walk_elements((value,))
