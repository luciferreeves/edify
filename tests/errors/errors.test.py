from edify.errors.anchors import (
    CannotDefineStartAfterEndError,
    EndInputAlreadyDefinedError,
    StartInputAlreadyDefinedError,
)
from edify.errors.captures import InvalidTotalCaptureGroupsIndexError
from edify.errors.input import (
    MustBeAStringError,
    MustBeAtLeastTwoOperandsError,
    MustBeInstanceError,
    MustBeIntegerGreaterThanZeroError,
    MustBeLessThanError,
    MustBeOneCharacterError,
    MustBePositiveIntegerError,
    MustBeSingleCharacterError,
    MustHaveASmallerValueError,
)
from edify.errors.internal import (
    FailedToCompileRegexError,
    NonFusableElementError,
    UnexpectedFrameTypeError,
    UnknownElementTypeError,
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
    assert "already has a start" in str(error)
    assert "ignore_start_and_end" not in str(error)


def test_start_input_already_defined_in_subexpression():
    error = StartInputAlreadyDefinedError(in_subexpression=True)
    assert "ignore_start_and_end" in str(error)


def test_end_input_already_defined_outside_subexpression():
    error = EndInputAlreadyDefinedError()
    assert "already has an end" in str(error)
    assert "ignore_start_and_end" not in str(error)


def test_end_input_already_defined_in_subexpression():
    error = EndInputAlreadyDefinedError(in_subexpression=True)
    assert "ignore_start_and_end" in str(error)


def test_cannot_define_start_after_end():
    error = CannotDefineStartAfterEndError()
    assert "start of input after defining an end" in str(error)


def test_invalid_total_capture_groups_index():
    error = InvalidTotalCaptureGroupsIndexError(5, 3)
    assert "Invalid index #5" in str(error)
    assert "only 3 capture groups" in str(error)


def test_must_be_a_string():
    error = MustBeAStringError("Name", "int")
    assert "Name must be a string" in str(error)
    assert "int" in str(error)


def test_must_be_one_character():
    error = MustBeOneCharacterError("Value")
    assert "Value must be one character long" in str(error)


def test_must_be_single_character():
    error = MustBeSingleCharacterError("Value", "str")
    assert "Value must be a single character" in str(error)
    assert "str" in str(error)


def test_must_be_positive_integer():
    error = MustBePositiveIntegerError("count")
    assert "count must be a positive integer" in str(error)


def test_must_be_integer_greater_than_zero():
    error = MustBeIntegerGreaterThanZeroError("x")
    assert "x must be an integer greater than zero" in str(error)


def test_must_be_instance():
    error = MustBeInstanceError("Expression", "str", "RegexBuilder")
    assert "Expression must be an instance of RegexBuilder" in str(error)
    assert "str" in str(error)


def test_must_have_a_smaller_value():
    error = MustHaveASmallerValueError("z", "a")
    assert "z must have a smaller character value than a" in str(error)


def test_must_be_less_than():
    error = MustBeLessThanError("X", "Y")
    assert "X must be less than Y" in str(error)


def test_must_be_at_least_two_operands():
    error = MustBeAtLeastTwoOperandsError("any_of")
    assert "any_of requires at least two operands" in str(error)


def test_name_not_valid():
    error = NameNotValidError("bad name")
    assert "Name bad name is not valid" in str(error)


def test_cannot_create_duplicate_named_group():
    error = CannotCreateDuplicateNamedGroupError("dup")
    assert 'Can not create duplicate named group "dup"' in str(error)


def test_named_group_does_not_exist():
    error = NamedGroupDoesNotExistError("missing")
    assert 'Named group "missing" does not exist' in str(error)


def test_cannot_end_while_building_root_expression():
    error = CannotEndWhileBuildingRootExpressionError()
    assert "Can not end while building the root expression" in str(error)


def test_cannot_call_subexpression():
    error = CannotCallSubexpressionError("capture")
    assert "Can not call subexpression" in str(error)
    assert "capture" in str(error)


def test_unknown_element_type():
    error = UnknownElementTypeError("WeirdElement")
    assert "WeirdElement" in str(error)


def test_non_fusable_element():
    error = NonFusableElementError("DigitElement")
    assert "Cannot fuse element of type DigitElement" in str(error)


def test_unexpected_frame_type():
    error = UnexpectedFrameTypeError("DigitElement")
    assert "Stack frame anchored at unexpected element type DigitElement" in str(error)


def test_failed_to_compile_regex():
    error = FailedToCompileRegexError("missing )")
    assert "Cannot compile regex: missing )" in str(error)
