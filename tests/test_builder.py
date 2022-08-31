import re

from edify.builder import ANY
from edify.builder import DIGIT
from edify.builder import WORD
from edify.builder import AtLeast
from edify.builder import AtMost
from edify.builder import Escaped
from edify.builder import Exact
from edify.builder import OneOrMore
from edify.builder import Optional
from edify.builder import Range
from edify.builder import RegexBuilder
from edify.builder import ZeroOrMore


def catch_exception(subroutine):
    try:
        subroutine()
    except Exception as e:
        return e.__class__


def test_invalid_section_error():
    assert catch_exception(lambda: RegexBuilder().add(1)) is ValueError


def test_optional():
    regex = (
        RegexBuilder()
        .add(Optional(ANY))
        .build()
    )
    assert re.match(regex, "hello") is not None
    assert re.match(regex, "") is not None


def test_zero_or_more():
    regex = (
        RegexBuilder()
        .add(ZeroOrMore(ANY))
        .build()
    )
    assert re.match(regex, "hello") is not None
    assert re.match(regex, "") is not None


def test_one_or_more():
    regex = (
        RegexBuilder()
        .add(OneOrMore(ANY))
        .build()
    )
    assert re.match(regex, "hello") is not None
    assert re.match(regex, "") is None


def test_exact():
    regex = (
        RegexBuilder()
        .add(Exact(WORD, 2))
        .build()
    )
    assert re.match(regex, "hello") is not None
    assert re.match(regex, "hello world") is not None
    assert re.match(regex, "hello world hello") is not None


def test_range():
    regex = (
        RegexBuilder()
        .add(Range(DIGIT, 1, 2))
        .build()
    )
    assert re.match(regex, "1") is not None
    assert re.match(regex, "2") is not None


def test_at_least():
    regex = (
        RegexBuilder()
        .add(AtLeast(ANY, 2))
        .build()
    )
    assert re.match(regex, "hello") is not None
    assert re.match(regex, "hello world") is not None
    assert re.match(regex, "hello world hello") is not None


def test_at_most():
    regex = (
        RegexBuilder()
        .add(AtMost(ANY, 2))
        .build()
    )
    assert re.match(regex, "hello") is not None
    assert re.match(regex, "hello world") is not None
    assert re.match(regex, "hello world hello") is not None


def test_escaped():
    regex = (
        RegexBuilder()
        .add(Escaped('.'))
        .build()
    )
    assert re.match(regex, ".") is not None
    assert re.match(regex, "..") is not None
    assert re.match(regex, "...") is not None


def test_escaped_with_quantifier():
    regex = (
        RegexBuilder()
        .add(Escaped('.'))
        .add(AtLeast(ANY, 2))
        .build()
    )
    assert re.match(regex, "..") is None
    assert re.match(regex, "...") is not None
    assert re.match(regex, "....") is not None


def test_escaped_with_quantifier_and_optional():
    regex = (
        RegexBuilder()
        .add(Escaped('.'))
        .add(Optional(ANY))
        .add(AtLeast(ANY, 2))
        .build()
    )
    assert re.match(regex, "..") is None
    assert re.match(regex, "...") is not None
    assert re.match(regex, "....") is not None
    assert re.match(regex, ".....") is not None


def test_email_using_builder():
    regex = (
        RegexBuilder()
        .add(OneOrMore(ANY))
        .add(Escaped('@'))
        .add(OneOrMore(ANY))
        .add(Escaped('.'))
        .add(OneOrMore(ANY))
        .build()
    )
    assert re.match(regex, "hello@example.com") is not None
    assert re.match(regex, "hello@example") is None
