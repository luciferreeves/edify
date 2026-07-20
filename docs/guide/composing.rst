Composing and reusing
=====================

Patterns are values. You can name them, hand them around, and combine them —
several ways, depending on how it reads best.

Subexpressions and ``.use()``
-----------------------------

The most direct way to reuse a pattern is to drop it into a chain with
:meth:`~edify.RegexBuilder.subexpression` or its alias
:meth:`~edify.RegexBuilder.use`:

.. code-block:: python

   from edify import RegexBuilder as R

   octet = R().between(1, 3).digit()
   ipv4 = (
       R().use(octet).char(".").use(octet).char(".").use(octet).char(".").use(octet)
   )
   ipv4.to_regex_string()   # '\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}'

The same ``octet`` is reused four times. Because builders are immutable, sharing
it is completely safe — no copy needed.

The ``+`` and ``|`` operators
-----------------------------

For quick composition, two operators read even cleaner. ``a + b`` concatenates —
it embeds ``b`` at the end of ``a``. ``a | b`` alternates — it matches either:

.. code-block:: python

   from edify import DIGIT, WORD, START, END

   (DIGIT + WORD).to_regex_string()     # '\\d\\w'       digit then word char
   (DIGIT | WORD).to_regex_string()     # '(?:\\d|\\w)'  digit or word char

Anchors survive composition, so you can bracket a pattern with ``START`` and
``END``:

.. code-block:: python

   (START + R().exactly(4).digit() + END).to_regex_string()   # '^\\d{4}$'

Module constants
----------------

``START``, ``END``, ``DIGIT``, and ``WORD`` above are **module constants** —
ready-made single-token patterns you can import and combine directly, no builder
needed. The full set covers every character class and anchor:

.. code-block:: python

   from edify import (
       START, END, WORD_BOUNDARY, NON_WORD_BOUNDARY,
       DIGIT, NON_DIGIT, WORD, NON_WORD, WHITESPACE, NON_WHITESPACE,
       LETTER, LOWERCASE, UPPERCASE, ALPHANUMERIC, ANY_CHAR,
       TAB, NEW_LINE, CARRIAGE_RETURN, NULL_BYTE,
   )

Each is a :class:`~edify.Pattern`, so it is also callable as a one-character
validator and reusable with ``.use()``:

.. code-block:: python

   DIGIT("5")   # True
   WORD("_")    # True

Factory functions
-----------------

Every builder method also exists as a standalone **factory function**, for a
functional style that skips the leading ``RegexBuilder()``:

.. code-block:: python

   from edify import char, exactly, capture, one_or_more, any_of, string, DIGIT

   char(".").to_regex_string()                      # '\\.'
   exactly(3, DIGIT).to_regex_string()              # '\\d{3}'
   capture(one_or_more(DIGIT)).to_regex_string()    # '(\\d+)'
   any_of(string("cat"), string("dog")).to_regex_string()   # '(?:cat|dog)'

Quantifier and group factories take the pattern they wrap as their last
argument — ``exactly(3, DIGIT)`` reads as *"exactly three digits."* The character
factories — ``char``, ``string``, ``chars``, ``nonchars``, ``range_of``,
``nonrange``, ``nonstring`` — build a fresh :class:`~edify.Pattern` from their
arguments:

.. code-block:: python

   from edify import chars, range_of, nonchars

   chars("aeiou").to_regex_string()      # '[aeiou]'
   range_of("a", "z").to_regex_string()  # '[a-z]'
   nonchars("aeiou").to_regex_string()   # '[^aeiou]'

Use whichever style is clearest for the pattern in front of you; they all produce
the same kind of ``Pattern``.

An explicit copy
----------------

Because every method returns a new builder, two extensions of a shared base are
already independent. When you want to make that intent obvious — stashing a
builder to branch from later — ask for a copy:

.. code-block:: python

   base = R().start_of_input().one_or_more().digit()
   snapshot = base.copy()   # a fresh builder with the same state (alias: .fork())

Putting it together
-------------------

Compose a small pattern from named parts and reuse them:

.. code-block:: python

   from edify import RegexBuilder as R

   label = R().one_or_more().any_of().range("a", "z").range("0", "9").end()
   dotted = R().use(label).one_or_more().group().char(".").use(label).end()
   dotted.to_regex_string()   # '[a-z0-9]+(?:\\.[a-z0-9]+)+'

.. edify-playground::

   (
       RegexBuilder()
       .use(RegexBuilder().one_or_more().any_of().range("a", "z").range("0", "9").end())
       .one_or_more()
       .group().char(".").use(RegexBuilder().one_or_more().any_of().range("a", "z").range("0", "9").end()).end()
   )

Next: :doc:`from-regex`, going the other direction — turning an existing regex
string back into a chain.
