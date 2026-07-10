"""Tests for the ASCII railroad-diagram renderer in :mod:`edify.introspect.ascii`."""

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
from edify.introspect.ascii import (
    _looks_like_single_box,
    _pad_right,
    _pluralize,
    _widen,
    render_ascii,
)
from edify.introspect.types import Diagram


def _render(*elements) -> str:
    return render_ascii(tuple(elements))


def test_empty_pattern_renders_start_arrow_end():
    assert _render() == ("   +-------+   +-----+\n   | START |-->| END |\n   +-------+   +-----+")


def test_single_digit_pattern():
    output = _render(DigitElement())
    assert output == (
        "   +-------+   +-------+   +-----+\n"
        "   | START |-->| digit |-->| END |\n"
        "   +-------+   +-------+   +-----+"
    )


def test_one_or_more_digit_reads_as_plural_english():
    output = _render(OneOrMoreElement(child=DigitElement()))
    assert "one or more digits" in output
    assert "START" in output
    assert "END" in output


def test_exactly_four_digits_reads_as_count_plural():
    output = _render(ExactlyElement(times=4, child=DigitElement()))
    assert "4 digits" in output


def test_exactly_one_digit_stays_singular():
    output = _render(ExactlyElement(times=1, child=DigitElement()))
    assert "1 digit" in output
    assert "1 digits" not in output


def test_start_of_input_reads_as_text_starts_here():
    output = _render(StartOfInputElement())
    assert "text starts here" in output


def test_end_of_input_reads_as_text_ends_here():
    output = _render(EndOfInputElement())
    assert "text ends here" in output


def test_character_literal_strips_regex_escape_for_display():
    output = _render(CharElement(value="\\-"))
    assert '"-"' in output
    assert '"\\-"' not in output


def test_string_literal_renders_in_quotes():
    output = _render(StringElement(value="hello"))
    assert '"hello"' in output


def test_alternation_lays_out_as_fork_and_merge():
    output = _render(
        AnyOfElement(
            children=(
                StringElement(value="cat"),
                StringElement(value="dog"),
                StringElement(value="fish"),
            )
        )
    )
    lines = output.splitlines()
    assert any("+--->" in line for line in lines)
    assert any("----+" in line for line in lines)
    assert any('"cat"' in line for line in lines)
    assert any('"dog"' in line for line in lines)
    assert any('"fish"' in line for line in lines)


def test_alternation_widens_smaller_boxes_to_match_widest():
    output = _render(
        AnyOfElement(
            children=(
                StringElement(value="cat"),
                StringElement(value="fish"),
            )
        )
    )
    assert output.count("+--------+") == 4
    assert '| "cat"  |' in output
    assert '| "fish" |' in output


def test_alternation_with_single_branch_still_renders():
    output = _render(AnyOfElement(children=(StringElement(value="only"),)))
    assert '"only"' in output


def test_named_capture_places_caption_below_child():
    output = _render(
        NamedCaptureElement(
            name="year",
            children=(ExactlyElement(times=4, child=DigitElement()),),
        )
    )
    lines = output.splitlines()
    assert any('(saved as "year")' in line for line in lines)
    assert any("4 digits" in line for line in lines)


def test_unnamed_capture_places_captured_caption_below_child():
    output = _render(CaptureElement(children=(DigitElement(),)))
    assert "(captured)" in output


def test_group_places_grouped_caption_below_child():
    output = _render(GroupElement(children=(DigitElement(),)))
    assert "(grouped)" in output


def test_subexpression_flattens_into_the_sequence():
    output = _render(SubexpressionElement(children=(DigitElement(), DigitElement())))
    assert output.count("digit") == 2


def test_backreference_reads_as_match_same_text_as_group_n():
    output = _render(BackReferenceElement(index=1))
    assert "match same text as group 1" in output


def test_named_backreference_reads_as_match_same_text_as_name():
    output = _render(NamedBackReferenceElement(name="year"))
    assert 'match same text as "year"' in output


def test_assert_ahead_caption():
    output = _render(AssertAheadElement(children=(DigitElement(),)))
    assert "(must be followed by)" in output


def test_assert_not_ahead_caption():
    output = _render(AssertNotAheadElement(children=(DigitElement(),)))
    assert "(must NOT be followed by)" in output


def test_assert_behind_caption():
    output = _render(AssertBehindElement(children=(DigitElement(),)))
    assert "(must be preceded by)" in output


def test_assert_not_behind_caption():
    output = _render(AssertNotBehindElement(children=(DigitElement(),)))
    assert "(must NOT be preceded by)" in output


def test_range_element_reads_as_from_x_to_y():
    output = _render(RangeElement(start="a", end="z"))
    assert 'from "a" to "z"' in output


def test_any_of_chars_reads_as_any_of_value():
    output = _render(AnyOfCharsElement(value="abc"))
    assert 'any of "abc"' in output


def test_anything_but_chars_reads_as_except_value():
    output = _render(AnythingButCharsElement(value="abc"))
    assert 'except "abc"' in output


def test_anything_but_range_reads_as_outside_range():
    output = _render(AnythingButRangeElement(start="a", end="z"))
    assert 'outside "a"-"z"' in output


def test_anything_but_string_reads_as_except_string():
    output = _render(AnythingButStringElement(value="stop"))
    assert 'except the string "stop"' in output


def test_optional_digit_reads_as_optional_singular():
    output = _render(OptionalElement(child=DigitElement()))
    assert "optional digit" in output


def test_zero_or_more_digits_reads_as_plural():
    output = _render(ZeroOrMoreElement(child=DigitElement()))
    assert "zero or more digits" in output


def test_zero_or_more_lazy_marks_lazy():
    output = _render(ZeroOrMoreLazyElement(child=DigitElement()))
    assert "zero or more digits (lazy)" in output


def test_one_or_more_lazy_marks_lazy():
    output = _render(OneOrMoreLazyElement(child=DigitElement()))
    assert "one or more digits (lazy)" in output


def test_at_least_reads_as_at_least_n_plural():
    output = _render(AtLeastElement(times=3, child=DigitElement()))
    assert "at least 3 digits" in output


def test_at_most_reads_as_at_most_n_plural():
    output = _render(AtMostElement(times=2, child=DigitElement()))
    assert "at most 2 digits" in output


def test_between_reads_as_lower_to_upper_plural():
    output = _render(BetweenElement(lower=2, upper=5, child=DigitElement()))
    assert "2 to 5 digits" in output


def test_between_lazy_marks_lazy():
    output = _render(BetweenLazyElement(lower=2, upper=5, child=DigitElement()))
    assert "2 to 5 digits (lazy)" in output


def test_letter_labeled_letter():
    output = _render(LetterElement())
    assert "letter" in output


def test_uppercase_labeled_uppercase_letter():
    output = _render(UppercaseElement())
    assert "uppercase letter" in output


def test_lowercase_labeled_lowercase_letter():
    output = _render(LowercaseElement())
    assert "lowercase letter" in output


def test_alphanumeric_labeled_letter_or_digit():
    output = _render(AlphanumericElement())
    assert "letter or digit" in output


def test_any_char_labeled_any_character():
    output = _render(AnyCharElement())
    assert "any character" in output


def test_whitespace_labeled_whitespace():
    output = _render(WhitespaceCharElement())
    assert "| whitespace |" in output


def test_non_whitespace_labeled_non_whitespace():
    output = _render(NonWhitespaceCharElement())
    assert "non-whitespace" in output


def test_non_digit_labeled_non_digit_character():
    output = _render(NonDigitElement())
    assert "non-digit character" in output


def test_word_char_labeled_word_character():
    output = _render(WordElement())
    assert "word character" in output


def test_non_word_char_labeled_non_word_character():
    output = _render(NonWordElement())
    assert "non-word character" in output


def test_word_boundary_labeled_word_boundary():
    output = _render(WordBoundaryElement())
    assert "word boundary" in output


def test_non_word_boundary_labeled_non_word_boundary():
    output = _render(NonWordBoundaryElement())
    assert "non-word boundary" in output


def test_newline_labeled_newline():
    output = _render(NewLineElement())
    assert "| newline |" in output


def test_carriage_return_labeled():
    output = _render(CarriageReturnElement())
    assert "carriage return" in output


def test_tab_labeled_tab():
    output = _render(TabElement())
    assert "| tab |" in output


def test_null_byte_labeled():
    output = _render(NullByteElement())
    assert "null byte" in output


def test_noop_labeled_noop():
    output = _render(NoopElement())
    assert "no-op" in output


def test_alternation_with_no_children_shows_nothing_placeholder():
    output = _render(AnyOfElement(children=()))
    assert "nothing" in output


def test_regex_visualize_end_to_end_delegates_to_render_ascii():
    regex = RegexBuilder().digit().to_regex()
    output = regex.visualize()
    assert "| digit |" in output
    assert "| START |" in output
    assert "| END |" in output


def test_visualize_with_alternation_end_to_end():
    regex = RegexBuilder().any_of("cat", "dog", "fish").to_regex()
    output = regex.visualize()
    assert '"cat"' in output
    assert '"dog"' in output
    assert '"fish"' in output
    assert "+--->" in output


def test_visualize_named_capture_end_to_end():
    regex = RegexBuilder().named_capture("year").exactly(4).digit().end().to_regex()
    output = regex.visualize()
    assert '(saved as "year")' in output
    assert "4 digits" in output


def test_visualize_anchored_pattern_end_to_end():
    regex = RegexBuilder().start_of_input().one_or_more().digit().end_of_input().to_regex()
    output = regex.visualize()
    assert "text starts here" in output
    assert "text ends here" in output
    assert "one or more digits" in output


def test_singular_stays_singular_for_literal_labels():
    output = _render(ExactlyElement(times=3, child=StringElement(value="ab")))
    assert '3 "ab"' in output


def test_pluralize_default_adds_s():
    assert _pluralize("digit") == "digits"


def test_pluralize_adds_es_after_ch_ending():
    assert _pluralize("match") == "matches"


def test_pluralize_adds_es_after_sh_ending():
    assert _pluralize("fish") == "fishes"


def test_pluralize_adds_es_after_x_ending():
    assert _pluralize("box") == "boxes"


def test_pluralize_adds_es_after_s_ending():
    assert _pluralize("miss") == "misses"


def test_pluralize_adds_es_after_z_ending():
    assert _pluralize("buzz") == "buzzes"


def test_pluralize_converts_y_to_ies_after_consonant():
    assert _pluralize("cherry") == "cherries"


def test_pluralize_adds_s_after_y_when_preceded_by_vowel():
    assert _pluralize("boy") == "boys"


def test_pluralize_leaves_quoted_literal_string_untouched():
    assert _pluralize('"cat"') == '"cat"'


def test_optional_of_capture_falls_back_to_group_label():
    inner_capture = CaptureElement(children=(DigitElement(),))
    output = _render(OptionalElement(child=inner_capture))
    assert "optional group" in output


def test_quantifier_around_alternation_falls_back_to_group_label():
    inner_alt = AnyOfElement(children=(StringElement(value="a"), StringElement(value="b")))
    output = _render(ExactlyElement(times=2, child=inner_alt))
    assert "2 groups" in output


def test_unknown_element_type_renders_placeholder_label():
    class MysteryElement(DigitElement.__mro__[1]):
        pass

    output = _render(MysteryElement())
    assert "?MysteryElement" in output


def test_empty_group_shows_nothing_placeholder():
    output = _render(GroupElement(children=()))
    assert "nothing" in output


def test_nested_alternation_pads_wider_branch_with_spaces():
    outer = AnyOfElement(
        children=(
            AnyOfElement(
                children=(
                    StringElement(value="a"),
                    StringElement(value="b"),
                )
            ),
            StringElement(value="verylongword"),
        )
    )
    output = _render(outer)
    assert '"a"' in output
    assert '"b"' in output
    assert '"verylongword"' in output


def test_single_branch_alternation_looks_like_single_branch():
    output = _render(AnyOfElement(children=(StringElement(value="only-one"),)))
    assert '"only-one"' in output
    assert "+--->" in output


def test_looks_like_single_box_rejects_multi_row_diagram():
    multi = Diagram(rows=("+---+", "|abc|", "+---+", "extra"), entry_row=1, width=5)
    assert _looks_like_single_box(multi) is False


def test_looks_like_single_box_rejects_asymmetric_borders():
    asymmetric = Diagram(rows=("+---+", "| a |", "+xxx+"), entry_row=1, width=5)
    assert _looks_like_single_box(asymmetric) is False


def test_looks_like_single_box_rejects_non_box_borders():
    non_box = Diagram(rows=("     ", "| a |", "     "), entry_row=1, width=5)
    assert _looks_like_single_box(non_box) is False


def test_looks_like_single_box_rejects_middle_without_pipes():
    bad_middle = Diagram(rows=("+---+", "  a  ", "+---+"), entry_row=1, width=5)
    assert _looks_like_single_box(bad_middle) is False


def test_looks_like_single_box_rejects_border_with_non_dash_interior():
    striped = Diagram(rows=("+-x-+", "| a |", "+-x-+"), entry_row=1, width=5)
    assert _looks_like_single_box(striped) is False


def test_pad_right_returns_diagram_untouched_when_already_wide_enough():
    original = Diagram(rows=("abcde",), entry_row=0, width=5)
    assert _pad_right(original, 3) is original


def test_widen_returns_diagram_untouched_when_already_wide_enough():
    original = Diagram(rows=("abcde",), entry_row=0, width=5)
    assert _widen(original, 3) is original
