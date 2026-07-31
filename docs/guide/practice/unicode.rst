Unicode
=======

Most patterns are written against ASCII examples and then meet a real name, a real
address, or a real search box. This page covers what edify's tokens actually do with
text beyond ASCII, and where the surprises are.

The short version: ``\w``, ``\d`` and ``\s`` are Unicode-aware by default, while
``letter`` is an explicit ``a-z`` range and is not.

Which tokens are Unicode-aware
------------------------------

:meth:`~edify.RegexBuilder.word` emits ``\w``, which in Python matches any word
character in any script — not just ``[A-Za-z0-9_]``:

.. code-block:: python

   from edify import RegexBuilder

   word = RegexBuilder().start_of_input().one_or_more().word().end_of_input().to_regex()

   word.match("hello")     # matches
   word.match("café")      # matches
   word.match("日本語")      # matches
   word.match("Ω")         # matches

:meth:`~edify.RegexBuilder.letter` is different. It is a literal ``[a-zA-Z]``
character range, so it stops at ASCII no matter what the input contains:

.. code-block:: python

   from edify import RegexBuilder

   letter = RegexBuilder().start_of_input().one_or_more().letter().end_of_input().to_regex()

   letter.match("hello")   # matches
   letter.match("café")    # no match — "é" is outside a-z
   letter.match("日本語")    # no match

That difference is the single most common Unicode bug in a validator: a name field
built on ``letter`` quietly rejects a large fraction of the world's names. Reach for
``word`` — or an explicit character class — when the field holds a human name.

.. edify-playground::
   :tests: hello|café|日本語|Ünal|_x9

   from edify import RegexBuilder

   RegexBuilder().start_of_input() \
       .one_or_more().word() \
       .end_of_input()

Swap ``word()`` for ``letter()`` and watch everything but ``hello`` drop out.

Digits are not only 0-9
-----------------------

:meth:`~edify.RegexBuilder.digit` emits ``\d``, which matches every decimal digit
Unicode defines — Arabic-Indic, Bengali, and dozens more:

.. code-block:: python

   from edify import RegexBuilder

   digits = RegexBuilder().start_of_input().one_or_more().digit().end_of_input().to_regex()

   digits.match("123")     # matches
   digits.match("١٢٣")     # matches — Arabic-Indic digits
   digits.match("১২৩")     # matches — Bengali digits

This matters when the matched text goes on to be parsed. ``int()`` accepts those
strings, but a downstream system that assumes ASCII may not. If you need ASCII
digits specifically, say so with :meth:`~edify.RegexBuilder.any_of_chars` or a
:meth:`~edify.RegexBuilder.range`:

.. code-block:: python

   from edify import RegexBuilder

   ascii_digits = (
       RegexBuilder().start_of_input()
       .one_or_more().range("0", "9")
       .end_of_input()
   )
   ascii_digits.to_regex_string()   # '^[0-9]+$'

.. edify-playground::
   :tests: 123|١٢٣|১২৩|12a

   from edify import RegexBuilder

   RegexBuilder().start_of_input() \
       .one_or_more().range("0", "9") \
       .end_of_input()

Restricting the whole pattern to ASCII
--------------------------------------

Rather than rewriting each token, :meth:`~edify.RegexBuilder.ascii_only` sets the
``re.A`` flag on the compiled pattern, which makes ``\w``, ``\d``, ``\s`` and ``\b``
revert to their ASCII meanings all at once:

.. code-block:: python

   from edify import RegexBuilder

   strict = (
       RegexBuilder().ascii_only().start_of_input()
       .one_or_more().word()
       .end_of_input()
       .to_regex()
   )

   strict.source            # '^\\w+$' — the flag rides on the compiled pattern
   strict.match("hello")    # matches
   strict.match("café")     # no match
   strict.match("日本語")     # no match

Note that ``source`` is unchanged: the restriction lives in the compiled pattern's
flags, not in the emitted text. If you hand ``source`` to another tool, the
narrowing does not travel with it — use an explicit range when the regex string has
to stand alone.

.. edify-playground::
   :tests: hello|café|日本語|user_1

   from edify import RegexBuilder

   RegexBuilder().ascii_only().start_of_input() \
       .one_or_more().word() \
       .end_of_input()

Composed characters and length
------------------------------

``é`` can be one code point (U+00E9) or two (``e`` followed by a combining acute).
The two look identical and compare unequal, and a quantifier counts code points, so
the same visible word has two different lengths:

.. code-block:: python

   import unicodedata

   from edify import RegexBuilder

   four = RegexBuilder().start_of_input().exactly(4).word().end_of_input().to_regex()

   len(unicodedata.normalize("NFC", "café"))   # 4
   len(unicodedata.normalize("NFD", "café"))   # 5

   four.match(unicodedata.normalize("NFC", "café"))   # matches
   four.match(unicodedata.normalize("NFD", "café"))   # no match

No regex flag fixes this, because the two strings genuinely differ. Normalize
*before* matching — ``unicodedata.normalize("NFC", value)`` — whenever a pattern
counts characters or compares literal text. Do it once at the boundary where text
enters your system and every pattern downstream gets it for free.

Emoji are not one character
---------------------------

:meth:`~edify.RegexBuilder.any_char` matches one code point. A simple emoji is one
code point, but an emoji built from a zero-width joiner sequence is several:

.. code-block:: python

   from edify import RegexBuilder

   one = RegexBuilder().start_of_input().exactly(1).any_char().end_of_input().to_regex()

   one.match("é")      # matches — one code point
   one.match("日")      # matches
   one.match("🎉")      # matches
   one.match("👩‍💻")     # no match — three code points joined into one glyph

If you are counting what a user *sees*, code points are the wrong unit and a regex
is the wrong tool; segment by grapheme cluster instead. If you are counting what a
database column stores, code points may be exactly right — just be deliberate about
which one you mean.

Case folding stops short of the hard cases
------------------------------------------

:meth:`~edify.RegexBuilder.ignore_case` handles the common mappings across scripts,
but it is a per-character fold. It cannot match one character against two:

.. code-block:: python

   from edify import RegexBuilder

   folded = (
       RegexBuilder().ignore_case().start_of_input()
       .string("straße")
       .end_of_input()
       .to_regex()
   )

   folded.match("STRAßE")    # matches
   folded.match("STRASSE")   # no match — "ß" folds to itself, not to "ss"

For search — where users expect ``strasse`` to find ``Straße`` — fold with
``str.casefold()`` before matching rather than relying on the flag. For validation,
the flag is usually what you want.

Choosing a strategy
-------------------

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - The field holds
     - Use
   * - A human name, city, or free text
     - ``word`` — Unicode-aware, normalize to NFC first
   * - An identifier, slug, or code
     - ``range("a", "z")`` or ``ascii_only`` — narrow on purpose
   * - A number you will parse
     - ``range("0", "9")`` — ``digit`` admits every script's digits
   * - Text a user will search
     - Match on ``casefold``-ed input, not on ``ignore_case`` alone

The library follows the same rule: :doc:`../../library/text/unicode` and
:doc:`../../library/text/script` accept text beyond ASCII, while
:doc:`../../library/text/ascii` and :doc:`../../library/text/slug` deliberately do
not. Pick the one whose answer you actually want.

Next: :doc:`recipes` puts these choices to work in complete, working patterns.
