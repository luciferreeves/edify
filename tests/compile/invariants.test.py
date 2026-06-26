"""Tests for the compile-path invariant raises that public-builder use never triggers.

These exercise defensive branches that fire only when an AST is constructed
outside the builder (so the type system can't catch it). They guarantee
the typed exception is raised instead of a silent miscompilation.
"""

import pytest

from edify.compile.dispatch import render_element
from edify.compile.fuse import _fragment_for
from edify.elements.types.base import BaseElement
from edify.elements.types.leaves import DigitElement
from edify.errors.internal import NonFusableElementError, UnknownElementTypeError


class _StrayElement(BaseElement):
    """A BaseElement subclass not in the ``Element`` union — used only here."""


def test_render_element_unknown_type_raises():
    stray = _StrayElement()
    with pytest.raises(UnknownElementTypeError, match="_StrayElement"):
        render_element(stray)


def test_fragment_for_non_fusable_raises():
    non_fusable = DigitElement()
    with pytest.raises(NonFusableElementError, match="DigitElement"):
        _fragment_for(non_fusable)
