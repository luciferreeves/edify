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

:meth:`~edify.RegexBuilder.anything_but_any_of` is the same frame, negated. Add
the members you want to *reject* and close it the same way:

.. code-block:: python

   from edify import RegexBuilder as R

   R().anything_but_any_of().range("a", "z").range("0", "9").end().to_regex_string()
   # '[^a-z0-9]'

   R().anything_but_any_of().range("a", "z").char("_").end().to_regex_string()
   # '[^a-z_]'

So the rule is: anything you can build positively, you can negate. The
single-member forms above are the shorthands — reach for the frame when the class
has more than one member.

.. edify-playground::

   from edify import Pattern

   # An identifier segment that may not contain lowercase letters, digits, or "_".
   shouty = (
       Pattern()
       .start_of_input()
       .one_or_more()
       .anything_but_any_of()
       .range("a", "z")
       .range("0", "9")
       .char("_")
       .end()
       .end_of_input()
   )

   shouty("HOSTNAME")    # uppercase is not excluded
   shouty("HOST-NAME")   # nor is the hyphen
   shouty("hostname")    # lowercase is
   shouty("HOST_NAME")   # so is the underscore
   shouty("HOST9")       # and so are digits

The frame rejects one character at a time, so every member has to be one
character wide. A multi-character member raises rather than emitting something
that does not mean what it reads like — to reject a whole sequence, use
:meth:`~edify.RegexBuilder.anything_but_string` or a negative lookahead.

ASCII or any script
-------------------

:meth:`~edify.RegexBuilder.letter` is ASCII: it emits ``[a-zA-Z]`` and stops
there. :meth:`~edify.RegexBuilder.unicode_letter` emits ``\p{L}`` and matches a
letter in any script:

.. code-block:: python

   from edify import RegexBuilder as R

   R().letter().to_regex_string()           # '[a-zA-Z]'
   R().unicode_letter().to_regex_string()   # '\\p{L}'

The same pairing runs through the set —
:meth:`~edify.RegexBuilder.unicode_uppercase` (``\p{Lu}``),
:meth:`~edify.RegexBuilder.unicode_lowercase` (``\p{Ll}``), and
:meth:`~edify.RegexBuilder.unicode_alphanumeric` (``[\p{L}\p{N}]``), which is
:meth:`~edify.RegexBuilder.word` without the underscore.

Property escapes are not part of the standard library's regex syntax, so the
Unicode four require ``pip install edify[regex]`` and
``.to_regex(engine="regex")``. Compiling one under the standard library raises a
clear error rather than emitting something else. :doc:`../practice/unicode` covers
which to reach for.

Character constants
-------------------

Every built-in **ASCII** class is also an importable :class:`~edify.Pattern`
constant. Each is callable as a one-character validator and composable with ``+``:

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

The Unicode classes have no constant. A constant is callable on the spot, and
calling one built on ``\p{...}`` would raise for anyone without the ``regex``
extra installed — so they stay methods, where the engine choice is explicit.

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
   * - ``anything_but_any_of().…​.end()``
     - ``[^…]`` — the same class, negated

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
