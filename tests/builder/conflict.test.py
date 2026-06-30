"""Tests for anchor conflicts when subexpressions merge with ``ignore_start_and_end=False``."""

import pytest

from edify import RegexBuilder
from edify.errors.anchors import EndInputAlreadyDefinedError, StartInputAlreadyDefinedError


def test_parent_with_start_merging_sub_with_start_raises():
    sub = RegexBuilder().start_of_input().digit()
    parent = RegexBuilder().start_of_input().digit()
    with pytest.raises(StartInputAlreadyDefinedError):
        parent.subexpression(sub, ignore_start_and_end=False)


def test_parent_with_end_merging_sub_with_end_raises():
    sub = RegexBuilder().digit().end_of_input()
    parent = RegexBuilder().digit().end_of_input()
    with pytest.raises(EndInputAlreadyDefinedError):
        parent.subexpression(sub, ignore_start_and_end=False)
