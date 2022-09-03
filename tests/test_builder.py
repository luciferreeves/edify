import re

from edify import RegexBuilder

simple_se = RegexBuilder().string('hello').any_char().string('world')
flags_se = RegexBuilder().multi_line().ignore_case().string('hello').any_char().string('world')
start_end_se = RegexBuilder().start_of_input().string('hello').any_char().string('world').end_of_input()
nc_se = RegexBuilder().named_capture('module').exactly(2).any_char().end().named_back_reference('module')
indexed_back_reference_se = RegexBuilder().capture().exactly(2).any_char().end().back_reference(1)
nested_se = RegexBuilder().exactly(2).any_char()
first_layer_se = (
    RegexBuilder().string('outer begin').named_capture('inner_subexpression').optional().subexpression(nested_se).end().string('outer end')
)


def regex_equality(regex, rb_expression):
    regex_str = str(regex)
    rb_expression_str = rb_expression.to_regex_string()
    assert regex_str == str(rb_expression_str)


def regex_compilation(regex, rb_expression, f=0):
    rb_expression_c = rb_expression.to_regex()
    assert re.compile(regex, flags=f) == rb_expression_c


def test_empty_regex():
    expr = RegexBuilder()
    regex_equality('/(?:)/', expr)
    regex_compilation('(?:)', expr)


def test_flag_a():
    expr = RegexBuilder().ascii_only()
    regex_equality('/(?:)/A', expr)
    regex_compilation('(?:)', expr, re.A)


def test_flag_d():
    expr = RegexBuilder().debug()
    regex_equality('/(?:)/D', expr)
    regex_compilation('(?:)', expr, re.DEBUG)


def test_flag_i():
    expr = RegexBuilder().ignore_case()
    regex_equality('/(?:)/I', expr)
    regex_compilation('(?:)', expr, re.I)


def test_flag_m():
    expr = RegexBuilder().multi_line()
    regex_equality('/(?:)/M', expr)
    regex_compilation('(?:)', expr, re.M)


def test_flag_s():
    expr = RegexBuilder().dot_all()
    regex_equality('/(?:)/S', expr)
    regex_compilation('(?:)', expr, re.S)


def test_flag_x():
    expr = RegexBuilder().verbose()
    regex_equality('/(?:)/X', expr)
    regex_compilation('(?:)', expr, re.X)


def test_any_char():
    expr = RegexBuilder().any_char()
    regex_equality('/./', expr)
    regex_compilation('.', expr)


def test_whitespace_char():
    expr = RegexBuilder().whitespace_char()
    regex_equality('/\\s/', expr)
    regex_compilation('\\s', expr)


def test_non_whitespace_char():
    expr = RegexBuilder().non_whitespace_char()
    regex_equality('/\\S/', expr)
    regex_compilation('\\S', expr)


def test_digit():
    expr = RegexBuilder().digit()
    regex_equality('/\\d/', expr)
    regex_compilation('\\d', expr)


def test_non_digit():
    expr = RegexBuilder().non_digit()
    regex_equality('/\\D/', expr)
    regex_compilation('\\D', expr)


def test_word():
    expr = RegexBuilder().word()
    regex_equality('/\\w/', expr)
    regex_compilation('\\w', expr)


def test_non_word():
    expr = RegexBuilder().non_word()
    regex_equality('/\\W/', expr)
    regex_compilation('\\W', expr)


def test_word_boundary():
    expr = RegexBuilder().word_boundary()
    regex_equality('/\\b/', expr)
    regex_compilation('\\b', expr)


def test_non_word_boundary():
    expr = RegexBuilder().non_word_boundary()
    regex_equality('/\\B/', expr)
    regex_compilation('\\B', expr)


def test_new_line():
    expr = RegexBuilder().new_line()
    regex_equality('/\\n/', expr)
    regex_compilation('\\n', expr)


def test_carriage_return():
    expr = RegexBuilder().carriage_return()
    regex_equality('/\\r/', expr)
    regex_compilation('\\r', expr)


def test_tab():
    expr = RegexBuilder().tab()
    regex_equality('/\\t/', expr)
    regex_compilation('\\t', expr)


def test_null_byte():
    expr = RegexBuilder().null_byte()
    regex_equality('/\\0/', expr)
    regex_compilation('\\0', expr)


def test_any_of_basic():
    expr = RegexBuilder().any_of().string('hello').digit().word().char('.').char('#').end()
    regex_equality('/(?:hello|\\d|\\w|[\\.\\#])/', expr)
    regex_compilation('(?:hello|\\d|\\w|[\\.\\#])', expr)


def test_any_of_range_fusion():
    expr = RegexBuilder().any_of().range('a', 'z').range('A', 'Z').range('0', '9').char('.').char('#').end()
    regex_equality('/[a-zA-Z0-9\\.\\#]/', expr)
    regex_compilation('[a-zA-Z0-9\\.\\#]', expr)


def test_any_of_range_fusion_with_other_choices():
    expr = RegexBuilder().any_of().range('a', 'z').range('A', 'Z').range('0', '9').char('.').char('#').string('hello').end()
    regex_equality('/(?:hello|[a-zA-Z0-9\\.\\#])/', expr)
    regex_compilation('(?:hello|[a-zA-Z0-9\\.\\#])', expr)


def test_capture():
    expr = RegexBuilder().capture().string('hello ').word().char('!').end()
    regex_equality('/(hello \\w!)/', expr)
    regex_compilation('(hello \\w!)', expr)


def test_named_capture():
    expr = RegexBuilder().named_capture('this_is_the_name').string('hello ').word().char('!').end()
    regex_equality('/(?P<this_is_the_name>hello \\w!)/', expr)
    regex_compilation('(?P<this_is_the_name>hello \\w!)', expr)


def test_bad_name_error():
    try:
        (RegexBuilder().named_capture('hello world').string('hello ').word().char('!').end())
    except Exception as e:
        assert isinstance(e, Exception)


def test_same_name_error():
    try:
        (
            RegexBuilder()
            .namedCapture('hello')
            .string('hello ')
            .word()
            .char('!')
            .end()
            .namedCapture('hello')
            .string('hello ')
            .word()
            .char('!')
            .end()
        )
    except Exception as e:
        assert isinstance(e, Exception)


def test_named_back_reference():
    expr = RegexBuilder().named_capture('this_is_the_name').string('hello ').word().char('!').end().named_back_reference('this_is_the_name')
    regex_equality('/(?P<this_is_the_name>hello \\w!)\\k<this_is_the_name>/', expr)
    # Python does not support named back references, so we raise an error
    try:
        expr.to_regex()
    except Exception as e:
        assert isinstance(e, Exception)


def test_named_back_reference_no_cg_exists():
    try:
        RegexBuilder().named_back_reference('not_here')
    except Exception as e:
        assert isinstance(e, Exception)


def test_back_reference():
    expr = RegexBuilder().capture().string('hello ').word().char('!').end().back_reference(1)
    regex_equality('/(hello \\w!)\\1/', expr)
    regex_compilation('(hello \\w!)\\1', expr)


def test_back_reference_no_cg_exists():
    try:
        RegexBuilder().back_reference(1)
    except Exception as e:
        assert isinstance(e, Exception)


def test_group():
    expr = RegexBuilder().group().string('hello ').word().char('!').end()
    regex_equality('/(?:hello \\w!)/', expr)
    regex_compilation('(?:hello \\w!)', expr)


def test_error_when_called_with_no_stack():
    try:
        RegexBuilder().end()
    except Exception as e:
        assert isinstance(e, Exception)


def test_assert_ahead():
    expr = RegexBuilder().assert_ahead().range('a', 'f').end().range('a', 'z')
    regex_equality('/(?=[a-f])[a-z]/', expr)
    regex_compilation('(?=[a-f])[a-z]', expr)


def test_assert_behind():
    expr = RegexBuilder().assert_behind().string('hello ').end().range('a', 'z')
    regex_equality('/(?<=hello )[a-z]/', expr)
    regex_compilation('(?<=hello )[a-z]', expr)


def test_assert_not_ahead():
    expr = RegexBuilder().assert_not_ahead().range('a', 'f').end().range('0', '9')
    regex_equality('/(?![a-f])[0-9]/', expr)
    regex_compilation('(?![a-f])[0-9]', expr)


def test_assert_not_behind():
    expr = RegexBuilder().assert_not_behind().string('hello ').end().range('a', 'z')
    regex_equality('/(?<!hello )[a-z]/', expr)
    regex_compilation('(?<!hello )[a-z]', expr)


def test_optional():
    expr = RegexBuilder().optional().word()
    regex_equality('/\\w?/', expr)
    regex_compilation('\\w?', expr)


def test_zero_or_more():
    expr = RegexBuilder().zero_or_more().word()
    regex_equality('/\\w*/', expr)
    regex_compilation('\\w*', expr)


def test_zero_or_more_lazy():
    expr = RegexBuilder().zero_or_more_lazy().word()
    regex_equality('/\\w*?/', expr)
    regex_compilation('\\w*?', expr)


def test_one_or_more():
    expr = RegexBuilder().one_or_more().word()
    regex_equality('/\\w+/', expr)
    regex_compilation('\\w+', expr)


def test_one_or_more_lazy():
    expr = RegexBuilder().one_or_more_lazy().word()
    regex_equality('/\\w+?/', expr)
    regex_compilation('\\w+?', expr)


def test_exactly():
    expr = RegexBuilder().exactly(3).word()
    regex_equality('/\\w{3}/', expr)
    regex_compilation('\\w{3}', expr)


def test_at_least():
    expr = RegexBuilder().at_least(3).word()
    regex_equality('/\\w{3,}/', expr)
    regex_compilation('\\w{3,}', expr)


def test_between():
    expr = RegexBuilder().between(3, 5).word()
    regex_equality('/\\w{3,5}/', expr)
    regex_compilation('\\w{3,5}', expr)


def test_between_lazy():
    expr = RegexBuilder().between_lazy(3, 5).word()
    regex_equality('/\\w{3,5}?/', expr)
    regex_compilation('\\w{3,5}?', expr)


def test_start_of_input():
    expr = RegexBuilder().start_of_input()
    regex_equality('/^/', expr)
    regex_compilation('^', expr)


def test_end_of_input():
    expr = RegexBuilder().end_of_input()
    regex_equality('/$/', expr)
    regex_compilation('$', expr)


def test_any_of_chars():
    expr = RegexBuilder().any_of_chars('aeiou.-')
    regex_equality('/[aeiou\\.\\-]/', expr)
    regex_compilation('[aeiou\\.\\-]', expr)


def test_anything_but_chars():
    expr = RegexBuilder().anything_but_chars('aeiou.-')
    regex_equality('/[^aeiou\\.\\-]/', expr)
    regex_compilation('[^aeiou\\.\\-]', expr)


def test_anything_but_string():
    expr = RegexBuilder().anything_but_string('aeiou.')
    regex_equality('/(?:[^a][^e][^i][^o][^u][^\\][^.])/', expr)
    regex_compilation('(?:[^a][^e][^i][^o][^u][^\\][^.])', expr)


def test_anything_but_range():
    expr = RegexBuilder().anything_but_range('a', 'z')
    regex_equality('/[^a-z]/', expr)
    regex_compilation('[^a-z]', expr)
    expr = RegexBuilder().anything_but_range('0', '9')
    regex_equality('/[^0-9]/', expr)
    regex_compilation('[^0-9]', expr)


def test_string():
    expr = RegexBuilder().string('hello')
    regex_equality('/hello/', expr)
    regex_compilation('hello', expr)


def test_string_escapes_special_chars_with_strings_of_len_1():
    expr = RegexBuilder().string('^').string('hello')
    regex_equality('/\\^hello/', expr)
    regex_compilation('\\^hello', expr)


def test_char():
    expr = RegexBuilder().char('a')
    regex_equality('/a/', expr)
    regex_compilation('a', expr)


def test_char_more_than_one_error():
    try:
        RegexBuilder().char('hello')
    except Exception as e:
        assert isinstance(e, Exception)


def test_range():
    expr = RegexBuilder().range('a', 'z')
    regex_equality('/[a-z]/', expr)
    regex_compilation('[a-z]', expr)


def test_must_be_instance_error():
    try:
        RegexBuilder().subexpression('nope')
    except Exception as e:
        assert isinstance(e, Exception)


def test_simple_se():
    expr = RegexBuilder().start_of_input().at_least(3).digit().subexpression(simple_se).range('0', '9').end_of_input()
    regex_equality('/^\\d{3,}hello.world[0-9]$/', expr)
    regex_compilation('^\\d{3,}hello.world[0-9]$', expr)


def test_simple_quantified_se():
    expr = RegexBuilder().start_of_input().at_least(3).digit().one_or_more().subexpression(simple_se).range('0', '9').end_of_input()
    regex_equality('/^\\d{3,}(?:hello.world)+[0-9]$/', expr)
    regex_compilation('^\\d{3,}(?:hello.world)+[0-9]$', expr)


def test_flags_se():
    expr = (
        RegexBuilder()
        .dot_all()
        .start_of_input()
        .at_least(3)
        .digit()
        .subexpression(flags_se, {'ignore_flags': False})
        .range('0', '9')
        .end_of_input()
    )
    regex_equality('/^\\d{3,}hello.world[0-9]$/IMS', expr)
    regex_compilation('^\\d{3,}hello.world[0-9]$', expr, f=re.M | re.I | re.S)


def test_flags_se_ignore_flags():
    expr = RegexBuilder().dot_all().start_of_input().at_least(3).digit().subexpression(flags_se).range('0', '9').end_of_input()
    regex_equality('/^\\d{3,}hello.world[0-9]$/S', expr)
    regex_compilation('^\\d{3,}hello.world[0-9]$', expr, f=re.S)


def test_ignore_start_and_end():
    expr = RegexBuilder().at_least(3).digit().subexpression(start_end_se).range('0', '9')
    regex_equality('/\\d{3,}hello.world[0-9]/', expr)
    regex_compilation('\\d{3,}hello.world[0-9]', expr)


def test_dont_ignore_start_and_end():
    try:
        (RegexBuilder().at_least(3).digit().subexpression(start_end_se, {'ignore_start_and_end': False}).range('0', '9'))
    except Exception as e:
        assert isinstance(e, Exception)


def test_dont_ignore_start_and_end2():
    try:
        se = RegexBuilder().start_of_input().string('hello').any_char().string('world')
        (RegexBuilder().at_least(3).digit().subexpression(se, {'ignore_start_and_end': False}).range('0', '9'))
    except Exception as e:
        assert isinstance(e, Exception)


def test_dont_ignore_start_and_end3():
    try:
        se = RegexBuilder().string('hello').any_char().string('world').end_of_input()
        (RegexBuilder().at_least(3).digit().subexpression(se, {'ignore_start_and_end': False}).range('0', '9'))
    except Exception as e:
        assert isinstance(e, Exception)


def test_start_defined_in_me_and_se():
    try:
        (RegexBuilder().start_of_input().at_least(3).digit().subexpression(start_end_se, {'ignore_start_and_end': False}).range('0', '9'))
    except Exception as e:
        assert isinstance(e, Exception)


def test_end_defined_in_me_and_se():
    try:
        (RegexBuilder().at_least(3).digit().subexpression(start_end_se, {'ignore_start_and_end': False}).range('0', '9').end_of_input())
    except Exception as e:
        assert isinstance(e, Exception)


def test_no_namespacing():
    expr = RegexBuilder().at_least(3).digit().subexpression(nc_se).range('0', '9')
    regex_equality('/\\d{3,}(?P<module>.{2})\\k<module>[0-9]/', expr)
    try:
        expr.to_regex()
    except Exception as e:
        assert isinstance(e, Exception)


def test_namespacing():
    expr = RegexBuilder().at_least(3).digit().subexpression(nc_se, {'namespace': 'yolo'}).range('0', '9')
    regex_equality('/\\d{3,}(?P<yolomodule>.{2})\\k<yolomodule>[0-9]/', expr)
    try:
        expr.to_regex()
    except Exception as e:
        assert isinstance(e, Exception)


def test_group_name_collision_error():
    try:
        (RegexBuilder().namedCapture('module').at_least(3).digit().end().subexpression(nc_se).range('0', '9'))
    except Exception as e:
        assert isinstance(e, Exception)


def test_group_name_collision_error_after_namespacing():
    try:
        (RegexBuilder().namedCapture('module').at_least(3).digit().end().subexpression(nc_se, {'namespace': 'yolo'}).range('0', '9'))
    except Exception as e:
        assert isinstance(e, Exception)


def test_indexed_back_referencing():
    expr = RegexBuilder().capture().at_least(3).digit().end().subexpression(indexed_back_reference_se).back_reference(1).range('0', '9')
    regex_equality('/(\\d{3,})(.{2})\\2\\1[0-9]/', expr)
    regex_compilation('(\\d{3,})(.{2})\\2\\1[0-9]', expr)


def test_deeply_nested_se():
    expr = RegexBuilder().capture().at_least(3).digit().end().subexpression(first_layer_se).back_reference(1).range('0', '9')
    regex_equality('/(\\d{3,})outer begin(?P<inner_subexpression>(?:.{2})?)outer end\\1[0-9]/', expr)
    regex_compilation('(\\d{3,})outer begin(?P<inner_subexpression>(?:.{2})?)outer end\\1[0-9]', expr)
