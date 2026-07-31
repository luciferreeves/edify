From an existing regex
======================

Sometimes you already have a raw regular expression — in a code review, a
config file, an answer you found online — and you want to *understand* it, not
rewrite it by hand. :meth:`~edify.RegexBuilder.from_regex` parses a regex string
back into an edify builder:

.. code-block:: python

   from edify import RegexBuilder

   builder = RegexBuilder.from_regex(r"^\d{4}-\d{2}$")
   builder.to_regex_string()   # '^\\d{4}\\-\\d{2}$'

The emitted string may differ cosmetically from the input — edify escapes the
literal ``-`` it found, for instance — but it matches exactly the same text.

Now it's an ordinary builder. You can extend it:

.. code-block:: python

   from edify import RegexBuilder

   RegexBuilder.from_regex(r"\d{4}").char("-").exactly(2).digit().to_regex_string()
   # '\\d{4}\\-\\d{2}'

or — most usefully — hand it to the introspection tools to find out what that
cryptic line actually does. Pair this with :doc:`seeing` to turn any regex into
a plain-English explanation or a diagram:

.. code-block:: python

   from edify import RegexBuilder

   mystery = RegexBuilder.from_regex(r"(?P<area>\d{3})-(?P<line>\d{4})").to_regex()
   print(mystery.explain())

.. code-block:: text

   - The text must contain exactly 3 digits (0-9).
   - Then the text must have "-".
   - Then the text must have exactly 4 digits (0-9).

   Text this pattern accepts:
       123-1234
       234-2345
       345-3456

.. edify-playground::
   :tests: 123-1234|555-0100|12-1234|abc-defg

   from edify import RegexBuilder

   RegexBuilder.from_regex(r"(?P<area>\d{3})-(?P<line>\d{4})")

Edit the raw regex in that playground and watch the emitted pattern track it —
this is the fastest way to work out what an inherited expression does.

Normalization, not transcription
--------------------------------

``from_regex`` rebuilds the *structure*, then re-emits it. The result is
equivalent, not byte-identical, and occasionally simpler than what you fed in.
A single-character alternation, for example, comes back as a character class:

.. code-block:: python

   from edify import RegexBuilder

   RegexBuilder.from_regex(r"a|b").to_regex_string()   # '[ab]'

Both match exactly the same strings; the class is the form edify would have
emitted if you had built it by hand. Treat the round-trip as "the same pattern,
said edify's way" rather than a transcription — and if you need the original text
preserved verbatim, keep the original text.

Inline flags come along
-----------------------

Flags declared in the source — ``(?i)``, ``(?m)``, ``(?s)``, ``(?x)``, ``(?a)`` —
are translated into the corresponding builder calls, so a reverse-parsed pattern
matches what its source matched:

.. code-block:: python

   import re

   from edify import RegexBuilder

   folded = RegexBuilder.from_regex(r"(?i)abc").to_regex()

   bool(folded.search("ABC"))          # True
   bool(folded.compiled.flags & re.IGNORECASE)   # True

Each maps onto the method of the same meaning — ``ignore_case``, ``multi_line``,
``dot_all``, ``verbose``, ``ascii_only`` — and several combine, so ``(?im)`` gives
you both. :doc:`../builder/flags` covers what each one changes.

What it understands
-------------------

``from_regex`` translates the constructs that map cleanly onto the builder:

- literal text (escaped for you) and the shorthand classes ``\d``, ``\w``, ``\s``
  and their negations, plus ``.``
- a simple character class — a single range like ``[a-z]`` or a set of literals
  like ``[abc]``
- every quantifier — ``?``, ``*``, ``+``, ``{m}``, ``{m,n}``, and their lazy forms
- groups ``(?:…)``, captures ``(…)``, and named captures ``(?P<name>…)``
- alternation ``a|b``, anchors ``^`` and ``$``, and word boundaries ``\b``
- lookahead and lookbehind, positive and negative
- inline flags, as above

A few constructs aren't translated yet — a multi-range or negated custom class
(``[a-z0-9]``, ``[^abc]``) and backreferences (``\1``). When ``from_regex`` meets
one, it raises a clear :class:`~edify.EdifyError` naming the exact construct
rather than guessing — so you know precisely what to hand-write instead:

.. code-block:: python

   from edify import RegexBuilder
   from edify.builder.reverse import UnsupportedReverseParseError

   try:
       RegexBuilder.from_regex(r"(a)\1")
   except UnsupportedReverseParseError as problem:
       print(problem)

.. code-block:: text

   from_regex cannot translate the regex construct 'GROUPREF' yet; hand-write the
   equivalent chain and file an issue with the source pattern.

Refusing is the right behavior here: a reverse parser that guessed would hand you
a builder that quietly disagrees with the regex you started from. An error tells
you exactly which piece to write yourself — and the rest of the pattern is still
worth translating, so split it, convert what converts, and chain the remainder:

.. code-block:: python

   from edify import RegexBuilder

   converted = RegexBuilder.from_regex(r"(?P<word>[a-z]+)")
   whole = converted.whitespace_char().named_back_reference("word")
   whole.to_regex_string()   # '(?P<word>[a-z]+)\\s(?P=word)'

.. edify-playground::
   :tests: this is is fine|hello hello|no repeat|abc

   from edify import RegexBuilder

   RegexBuilder.from_regex(r"(?P<word>[a-z]+)") \
       .whitespace_char() \
       .named_back_reference("word")

Where it pays off
-----------------

Three jobs this does well:

**Auditing.** Point it at a regex from a config file or a dependency and read the
``explain()`` output. If the prose is not what the regex was supposed to do, you
have found a bug without running a single test case.

**Migrating.** Convert an existing pattern, then keep extending it with the
builder. You do not have to rewrite a working expression from scratch to start
getting anchors, assertions, and diagnostics on it.

**Checking.** A reverse-parsed pattern is a normal pattern, so
:doc:`../practice/performance` applies — a ``ReDoSWarning`` on a regex you
inherited is worth knowing about before it reaches production.

Next: :doc:`matching`, for actually running a compiled pattern against text.
