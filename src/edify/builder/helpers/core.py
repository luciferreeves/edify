import re
def as_type(type, options={}):
    def as_type_fn(value=None):
        return {
            'type': type,
            'value': value,
            'options': options,
        }
    return as_type_fn


def deferred_type(type, options = {}):
    type_fn = as_type(type, options)
    return type_fn(type_fn)


def create_stack_frame(type):
    return {
        'type': type,
        'quantifier': None,
        'elements': [],
    }


def assertion(condition, message):
    if not condition:
        raise Exception(message)

# const escapeSpecial = s => specialChars.reduce((acc, char) => replaceAll(acc, char, `\\${char}`), s);
def escape_special(s):
    return re.escape(s)


