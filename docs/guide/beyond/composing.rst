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

Immutability is what makes this work
------------------------------------

Every method returns a *new* builder rather than mutating the one you called it
on. So a shared base can be extended in two directions with no interference:

.. code-block:: python

   from edify import RegexBuilder as R

   base = R().start_of_input().one_or_more().digit()

   with_dash = base.char("-")
   with_plus = base.char("+")

   base.to_regex_string()        # '^\\d+'    — untouched
   with_dash.to_regex_string()   # '^\\d+\\-'
   with_plus.to_regex_string()   # '^\\d+\\+'

That is why passing a builder into a function, storing one in a module constant,
or reusing one across threads needs no defensive copying. It is also why the
fragments in :doc:`../atoms/index` can be shared by every validator in the
:doc:`../../library/index` at once.

Patterns also compare by what they emit, not by identity — two chains that
produce the same regex are equal:

.. code-block:: python

   from edify import RegexBuilder as R

   R().digit() == R().digit()   # True

The ``+`` and ``|`` operators
-----------------------------

For quick composition, two operators read even cleaner. ``a + b`` concatenates —
it embeds ``b`` at the end of ``a``. ``a | b`` alternates — it matches either:

.. code-block:: python

   from edify import DIGIT, WORD

   (DIGIT + WORD).to_regex_string()     # '\\d\\w'       digit then word char
   (DIGIT | WORD).to_regex_string()     # '(?:\\d|\\w)'  digit or word char

``|`` wraps its result in a non-capturing group, which is what makes the operators
safe to nest: the alternation binds to exactly the two operands you wrote, never
leaking into whatever it is concatenated with.

Anchors survive composition, so you can bracket a pattern with ``START`` and
``END``:

.. code-block:: python

   from edify import RegexBuilder as R, START, END

   (START + R().exactly(4).digit() + END).to_regex_string()   # '^\\d{4}$'

``DIGIT + WORD`` reads *"a digit, then a word character"* — ``1a`` matches, ``a1``
doesn't:

.. edify-playground::
   :tests: 1a|12|a1|ab

   from edify import DIGIT, WORD
   DIGIT + WORD

Both operands must be patterns. ``DIGIT + "x"`` is not valid — wrap the literal
with :func:`~edify.string` or :func:`~edify.char` first, which also gets it
escaped correctly.

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

   from edify import DIGIT, WORD

   DIGIT("5")   # True
   WORD("_")    # True

.. edify-playground::
   :tests: 5|_|a|55

   from edify import START, END, DIGIT

   START + DIGIT + END

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

The factories nest, which is where the functional style pays off: the structure of
the call matches the structure of the pattern, outermost first, so a deeply
wrapped expression reads top-down instead of left-to-right.

.. edify-playground::
   :tests: cat|dog|cats|bird

   from edify import any_of, string, START, END

   START + any_of(string("cat"), string("dog")) + END

Use whichever style is clearest for the pattern in front of you; they all produce
the same kind of ``Pattern``.

An explicit copy
----------------

Because every method returns a new builder, two extensions of a shared base are
already independent. When you want to make that intent obvious — stashing a
builder to branch from later — ask for a copy:

.. code-block:: python

   from edify import RegexBuilder as R

   base = R().start_of_input().one_or_more().digit()
   snapshot = base.copy()   # a fresh builder with the same state (alias: .fork())

The copy is a distinct object that emits an identical pattern. It changes nothing
about safety — the original was never at risk — but it is a useful marker in code
that hands builders around.

Putting it together
-------------------

Compose a small pattern from named parts and reuse them:

.. code-block:: python

   from edify import RegexBuilder as R

   label = R().one_or_more().any_of().range("a", "z").range("0", "9").end()
   dotted = R().use(label).one_or_more().group().char(".").use(label).end()
   dotted.to_regex_string()   # '[a-z0-9]+(?:\\.[a-z0-9]+)+'

.. edify-playground::
   :tests: 192.168.0.1|10.0.0.255|1.2.3|host

   octet = RegexBuilder().between(1, 3).digit()
   RegexBuilder() \
       .use(octet).char(".").use(octet) \
       .char(".").use(octet).char(".").use(octet)

That four-octet pattern is deliberately loose — ``999.999.999.999`` matches it.
The real thing is in :doc:`../../library/address/ipv4`, and
:doc:`../atoms/network` has the fragment to compose with. Reaching for those
first is almost always the right call; build by hand when nothing in the library
fits.

Next: :doc:`from-regex`, going the other direction — turning an existing regex
string back into a chain.
