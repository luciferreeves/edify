import re
from sys import _current_frames
from .helpers.core import create_stack_frame, assertion, escape_special
from .helpers.t import t
from .helpers.regex_vars import named_group_regex
from .errors import *

class RegexBuilder:
    """Regular Expression Builder Class.
    """

    state = {}


    def __init__(self):
        self.state = {
            'has_defined_start': False,
            'has_defined_end': False,
            'flags': {
                'g': False,
                'y': False,
                'm': False,
                'i': False,
                'u': False,
                's': False,
            },
            'stack': create_stack_frame(t['root']),
            'named_groups': [],
            'total_capture_groups': 0,
        }


    def allow_multiple_matches(self):
        self.state['stack']['flags']['g'] = True


    def sticky(self):
        self.state['stack']['flags']['y'] = True


    def line_by_line(self):
        self.state['stack']['flags']['m'] = True


    def case_insensitive(self):
        self.state['stack']['flags']['i'] = True


    def unicode(self):
        self.state['stack']['flags']['u'] = True


    def single_line(self):
        self.state['stack']['flags']['s'] = True


    def get_current_frame(self):
        return self.state['stack']


    def get_current_element_array(self):
        return self.get_current_frame()['elements']


    def match_element(self, type_fn):
        current_element_array = self.get_current_element_array()
        current_element_array.append(self.apply_quantifier(type_fn))
        return self


    def apply_quantifier(self, element):
        current_frame = self.get_current_frame()
        if current_frame['quantifier'] is not None:
            wrapped = current_frame['quantifier']['value'](element)
            current_frame['quantifier'] = None
            return wrapped
        return element


    def frame_creating_element(self, type_fn):
        new_frame = create_stack_frame(type_fn)
        self.state['stack'] = new_frame
        return self


    def tracked_named_group(self, name):
        assertion(type(name) is str, must_be_a_string("Name", type(name)))
        assertion(len(name) > 0, must_be_one_character("Name"))
        assertion(name not in self.state['named_groups'], cannot_create_duplicate_named_group(name))
        assertion(re.compile(named_group_regex, re.I).match(name), name_not_valid(name))
        self.state['named_groups'].append(name)


    def capture(self):
        new_frame = create_stack_frame(t['capture'])
        self.state['stack'] = new_frame
        self.state['total_capture_groups'] += 1
        return self


    def named_capture(self, name):
        new_frame = create_stack_frame(t['named_capture'](name))
        self.tracked_named_group(name)
        self.state['stack'] = new_frame
        self.state['total_capture_groups'] += 1
        return self


    def quantifier_element(self, type_fn):
        current_frame = self.get_current_frame()
        if current_frame['quantifier'] is not None:
            raise Exception(unable_to_quantify(type_fn, current_frame['quantifier']['type']))
        current_frame['quantifier'] = t[type_fn]
        return self


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
            invalid_total_capture_groups_index(index, self.state['total_capture_groups'])
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
        if current_frame['quantifier'] is not None:
            raise Exception(unable_to_quantify("exactly", current_frame['quantifier']['type']))
        current_frame['quantifier'] = t['exactly'](count)
        return self


    def at_least(self, count):
        assertion(type(count) is int and count > 0, must_be_positive_integer('count'))
        current_frame = self.get_current_frame()
        if current_frame['quantifier'] is not None:
            raise Exception(unable_to_quantify("at_least", current_frame['quantifier']['type']))
        current_frame['quantifier'] = t['at_least'](count)
        return self


    def between(self, x, y):
        assertion(type(x) is int and x >= 0, must_be_integer_greater_than_zero('x'))
        assertion(type(y) is int and y > 0, must_be_positive_integer('y'))
        assertion(x < y, 'X must be less than Y.')
        current_frame = self.get_current_frame()
        if current_frame['quantifier'] is not None:
            raise Exception(unable_to_quantify("between", current_frame['quantifier']['type']))
        current_frame['quantifier'] = t['between'](x, y)
        return self


    def between_lazy(self, x, y):
        assertion(type(x) is int and x >= 0, must_be_integer_greater_than_zero('x'))
        assertion(type(y) is int and y > 0, must_be_positive_integer('y'))
        assertion(x < y, 'X must be less than Y.')
        current_frame = self.get_current_frame()
        if current_frame['quantifier'] is not None:
            raise Exception(unable_to_quantify("between_lazy", current_frame['quantifier']['type']))
        current_frame['quantifier'] = t['between_lazy'](x, y)
        return self

    def start_of_input(self):
        assertion(self.state['has_defined_start'] is False, start_input_already_defined())
        assertion(self.state['has_defined_end'] is False, cannot_define_start_after_end())
        self.state['has_defined_start'] = True
        current_element_array = self.get_current_element_array()
        current_element_array.append(t['start_of_input'])
        return self


    def end_of_input(self):
        assertion(self.state['has_defined_end'] is False, end_input_already_defined())
        self.state['has_defined_end'] = True
        current_element_array = self.get_current_element_array()
        current_element_array.append(t['end_of_input'])
        return self


    def any_of_chars(self, chars):
        element_value = t['any_of_chars'](escape_special(chars))
        current_frame = self.get_current_frame()
        current_frame['elements'].append(self.apply_quantifier(element_value))
        return self

    def end(self):
        assertion(len(self.state['stack']) > 1, can_not_end_while_building_root_exp())
        old_frame = self.state['stack'].pop()
        current_frame = self.get_current_frame()
        current_frame['elements'].append(self.apply_quantifier(old_frame['type']['value'](old_frame['elements'])))
        return self


