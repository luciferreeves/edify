RegexBuilder
============

RegexBuilder is a class that helps you build regular expressions. It is based on the `SuperExpressive <https://github.com/francisrstokes/super-expressive>`_ library. The API uses the `fluent builder pattern <https://en.wikipedia.org/wiki/Fluent_interface>`_, and is completely immutable. It is built to be discoverable and predictable.

- Properties and methods describe what they do in plain English.
- Order matters! Quantifiers are specified before the thing they change, just like in English (e.g. ``RegexBuilder().exactly(5).digit()``.)
- If you make a mistake, you'll know how to fix it. Edify will guide you towards a fix if your expression is invalid.
- ``subexpressions`` can be used to create meaningful, reusable components.

.any_char()
-----------

``.any_char()`` matches any single character.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('.')
    expr = RegexBuilder().any_char().to_regex()
    assert expr.match('a') # Matches
    assert expr.match('hello') # Matches


.whitespace_char()
------------------

``.whitespace_char()`` matches any whitespace character, including the special whitespace characters: ``\r\n\t\f\v``.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\s')
    expr = RegexBuilder().whitespace_char().to_regex()
    assert expr.match(' ') # Matches
    assert expr.match('\n') # Matches
    assert expr.match('\t') # Matches
    assert expr.match('\r') # Matches
    assert expr.match('\f') # Matches
    assert expr.match('\v') # Matches
    assert not expr.match('a') # Doesn't match
    assert not expr.match('hello') # Doesn't match


.non_whitespace_char()
----------------------

``.non_whitespace_char()`` matches any non-whitespace character, excluding also the special whitespace characters: ``\r\n\t\f\v``.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\S')
    expr = RegexBuilder().non_whitespace_char().to_regex()
    assert expr.match('a') # Matches
    assert expr.match('hello') # Matches
    assert not expr.match(' ') # Doesn't match
    assert not expr.match('\n') # Doesn't match
    assert not expr.match('\t') # Doesn't match
    assert not expr.match('\r') # Doesn't match
    assert not expr.match('\f') # Doesn't match
    assert not expr.match('\v') # Doesn't match
    assert not expr.match('\u00a0') # Doesn't match
    assert not expr.match('\u2000') # Doesn't match


.digit()
--------

``.digit()`` matches any digit from ``0-9``.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\d')
    expr = RegexBuilder().digit().to_regex()
    assert expr.match('1') # Matches
    assert expr.match('9') # Matches
    assert not expr.match('a') # Doesn't match
    assert not expr.match('\u00a0') # Doesn't match


.non_digit()
-------------

``.non_digit()`` matches any non-digit.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\D')
    expr = RegexBuilder().non_digit().to_regex()
    assert expr.match('a') # Matches
    assert expr.match('\u00a0') # Matches
    assert not expr.match('1') # Doesn't match
    assert not expr.match('9') # Doesn't match

.. _word:

.word()
-------


``.word()`` matches any alpha-numeric ``(a-z, A-Z, 0-9)`` characters, as well as ``_``.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\w')
    expr = RegexBuilder().word().to_regex()
    assert expr.match('a') # Matches
    assert expr.match('1') # Matches
    assert expr.match('_') # Matches
    assert expr.match('hello') # Matches


.non_word()
-----------

``.non_word()`` matches any non-alpha-numeric ``(a-z, A-Z, 0-9)`` characters, excluding ``_`` as well.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\W')
    expr = RegexBuilder().non_word().to_regex()
    assert not expr.match('a') # Doesn't match
    assert not expr.match('1') # Doesn't match
    assert expr.match('\u00a0') # Matches
    assert expr.match('\u2000') # Matches
    assert not expr.match('_') # Doesn't match
    assert not expr.match('hello') # Doesn't match


.word_boundary()
-----------------

``.word_boundary()`` matches (without consuming any characters) immediately between a character matched by :ref:`word` and a character not matched by :ref:`word` (in either order).

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\d\b')
    expr = RegexBuilder().digit().word_boundary().to_regex()


.non_word_boundary()
--------------------

``.non_word_boundary()`` matches (without consuming any characters) at the position between two characters matched by :ref:`word`.

.. code-block:: python


    from edify import RegexBuilder

    # returns re.compile('\d\B')
    expr = RegexBuilder().digit().non_word_boundary().to_regex()

.new_line()
-----------

``.new_line()`` matches the newline ``\n`` character.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\n')
    expr = RegexBuilder().new_line().to_regex()
    assert expr.match('\n') # Matches
    assert not expr.match('a') # Doesn't match
    assert not expr.match('hello') # Doesn't match

.carriage_return()
-------------------

``.carriage_return()`` matches the carriage return ``\r`` character.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\r')
    expr = RegexBuilder().carriage_return().to_regex()
    assert expr.match('\r') # Matches
    assert not expr.match('a') # Doesn't match
    assert not expr.match('hello') # Doesn't match


.tab()
------

``.tab()`` matches the tab ``\t`` character.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\t')
    expr = RegexBuilder().tab().to_regex()
    assert expr.match('\t') # Matches
    assert not expr.match('a') # Doesn't match
    assert not expr.match('hello') # Doesn't match


.null_byte()
------------

``.null_byte()`` matches the null byte ``\0`` character.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\0')
    expr = RegexBuilder().null_byte().to_regex()
    assert expr.match('\0') # Matches
    assert not expr.match('a') # Doesn't match
    assert not expr.match('hello') # Doesn't match

.. _any_of:

.any_of()
---------

``.any_of()`` matches a choice between specified elements. Needs to be finalised with :ref:`end`.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('(?:hello|[a-f0-9])')
    expr = (
        RegexBuilder()
        .any_of()
            .range('a', 'f')
            .range('0', '9')
            .string('hello')
        .end()
        .to_regex()
    )
    assert expr.match('a') # Matches
    assert expr.match('f') # Matches
    assert expr.match('9') # Matches
    assert expr.match('hello') # Matches
    assert not expr.match('g') # Doesn't match
    assert not expr.match('good world') # Doesn't match

.. _capture:

.capture()
-----------

``.capture()`` creates a capture group for the proceeding elements. Needs to be finalised with :ref:`end`. Can be later referenced with :ref:`backreference`.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('([a-f][0-9]hello)')
    expr = (
        RegexBuilder()
        .capture()
            .range('a', 'f')
            .range('0', '9')
            .string('hello')
        .end()
        .to_regex()
    )
    assert expr.match('a9hello') # Matches
    assert expr.match('f0hello') # Matches
    assert not expr.match('g9hello') # Doesn't match

.. _named_capture:

.named_capture(name)
--------------------

``.named_capture()`` creates a named capture group for the proceeding elements. Needs to be finalised with :ref:`end`. Can be later referenced with :ref:`named_back_reference` or :ref:`backreference`.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('(?P<interestingStuff>[a-f][0-9]hello)')
    expr = (
        RegexBuilder()
        .named_capture('interestingStuff')
            .range('a', 'f')
            .range('0', '9')
            .string('hello')
        .end()
        .to_regex()
    )
    assert expr.match('a9hello') # Matches
    assert expr.match('f0hello') # Matches
    assert not expr.match('g9hello') # Doesn't match

.. _named_back_reference:

.named_back_reference(name)
---------------------------

``.named_back_reference()`` matches exactly what was previously matched by a :ref:`named_capture`.

.. warning::

    Python does not support named back references. If you try to call the ``to_regex()`` method on a named back reference, it will raise an exception. For, those reasons, ``to_regex_string()`` is provided instead. It returns a string that can be used to create a regular expression. You can try using the regular expression directly with another library like `regex <https://pypi.python.org/pypi/regex>`_.

.. code-block:: python

    from edify import RegexBuilder

    # returns /(?<interestingStuff>[a-f][0-9]hello)something else\k<interestingStuff>/
    expr = (
        RegexBuilder()
        .named_capture('interestingStuff')
            .range('a', 'f')
            .range('0', '9')
            .string('hello')
        .end()
        .string('something else')
        .named_back_reference('interestingStuff')
        .to_regex_string()
    )

.. _backreference:

.back_reference(index)
----------------------

``.back_reference()`` matches exactly what was previously matched by a :ref:`capture` or :ref:`named_capture` using a positional index. Note regex indexes start at 1, so the first capture group has index 1.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('([a-f][0-9]hello)\\1')
    expr = (
        RegexBuilder()
        .capture()
            .range('a', 'f')
            .range('0', '9')
            .string('hello')
        .end()
        .back_reference(1)
        .to_regex()
    )
    assert expr.match('a9helloa9hello') # Matches
    assert not expr.match('a9helloa9hell') # Doesn't match

.. _group:

.group()
--------

``.group()`` creates a non-capturing group for the proceeding elements. Needs to be finalised with :ref:`end`.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('(?:[a-f][0-9]hello)?')
    expr = (
        RegexBuilder()
        .optional().group()
            .range('a', 'f')
            .range('0', '9')
            .string('hello')
        .end()
        .to_regex()
    )
    assert expr.match('a9hello') # Matches
    assert expr.match('') # Matches
    assert not expr.match('g9hello') # Matches

.. _end:

.end()
------

``.end()`` signifies the end of a ``RegexBuilder`` grouping, such as :ref:`capture`, :ref:`group` or :ref:`any_of` element.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('((?:hello|[a-f0-9]))')
    expr = (
        RegexBuilder()
        .capture()
            .any_of()
                .range('a', 'f')
                .range('0', '9')
                .string('hello')
            .end()
        .end()
        .to_regex()
    )

.. _assert_ahead:

.assert_ahead()
---------------

``.assert_ahead()`` asserts that the proceeding elements are found without consuming them. Needs to be finalised with :ref:`end`.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('(?=[a-f])[a-z]')
    expr = (
        RegexBuilder()
        .assert_ahead()
            .range('a', 'f')
        .end()
        .range('a', 'z')
        .to_regex()
    )
    assert expr.match('a') # Matches
    assert expr.match('f') # Matches
    assert not expr.match('g') # Doesn't match

.. _assert_not_ahead:

.assert_not_ahead()
-------------------

``.assert_not_ahead()`` asserts that the proceeding elements are not found without consuming them. Needs to be finalised with :ref:`end`.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('(?![a-f])[g-z]')
    expr = (
        RegexBuilder()
        .assert_not_ahead()
            .range('a', 'f')
        .end()
        .range('g', 'z')
        .to_regex()
    )
    assert expr.match('g') # Matches
    assert expr.match('z') # Matches
    assert not expr.match('a') # Doesn't match

.. _assert_behind:

.assert_behind()
----------------

``.assert_behind()`` asserts that the elements contained within are found immediately before this point in the string. Needs to be finalised with :ref:`end`.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('(?<=hello )world')
    expr = (
        RegexBuilder()
        .assert_behind()
            .string('hello ')
        .end()
        .string('world')
        .to_regex()
    )

.. _assert_not_behind:

.assert_not_behind()
--------------------

``.assert_not_behind()`` asserts that the elements contained within are not found immediately before this point in the string. Needs to be finalised with :ref:`end`.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('(?<!hello )world')
    expr = (
        RegexBuilder()
        .assert_not_behind()
            .string('hello ')
        .end()
        .string('world')
        .to_regex()
    )

.. _optional:

.optional()
-----------

``.optional()`` asserts that the proceeding element may or may not be matched.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\d?')
    expr = (
        RegexBuilder()
        .optional()
            .digit()
        .to_regex()
    )

.. _zero_or_more:

.zero_or_more()
---------------

``.zero_or_more()`` asserts that the proceeding element may not be matched, or may be matched multiple times.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\d*')
    expr = (
        RegexBuilder()
        .zero_or_more()
            .digit()
        .to_regex()
    )

.. _zero_or_more_lazy:

.zero_or_more_lazy()
--------------------

``.zero_or_more_lazy()`` asserts that the proceeding element may not be matched, or may be matched multiple times, but as few times as possible.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\d*?')
    expr = (
        RegexBuilder()
        .zero_or_more_lazy()
            .digit()
        .to_regex()
    )

.. _one_or_more:

.one_or_more()
--------------

``.one_or_more()`` asserts that the proceeding element may be matched once or more times.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\d+')
    expr = (
        RegexBuilder()
        .one_or_more()
            .digit()
        .to_regex()
    )

.. _one_or_more_lazy:

.one_or_more_lazy()
-------------------

``.one_or_more_lazy()`` asserts that the proceeding element may be matched once or more times, but as few times as possible.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\d+?')
    expr = (
        RegexBuilder()
        .one_or_more_lazy()
            .digit()
        .to_regex()
    )

.. _exactly:

.exactly(n)
-----------

``.exactly(n)`` asserts that the proceeding element will be matched exactly ``n`` times.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\d{3}')
    expr = (
        RegexBuilder()
        .exactly(3)
            .digit()
        .to_regex()
    )

.. _at_least:

.at_least(n)
------------

``.at_least(n)`` asserts that the proceeding element will be matched at least ``n`` times.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\d{3,}')
    expr = (
        RegexBuilder()
        .at_least(3)
            .digit()
        .to_regex()
    )

.. _between:

.between(n, m)
--------------

``.between(n, m)`` asserts that the proceeding element will be matched between ``n`` and ``m`` times.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\d{3,5}')
    expr = (
        RegexBuilder()
        .between(3, 5)
            .digit()
        .to_regex()
    )

.. _between_lazy:

.between_lazy(n, m)
--------------------

``.between_lazy(n, m)`` asserts that the proceeding element will be matched between ``n`` and ``m`` times, but as few times as possible.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('\d{3,5}?')
    expr = (
        RegexBuilder()
        .between_lazy(3, 5)
            .digit()
        .to_regex()
    )

.. _start_of_input:

.start_of_input()
-----------------

``.start_of_input()`` asserts the start of input, or the start of a line when ``M`` flag is used.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('^hello')
    expr = (
        RegexBuilder()
        .start_of_input()
        .string('hello')
        .to_regex()
    )

.. _end_of_input:

.end_of_input()
---------------

``.end_of_input()`` asserts the end of input, or the end of a line when ``M`` flag is used.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('hello$')
    expr = (
        RegexBuilder()
        .string('hello')
        .end_of_input()
        .to_regex()
    )

.. _any_of_chars:

.any_of_chars(chars)
--------------------

``.any_of_chars(chars)`` matches any of the characters in the provided string ``chars``.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('[abc]')
    expr = (
        RegexBuilder()
        .any_of_chars('abc')
        .to_regex()
    )

.. _anything_but_chars:

.anything_but_chars(chars)
--------------------------

``.anything_but_chars(chars)`` matches any character except those in the provided string ``chars``.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('[^abc]')
    expr = (
        RegexBuilder()
        .anything_but_chars('abc')
        .to_regex()
    )

.. _anything_but_string:

.anything_but_string(string)
----------------------------

``.anything_but_string(string)`` matches any string the same length as ``string``, except the characters sequentially defined in ``string``.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('(?:[^a][^e][^i][^o][^u])')
    expr = (
        RegexBuilder()
        .anything_but_string('aeiou')
        .to_regex()
    )

.. _anything_but_range:

.anything_but_range(start, end)
--------------------------------

``.anything_but_range(start, end)`` matches any character except those that would be captured by the :ref:`range` specified by ``start`` and ``end``.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('[^a-z]')
    expr = (
        RegexBuilder()
        .anything_but_range('a', 'z')
        .to_regex()
    )

.. _string:

.string(s)
---------------

``.string(string)`` matches the exact string ``s``.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('hello')
    expr = (
        RegexBuilder()
        .string('hello')
        .to_regex()
    )

.. _char:

.char(c)
--------

``.char(c)`` matches the exact character ``c``.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('h')
    expr = (
        RegexBuilder()
        .char('h')
        .to_regex()
    )

.. _range:

.range(start, end)
------------------

``.range(start, end)`` matches any character that falls between ``start`` and ``end``. Ordering is defined by a characters ASCII or unicode value.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('[a-z]')
    expr = (
        RegexBuilder()
        .range('a', 'z')
        .to_regex()
    )

.. _subexpression:

.subexpression(expr, opts)
--------------------------

``.subexpression()`` matches another ``RegexBuilder`` instance inline. Can be used to create libraries, or to modularise you code. By default, flags and start/end of input markers are ignored, but can be explcitly turned on in the options object.

``opts`` is an optional dictionary that can be used to control how the subexpression is treated. It has the following properties:

    ``namespace``
        A string namespace to use on all named capture groups in the subexpression, to avoid naming collisions with your own named groups. Defaults to ``' '``.

    ``ignore_flags``
        If set to ``True``, any flags this subexpression specifies should be disregarded. Defaults to ``True``.

    ``ignore_start_and_end``
        If set to ``True``, any start_of_input/end_of_input asserted in this subexpression specifies should be disregarded. Defaults to ``True``.

A sample ``opts`` dictionary might look like this::

    opts = {
        'namespace': 'my_namespace',
        'ignore_flags': False,
        'ignore_start_and_end': False
    }

You can use the ``.subexpression()`` method like this:


.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('[a-z]+.{3,}\d{5}')
    five_digits = RegexBuilder().exactly(5).digit()
    expr = (
        RegexBuilder()
        .one_or_more().range('a', 'z')
        .at_least(3).any_char()
        .subexpression(five_digits)
        .to_regex()
    )

.. _to_regex_string:

.to_regex_string()
------------------

``.to_regex_string()`` returns a string representation of the regular expression that this ``RegexBuilder`` instance represents.

.. code-block:: python

    from edify import RegexBuilder

    # returns '/^(?:0x)?([A-Fa-f0-9]{4})$/IM'
    expr = (
        RegexBuilder()
        .ignore_case()
        .multiline()
        .start_of_input()
        .optional().string('0x')
        .capture()
            .exactly(4).any_of()
                .range('A', 'F')
                .range('a', 'f')
                .range('0', '9')
            .end()
        .end()
        .end_of_input()
        .to_regex_string()
    )

.. _to_regex:

.to_regex()
-----------

``.to_regex()`` returns a compiled regular expression object that this ``RegexBuilder`` instance represents. The complied regular expression is an instance of ``re.compile``, so any ``re`` module methods like ``.search()``, ``.match()``, ``.findall()``, etc. can be used on it.

.. code-block:: python

    from edify import RegexBuilder

    # returns re.compile('^(?:0x)?([A-Fa-f0-9]{4})$', re.MULTILINE | re.IGNORECASE)
    expr = (
        RegexBuilder()
        .ignore_case()
        .multiline()
        .start_of_input()
        .optional().string('0x')
        .capture()
            .exactly(4).any_of()
                .range('A', 'F')
                .range('a', 'f')
                .range('0', '9')
            .end()
        .end()
        .end_of_input()
        .to_regex()
    )

    # returns re.Match object
    expr.match('0x1234')
