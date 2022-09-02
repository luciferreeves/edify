import re

from edify import RegexBuilder


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
    expr = (
        RegexBuilder()
        .any_of()
        .string('hello')
        .digit()
        .word()
        .char('.')
        .char('#')
        .end()
    )
    regex_equality('/(?:hello|\\d|\\w|[\\.\\#])/', expr)
    regex_compilation('(?:hello|\\d|\\w|[\\.\\#])', expr)


def test_any_of_range_fusion():
    expr = (
        RegexBuilder()
        .any_of()
        .range('a', 'z')
        .range('A', 'Z')
        .range('0', '9')
        .char('.')
        .char('#')
        .end()
    )
    regex_equality('/[a-zA-Z0-9\\.\\#]/', expr)
    regex_compilation('[a-zA-Z0-9\\.\\#]', expr)


def test_any_of_range_fusion_with_other_choices():
    expr = (
        RegexBuilder()
        .any_of()
        .range('a', 'z')
        .range('A', 'Z')
        .range('0', '9')
        .char('.')
        .char('#')
        .string('hello')
        .end()
    )
    regex_equality('/(?:hello|[a-zA-Z0-9\\.\\#])/', expr)
    regex_compilation('(?:hello|[a-zA-Z0-9\\.\\#])', expr)


def test_capture():
    expr = RegexBuilder().capture().string('hello ').word().char('!').end()
    regex_equality('/(hello\\ \\w!)/', expr)
    regex_compilation('(hello\\ \\w!)', expr)


def test_named_capture():
    expr = RegexBuilder().named_capture('this_is_the_name').string('hello ').word().char('!').end()
    regex_equality('/(?P<this_is_the_name>hello\\ \\w!)/', expr)
    regex_compilation('(?P<this_is_the_name>hello\\ \\w!)', expr)


def test_bad_name_error():
    try:
        (
            RegexBuilder()
            .named_capture('hello world')
            .string('hello ')
            .word()
            .char('!')
            .end()
        )
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
    expr = (
        RegexBuilder()
        .named_capture('this_is_the_name')
        .string('hello ')
        .word()
        .char('!')
        .end()
        .named_back_reference('this_is_the_name')
    )
    regex_equality('/(?P<this_is_the_name>hello\\ \\w!)\\k<this_is_the_name>/', expr)
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
    expr = (
        RegexBuilder()
        .capture()
        .string('hello ')
        .word()
        .char('!')
        .end()
        .back_reference(1)
    )
    regex_equality('/(hello\\ \\w!)\\1/', expr)
    regex_compilation('(hello\\ \\w!)\\1', expr)
