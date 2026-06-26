"""Recursively transform a subexpression's elements when merging into a parent.

When ``.subexpression(other_builder)`` is invoked, every element from
``other_builder`` is rewritten before it lands in the parent:

* Numbered back-references shift by the parent's existing capture count.
* Numbered captures count toward an "added" counter so the parent can
  increment its own total.
* Named captures and named back-references get prefixed by the merge
  namespace (when one is supplied).
* ``StartOfInputElement`` / ``EndOfInputElement`` collapse to
  ``NoopElement`` when ``ignore_start_and_end`` is True; otherwise they
  raise if the parent already declared the corresponding anchor.

The transform returns the rewritten element plus the count of capture
groups it introduced (zero for non-capture elements).
"""

from __future__ import annotations

from dataclasses import dataclass

from edify.elements.types.base import BaseElement
from edify.elements.types.captures import (
    BackReferenceElement,
    CaptureElement,
    NamedBackReferenceElement,
    NamedCaptureElement,
)
from edify.elements.types.groups import (
    AnyOfElement,
    AssertAheadElement,
    AssertBehindElement,
    AssertNotAheadElement,
    AssertNotBehindElement,
    GroupElement,
    SubexpressionElement,
)
from edify.elements.types.leaves import EndOfInputElement, NoopElement, StartOfInputElement
from edify.elements.types.quantifiers import (
    AtLeastElement,
    BetweenElement,
    BetweenLazyElement,
    ExactlyElement,
    OneOrMoreElement,
    OneOrMoreLazyElement,
    OptionalElement,
    ZeroOrMoreElement,
    ZeroOrMoreLazyElement,
)
from edify.errors.anchors import EndInputAlreadyDefinedError, StartInputAlreadyDefinedError


@dataclass(frozen=True)
class MergeContext:
    """Configuration for a subexpression merge.

    Attributes:
        capture_index_offset: Added to every numbered back-reference in the merged elements.
        namespace: Prefix prepended to every named-capture and named-back-reference name.
        ignore_start_and_end: When True, anchor elements collapse to no-ops.
        parent_has_start: True when the parent builder already declared ``start_of_input``.
        parent_has_end: True when the parent builder already declared ``end_of_input``.
    """

    capture_index_offset: int
    namespace: str
    ignore_start_and_end: bool
    parent_has_start: bool
    parent_has_end: bool


@dataclass(frozen=True)
class MergeResult:
    """The transformed element plus the count of capture groups it introduced."""

    element: BaseElement
    captures_added: int


def merge_element(element: BaseElement, context: MergeContext) -> MergeResult:
    """Return the transformed element and the number of capture groups it added.

    Args:
        element: The element from the merged-in builder.
        context: The merge configuration controlling renames, offsets, and anchor handling.

    Returns:
        A :class:`MergeResult` containing the rewritten element and the count
        of numbered + named capture groups discovered inside it.
    """
    if isinstance(element, BackReferenceElement):
        return _merge_back_reference(element, context)
    if isinstance(element, NamedBackReferenceElement):
        return _merge_named_back_reference(element, context)
    if isinstance(element, NamedCaptureElement):
        return _merge_named_capture(element, context)
    if isinstance(element, CaptureElement):
        return _merge_capture(element, context)
    if isinstance(element, StartOfInputElement):
        return _merge_start_of_input(element, context)
    if isinstance(element, EndOfInputElement):
        return _merge_end_of_input(element, context)
    if isinstance(element, GroupElement):
        return _merge_container(element, context, GroupElement)
    if isinstance(element, AnyOfElement):
        return _merge_container(element, context, AnyOfElement)
    if isinstance(element, SubexpressionElement):
        return _merge_container(element, context, SubexpressionElement)
    if isinstance(element, AssertAheadElement):
        return _merge_container(element, context, AssertAheadElement)
    if isinstance(element, AssertNotAheadElement):
        return _merge_container(element, context, AssertNotAheadElement)
    if isinstance(element, AssertBehindElement):
        return _merge_container(element, context, AssertBehindElement)
    if isinstance(element, AssertNotBehindElement):
        return _merge_container(element, context, AssertNotBehindElement)
    if isinstance(element, OptionalElement):
        return _merge_quantifier(element, context, OptionalElement)
    if isinstance(element, ZeroOrMoreElement):
        return _merge_quantifier(element, context, ZeroOrMoreElement)
    if isinstance(element, ZeroOrMoreLazyElement):
        return _merge_quantifier(element, context, ZeroOrMoreLazyElement)
    if isinstance(element, OneOrMoreElement):
        return _merge_quantifier(element, context, OneOrMoreElement)
    if isinstance(element, OneOrMoreLazyElement):
        return _merge_quantifier(element, context, OneOrMoreLazyElement)
    if isinstance(element, ExactlyElement):
        return _merge_exactly(element, context)
    if isinstance(element, AtLeastElement):
        return _merge_at_least(element, context)
    if isinstance(element, BetweenElement):
        return _merge_between(element, context)
    if isinstance(element, BetweenLazyElement):
        return _merge_between_lazy(element, context)
    return MergeResult(element=element, captures_added=0)


def _merge_back_reference(element: BackReferenceElement, context: MergeContext) -> MergeResult:
    """Shift the back-reference index by the parent's existing capture count."""
    shifted_index = element.index + context.capture_index_offset
    new_element = BackReferenceElement(index=shifted_index)
    return MergeResult(element=new_element, captures_added=0)


def _merge_named_back_reference(
    element: NamedBackReferenceElement, context: MergeContext
) -> MergeResult:
    """Prefix the named back-reference name with the merge namespace."""
    new_name = _apply_namespace(element.name, context.namespace)
    new_element = NamedBackReferenceElement(name=new_name)
    return MergeResult(element=new_element, captures_added=0)


def _merge_named_capture(element: NamedCaptureElement, context: MergeContext) -> MergeResult:
    """Prefix the named capture name and recurse into its children."""
    new_name = _apply_namespace(element.name, context.namespace)
    merged_children, child_captures_added = _merge_children(element.children, context)
    new_element = NamedCaptureElement(name=new_name, children=merged_children)
    return MergeResult(element=new_element, captures_added=child_captures_added + 1)


def _merge_capture(element: CaptureElement, context: MergeContext) -> MergeResult:
    """Recurse into capture children and count this capture toward the added total."""
    merged_children, child_captures_added = _merge_children(element.children, context)
    new_element = CaptureElement(children=merged_children)
    return MergeResult(element=new_element, captures_added=child_captures_added + 1)


def _merge_start_of_input(element: StartOfInputElement, context: MergeContext) -> MergeResult:
    """Collapse to no-op when ignoring, else raise if the parent already has a start."""
    if context.ignore_start_and_end:
        return MergeResult(element=NoopElement(), captures_added=0)
    if context.parent_has_start:
        raise StartInputAlreadyDefinedError(in_subexpression=True)
    return MergeResult(element=element, captures_added=0)


def _merge_end_of_input(element: EndOfInputElement, context: MergeContext) -> MergeResult:
    """Collapse to no-op when ignoring, else raise if the parent already has an end."""
    if context.ignore_start_and_end:
        return MergeResult(element=NoopElement(), captures_added=0)
    if context.parent_has_end:
        raise EndInputAlreadyDefinedError(in_subexpression=True)
    return MergeResult(element=element, captures_added=0)


def _merge_container(element: BaseElement, context: MergeContext, container_class) -> MergeResult:
    """Recurse into a container element's children and re-wrap in the same class."""
    merged_children, child_captures_added = _merge_children(element.children, context)
    new_element = container_class(children=merged_children)
    return MergeResult(element=new_element, captures_added=child_captures_added)


def _merge_quantifier(element: BaseElement, context: MergeContext, quantifier_class) -> MergeResult:
    """Recurse into a no-parameter quantifier's child and re-wrap in the same class."""
    child_result = merge_element(element.child, context)
    new_element = quantifier_class(child=child_result.element)
    return MergeResult(element=new_element, captures_added=child_result.captures_added)


def _merge_exactly(element: ExactlyElement, context: MergeContext) -> MergeResult:
    """Recurse into an :class:`ExactlyElement`'s child."""
    child_result = merge_element(element.child, context)
    new_element = ExactlyElement(times=element.times, child=child_result.element)
    return MergeResult(element=new_element, captures_added=child_result.captures_added)


def _merge_at_least(element: AtLeastElement, context: MergeContext) -> MergeResult:
    """Recurse into an :class:`AtLeastElement`'s child."""
    child_result = merge_element(element.child, context)
    new_element = AtLeastElement(times=element.times, child=child_result.element)
    return MergeResult(element=new_element, captures_added=child_result.captures_added)


def _merge_between(element: BetweenElement, context: MergeContext) -> MergeResult:
    """Recurse into a :class:`BetweenElement`'s child."""
    child_result = merge_element(element.child, context)
    new_element = BetweenElement(
        lower=element.lower, upper=element.upper, child=child_result.element
    )
    return MergeResult(element=new_element, captures_added=child_result.captures_added)


def _merge_between_lazy(element: BetweenLazyElement, context: MergeContext) -> MergeResult:
    """Recurse into a :class:`BetweenLazyElement`'s child."""
    child_result = merge_element(element.child, context)
    new_element = BetweenLazyElement(
        lower=element.lower, upper=element.upper, child=child_result.element
    )
    return MergeResult(element=new_element, captures_added=child_result.captures_added)


def _merge_children(
    children: tuple[BaseElement, ...], context: MergeContext
) -> tuple[tuple[BaseElement, ...], int]:
    """Merge each child and return ``(merged_tuple, total_captures_added)``."""
    merged_list: list[BaseElement] = []
    total_captures_added = 0
    for child in children:
        result = merge_element(child, context)
        merged_list.append(result.element)
        total_captures_added += result.captures_added
    return tuple(merged_list), total_captures_added


def _apply_namespace(name: str, namespace: str) -> str:
    """Prefix ``name`` with ``namespace`` (returns ``name`` unchanged when namespace is empty)."""
    if namespace == "":
        return name
    return f"{namespace}{name}"
