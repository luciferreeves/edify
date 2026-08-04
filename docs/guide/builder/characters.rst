Characters
==========

These are the tokens that actually match text. Everything else in the builder —
quantifiers, groups, anchors — arranges characters; this page is the alphabet.

Built-in classes
----------------

The common character classes read as plain nouns:

.. code-block:: python

   from edify import RegexBuilder as R

   R().digit().to_regex_string()                # '\\d'   any digit 0-9
   R().non_digit().to_regex_string()            # '\\D'   anything but a digit
   R().word().to_regex_string()                 # '\\w'   letter, digit, or underscore
   R().non_word().to_regex_string()             # '\\W'   anything but a word character
   R().whitespace_char().to_regex_string()      # '\\s'   space, tab, newline, ...
   R().non_whitespace_char().to_regex_string()  # '\\S'   anything but whitespace
   R().any_char().to_regex_string()             # '.'     any character (except newline)

And the letter classes spell out their ranges for you:

.. code-block:: python

   from edify import RegexBuilder as R

   R().letter().to_regex_string()        # '[a-zA-Z]'
   R().uppercase().to_regex_string()     # '[A-Z]'
   R().lowercase().to_regex_string()     # '[a-z]'
   R().alphanumeric().to_regex_string()  # '[a-zA-Z0-9]'

By default ``\w``, ``\d``, and ``\s`` match the full Unicode ranges. Restrict
them to plain ASCII with the :meth:`~edify.RegexBuilder.ascii_only` flag (see
:doc:`flags`), and let ``any_char`` also match newlines with
:meth:`~edify.RegexBuilder.dot_all`.

Whitespace and control literals
-------------------------------

Named tokens for the characters you can't type comfortably:

.. code-block:: python

   from edify import RegexBuilder as R

   R().tab().to_regex_string()              # '\\t'
   R().new_line().to_regex_string()         # '\\n'
   R().carriage_return().to_regex_string()  # '\\r'
   R().null_byte().to_regex_string()        # '\\0'

Literal text
------------

:meth:`~edify.RegexBuilder.char` matches one literal character and
:meth:`~edify.RegexBuilder.string` matches a run of them. Both escape regex
metacharacters for you, so you never have to think about backslashes:

.. code-block:: python

   from edify import RegexBuilder as R

   R().char(".").to_regex_string()      # '\\.'    a literal dot, not "any char"
   R().string("c.t").to_regex_string()  # 'c\\.t'  the dot is escaped for you
   R().string("a+b*c").to_regex_string()   # 'a\\+b\\*c'  only what needs escaping

That automatic escaping is the point: you write the text you mean, and edify
emits the regex that matches exactly that text — no matter which metacharacters
it happens to contain. The dot below is a *literal* dot, so ``a.b`` matches but
``axb`` doesn't:

.. edify-playground::
   :tests: a.b|axb|a-b|xyz

   RegexBuilder() \
       .string("a.b")

Ranges and sets
---------------

:meth:`~edify.RegexBuilder.range` matches any single character between two
endpoints, and :meth:`~edify.RegexBuilder.any_of_chars` matches any one
character from a set you list:

.. code-block:: python

   from edify import RegexBuilder as R

   R().range("a", "z").to_regex_string()          # '[a-z]'
   R().any_of_chars("aeiou").to_regex_string()    # '[aeiou]'

Each has a negated twin that matches any character *not* in the set — and
:meth:`~edify.RegexBuilder.anything_but_string` matches any run of characters
that isn't the given literal:

.. code-block:: python

   from edify import RegexBuilder as R

   R().anything_but_chars("aeiou").to_regex_string()      # '[^aeiou]'
   R().anything_but_range("a", "z").to_regex_string()     # '[^a-z]'
   R().anything_but_string("cat").to_regex_string()       # '(?:[^c][^a][^t])'

Inside a character set, edify escapes only what actually needs escaping for that
position — so ``any_of_chars("#?!@$%^&*-")`` emits the minimal correct class,
not a thicket of backslashes:

.. code-block:: python

   from edify import RegexBuilder as R

   R().any_of_chars("#?!@$%^&*-").to_regex_string()   # '[#?!@$%^&*-]'

Combining classes
-----------------

To match a character from *several* ranges or sets at once, open an
:meth:`~edify.RegexBuilder.any_of` class, add each range or character, and close
it with :meth:`~edify.RegexBuilder.end`. It folds them into one class:

.. code-block:: python

   from edify import RegexBuilder as R

   R().any_of().range("0", "9").range("a", "f").range("A", "F").end().to_regex_string()
   # '[0-9a-fA-F]'

Note the difference from ``any_of_chars``: that method takes *literal*
characters — a dash inside it is a literal dash — while ``any_of().range(...)``
builds true ranges. When you pass ``any_of`` plain strings instead, it becomes an
alternation between whole branches; that's covered on :doc:`groups`.

Character constants
-------------------

Every built-in class is also an importable :class:`~edify.Pattern` constant.
Each is callable as a one-character validator and composable with ``+``:

.. code-block:: python

   from edify import DIGIT, LETTER, WORD, WHITESPACE, ALPHANUMERIC, ANY_CHAR

   DIGIT("5")                        # True
   DIGIT("x")                        # False
   DIGIT.to_regex_string()           # '\\d'
   (DIGIT + LETTER).to_regex_string()   # '\\d[a-zA-Z]'

The full set mirrors the methods above: ``DIGIT``, ``NON_DIGIT``, ``WORD``,
``NON_WORD``, ``WHITESPACE``, ``NON_WHITESPACE``, ``LETTER``, ``LOWERCASE``,
``UPPERCASE``, ``ALPHANUMERIC``, ``ANY_CHAR``, ``TAB``, ``NEW_LINE``,
``CARRIAGE_RETURN``, and ``NULL_BYTE``. See :doc:`../beyond/composing` for combining them.

Quick reference
---------------

Every single-character token, its importable constant, and what it emits:

.. list-table::
   :header-rows: 1
   :widths: 34 30 36

   * - Method
     - Constant
     - Emits
   * - ``digit()``
     - ``DIGIT``
     - ``\d`` — a digit 0–9
   * - ``non_digit()``
     - ``NON_DIGIT``
     - ``\D`` — any non-digit
   * - ``word()``
     - ``WORD``
     - ``\w`` — letter, digit, or underscore
   * - ``non_word()``
     - ``NON_WORD``
     - ``\W`` — any non-word character
   * - ``whitespace_char()``
     - ``WHITESPACE``
     - ``\s`` — space, tab, newline, …
   * - ``non_whitespace_char()``
     - ``NON_WHITESPACE``
     - ``\S`` — any non-whitespace
   * - ``any_char()``
     - ``ANY_CHAR``
     - ``.`` — any character but newline
   * - ``letter()``
     - ``LETTER``
     - ``[a-zA-Z]``
   * - ``lowercase()``
     - ``LOWERCASE``
     - ``[a-z]``
   * - ``uppercase()``
     - ``UPPERCASE``
     - ``[A-Z]``
   * - ``alphanumeric()``
     - ``ALPHANUMERIC``
     - ``[a-zA-Z0-9]``
   * - ``tab()``
     - ``TAB``
     - ``\t``
   * - ``new_line()``
     - ``NEW_LINE``
     - ``\n``
   * - ``carriage_return()``
     - ``CARRIAGE_RETURN``
     - ``\r``
   * - ``null_byte()``
     - ``NULL_BYTE``
     - ``\0``

And the text/set builders:

.. list-table::
   :header-rows: 1
   :widths: 42 58

   * - Method
     - Emits / meaning
   * - ``char(c)``
     - one literal character, escaped as needed
   * - ``string(s)``
     - a literal run of characters, escaped as needed
   * - ``range(a, z)``
     - ``[a-z]`` — one character in a range
   * - ``any_of_chars(s)``
     - ``[…]`` — one of the listed literal characters
   * - ``anything_but_chars(s)``
     - ``[^…]`` — any character not listed
   * - ``anything_but_range(a, z)``
     - ``[^a-z]`` — any character outside the range
   * - ``anything_but_string(s)``
     - a per-character negation of the literal
   * - ``any_of().…​.end()``
     - one class folding several ranges/sets together

Putting it together
-------------------

A hex color is a ``#`` followed by exactly six hex digits:

.. code-block:: python

   from edify import RegexBuilder as R

   hex_color = (
       R().start_of_input()
       .char("#")
       .exactly(6).any_of().range("0", "9").range("a", "f").range("A", "F").end()
       .end_of_input()
   )

   hex_color.to_regex_string()   # '^\\#[0-9a-fA-F]{6}$'

.. edify-playground::
   :tests: #a3c113|#FF0000|#fff|red

   RegexBuilder() \
       .start_of_input() \
       .char("#") \
       .exactly(6).any_of().range("0", "9").range("a", "f").range("A", "F").end() \
       .end_of_input()

Next up: :doc:`quantifiers`, which control *how many* of any of these tokens to
match.
