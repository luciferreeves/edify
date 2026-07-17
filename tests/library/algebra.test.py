"""Chain <-> operator-algebra equivalence: ``+``, ``|`` and ``.use()`` emit the fluent-chain regex.

Every character-class module constant is driven through both surfaces and the two
emitted regex strings are asserted identical, so the operator algebra can never
drift from the fluent builder it stands in for.
"""

import pytest

from edify import (
    ALPHANUMERIC,
    ANY_CHAR,
    CARRIAGE_RETURN,
    DIGIT,
    LETTER,
    LOWERCASE,
    NEW_LINE,
    NON_DIGIT,
    NON_WHITESPACE,
    NON_WORD,
    NULL_BYTE,
    TAB,
    UPPERCASE,
    WHITESPACE,
    WORD,
    Pattern,
)

_CONSTANTS: dict[str, Pattern] = {
    "ANY_CHAR": ANY_CHAR,
    "WHITESPACE": WHITESPACE,
    "NON_WHITESPACE": NON_WHITESPACE,
    "DIGIT": DIGIT,
    "NON_DIGIT": NON_DIGIT,
    "WORD": WORD,
    "NON_WORD": NON_WORD,
    "NEW_LINE": NEW_LINE,
    "CARRIAGE_RETURN": CARRIAGE_RETURN,
    "TAB": TAB,
    "NULL_BYTE": NULL_BYTE,
    "LETTER": LETTER,
    "UPPERCASE": UPPERCASE,
    "LOWERCASE": LOWERCASE,
    "ALPHANUMERIC": ALPHANUMERIC,
}
_IDS = list(_CONSTANTS)
_VALUES = list(_CONSTANTS.values())


@pytest.mark.parametrize("constant", _VALUES, ids=_IDS)
def test_plus_matches_chain_subexpression(constant: Pattern):
    operator_form = (constant + DIGIT).to_regex_string()
    chain_form = Pattern().subexpression(constant).subexpression(DIGIT).to_regex_string()
    assert operator_form == chain_form


@pytest.mark.parametrize("constant", _VALUES, ids=_IDS)
def test_or_matches_chain_any_of(constant: Pattern):
    operator_form = (constant | DIGIT).to_regex_string()
    chain_form = (
        Pattern().any_of().subexpression(constant).subexpression(DIGIT).end().to_regex_string()
    )
    assert operator_form == chain_form


@pytest.mark.parametrize("constant", _VALUES, ids=_IDS)
def test_use_matches_chain_subexpression(constant: Pattern):
    use_form = Pattern().use(constant).to_regex_string()
    chain_form = Pattern().subexpression(constant).to_regex_string()
    assert use_form == chain_form


@pytest.mark.parametrize("constant", _VALUES, ids=_IDS)
def test_operator_and_chain_compile_to_the_same_matcher(constant: Pattern):
    operator_compiled = (constant + DIGIT).to_regex().source
    chain_compiled = Pattern().subexpression(constant).subexpression(DIGIT).to_regex().source
    assert operator_compiled == chain_compiled
