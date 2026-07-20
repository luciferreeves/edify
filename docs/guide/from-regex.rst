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

   RegexBuilder.from_regex(r"\d{4}").char("-").exactly(2).digit().to_regex_string()
   # '\\d{4}\\-\\d{2}'

or — most usefully — hand it to the introspection tools to find out what that
cryptic line actually does. Pair this with :doc:`seeing` to turn any regex into
a plain-English explanation or a diagram:

.. code-block:: python

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

A few constructs aren't translated yet — a multi-range or negated custom class
(``[a-z0-9]``, ``[^abc]``) and backreferences (``\1``). When ``from_regex`` meets
one, it raises a clear :class:`~edify.EdifyError` naming the exact construct
rather than guessing — so you know precisely what to hand-write instead:

.. code-block:: python

   RegexBuilder.from_regex(r"(a)\1")
   # error: from_regex cannot translate the regex construct 'GROUPREF' yet ...

Next: :doc:`matching`, for actually running a compiled pattern against text.
