"""Tests for the :class:`MatcherMixin` proxy methods on both fluent surfaces."""

from edify import DIGIT, END, START, Pattern, RegexBuilder, exactly, one_or_more, range_of


def test_pattern_match_delegates_to_re_pattern_match():
    zip_code = START + exactly(5, DIGIT) + END
    hit = zip_code.match("10001")
    assert hit is not None
    assert hit.group() == "10001"


def test_pattern_match_returns_none_for_non_matching_input():
    zip_code = START + exactly(5, DIGIT) + END
    assert zip_code.match("1234") is None


def test_pattern_search_finds_a_substring_hit():
    lower = one_or_more(range_of("a", "z"))
    hit = lower.search("HELLO world")
    assert hit is not None
    assert hit.group() == "world"


def test_pattern_fullmatch_via_to_regex_requires_the_entire_string():
    zip_code = START + exactly(5, DIGIT) + END
    assert zip_code.to_regex().fullmatch("10001") is not None
    assert zip_code.to_regex().fullmatch("10001x") is None


def test_pattern_findall_returns_every_hit():
    lower = one_or_more(range_of("a", "z"))
    assert lower.findall("hi there") == ["hi", "there"]


def test_pattern_finditer_via_to_regex_yields_match_objects():
    lower = one_or_more(range_of("a", "z"))
    hits = list(lower.to_regex().finditer("foo bar"))
    assert [match.group() for match in hits] == ["foo", "bar"]


def test_pattern_sub_replaces_hits():
    lower = one_or_more(range_of("a", "z"))
    assert lower.sub("[X]", "hi and hello!") == "[X] [X] [X]!"


def test_pattern_subn_via_to_regex_returns_count_of_replacements():
    lower = one_or_more(range_of("a", "z"))
    result, count = lower.to_regex().subn("[X]", "hi hi hi")
    assert result == "[X] [X] [X]"
    assert count == 3


def test_pattern_split_via_to_regex_splits_on_matches():
    lower = one_or_more(range_of("a", "z"))
    assert lower.to_regex().split("one two three") == ["", " ", " ", ""]


def test_regex_builder_match_delegates_to_re_pattern_match():
    zip_code = RegexBuilder().start_of_input().exactly(5).digit().end_of_input()
    hit = zip_code.match("10001")
    assert hit is not None
    assert hit.group() == "10001"


def test_regex_builder_search_and_findall_work():
    lower = RegexBuilder().one_or_more().range("a", "z")
    assert lower.search("HELLO world") is not None
    assert lower.findall("foo bar baz") == ["foo", "bar", "baz"]


def test_pattern_and_builder_yield_identical_results_for_same_regex():
    from_pattern = (START + exactly(5, DIGIT) + END).match("10001")
    from_builder = RegexBuilder().start_of_input().exactly(5).digit().end_of_input().match("10001")
    assert from_pattern is not None
    assert from_builder is not None
    assert from_pattern.group() == from_builder.group()


def test_pattern_match_falls_back_when_only_pattern_class_used():
    fluent = Pattern().start_of_input().exactly(5).digit().end_of_input()
    assert fluent.match("10001") is not None


def test_test_returns_true_when_pattern_matches_anywhere():
    lower = one_or_more(range_of("a", "z"))
    assert lower.test("HELLO world") is True


def test_test_returns_false_when_pattern_does_not_match():
    lower = one_or_more(range_of("a", "z"))
    assert lower.test("12345") is False


def test_test_respects_anchors():
    zip_code = START + exactly(5, DIGIT) + END
    assert zip_code.test("10001") is True
    assert zip_code.test("foo 10001 bar") is False


def test_test_returns_a_bool_not_a_match_object():
    lower = one_or_more(range_of("a", "z"))
    assert isinstance(lower.test("hello"), bool)


def test_test_respects_the_pos_argument():
    lower = one_or_more(range_of("a", "z"))
    assert lower.test("!hello", pos=1) is True
    assert lower.test("!hello", pos=6) is False


def test_test_on_regex_builder_works():
    lower = RegexBuilder().one_or_more().range("a", "z")
    assert lower.test("hello") is True
    assert lower.test("12345") is False
