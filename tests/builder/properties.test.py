"""Property assertion — no chain ever silently drops a quantifier.

For any list of ``(quantifier method, args)`` calls, each immediately
followed by a leaf-element call, the emitted regex is the concatenation
of ``<element><suffix>`` fragments in the same order — no quantifier is
lost, none appears twice.
"""

from hypothesis import given
from hypothesis import strategies as st

from edify import RegexBuilder

_QUANTIFIER_STRATEGIES: list[st.SearchStrategy[tuple[str, tuple[int, ...], str]]] = [
    st.just(("optional", (), "?")),
    st.just(("zero_or_more", (), "*")),
    st.just(("zero_or_more_lazy", (), "*?")),
    st.just(("one_or_more", (), "+")),
    st.just(("one_or_more_lazy", (), "+?")),
    st.integers(min_value=1, max_value=8).map(lambda n: ("exactly", (n,), f"{{{n}}}")),
    st.integers(min_value=1, max_value=8).map(lambda n: ("at_least", (n,), f"{{{n},}}")),
    st.integers(min_value=1, max_value=8).map(lambda n: ("at_most", (n,), f"{{0,{n}}}")),
    st.tuples(
        st.integers(min_value=0, max_value=6),
        st.integers(min_value=1, max_value=8),
    )
    .filter(lambda pair: pair[0] < pair[1])
    .map(lambda pair: ("between", pair, f"{{{pair[0]},{pair[1]}}}")),
    st.tuples(
        st.integers(min_value=0, max_value=6),
        st.integers(min_value=1, max_value=8),
    )
    .filter(lambda pair: pair[0] < pair[1])
    .map(lambda pair: ("between_lazy", pair, f"{{{pair[0]},{pair[1]}}}?")),
]

_ELEMENT_STRATEGIES = [
    st.just(("digit", (), "\\d")),
    st.just(("word", (), "\\w")),
    st.just(("whitespace_char", (), "\\s")),
    st.just(("letter", (), "[a-zA-Z]")),
    st.just(("uppercase", (), "[A-Z]")),
    st.just(("lowercase", (), "[a-z]")),
    st.just(("alphanumeric", (), "[a-zA-Z0-9]")),
]

_quantifier_element_pair = st.tuples(
    st.one_of(*_QUANTIFIER_STRATEGIES),
    st.one_of(*_ELEMENT_STRATEGIES),
)


@given(st.lists(_quantifier_element_pair, min_size=1, max_size=8))
def test_every_quantifier_chain_call_produces_exactly_one_output_quantifier(pairs):
    builder = RegexBuilder()
    expected_fragments: list[str] = []
    for quantifier_call, element_call in pairs:
        quantifier_name, quantifier_args, quantifier_suffix = quantifier_call
        element_name, element_args, element_regex = element_call
        builder = getattr(builder, quantifier_name)(*quantifier_args)
        builder = getattr(builder, element_name)(*element_args)
        expected_fragments.append(f"{element_regex}{quantifier_suffix}")
    assert builder.to_regex_string() == "".join(expected_fragments)


@given(st.lists(st.one_of(*_ELEMENT_STRATEGIES), min_size=1, max_size=8))
def test_bare_element_chain_emits_the_concatenation_of_element_fragments(elements):
    builder = RegexBuilder()
    expected_fragments: list[str] = []
    for element_name, element_args, element_regex in elements:
        builder = getattr(builder, element_name)(*element_args)
        expected_fragments.append(element_regex)
    assert builder.to_regex_string() == "".join(expected_fragments)
