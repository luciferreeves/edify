def must_be_a_string(value, variable_name):
    return '{} must be a string. (got {})'.format(value, type(variable_name))


def must_be_one_character(variable_name):
    return '{} must be one character long.'.format(variable_name)


def cannot_create_duplicate_named_group(name):
    return 'Can not create duplicate named group "{}".'.format(name)


def name_not_valid(name):
    return 'Name {} is not valid. (only alphanumeric characters and underscores are allowed)'.format(name)


def named_group_does_not_exist(name):
    return 'Named group "{}" does not exist (create one with .named_capture()).'.format(name)


def invalid_total_capture_groups_index(index, total_capture_groups):
    return 'Invalid index #{}. There are only {} capture groups.'.format(index, total_capture_groups)


def must_be_positive_integer(variable_name):
    return '{} must be a positive integer.'.format(variable_name)


def must_be_integer_greater_than_zero(variable_name):
    return '{} must be an integer greater than zero.'.format(variable_name)


# def unable_to_quantify(quantifier, type):
#     return 'Can not quantify regular expression with {}, because it has already been quantified with {}.'.format(quantifier, type)


def start_input_already_defined():
    return 'Regex already has a start of input.'


def cannot_define_start_after_end():
    return 'Can not define a start of input after defining an end of input.'


def end_input_already_defined():
    return 'Regex already has an end of input.'


def can_not_end_while_building_root_exp():
    return 'Can not end while building the root expression.'


def must_be_single_character(value, variable_name):
    return '{} must be a single character. (got {})'.format(value, type(variable_name))


def must_have_a_smaller_value(a, b):
    return '{} must have a smaller character value than {}. (a = {}, b = {})'.format(a, b, ord(a), ord(b))


def ignore_se():
    return 'You can ignore a subexpressions start_of_input/end_of_input markers with the ignore_start_and_end option'


def must_be_instance(value, variable_name, class_name):
    return '{} must be an instance of {}. (got {})'.format(value, class_name, type(variable_name))


def can_not_call_se(cft):
    return "Can not call subexpression a not yet fully specified regex object. \
        \n (Try adding a .end() call to match the {} on the subexpression)".format(
        cft
    )
