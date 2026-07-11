"""Tests for the re.VERBOSE-compatible renderer in :mod:`edify.introspect.verbose`."""

import re

from edify import RegexBuilder
from edify.elements.types.captures import (
    BackReferenceElement,
    CaptureElement,
    NamedBackReferenceElement,
    NamedCaptureElement,
)
from edify.elements.types.chars import (
    AnyOfCharsElement,
    AnythingButCharsElement,
    AnythingButRangeElement,
    AnythingButStringElement,
    CharElement,
    RangeElement,
    StringElement,
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
from edify.elements.types.leaves import (
    AlphanumericElement,
    AnyCharElement,
    CarriageReturnElement,
    DigitElement,
    EndOfInputElement,
    LetterElement,
    LowercaseElement,
    NewLineElement,
    NonDigitElement,
    NonWhitespaceCharElement,
    NonWordBoundaryElement,
    NonWordElement,
    NoopElement,
    NullByteElement,
    StartOfInputElement,
    TabElement,
    UppercaseElement,
    WhitespaceCharElement,
    WordBoundaryElement,
    WordElement,
)
from edify.elements.types.quantifiers import (
    AtLeastElement,
    AtMostElement,
    BetweenElement,
    BetweenLazyElement,
    ExactlyElement,
    OneOrMoreElement,
    OneOrMoreLazyElement,
    OptionalElement,
    ZeroOrMoreElement,
    ZeroOrMoreLazyElement,
)
from edify.introspect import verbose as verbose_module
from edify.introspect.verbose import verbose_elements


def _verbose(*elements) -> str:
    return verbose_elements(tuple(elements))


def _strip_pattern(output: str) -> str:
    fragments = []
    for line in output.splitlines():
        without_comment = line.split("#", 1)[0]
        code = without_comment.strip()
        if code:
            fragments.append(code)
    return "".join(fragments)


def test_empty_elements_produces_empty_string():
    assert _verbose() == ""


def test_single_digit_reads_as_backslash_d_with_comment():
    output = _verbose(DigitElement())
    assert output.startswith("\\d")
    assert "any digit (0-9)" in output


def test_start_of_input_reads_as_caret_with_comment():
    output = _verbose(StartOfInputElement())
    assert output.startswith("^")
    assert "start of input" in output


def test_end_of_input_reads_as_dollar_with_comment():
    output = _verbose(EndOfInputElement())
    assert output.startswith("$")
    assert "end of input" in output


def test_any_char_reads_as_dot_with_comment():
    output = _verbose(AnyCharElement())
    assert output.startswith(".")
    assert "any single character" in output


def test_whitespace_reads_as_backslash_s():
    output = _verbose(WhitespaceCharElement())
    assert output.startswith("\\s")


def test_non_whitespace_reads_as_backslash_capital_s():
    output = _verbose(NonWhitespaceCharElement())
    assert output.startswith("\\S")


def test_non_digit_reads_as_backslash_capital_d():
    output = _verbose(NonDigitElement())
    assert output.startswith("\\D")


def test_word_reads_as_backslash_w():
    output = _verbose(WordElement())
    assert output.startswith("\\w")


def test_non_word_reads_as_backslash_capital_w():
    output = _verbose(NonWordElement())
    assert output.startswith("\\W")


def test_word_boundary_reads_as_backslash_b():
    output = _verbose(WordBoundaryElement())
    assert output.startswith("\\b")


def test_non_word_boundary_reads_as_backslash_capital_b():
    output = _verbose(NonWordBoundaryElement())
    assert output.startswith("\\B")


def test_new_line_reads_as_backslash_n():
    output = _verbose(NewLineElement())
    assert output.startswith("\\n")


def test_carriage_return_reads_as_backslash_r():
    output = _verbose(CarriageReturnElement())
    assert output.startswith("\\r")


def test_tab_reads_as_backslash_t():
    output = _verbose(TabElement())
    assert output.startswith("\\t")


def test_null_byte_reads_as_backslash_zero():
    output = _verbose(NullByteElement())
    assert output.startswith("\\0")


def test_letter_reads_as_alpha_class():
    output = _verbose(LetterElement())
    assert output.startswith("[a-zA-Z]")


def test_uppercase_reads_as_uppercase_class():
    output = _verbose(UppercaseElement())
    assert output.startswith("[A-Z]")


def test_lowercase_reads_as_a_z_class():
    output = _verbose(LowercaseElement())
    assert output.startswith("[a-z]")


def test_alphanumeric_reads_as_alphanum_class():
    output = _verbose(AlphanumericElement())
    assert output.startswith("[a-zA-Z0-9]")


def test_noop_reads_as_no_op_comment_and_empty_pattern():
    output = _verbose(NoopElement())
    assert "no-op" in output
    assert _strip_pattern(output) == ""


def test_char_literal_shows_raw_value_and_literal_comment():
    output = _verbose(CharElement(value="a"))
    assert output.startswith("a")
    assert 'literal "a"' in output


def test_string_literal_shows_raw_value_and_literal_string_comment():
    output = _verbose(StringElement(value="hello"))
    assert output.startswith("hello")
    assert 'literal string "hello"' in output


def test_range_reads_as_bracketed_range_class():
    output = _verbose(RangeElement(start="a", end="z"))
    assert output.startswith("[a-z]")
    assert "range a-z" in output


def test_any_of_chars_reads_as_bracketed_class():
    output = _verbose(AnyOfCharsElement(value="abc"))
    assert output.startswith("[abc]")


def test_anything_but_chars_reads_as_negated_bracketed_class():
    output = _verbose(AnythingButCharsElement(value="abc"))
    assert output.startswith("[^abc]")


def test_anything_but_range_reads_as_negated_range_class():
    output = _verbose(AnythingButRangeElement(start="a", end="z"))
    assert output.startswith("[^a-z]")


def test_anything_but_string_produces_per_position_negation():
    output = _verbose(AnythingButStringElement(value="ab"))
    assert "per-position negation" in output


def test_optional_digit_reads_as_question_mark_with_comment():
    output = _verbose(OptionalElement(child=DigitElement()))
    assert output.startswith("\\d?")
    assert "optional (zero or one)" in output


def test_zero_or_more_digit_reads_as_star_greedy():
    output = _verbose(ZeroOrMoreElement(child=DigitElement()))
    assert output.startswith("\\d*")
    assert "zero or more (greedy)" in output


def test_zero_or_more_lazy_reads_as_star_lazy():
    output = _verbose(ZeroOrMoreLazyElement(child=DigitElement()))
    assert output.startswith("\\d*?")
    assert "zero or more (lazy)" in output


def test_one_or_more_digit_reads_as_plus_greedy():
    output = _verbose(OneOrMoreElement(child=DigitElement()))
    assert output.startswith("\\d+")
    assert "one or more (greedy)" in output


def test_one_or_more_lazy_reads_as_plus_lazy():
    output = _verbose(OneOrMoreLazyElement(child=DigitElement()))
    assert output.startswith("\\d+?")


def test_exactly_reads_as_curly_braces_with_count():
    output = _verbose(ExactlyElement(times=4, child=DigitElement()))
    assert output.startswith("\\d{4}")
    assert "exactly 4" in output


def test_at_least_reads_as_curly_braces_with_open_upper():
    output = _verbose(AtLeastElement(times=3, child=DigitElement()))
    assert output.startswith("\\d{3,}")
    assert "at least 3" in output


def test_at_most_reads_as_curly_braces_with_zero_lower():
    output = _verbose(AtMostElement(times=5, child=DigitElement()))
    assert output.startswith("\\d{0,5}")
    assert "at most 5" in output


def test_between_reads_as_curly_braces_with_lower_upper():
    output = _verbose(BetweenElement(lower=2, upper=5, child=DigitElement()))
    assert output.startswith("\\d{2,5}")
    assert "between 2 and 5 (greedy)" in output


def test_between_lazy_reads_as_curly_braces_with_question_mark():
    output = _verbose(BetweenLazyElement(lower=2, upper=5, child=DigitElement()))
    assert output.startswith("\\d{2,5}?")
    assert "between 2 and 5 (lazy)" in output


def test_quantifier_around_multi_char_string_wraps_child_in_non_capturing_group():
    output = _verbose(OneOrMoreElement(child=StringElement(value="ab")))
    assert output.startswith("(?:ab)+")


def test_quantifier_around_single_char_string_does_not_add_grouping():
    output = _verbose(OneOrMoreElement(child=StringElement(value="a")))
    assert output.startswith("a+")


def test_quantifier_around_group_uses_multi_line_wrap():
    inner = GroupElement(children=(DigitElement(), WordElement()))
    output = _verbose(OneOrMoreElement(child=inner))
    assert "begin group for one or more (greedy)" in output
    assert "end group; apply one or more (greedy)" in output


def test_non_capturing_group_reads_with_begin_and_end_comments():
    output = _verbose(GroupElement(children=(DigitElement(),)))
    assert "begin non-capturing group" in output
    assert "end non-capturing group" in output


def test_alternation_with_multiple_alternatives_lists_each_with_pipe():
    output = _verbose(
        AnyOfElement(
            children=(
                StringElement(value="cat"),
                StringElement(value="dog"),
                StringElement(value="fish"),
            )
        )
    )
    assert "begin alternation" in output
    assert "end alternation" in output
    assert "alternative 1" in output
    assert "alternative 2" in output
    assert "alternative 3" in output
    assert output.count(" or") >= 2


def test_alternation_with_no_children_reads_as_empty_alternation():
    output = _verbose(AnyOfElement(children=()))
    assert "empty alternation" in output
    assert "(?:)" in output


def test_subexpression_inlines_its_children_without_extra_scoping():
    output = _verbose(SubexpressionElement(children=(DigitElement(), CharElement(value="-"))))
    assert "begin non-capturing group" not in output
    lines = [line for line in output.splitlines() if line.strip()]
    assert len(lines) == 2


def test_capture_reads_with_begin_captured_group_comment():
    output = _verbose(CaptureElement(children=(DigitElement(),)))
    assert "begin captured group" in output
    assert "end captured group" in output


def test_named_capture_includes_the_name_in_both_comments():
    output = _verbose(NamedCaptureElement(name="year", children=(DigitElement(),)))
    assert 'begin group named "year"' in output
    assert 'end group named "year"' in output
    assert "(?P<year>" in output


def test_backreference_reads_as_backslash_index_with_comment():
    output = _verbose(BackReferenceElement(index=1))
    assert output.startswith("\\1")
    assert "back-reference to group 1" in output


def test_named_backreference_reads_as_named_backref_syntax():
    output = _verbose(NamedBackReferenceElement(name="year"))
    assert "(?P=year)" in output
    assert 'back-reference to group "year"' in output


def test_assert_ahead_reads_as_positive_lookahead():
    output = _verbose(AssertAheadElement(children=(DigitElement(),)))
    assert "begin positive lookahead" in output
    assert "(?=" in output


def test_assert_not_ahead_reads_as_negative_lookahead():
    output = _verbose(AssertNotAheadElement(children=(DigitElement(),)))
    assert "begin negative lookahead" in output
    assert "(?!" in output


def test_assert_behind_reads_as_positive_lookbehind():
    output = _verbose(AssertBehindElement(children=(DigitElement(),)))
    assert "begin positive lookbehind" in output
    assert "(?<=" in output


def test_assert_not_behind_reads_as_negative_lookbehind():
    output = _verbose(AssertNotBehindElement(children=(DigitElement(),)))
    assert "begin negative lookbehind" in output
    assert "(?<!" in output


def test_unrecognized_element_falls_back_to_render_element_with_marker(monkeypatch):
    class MysteryElement(DigitElement.__mro__[1]):
        pass

    monkeypatch.setattr(verbose_module, "render_element", lambda element: "?mystery")
    mystery = MysteryElement()
    output = _verbose(mystery)
    assert "unrecognized (MysteryElement)" in output
    assert "?mystery" in output


def test_output_is_a_re_verbose_compatible_pattern_that_compiles():
    output = _verbose(
        StartOfInputElement(),
        OneOrMoreElement(child=DigitElement()),
        EndOfInputElement(),
    )
    compiled = re.compile(output, flags=re.VERBOSE)
    assert compiled.match("42") is not None
    assert compiled.match("abc") is None


def test_output_compiles_and_matches_for_alternation_pattern():
    output = _verbose(
        AnyOfElement(
            children=(
                StringElement(value="cat"),
                StringElement(value="dog"),
                StringElement(value="fish"),
            )
        )
    )
    compiled = re.compile(output, flags=re.VERBOSE)
    for word in ("cat", "dog", "fish"):
        assert compiled.match(word) is not None
    assert compiled.match("bird") is None


def test_alignment_uses_common_comment_column_across_lines():
    output = _verbose(DigitElement(), CharElement(value="-"), DigitElement())
    hash_columns = [line.index("#") for line in output.splitlines() if "#" in line]
    assert len(set(hash_columns)) == 1


def test_line_with_long_fragment_still_leaves_two_space_gap_before_comment():
    output = _verbose(StringElement(value="a" * 30))
    assert "  # " in output


def test_regex_to_verbose_string_end_to_end_via_builder():
    output = RegexBuilder().digit().to_regex().to_verbose_string()
    assert output.startswith("\\d")


def test_regex_verbose_output_is_accepted_by_re_verbose_mode():
    output = RegexBuilder().string("hello").to_regex().to_verbose_string()
    compiled = re.compile(output, flags=re.VERBOSE)
    assert compiled.match("hello") is not None
