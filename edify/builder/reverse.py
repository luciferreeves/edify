"""Reverse parser: translate a raw regex string into an equivalent builder chain."""

from __future__ import annotations

import re
from typing import cast

import edify.builder.fluent as builder_module
import edify.builder.sre as sre
from edify.builder.sre import SreArgument, SrePattern

_ANCHOR_METHOD_BY_CONSTANT: dict[int, str] = {
    sre.AT_BEGINNING: "start_of_input",
    sre.AT_BEGINNING_STRING: "start_of_input",
    sre.AT_END: "end_of_input",
    sre.AT_END_STRING: "end_of_input",
    sre.AT_BOUNDARY: "word_boundary",
    sre.AT_NON_BOUNDARY: "non_word_boundary",
}

_CATEGORY_METHOD_BY_CONSTANT: dict[int, str] = {
    sre.CATEGORY_DIGIT: "digit",
    sre.CATEGORY_NOT_DIGIT: "non_digit",
    sre.CATEGORY_WORD: "word",
    sre.CATEGORY_NOT_WORD: "non_word",
    sre.CATEGORY_SPACE: "whitespace_char",
    sre.CATEGORY_NOT_SPACE: "non_whitespace_char",
}


class UnsupportedReverseParseError(ValueError):
    """Raised when ``from_regex`` encounters a construct the reverse parser cannot translate."""

    def __init__(self, construct: str) -> None:
        message = (
            f"from_regex cannot translate the regex construct {construct!r} yet; "
            "hand-write the equivalent chain and file an issue with the source pattern."
        )
        super().__init__(message)


def build_from_regex(pattern_text: str) -> builder_module.RegexBuilder:
    """Return a :class:`RegexBuilder` whose emitted pattern is equivalent to ``pattern_text``."""
    node_list = sre.parse(pattern_text)
    name_by_number = _name_by_group_number(pattern_text)
    empty_builder = builder_module.RegexBuilder()
    return _translate_sequence(empty_builder, node_list, name_by_number)


def _name_by_group_number(pattern_text: str) -> dict[int, str]:
    compiled_pattern = re.compile(pattern_text)
    return {number: name for name, number in compiled_pattern.groupindex.items()}


def _translate_sequence(
    builder: builder_module.RegexBuilder,
    nodes: SrePattern,
    names: dict[int, str],
) -> builder_module.RegexBuilder:
    current = builder
    literal_run: list[str] = []
    for node in nodes:
        opcode, argument = node
        if opcode == sre.LITERAL:
            literal_run.append(chr(cast(int, argument)))
            continue
        if literal_run:
            current = _emit_string(current, literal_run)
            literal_run = []
        current = _translate_node(current, opcode, argument, names)
    if literal_run:
        current = _emit_string(current, literal_run)
    return current


def _emit_string(
    builder: builder_module.RegexBuilder, literal_run: list[str]
) -> builder_module.RegexBuilder:
    joined = "".join(literal_run)
    if len(joined) == 1:
        return builder.char(joined)
    return builder.string(joined)


def _translate_node(
    builder: builder_module.RegexBuilder,
    opcode: int,
    argument: SreArgument,
    names: dict[int, str],
) -> builder_module.RegexBuilder:
    if opcode == sre.ANY:
        return builder.any_char()
    if opcode == sre.AT:
        return _translate_anchor(builder, cast(int, argument))
    if opcode == sre.IN:
        return _translate_character_class(builder, cast(SrePattern, argument))
    if opcode == sre.MAX_REPEAT:
        return _translate_repeat(
            builder, cast("tuple[int, int, SrePattern]", argument), names, lazy=False
        )
    if opcode == sre.MIN_REPEAT:
        return _translate_repeat(
            builder, cast("tuple[int, int, SrePattern]", argument), names, lazy=True
        )
    if opcode == sre.SUBPATTERN:
        return _translate_subpattern(
            builder, cast("tuple[int | None, int, int, SrePattern]", argument), names
        )
    if opcode == sre.BRANCH:
        return _translate_branch(builder, cast("tuple[None, list[SrePattern]]", argument))
    if opcode == sre.ASSERT:
        return _translate_lookaround(
            builder, cast("tuple[int, SrePattern]", argument), names, negative=False
        )
    if opcode == sre.ASSERT_NOT:
        return _translate_lookaround(
            builder, cast("tuple[int, SrePattern]", argument), names, negative=True
        )
    raise UnsupportedReverseParseError(str(opcode))


def _translate_anchor(
    builder: builder_module.RegexBuilder, argument: int
) -> builder_module.RegexBuilder:
    method_name = _ANCHOR_METHOD_BY_CONSTANT[argument]
    anchor_method = getattr(builder, method_name)
    return cast(builder_module.RegexBuilder, anchor_method())


def _translate_character_class(
    builder: builder_module.RegexBuilder, members: SrePattern
) -> builder_module.RegexBuilder:
    if len(members) == 1:
        return _translate_single_class_member(builder, members[0])
    literal_chars: list[str] = []
    for member in members:
        opcode, argument = member
        if opcode == sre.LITERAL:
            literal_chars.append(chr(cast(int, argument)))
            continue
        raise UnsupportedReverseParseError(f"character-class member {member!r}")
    joined_chars = "".join(literal_chars)
    return builder.any_of_chars(joined_chars)


def _translate_single_class_member(
    builder: builder_module.RegexBuilder, member: tuple[int, SreArgument]
) -> builder_module.RegexBuilder:
    opcode, argument = member
    if opcode == sre.RANGE:
        start_codepoint, end_codepoint = cast("tuple[int, int]", argument)
        return builder.range(chr(start_codepoint), chr(end_codepoint))
    method_name = _CATEGORY_METHOD_BY_CONSTANT[cast(int, argument)]
    category_method = getattr(builder, method_name)
    return cast(builder_module.RegexBuilder, category_method())


def _translate_repeat(
    builder: builder_module.RegexBuilder,
    argument: tuple[int, int, SrePattern],
    names: dict[int, str],
    lazy: bool,
) -> builder_module.RegexBuilder:
    min_count, max_count, body = argument
    quantified = _apply_quantifier(builder, min_count, max_count, lazy)
    body_nodes = list(body)
    return _translate_sequence(quantified, body_nodes, names)


def _apply_quantifier(
    builder: builder_module.RegexBuilder, min_count: int, max_count: int, lazy: bool
) -> builder_module.RegexBuilder:
    if min_count == 0 and max_count == 1:
        return builder.optional()
    if min_count == 0 and max_count == sre.MAXREPEAT:
        return builder.zero_or_more_lazy() if lazy else builder.zero_or_more()
    if min_count == 1 and max_count == sre.MAXREPEAT:
        return builder.one_or_more_lazy() if lazy else builder.one_or_more()
    if min_count == max_count:
        return builder.exactly(min_count)
    if max_count == sre.MAXREPEAT:
        return builder.at_least(min_count)
    if lazy:
        return builder.between_lazy(min_count, max_count)
    return builder.between(min_count, max_count)


def _translate_subpattern(
    builder: builder_module.RegexBuilder,
    argument: tuple[int | None, int, int, SrePattern],
    names: dict[int, str],
) -> builder_module.RegexBuilder:
    group_number, _in_flags, _out_flags, body = argument
    body_nodes = list(body)
    if group_number is not None and group_number in names:
        opened = builder.named_capture(names[group_number])
    else:
        opened = builder.capture()
    populated = _translate_sequence(opened, body_nodes, names)
    return populated.end()


def _translate_branch(
    builder: builder_module.RegexBuilder, argument: tuple[None, list[SrePattern]]
) -> builder_module.RegexBuilder:
    _leading, branches = argument
    literal_branches: list[str] = []
    for branch in branches:
        branch_nodes = list(branch)
        literal_string = _branch_as_literal_string(branch_nodes)
        if literal_string is None:
            raise UnsupportedReverseParseError("alternation with non-literal branch")
        literal_branches.append(literal_string)
    return builder.any_of(*literal_branches)


def _branch_as_literal_string(nodes: SrePattern) -> str | None:
    characters: list[str] = []
    for node in nodes:
        opcode, argument = node
        if opcode != sre.LITERAL:
            return None
        characters.append(chr(cast(int, argument)))
    return "".join(characters)


def _translate_lookaround(
    builder: builder_module.RegexBuilder,
    argument: tuple[int, SrePattern],
    names: dict[int, str],
    negative: bool,
) -> builder_module.RegexBuilder:
    direction, body = argument
    method_name = _lookaround_method(direction, negative)
    lookaround_opener = getattr(builder, method_name)
    opened = cast(builder_module.RegexBuilder, lookaround_opener())
    body_nodes = list(body)
    populated = _translate_sequence(opened, body_nodes, names)
    return populated.end()


def _lookaround_method(direction: int, negative: bool) -> str:
    if direction == 1:
        return "assert_not_ahead" if negative else "assert_ahead"
    return "assert_not_behind" if negative else "assert_behind"
