"""Tests for the plain-English explanation renderer in :mod:`edify.introspect.explain`."""

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
from edify.introspect.explain import (
    _describe_inline,
    _describe_inline_children,
    _describe_optional_inner,
    _describe_plural,
    _example_for,
    _pick_character_not_in,
    _pick_character_outside_range,
    _wrap_step,
    explain_elements,
)


def _explain(*elements) -> str:
    return explain_elements(tuple(elements))


def _accepted_examples(output: str) -> list[str]:
    if "Text this pattern accepts:" not in output:
        return []
    accept_block = output.split("Text this pattern accepts:")[1]
    stripped_block = accept_block.strip()
    lines = stripped_block.splitlines()
    return [line.strip() for line in lines if line.strip()]


def test_empty_elements_produces_empty_string_notice():
    assert _explain() == "This pattern is empty and matches an empty string."


def test_single_digit_reads_as_must_contain_one_digit():
    output = _explain(DigitElement())
    assert output.startswith("- The text must contain one digit (0-9).")
    assert "Text this pattern accepts:" in output


def test_start_of_input_switches_lead_in_to_must_start_with():
    output = _explain(StartOfInputElement(), DigitElement())
    assert "The text must start with" in output


def test_trailing_end_of_input_alone_is_absorbed_silently():
    output = _explain(DigitElement(), EndOfInputElement())
    assert "The text must contain one digit" in output
    assert "very end" not in output


def test_trailing_assert_ahead_then_end_becomes_must_end_at_line():
    output = _explain(
        DigitElement(),
        AssertAheadElement(children=(CharElement(value="/"),)),
        EndOfInputElement(),
    )
    assert 'The text must end at "/".' in output


def test_second_element_uses_then_the_text_must_have():
    output = _explain(DigitElement(), CharElement(value="-"))
    assert "Then the text must have" in output


def test_optional_element_gets_dedicated_optional_prefix():
    output = _explain(OptionalElement(child=DigitElement()))
    assert "Optional:" in output


def test_zero_or_more_reads_as_zero_or_more_phrase():
    output = _explain(ZeroOrMoreElement(child=DigitElement()))
    assert "zero or more digits" in output


def test_zero_or_more_lazy_reads_as_as_few_as_possible():
    output = _explain(ZeroOrMoreLazyElement(child=DigitElement()))
    assert "as few as possible" in output


def test_one_or_more_reads_as_one_or_more_phrase():
    output = _explain(OneOrMoreElement(child=DigitElement()))
    assert "one or more digits" in output


def test_one_or_more_lazy_reads_as_as_few_as_possible():
    output = _explain(OneOrMoreLazyElement(child=DigitElement()))
    assert "as few as possible" in output


def test_exactly_reads_as_exactly_n_phrase():
    output = _explain(ExactlyElement(times=4, child=DigitElement()))
    assert "exactly 4 digits" in output


def test_at_least_reads_as_at_least_n_phrase():
    output = _explain(AtLeastElement(times=3, child=DigitElement()))
    assert "at least 3 digits" in output


def test_at_most_reads_as_at_most_n_phrase():
    output = _explain(AtMostElement(times=5, child=DigitElement()))
    assert "at most 5 digits" in output


def test_between_reads_as_between_lower_and_upper_phrase():
    output = _explain(BetweenElement(lower=2, upper=5, child=DigitElement()))
    assert "between 2 and 5 digits" in output


def test_between_lazy_reads_as_as_few_as_possible():
    output = _explain(BetweenLazyElement(lower=2, upper=5, child=DigitElement()))
    assert "as few as possible" in output


def test_word_boundary_gets_a_dedicated_bullet():
    output = _explain(WordBoundaryElement())
    assert "word boundary" in output


def test_non_word_boundary_gets_a_dedicated_bullet():
    output = _explain(NonWordBoundaryElement())
    assert "must NOT fall on a word boundary" in output


def test_capture_step_describes_children_inline():
    output = _explain(CaptureElement(children=(DigitElement(),)))
    assert "one digit" in output


def test_named_capture_step_describes_children_inline():
    output = _explain(
        NamedCaptureElement(name="year", children=(DigitElement(),))
    )
    assert "one digit" in output


def test_backreference_step_names_the_group_index():
    output = _explain(BackReferenceElement(index=2))
    assert "group #2" in output


def test_named_backreference_step_names_the_group_label():
    output = _explain(NamedBackReferenceElement(name="year"))
    assert 'group labeled "year"' in output


def test_assert_ahead_reads_as_must_be_followed_by():
    output = _explain(
        DigitElement(), AssertAheadElement(children=(CharElement(value="/"),))
    )
    assert "must be followed by" in output


def test_assert_not_ahead_reads_as_must_not_be_followed_by():
    output = _explain(
        DigitElement(),
        AssertNotAheadElement(children=(CharElement(value="/"),)),
    )
    assert "must NOT be followed by" in output


def test_assert_behind_reads_as_just_before_this_point():
    output = _explain(
        DigitElement(), AssertBehindElement(children=(CharElement(value="/"),))
    )
    assert "Just before this point" in output


def test_assert_not_behind_reads_as_just_before_must_not_have_appeared():
    output = _explain(
        DigitElement(),
        AssertNotBehindElement(children=(CharElement(value="/"),)),
    )
    assert "must NOT have appeared" in output


def test_group_step_describes_children_inline():
    output = _explain(GroupElement(children=(DigitElement(),)))
    assert "one digit" in output


def test_alternation_uses_either_or_for_two_alternatives():
    output = _explain(
        AnyOfElement(
            children=(StringElement(value="cat"), StringElement(value="dog"))
        )
    )
    assert 'either "cat" or "dog"' in output


def test_alternation_uses_either_a_b_or_c_for_three_alternatives():
    output = _explain(
        AnyOfElement(
            children=(
                StringElement(value="cat"),
                StringElement(value="dog"),
                StringElement(value="fish"),
            )
        )
    )
    assert 'either "cat", "dog", or "fish"' in output


def test_alternation_with_single_child_falls_through_to_single_phrase():
    output = _explain(AnyOfElement(children=(StringElement(value="only"),)))
    assert '"only"' in output


def test_alternation_with_no_children_reads_as_nothing():
    output = _explain(AnyOfElement(children=()))
    assert "nothing" in output


def test_examples_section_lists_up_to_three_accepted_strings():
    output = _explain(DigitElement())
    strings = _accepted_examples(output)
    assert 1 <= len(strings) <= 3


def test_examples_are_unique_across_the_three_seeds():
    output = _explain(DigitElement())
    strings = _accepted_examples(output)
    assert len(set(strings)) == len(strings)


def test_examples_section_omitted_when_only_empty_strings_are_generated():
    output = _explain(StartOfInputElement(), EndOfInputElement())
    assert "Text this pattern accepts:" not in output


def test_subexpression_is_flattened_into_the_step_list():
    output = _explain(
        SubexpressionElement(children=(DigitElement(), CharElement(value="-")))
    )
    assert output.count("- ") >= 2


def test_char_element_reads_as_quoted_literal():
    output = _explain(CharElement(value="\\-"))
    assert '"-"' in output


def test_string_element_reads_as_quoted_literal():
    output = _explain(StringElement(value="hi"))
    assert '"hi"' in output


def test_range_element_describes_from_start_to_end():
    output = _explain(RangeElement(start="a", end="z"))
    assert 'from "a" through "z"' in output


def test_any_of_chars_describes_from_the_set():
    output = _explain(AnyOfCharsElement(value="abc"))
    assert 'from the set "abc"' in output


def test_anything_but_chars_describes_not_from_the_set():
    output = _explain(AnythingButCharsElement(value="abc"))
    assert 'NOT from the set "abc"' in output


def test_anything_but_range_describes_outside_range():
    output = _explain(AnythingButRangeElement(start="a", end="z"))
    assert 'outside "a" through "z"' in output


def test_anything_but_string_describes_position_for_position_mismatch():
    output = _explain(AnythingButStringElement(value="stop"))
    assert "position-for-position" in output


def test_any_char_reads_as_any_single_character():
    output = _explain(AnyCharElement())
    assert "any single character" in output


def test_whitespace_char_mentions_space_tab_newline():
    output = _explain(WhitespaceCharElement())
    assert "whitespace character" in output


def test_non_whitespace_char_reads_as_non_whitespace():
    output = _explain(NonWhitespaceCharElement())
    assert "non-whitespace character" in output


def test_non_digit_char_reads_as_non_digit_character():
    output = _explain(NonDigitElement())
    assert "non-digit character" in output


def test_word_element_reads_as_letter_digit_or_underscore():
    output = _explain(WordElement())
    assert "one letter, digit, or underscore" in output


def test_non_word_element_reads_as_not_letter_digit_or_underscore():
    output = _explain(NonWordElement())
    assert "not a letter, digit, or underscore" in output


def test_new_line_element_labeled_as_line_feed():
    output = _explain(NewLineElement())
    assert "line-feed character" in output


def test_carriage_return_element_labeled_as_carriage_return():
    output = _explain(CarriageReturnElement())
    assert "carriage-return character" in output


def test_tab_element_labeled_as_tab_character():
    output = _explain(TabElement())
    assert "tab character" in output


def test_null_byte_element_labeled_as_null_byte():
    output = _explain(NullByteElement())
    assert "null byte" in output


def test_letter_element_labeled_a_to_z_case_insensitive():
    output = _explain(LetterElement())
    assert "one letter" in output


def test_uppercase_element_labeled_uppercase_range():
    output = _explain(UppercaseElement())
    assert "uppercase letter" in output


def test_lowercase_element_labeled_lowercase_range():
    output = _explain(LowercaseElement())
    assert "lowercase letter" in output


def test_alphanumeric_element_labeled_letter_or_digit():
    output = _explain(AlphanumericElement())
    assert "letter or digit" in output


def test_noop_element_labeled_nothing_inline():
    output = _explain(GroupElement(children=(NoopElement(),)))
    assert "nothing" in output


def test_regex_explain_end_to_end_via_builder():
    output = RegexBuilder().digit().to_regex().explain()
    assert "one digit" in output


def test_examples_use_digit_rotation_for_a_pure_digit_pattern():
    output = _explain(DigitElement())
    strings = _accepted_examples(output)
    assert all(text.isdigit() for text in strings)


def test_examples_for_alternation_pick_a_different_branch_per_seed():
    output = _explain(
        AnyOfElement(
            children=(
                StringElement(value="cat"),
                StringElement(value="dog"),
                StringElement(value="fish"),
            )
        )
    )
    strings = set(_accepted_examples(output))
    assert strings == {"cat", "dog", "fish"}


def test_examples_for_optional_include_both_present_and_absent_forms():
    output = _explain(
        DigitElement(), OptionalElement(child=CharElement(value="x")), DigitElement()
    )
    strings = _accepted_examples(output)
    assert any("x" in text for text in strings)


def test_examples_for_exactly_produce_that_length_string():
    output = _explain(ExactlyElement(times=4, child=DigitElement()))
    strings = _accepted_examples(output)
    assert all(len(text) == 4 for text in strings)


def test_examples_for_at_least_produce_more_than_lower_bound_length():
    output = _explain(AtLeastElement(times=2, child=DigitElement()))
    strings = _accepted_examples(output)
    assert all(len(text) >= 2 for text in strings)


def test_examples_for_at_most_produce_bounded_length():
    output = _explain(AtMostElement(times=3, child=DigitElement()))
    strings = _accepted_examples(output)
    assert all(1 <= len(text) <= 3 for text in strings)


def test_examples_for_between_stay_within_range():
    output = _explain(BetweenElement(lower=2, upper=4, child=DigitElement()))
    strings = _accepted_examples(output)
    assert all(2 <= len(text) <= 4 for text in strings)


def test_examples_for_between_lazy_stay_within_range():
    output = _explain(BetweenLazyElement(lower=2, upper=4, child=DigitElement()))
    strings = _accepted_examples(output)
    assert all(2 <= len(text) <= 4 for text in strings)


def test_examples_for_backreference_use_a_placeholder():
    output = _explain(
        CaptureElement(children=(DigitElement(),)),
        BackReferenceElement(index=1),
    )
    strings = _accepted_examples(output)
    assert all("a" in text for text in strings)


def test_examples_for_named_backreference_use_a_placeholder():
    output = _explain(
        NamedCaptureElement(name="a", children=(DigitElement(),)),
        NamedBackReferenceElement(name="a"),
    )
    strings = _accepted_examples(output)
    assert all("a" in text for text in strings)


def test_examples_for_anything_but_chars_pick_a_char_not_in_set():
    output = _explain(AnythingButCharsElement(value="abc"))
    strings = _accepted_examples(output)
    for text in strings:
        for character in text:
            assert character not in "abc"


def test_examples_for_anything_but_range_pick_a_char_outside_range():
    output = _explain(AnythingButRangeElement(start="a", end="z"))
    strings = _accepted_examples(output)
    for text in strings:
        for character in text:
            assert not ("a" <= character <= "z")


def test_examples_for_anything_but_string_have_matching_length():
    output = _explain(AnythingButStringElement(value="stop"))
    strings = _accepted_examples(output)
    assert all(len(text) == 4 for text in strings)


def test_examples_for_anything_but_string_empty_produces_empty_seed():
    output = _explain(AnythingButStringElement(value=""))
    assert "Text this pattern accepts:" not in output


def test_examples_for_any_of_chars_empty_uses_default_letter():
    output = _explain(AnyOfCharsElement(value=""))
    strings = _accepted_examples(output)
    assert all(text == "a" for text in strings)


def test_examples_for_negative_lookaround_contribute_nothing():
    output = _explain(
        DigitElement(),
        AssertNotAheadElement(children=(CharElement(value="/"),)),
    )
    strings = _accepted_examples(output)
    assert all(text.isdigit() for text in strings)


def test_pick_character_not_in_uses_bang_when_set_exhausts_alphanumerics():
    everything = "abcdefghijklmnopqrstuvwxyz0123456789"
    assert _pick_character_not_in(everything) == "!"


def test_pick_character_outside_range_uses_bang_when_range_covers_alphanumerics():
    assert _pick_character_outside_range("0", "z") == "!"


def test_step_wrap_returns_empty_prefix_for_empty_description():
    wrapped = _wrap_step(1, "")
    assert wrapped.strip() == "1."


def test_step_wrap_breaks_long_descriptions_across_continuation_lines():
    long_description = " ".join(["word"] * 40)
    wrapped = _wrap_step(1, long_description)
    assert "\n" in wrapped


def test_optional_inner_wraps_char_literal():
    assert _describe_optional_inner(CharElement(value="\\-")) == '"-"'


def test_optional_inner_wraps_string_literal():
    assert _describe_optional_inner(StringElement(value="hi")) == '"hi"'


def test_optional_inner_delegates_to_inline_for_leaf_elements():
    assert "one digit" in _describe_optional_inner(DigitElement())


def test_describe_inline_falls_back_to_class_name_for_unknown_type():
    class MysteryElement(DigitElement.__mro__[1]):
        pass

    mystery = MysteryElement()
    description = _describe_inline(mystery)
    assert description == "MysteryElement"


def test_describe_plural_falls_back_to_of_inline_for_unknown_type():
    class MysteryElement(DigitElement.__mro__[1]):
        pass

    mystery = MysteryElement()
    plural = _describe_plural(mystery)
    assert plural.startswith("of ")


def test_step_wrapper_directly_wraps_first_line_at_width_boundary():
    words = " ".join(["w"] * 100)
    wrapped = _wrap_step(1, words)
    for line in wrapped.splitlines():
        stripped_line = line.strip()
        assert len(line) <= 76 or stripped_line.startswith("w")


def _plural(element) -> str:
    return _describe_plural(element)


def _inline(element) -> str:
    return _describe_inline(element)


def test_plural_any_char_reads_as_generic_characters():
    assert _plural(AnyCharElement()) == "characters (any character)"


def test_plural_whitespace_reads_as_whitespace_characters():
    assert "whitespace characters" in _plural(WhitespaceCharElement())


def test_plural_non_whitespace_reads_as_non_whitespace_characters():
    assert _plural(NonWhitespaceCharElement()) == "non-whitespace characters"


def test_plural_non_digit_reads_as_non_digit_characters():
    assert _plural(NonDigitElement()) == "non-digit characters"


def test_plural_word_reads_as_letters_digits_underscores():
    assert _plural(WordElement()) == "letters, digits, or underscores"


def test_plural_non_word_reads_as_not_letters_digits_or_underscores():
    assert "not letters, digits, or underscores" in _plural(NonWordElement())


def test_plural_new_line_reads_as_line_feed_characters():
    assert "line-feed characters" in _plural(NewLineElement())


def test_plural_carriage_return_reads_as_carriage_return_characters():
    assert "carriage-return characters" in _plural(CarriageReturnElement())


def test_plural_tab_reads_as_tab_characters():
    assert "tab characters" in _plural(TabElement())


def test_plural_null_byte_reads_as_null_bytes():
    assert "null bytes" in _plural(NullByteElement())


def test_plural_letter_reads_as_letters_a_to_z():
    assert _plural(LetterElement()) == "letters (a-z or A-Z)"


def test_plural_uppercase_reads_as_uppercase_letters():
    assert "uppercase letters" in _plural(UppercaseElement())


def test_plural_lowercase_reads_as_lowercase_letters():
    assert "lowercase letters" in _plural(LowercaseElement())


def test_plural_alphanumeric_reads_as_letters_or_digits():
    assert "letters or digits" in _plural(AlphanumericElement())


def test_plural_char_literal_reads_as_copies_of_character():
    assert "copies of the character" in _plural(CharElement(value="\\-"))


def test_plural_string_literal_reads_as_copies_of_text():
    assert "copies of the text" in _plural(StringElement(value="hi"))


def test_plural_range_reads_as_from_through():
    assert 'from "a" through "z"' in _plural(RangeElement(start="a", end="z"))


def test_plural_any_of_chars_reads_as_from_the_set():
    assert 'from the set "abc"' in _plural(AnyOfCharsElement(value="abc"))


def test_plural_anything_but_chars_reads_as_not_from_the_set():
    assert 'NOT from the set "abc"' in _plural(AnythingButCharsElement(value="abc"))


def test_plural_anything_but_range_reads_as_outside_range():
    assert 'outside "a" through "z"' in _plural(
        AnythingButRangeElement(start="a", end="z")
    )


def test_plural_unknown_element_falls_back_to_of_inline_form():
    class MysteryElement(DigitElement.__mro__[1]):
        pass

    mystery = MysteryElement()
    plural = _plural(mystery)
    assert plural.startswith("of ")


def test_inline_start_of_input_reads_as_very_beginning_of_text():
    assert _inline(StartOfInputElement()) == "the very beginning of the text"


def test_inline_end_of_input_reads_as_very_end_of_text():
    assert _inline(EndOfInputElement()) == "the very end of the text"


def test_inline_word_boundary_reads_as_word_boundary():
    assert _inline(WordBoundaryElement()) == "a word boundary"


def test_inline_non_word_boundary_reads_as_non_word_boundary_position():
    assert _inline(NonWordBoundaryElement()) == "a non-word-boundary position"


def test_inline_optional_reads_as_an_optional_x():
    element = OptionalElement(child=DigitElement())

    phrase = _inline(element)

    assert phrase.startswith("an optional ")


def test_inline_zero_or_more_reads_as_zero_or_more_x():
    element = ZeroOrMoreElement(child=DigitElement())

    phrase = _inline(element)

    assert phrase.startswith("zero or more")


def test_inline_zero_or_more_lazy_notes_as_few_as_possible():
    assert "as few as possible" in _inline(ZeroOrMoreLazyElement(child=DigitElement()))


def test_inline_one_or_more_reads_as_one_or_more_x():
    element = OneOrMoreElement(child=DigitElement())

    phrase = _inline(element)

    assert phrase.startswith("one or more")


def test_inline_one_or_more_lazy_notes_as_few_as_possible():
    assert "as few as possible" in _inline(OneOrMoreLazyElement(child=DigitElement()))


def test_inline_exactly_reads_as_exactly_n_x():
    element = ExactlyElement(times=4, child=DigitElement())

    phrase = _inline(element)

    assert phrase.startswith("exactly 4")


def test_inline_at_least_reads_as_at_least_n_x():
    element = AtLeastElement(times=3, child=DigitElement())

    phrase = _inline(element)

    assert phrase.startswith("at least 3")


def test_inline_at_most_reads_as_at_most_n_x():
    element = AtMostElement(times=2, child=DigitElement())

    phrase = _inline(element)

    assert phrase.startswith("at most 2")


def test_inline_between_reads_as_between_lower_and_upper():
    assert "between 2 and 5" in _inline(
        BetweenElement(lower=2, upper=5, child=DigitElement())
    )


def test_inline_between_lazy_notes_as_few_as_possible():
    assert "as few as possible" in _inline(
        BetweenLazyElement(lower=2, upper=5, child=DigitElement())
    )


def test_inline_capture_reads_as_child_captured_marker():
    assert "(captured)" in _inline(CaptureElement(children=(DigitElement(),)))


def test_inline_named_capture_includes_the_label():
    assert 'label "year"' in _inline(
        NamedCaptureElement(name="year", children=(DigitElement(),))
    )


def test_inline_group_reads_as_children_inline():
    assert "one digit" in _inline(GroupElement(children=(DigitElement(),)))


def test_inline_subexpression_reads_as_children_inline():
    assert "one digit" in _inline(SubexpressionElement(children=(DigitElement(),)))


def test_inline_alternation_reads_as_either_or_phrase():
    assert "either" in _inline(
        AnyOfElement(
            children=(StringElement(value="a"), StringElement(value="b"))
        )
    )


def test_inline_backreference_reads_as_same_text_that_group_captured():
    assert "group #1 captured" in _inline(BackReferenceElement(index=1))


def test_inline_named_backreference_reads_as_that_the_name_group_captured():
    assert 'the "year" group captured' in _inline(NamedBackReferenceElement(name="year"))


def test_optional_inner_reads_group_children_inline():
    assert "one digit" in _describe_optional_inner(
        GroupElement(children=(DigitElement(),))
    )


def test_describe_inline_children_reads_as_nothing_when_empty():
    assert _describe_inline_children(()) == "nothing"


def test_describe_inline_children_joins_multiple_phrases_with_then():
    joined = _describe_inline_children((DigitElement(), StringElement(value="X")))
    assert ", then " in joined


def test_example_for_unknown_element_returns_empty_string():
    class MysteryElement(DigitElement.__mro__[1]):
        pass

    assert _example_for(MysteryElement(), 0) == ""
