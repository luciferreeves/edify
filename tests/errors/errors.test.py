from edify.errors.anchors import (
    CannotDefineStartAfterEndError,
    EndInputAlreadyDefinedError,
    StartInputAlreadyDefinedError,
)
from edify.errors.captures import InvalidTotalCaptureGroupsIndexError
from edify.errors.input import (
    MustBeAStringError,
    MustBeAtLeastOneLiteralError,
    MustBeAtLeastTwoOperandsError,
    MustBeInstanceError,
    MustBeIntegerGreaterThanZeroError,
    MustBeLessThanError,
    MustBeOneCharacterError,
    MustBePositiveIntegerError,
    MustBeSingleCharacterError,
    MustHaveASmallerValueError,
)
from edify.errors.naming import (
    CannotCreateDuplicateNamedGroupError,
    NamedGroupDoesNotExistError,
    NameNotValidError,
)
from edify.errors.structure import (
    CannotCallSubexpressionError,
    CannotEndWhileBuildingRootExpressionError,
)


def test_start_input_already_defined_outside_subexpression():
    error = StartInputAlreadyDefinedError()
    text = str(error)
    assert "start_of_input has already been added" in text
    assert "help: remove the duplicate .start_of_input()" in text
    assert "ignore_start_and_end" not in text


def test_start_input_already_defined_in_subexpression():
    error = StartInputAlreadyDefinedError(in_subexpression=True)
    text = str(error)
    assert "start_of_input has already been added" in text
    assert "ignore_start_and_end=True" in text


def test_end_input_already_defined_outside_subexpression():
    error = EndInputAlreadyDefinedError()
    text = str(error)
    assert "end_of_input has already been added" in text
    assert "help: remove the duplicate .end_of_input()" in text
    assert "ignore_start_and_end" not in text


def test_end_input_already_defined_in_subexpression():
    error = EndInputAlreadyDefinedError(in_subexpression=True)
    text = str(error)
    assert "end_of_input has already been added" in text
    assert "ignore_start_and_end=True" in text


def test_cannot_define_start_after_end():
    error = CannotDefineStartAfterEndError()
    text = str(error)
    assert "start_of_input cannot follow end_of_input" in text
    assert "move .start_of_input() to before" in text


def test_invalid_total_capture_groups_index_reports_out_of_range():
    error = InvalidTotalCaptureGroupsIndexError(5, 3)
    text = str(error)
    assert "back_reference index #5 is out of range" in text
    assert "3 capture groups" in text
    assert "valid indices are 1 to 3" in text


def test_invalid_total_capture_groups_index_with_no_capture_groups_prompts_add_one():
    error = InvalidTotalCaptureGroupsIndexError(1, 0)
    text = str(error)
    assert "no capture groups yet" in text
    assert "add a .capture()" in text


def test_must_be_a_string():
    error = MustBeAStringError("Name", "int")
    text = str(error)
    assert "Name must be a string" in text
    assert "int" in text
    assert "convert the value with str(...)" in text


def test_must_be_one_character():
    error = MustBeOneCharacterError("Value")
    text = str(error)
    assert "Value must be one character long" in text


def test_must_be_single_character():
    error = MustBeSingleCharacterError("Value", "str")
    text = str(error)
    assert "Value must be a single character" in text
    assert "str" in text


def test_must_be_positive_integer():
    error = MustBePositiveIntegerError("count")
    text = str(error)
    assert "count must be a positive integer" in text


def test_must_be_integer_greater_than_zero():
    error = MustBeIntegerGreaterThanZeroError("x")
    text = str(error)
    assert "x must be an integer greater than zero" in text


def test_must_be_instance():
    error = MustBeInstanceError("Expression", "str", "RegexBuilder")
    text = str(error)
    assert "Expression must be an instance of RegexBuilder" in text
    assert "str" in text


def test_must_have_a_smaller_value_reports_the_codepoints():
    error = MustHaveASmallerValueError("z", "a")
    text = str(error)
    assert "range bounds are inverted" in text
    assert "'z'" in text
    assert "'a'" in text
    assert "= 122" in text
    assert "= 97" in text


def test_must_be_less_than():
    error = MustBeLessThanError("X", "Y")
    text = str(error)
    assert "X must be less than Y" in text


def test_must_be_at_least_two_operands():
    error = MustBeAtLeastTwoOperandsError("any_of")
    text = str(error)
    assert "any_of requires at least two operands" in text


def test_must_be_at_least_one_literal():
    error = MustBeAtLeastOneLiteralError("one_of")
    text = str(error)
    assert "one_of requires at least one literal" in text


def test_name_not_valid():
    error = NameNotValidError("bad name")
    text = str(error)
    assert "'bad name' is not a valid identifier" in text
    assert "letters, digits, and underscores" in text


def test_cannot_create_duplicate_named_group():
    error = CannotCreateDuplicateNamedGroupError("dup")
    text = str(error)
    assert "named group 'dup' already exists" in text
    assert ".named_back_reference('dup')" in text


def test_named_group_does_not_exist():
    error = NamedGroupDoesNotExistError("missing")
    text = str(error)
    assert "named group 'missing' does not exist" in text
    assert ".named_capture('missing')" in text


def test_cannot_end_while_building_root_expression():
    error = CannotEndWhileBuildingRootExpressionError()
    text = str(error)
    assert "cannot .end() while building the root expression" in text
    assert "no matching opener" in text or "no frame to close" in text


def test_cannot_call_subexpression():
    error = CannotCallSubexpressionError("capture")
    text = str(error)
    assert "cannot merge a subexpression that has an unclosed frame" in text
    assert "capture" in text


def test_every_annotated_error_message_starts_with_error_prefix():
    errors = [
        StartInputAlreadyDefinedError(),
        CannotDefineStartAfterEndError(),
        EndInputAlreadyDefinedError(),
        InvalidTotalCaptureGroupsIndexError(1, 0),
        MustBeAStringError("X", "int"),
        MustBeOneCharacterError("X"),
        MustBeSingleCharacterError("X", "int"),
        MustBePositiveIntegerError("X"),
        MustBeIntegerGreaterThanZeroError("X"),
        MustBeInstanceError("X", "int", "Y"),
        MustHaveASmallerValueError("z", "a"),
        MustBeLessThanError("A", "B"),
        MustBeAtLeastTwoOperandsError("f"),
        MustBeAtLeastOneLiteralError("f"),
        NameNotValidError("x"),
        CannotCreateDuplicateNamedGroupError("x"),
        NamedGroupDoesNotExistError("x"),
        CannotEndWhileBuildingRootExpressionError(),
        CannotCallSubexpressionError("capture"),
    ]
    for error in errors:
        text = str(error)
        assert text.startswith("error:")
        assert "help:" in text
        assert "= note:" in text
