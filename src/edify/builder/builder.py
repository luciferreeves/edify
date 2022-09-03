import re
from copy import deepcopy as clone

from .errors import can_not_call_se
from .errors import can_not_end_while_building_root_exp
from .errors import cannot_create_duplicate_named_group
from .errors import cannot_define_start_after_end
from .errors import end_input_already_defined
from .errors import ignore_se
from .errors import invalid_total_capture_groups_index
from .errors import must_be_a_string
from .errors import must_be_instance
from .errors import must_be_integer_greater_than_zero
from .errors import must_be_one_character
from .errors import must_be_positive_integer
from .errors import must_be_single_character
from .errors import must_have_a_smaller_value
from .errors import name_not_valid
from .errors import named_group_does_not_exist
from .errors import start_input_already_defined
# from .helpers.core import deep_copy
# from .errors import unable_to_quantify
from .helpers.core import apply_subexpression_defaults
from .helpers.core import assertion
from .helpers.core import create_stack_frame
from .helpers.core import escape_special
from .helpers.core import fuse_elements
from .helpers.quantifiers import quantifier_table
from .helpers.regex_vars import named_group_regex
from .helpers.t import t


class RegexBuilder:
    """Regular Expression Builder Class."""

    state = {}

    def __init__(self):
        self.state = {
            'has_defined_start': False,
            'has_defined_end': False,
            'flags': {
                'A': False,
                'D': False,
                'I': False,
                'M': False,
                'S': False,
                'X': False,
            },
            'stack': [create_stack_frame(t['root'])],
            'named_groups': [],
            'total_capture_groups': 0,
        }

    def ascii_only(self):
        next = clone(self)
        next.state['flags']['A'] = True
        return next

    def debug(self):
        next = clone(self)
        next.state['flags']['D'] = True
        return next

    def ignore_case(self):
        next = clone(self)
        next.state['flags']['I'] = True
        return next

    def multi_line(self):
        next = clone(self)
        next.state['flags']['M'] = True
        return next

    def dot_all(self):
        next = clone(self)
        next.state['flags']['S'] = True
        return next

    def verbose(self):
        next = clone(self)
        next.state['flags']['X'] = True
        return next

    def get_current_frame(self):
        return self.state['stack'][len(self.state['stack']) - 1]

    def get_current_element_array(self):
        return self.get_current_frame()['elements']

    def match_element(self, type_fn):
        next = clone(self)
        next.get_current_element_array().append(next.apply_quantifier(type_fn))
        return next

    def apply_quantifier(self, element):
        current_frame = self.get_current_frame()
        if current_frame['quantifier'] is not None:
            wrapped = current_frame['quantifier']['value'](element)
            current_frame['quantifier'] = None
            return wrapped
        return element

    def frame_creating_element(self, type_fn):
        next = clone(self)
        new_frame = create_stack_frame(type_fn)
        next.state['stack'].append(new_frame)
        return next

    def tracked_named_group(self, name):
        assertion(type(name) is str, must_be_a_string("Name", type(name)))
        assertion(len(name) > 0, must_be_one_character("Name"))
        assertion(name not in self.state['named_groups'], cannot_create_duplicate_named_group(name))
        assertion(re.compile(named_group_regex, re.I).match(name), name_not_valid(name))
        self.state['named_groups'].append(name)

    def capture(self):
        next = clone(self)
        new_frame = create_stack_frame(t['capture'])
        next.state['stack'].append(new_frame)
        next.state['total_capture_groups'] += 1
        return next

    def named_capture(self, name):
        next = clone(self)
        new_frame = create_stack_frame(t['named_capture'](name))
        next.tracked_named_group(name)
        next.state['stack'].append(new_frame)
        next.state['total_capture_groups'] += 1
        return next

    def quantifier_element(self, type_fn):
        next = clone(self)
        current_frame = next.get_current_frame()
        # if current_frame['quantifier'] is not None:
        #     raise Exception(unable_to_quantify(type_fn, current_frame['quantifier']['type']))
        current_frame['quantifier'] = t[type_fn]
        return next

    def any_char(self):
        return self.match_element(t['any_char'])

    def whitespace_char(self):
        return self.match_element(t['whitespace_char'])

    def non_whitespace_char(self):
        return self.match_element(t['non_whitespace_char'])

    def digit(self):
        return self.match_element(t['digit'])

    def non_digit(self):
        return self.match_element(t['non_digit'])

    def word(self):
        return self.match_element(t['word'])

    def non_word(self):
        return self.match_element(t['non_word'])

    def word_boundary(self):
        return self.match_element(t['word_boundary'])

    def non_word_boundary(self):
        return self.match_element(t['non_word_boundary'])

    def new_line(self):
        return self.match_element(t['new_line'])

    def carriage_return(self):
        return self.match_element(t['carriage_return'])

    def tab(self):
        return self.match_element(t['tab'])

    def null_byte(self):
        return self.match_element(t['null_byte'])

    def named_back_reference(self, name):
        assertion(name in self.state['named_groups'], named_group_does_not_exist(name))
        return self.match_element(t['named_back_reference'](name))

    def back_reference(self, index: int):
        assertion(type(index) is int, 'Index must be an integer.')
        assertion(
            index > 0 and index <= self.state['total_capture_groups'],
            invalid_total_capture_groups_index(index, self.state['total_capture_groups']),
        )
        return self.match_element(t['back_reference'](index))

    def any_of(self):
        return self.frame_creating_element(t['any_of'])

    def group(self):
        return self.frame_creating_element(t['group'])

    def assert_ahead(self):
        return self.frame_creating_element(t['assert_ahead'])

    def assert_not_ahead(self):
        return self.frame_creating_element(t['assert_not_ahead'])

    def assert_behind(self):
        return self.frame_creating_element(t['assert_behind'])

    def assert_not_behind(self):
        return self.frame_creating_element(t['assert_not_behind'])

    def optional(self):
        return self.quantifier_element('optional')

    def zero_or_more(self):
        return self.quantifier_element('zero_or_more')

    def zero_or_more_lazy(self):
        return self.quantifier_element('zero_or_more_lazy')

    def one_or_more(self):
        return self.quantifier_element('one_or_more')

    def one_or_more_lazy(self):
        return self.quantifier_element('one_or_more_lazy')

    def exactly(self, count):
        assertion(type(count) is int and count > 0, must_be_positive_integer('count'))
        current_frame = self.get_current_frame()
        # if current_frame['quantifier'] is not None:
        #     raise Exception(unable_to_quantify("exactly", current_frame['quantifier']['type']))
        current_frame['quantifier'] = t['exactly'](count)
        return self

    def at_least(self, count):
        assertion(type(count) is int and count > 0, must_be_positive_integer('count'))
        next = clone(self)
        current_frame = next.get_current_frame()
        # if current_frame['quantifier'] is not None:
        #     raise Exception(unable_to_quantify("at_least", current_frame['quantifier']['type']))
        current_frame['quantifier'] = t['at_least'](count)
        return next

    def between(self, x, y):
        assertion(type(x) is int and x >= 0, must_be_integer_greater_than_zero('x'))
        assertion(type(y) is int and y > 0, must_be_positive_integer('y'))
        assertion(x < y, 'X must be less than Y.')
        next = clone(self)
        current_frame = next.get_current_frame()
        # if current_frame['quantifier'] is not None:
        #     raise Exception(unable_to_quantify("between", current_frame['quantifier']['type']))
        current_frame['quantifier'] = t['between'](x, y)
        return next

    def between_lazy(self, x, y):
        assertion(type(x) is int and x >= 0, must_be_integer_greater_than_zero('x'))
        assertion(type(y) is int and y > 0, must_be_positive_integer('y'))
        assertion(x < y, 'X must be less than Y.')
        next = clone(self)
        current_frame = next.get_current_frame()
        # if current_frame['quantifier'] is not None:
        #     raise Exception(unable_to_quantify("between_lazy", current_frame['quantifier']['type']))
        current_frame['quantifier'] = t['between_lazy'](x, y)
        return next

    def start_of_input(self):
        assertion(self.state['has_defined_start'] is False, start_input_already_defined())
        assertion(self.state['has_defined_end'] is False, cannot_define_start_after_end())
        next = clone(self)
        next.state['has_defined_start'] = True
        next.get_current_element_array().append(t['start_of_input'])
        return next

    def end_of_input(self):
        assertion(self.state['has_defined_end'] is False, end_input_already_defined())
        next = clone(self)
        next.state['has_defined_end'] = True
        next.get_current_element_array().append(t['end_of_input'])
        return next

    def any_of_chars(self, chars):
        next = clone(self)
        element_value = t['any_of_chars'](escape_special(chars))
        current_frame = next.get_current_frame()
        current_frame['elements'].append(next.apply_quantifier(element_value))
        return next

    def end(self):
        assertion(len(self.state['stack']) > 1, can_not_end_while_building_root_exp())
        next = clone(self)
        old_frame = next.state['stack'].pop()
        current_frame = next.get_current_frame()
        current_frame['elements'].append(next.apply_quantifier(old_frame['type']['value'](old_frame['elements'])))
        return next

    def anything_but_string(self, string):
        assertion(type(string) is str, must_be_a_string('Value', string))
        assertion(len(string) > 0, must_be_one_character('Value'))
        next = clone(self)
        element_value = t['anything_but_string'](escape_special(string))
        current_frame = next.get_current_frame()
        current_frame['elements'].append(next.apply_quantifier(element_value))
        return next

    def anything_but_chars(self, chars):
        assertion(type(chars) is str, must_be_a_string('Value', chars))
        assertion(len(chars) > 0, must_be_one_character('Value'))
        next = clone(self)
        element_value = t['anything_but_chars'](escape_special(chars))
        current_frame = next.get_current_frame()
        current_frame['elements'].append(next.apply_quantifier(element_value))
        return next

    def anything_but_range(self, a, b):
        str_a = str(a)
        str_b = str(b)
        assertion(len(str_a) == 1, must_be_single_character('a', str_a))
        assertion(len(str_b) == 1, must_be_single_character('b', str_b))
        assertion(ord(str_a) < ord(str_b), must_have_a_smaller_value(str_a, str_b))
        next = clone(self)
        element_value = t['anything_but_range']([a, b])
        current_frame = next.get_current_frame()
        current_frame['elements'].append(next.apply_quantifier(element_value))
        return next

    def string(self, s):
        assertion(type(s) is str, must_be_a_string('Value', s))
        assertion(len(s) > 0, must_be_one_character('Value'))
        next = clone(self)
        element_value = t['string'](escape_special(s)) if len(s) > 1 else t['char'](escape_special(s))
        current_frame = next.get_current_frame()
        current_frame['elements'].append(next.apply_quantifier(element_value))
        return next

    def char(self, c):
        assertion(type(c) is str, must_be_a_string('Value', c))
        assertion(len(c) == 1, must_be_single_character('Value', c))
        next = clone(self)
        element_value = t['char'](escape_special(c))
        current_frame = next.get_current_frame()
        current_frame['elements'].append(next.apply_quantifier(element_value))
        return next

    def range(self, a, b):
        str_a = str(a)
        str_b = str(b)
        assertion(len(str_a) == 1, must_be_single_character('a', str_a))
        assertion(len(str_b) == 1, must_be_single_character('b', str_b))
        assertion(ord(str_a) < ord(str_b), must_have_a_smaller_value(str_a, str_b))
        next = clone(self)
        element_value = t['range']([a, b])
        current_frame = next.get_current_frame()
        current_frame['elements'].append(next.apply_quantifier(element_value))
        return next

    def merge_subexpression(self, el, options, parent, increment_capture_groups):
        next_el = clone(el)

        if next_el['type'] == 'back_reference':
            next_el['index'] += parent.state['total_capture_groups']
        if next_el['type'] == 'capture':
            increment_capture_groups()
        if next_el['type'] == 'named_capture':
            group_name = '{}{}'.format(options['namespace'], next_el['name']) if options['namespace'] else next_el['name']
            # parent.tracked_named_group(group_name)
            next_el['name'] = group_name
        if next_el['type'] == 'named_back_reference':
            next_el['name'] = '{}{}'.format(options['namespace'], next_el['name']) if options['namespace'] else next_el['name']
        if 'contains_child' in next_el:
            next_el['value'] = self.merge_subexpression(next_el['value'], options, parent, increment_capture_groups)
        elif 'contains_children' in next_el:
            next_el['value'] = list(map(lambda e: self.merge_subexpression(e, options, parent, increment_capture_groups), next_el['value']))
        if next_el['type'] == 'start_of_input':
            if options['ignore_start_and_end']:
                return t['noop']
            assertion(parent.state['has_defined_start'] is False, str(start_input_already_defined()) + " " + str(ignore_se()))
            # assertion(parent.state['has_defined_end'] is False, str(end_input_already_defined()) + " " + str(ignore_se()))
            # parent.state['has_defined_start'] = True
        if next_el['type'] == 'end_of_input':
            if options['ignore_start_and_end']:
                return t['noop']
            assertion(parent.state['has_defined_end'] is False, str(end_input_already_defined()) + str(ignore_se()))
            # parent.state['has_defined_end'] = True
        return next_el

    def subexpression(self, expr, opts={}):
        assertion(isinstance(expr, RegexBuilder), must_be_instance("Expression", expr, "RegexBuilder"))
        assertion(len(expr.state['stack']) == 1, can_not_call_se(expr.get_current_frame()['type']['type']))
        options = apply_subexpression_defaults(opts)
        expr_next = clone(expr)
        next = clone(self)
        additional_capture_groups = 0
        expr_frame = expr_next.get_current_frame()

        def increment_capture_groups():
            nonlocal additional_capture_groups
            additional_capture_groups += 1

        expr_frame['elements'] = list(
            map(lambda e: self.merge_subexpression(e, options, expr_next, increment_capture_groups), expr_frame['elements'])
        )
        next.state['total_capture_groups'] += additional_capture_groups
        if not options['ignore_flags']:
            for flag_name, enabled in expr_next.state['flags'].items():
                next.state['flags'][flag_name] = enabled or next.state['flags'][flag_name]
        current_frame = next.get_current_frame()
        current_frame['elements'].append(next.apply_quantifier(t['subexpression'](expr_frame['elements'])))
        return next

    def evaluate(self, el):
        if el['type'] == 'noop':
            return ''
        if el['type'] == 'any_char':
            return '.'
        if el['type'] == 'whitespace_char':
            return '\\s'
        if el['type'] == 'non_whitespace_char':
            return '\\S'
        if el['type'] == 'digit':
            return '\\d'
        if el['type'] == 'non_digit':
            return '\\D'
        if el['type'] == 'word':
            return '\\w'
        if el['type'] == 'non_word':
            return '\\W'
        if el['type'] == 'word_boundary':
            return '\\b'
        if el['type'] == 'non_word_boundary':
            return '\\B'
        if el['type'] == 'start_of_input':
            return '^'
        if el['type'] == 'end_of_input':
            return '$'
        if el['type'] == 'new_line':
            return '\\n'
        if el['type'] == 'carriage_return':
            return '\\r'
        if el['type'] == 'tab':
            return '\\t'
        if el['type'] == 'null_byte':
            return '\\0'
        if el['type'] == 'string':
            return el['value']
        if el['type'] == 'char':
            return el['value']
        if el['type'] == 'range':
            return '[{}-{}]'.format(el['value'][0], el['value'][1])
        if el['type'] == 'anything_but_range':
            return '[^{}-{}]'.format(el['value'][0], el['value'][1])
        if el['type'] == 'any_of_chars':
            return '[' + ''.join(el['value']) + ']'
        if el['type'] == 'anything_but_chars':
            return '[^' + ''.join(el['value']) + ']'
        if el['type'] == 'named_back_reference':
            return '\\k<{}>'.format(el['name'])
        if el['type'] == 'back_reference':
            return '\\{}'.format(el['index'])
        if el['type'] == 'subexpression':
            return ''.join(map(lambda e: self.evaluate(e), el['value']))
        cg1 = ['optional', 'zero_or_more', 'zero_or_more_lazy', 'one_or_more', 'one_or_more_lazy']
        if el['type'] in cg1:
            inner = self.evaluate(el['value'])
            with_group = "(?:{})".format(inner) if 'quantifiers_require_group' in el['value'] else inner
            symbol = quantifier_table[el['type']]
            return '{}{}'.format(with_group, symbol)
        cg2 = ['between', 'between_lazy', 'at_least', 'exactly']
        if el['type'] in cg2:
            inner = self.evaluate(el['value'])
            with_group = "(?:{})".format(inner) if 'quantifiers_require_group' in el['value'] else inner
            return '{}{}'.format(with_group, quantifier_table[el['type']](el['times']))
        if el['type'] == 'anything_but_string':
            chars = ''.join(map(lambda c: '[^{}]'.format(c), el['value']))
            return '(?:{})'.format(chars)
        if el['type'] == 'assert_ahead':
            evaluated = ''.join(map(lambda e: self.evaluate(e), el['value']))
            return '(?={})'.format(evaluated)
        if el['type'] == 'assert_behind':
            evaluated = ''.join(map(lambda e: self.evaluate(e), el['value']))
            return '(?<={})'.format(evaluated)
        if el['type'] == 'assert_not_ahead':
            evaluated = ''.join(map(lambda e: self.evaluate(e), el['value']))
            return '(?!{})'.format(evaluated)
        if el['type'] == 'assert_not_behind':
            evaluated = ''.join(map(lambda e: self.evaluate(e), el['value']))
            return '(?<!{})'.format(evaluated)
        if el['type'] == 'any_of':
            [fused, rest] = fuse_elements(el['value'])
            if len(rest) == 0:
                return '[{}]'.format(fused)
            evaluated_rest = list(map(lambda e: self.evaluate(e), rest))
            separator = '|' if len(evaluated_rest) > 0 and len(fused) > 0 else ''
            return '(?:{}{}{})'.format('|'.join(evaluated_rest), separator, '[{}]'.format(fused) if fused else '')
        if el['type'] == 'capture':
            evaluated = ''.join(map(lambda e: self.evaluate(e), el['value']))
            return '({})'.format(evaluated)
        if el['type'] == 'named_capture':
            evaluated = ''.join(map(lambda e: self.evaluate(e), el['value']))
            return '(?P<{}>{})'.format(el['name'], evaluated)
        if el['type'] == 'group':
            evaluated = ''.join(map(lambda e: self.evaluate(e), el['value']))
            return '(?:{})'.format(evaluated)

        raise Exception('Can not process unsupported element type: {}'.format(el['type']))  # pragma: no cover

    def get_regex_patterns_and_flags(self):
        assertion(len(self.state['stack']) == 1, can_not_call_se(self.get_current_frame()['type']['type']))
        pattern = "".join(list(map(lambda e: self.evaluate(e), self.get_current_element_array())))
        flags = ""
        for flag_name, enabled in self.state['flags'].items():
            if enabled:
                flags += flag_name
        pattern = "(?:)" if pattern == "" else pattern
        flags = "".join(sorted(flags))
        return pattern, flags

    def to_regex_string(self):
        patterns, flags = self.get_regex_patterns_and_flags()
        return '/{}/{}'.format(str(patterns.replace('\\ ', ' ')), str(flags))

    def to_regex(self):
        patterns, flags = self.get_regex_patterns_and_flags()
        patterns = r"{}".format(patterns.replace("\\ ", ' '))
        flag = 0
        if flags != '':
            for flag_name in flags:
                if flag_name == 'D':
                    flag |= getattr(re, 'DEBUG')
                else:
                    flag |= getattr(re, flag_name)

        try:
            return re.compile(patterns, flags=flag)
        except Exception as e:
            raise Exception('Can not compile regex: {}'.format(e))
