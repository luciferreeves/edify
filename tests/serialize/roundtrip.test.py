"""Round-trip tests for Pattern.to_dict/from_dict and to_json/from_json."""

from edify import END, START, Pattern
from edify.serialize import JSONValue


def _roundtrip_dict(pattern: Pattern) -> Pattern:
    return Pattern.from_dict(pattern.to_dict())


def _roundtrip_json(pattern: Pattern) -> Pattern:
    return Pattern.from_json(pattern.to_json())


def test_empty_pattern_roundtrips():
    original = Pattern()
    assert _roundtrip_dict(original) == original
    assert _roundtrip_json(original) == original


def test_simple_digit_pattern_roundtrips():
    original = Pattern().digit()
    restored = _roundtrip_dict(original)
    assert restored == original
    assert restored.to_regex_string() == original.to_regex_string()


def test_anchored_pattern_roundtrips():
    original = Pattern().start_of_input().one_or_more().digit().end_of_input()
    restored = _roundtrip_json(original)
    assert restored == original
    assert restored.state.has_defined_start
    assert restored.state.has_defined_end


def test_char_class_pattern_roundtrips():
    original = Pattern().any_of().range("a", "z").range("0", "9").char("_").end()
    assert _roundtrip_dict(original) == original


def test_negated_class_roundtrips():
    original = Pattern().anything_but_chars("abc")
    assert _roundtrip_dict(original) == original


def test_negated_range_roundtrips():
    original = Pattern().anything_but_range("a", "z")
    assert _roundtrip_dict(original) == original


def test_anything_but_string_roundtrips():
    original = Pattern().anything_but_string("bad")
    assert _roundtrip_dict(original) == original


def test_capture_group_roundtrips():
    original = Pattern().capture().digit().end()
    assert _roundtrip_dict(original) == original
    assert _roundtrip_dict(original).state.total_capture_groups == 1


def test_named_capture_roundtrips_with_names_and_count():
    original = Pattern().named_capture("year").exactly(4).digit().end()
    restored = _roundtrip_dict(original)
    assert restored == original
    assert restored.state.named_groups == ("year",)
    assert restored.state.total_capture_groups == 1


def test_backreference_roundtrips():
    original = Pattern().capture().digit().end().back_reference(1)
    assert _roundtrip_dict(original) == original


def test_named_backreference_roundtrips():
    original = Pattern().named_capture("d").digit().end().named_back_reference("d")
    assert _roundtrip_dict(original) == original


def test_group_roundtrips():
    original = Pattern().group().letter().digit().end()
    assert _roundtrip_dict(original) == original


def test_any_of_alternation_roundtrips():
    original = Pattern().any_of().string("cat").string("dog").end()
    assert _roundtrip_dict(original) == original


def test_positive_lookahead_roundtrips():
    original = Pattern().assert_ahead().digit().end()
    assert _roundtrip_dict(original) == original


def test_negative_lookahead_roundtrips():
    original = Pattern().assert_not_ahead().digit().end()
    assert _roundtrip_dict(original) == original


def test_positive_lookbehind_roundtrips():
    original = Pattern().assert_behind().digit().end()
    assert _roundtrip_dict(original) == original


def test_negative_lookbehind_roundtrips():
    original = Pattern().assert_not_behind().digit().end()
    assert _roundtrip_dict(original) == original


def test_optional_quantifier_roundtrips():
    original = Pattern().optional().digit()
    assert _roundtrip_dict(original) == original


def test_zero_or_more_roundtrips():
    original = Pattern().zero_or_more().digit()
    assert _roundtrip_dict(original) == original


def test_zero_or_more_lazy_roundtrips():
    original = Pattern().zero_or_more_lazy().digit()
    assert _roundtrip_dict(original) == original


def test_one_or_more_roundtrips():
    original = Pattern().one_or_more().digit()
    assert _roundtrip_dict(original) == original


def test_one_or_more_lazy_roundtrips():
    original = Pattern().one_or_more_lazy().digit()
    assert _roundtrip_dict(original) == original


def test_exactly_roundtrips_and_preserves_count():
    original = Pattern().exactly(5).digit()
    restored = _roundtrip_dict(original)
    assert restored == original


def test_at_least_roundtrips():
    original = Pattern().at_least(3).digit()
    assert _roundtrip_dict(original) == original


def test_at_most_roundtrips():
    original = Pattern().at_most(5).digit()
    assert _roundtrip_dict(original) == original


def test_between_roundtrips_and_preserves_bounds():
    original = Pattern().between(2, 5).digit()
    assert _roundtrip_dict(original) == original


def test_between_lazy_roundtrips():
    original = Pattern().between_lazy(2, 5).digit()
    assert _roundtrip_dict(original) == original


def test_all_leaves_roundtrip():
    for construction in (
        Pattern().any_char(),
        Pattern().whitespace_char(),
        Pattern().non_whitespace_char(),
        Pattern().digit(),
        Pattern().non_digit(),
        Pattern().word(),
        Pattern().non_word(),
        Pattern().word_boundary(),
        Pattern().non_word_boundary(),
        Pattern().new_line(),
        Pattern().carriage_return(),
        Pattern().tab(),
        Pattern().null_byte(),
        Pattern().letter(),
        Pattern().uppercase(),
        Pattern().lowercase(),
        Pattern().alphanumeric(),
    ):
        assert _roundtrip_dict(construction) == construction


def test_module_constants_roundtrip():
    assert _roundtrip_dict(START) == START
    assert _roundtrip_dict(END) == END


def test_flags_survive_roundtrip():
    original = Pattern().ignore_case().multi_line().digit()
    restored = _roundtrip_dict(original)
    assert restored == original
    assert restored.state.flags.ignore_case
    assert restored.state.flags.multiline


def test_string_element_roundtrips():
    original = Pattern().string("hello")
    assert _roundtrip_dict(original) == original


def test_char_element_roundtrips():
    original = Pattern().char("!")
    assert _roundtrip_dict(original) == original


def test_range_element_roundtrips():
    original = Pattern().range("a", "z")
    assert _roundtrip_dict(original) == original


def test_any_of_chars_roundtrips():
    original = Pattern().any_of_chars("abc")
    assert _roundtrip_dict(original) == original


def test_subexpression_survives_roundtrip():
    inner = Pattern().digit()
    original = Pattern().string("v=").subexpression(inner)
    assert _roundtrip_dict(original) == original


def test_pattern_output_dict_carries_schema_version_zero():
    document = Pattern().digit().to_dict()
    assert document["edify"] == 0


def test_flags_key_omitted_when_no_flags_set():
    document = Pattern().digit().to_dict()
    assert "flags" not in document


def test_unknown_element_field_is_ignored_for_forward_compatibility():
    document: dict[str, JSONValue] = {
        "edify": 0,
        "pattern": {
            "kind": "root",
            "children": [
                {"kind": "digit", "future_field_from_a_newer_edify": "ignored"},
            ],
        },
    }
    restored = Pattern.from_dict(document)
    assert restored.to_regex_string() == r"\d"
