Composing and reusing
=====================

Patterns are values. You can name them, hand them around, and combine them —
three ways, depending on how it reads best.

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

The same ``octet`` is reused four times. Because builders are immutable, sharing
it is completely safe.

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

   from edify import DIGIT, LETTER, WHITESPACE, WORD, ALPHANUMERIC   # ... and more

Each is a ``Pattern``, so it is also callable as a validator and reusable with
``.use()``.

Factory functions
-----------------

Every builder method also exists as a standalone **factory function**, for a
functional style that skips the leading ``RegexBuilder()``:

.. code-block:: python

   from edify import char, exactly, capture, one_or_more, any_of

   char(".").to_regex_string()                      # '\\.'
   exactly(3, DIGIT).to_regex_string()              # '\\d{3}'
   capture(one_or_more(DIGIT)).to_regex_string()    # '(\\d+)'
   any_of(R().string("cat"), R().string("dog")).to_regex_string()   # '(?:cat|dog)'

Quantifier and group factories take the pattern they wrap as their last
argument — ``exactly(3, DIGIT)`` reads as *"exactly three digits."* Use whichever
style is clearest for the pattern in front of you; they all produce the same
kind of ``Pattern``.

Next: :doc:`from-regex`, going the other direction — turning an existing regex
string back into a chain.
