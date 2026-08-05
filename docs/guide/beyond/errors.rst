Errors that guide you
=====================

Most regex mistakes fail silently or blow up with a cryptic message pointing at
a character offset. Edify does the opposite: when you build something invalid, it
tells you *what* went wrong, *where*, and *how to fix it*.

Try giving a named capture an invalid name:

.. code-block:: python

   from edify import EdifyError, RegexBuilder

   try:
       RegexBuilder().named_capture("2bad").digit().end().to_regex_string()
   except EdifyError as problem:
       print(problem)

Instead of a traceback into the regex engine, you get:

.. code-block:: text

   error: named-group name '2bad' is not a valid identifier

    --> validators.py:4:5
     |
   4 |     RegexBuilder().named_capture("2bad").digit().end().to_regex_string()
     |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ invalid name passed here
     |
      = note: named-group names must be non-empty and contain only letters, digits,
        and underscores (no spaces, hyphens, or punctuation).

   help: rename '2bad' to a bare identifier (e.g. 'year', 'user_id', 'scheme').

Anatomy of a diagnostic
-----------------------

Every edify error has the same four parts, and each answers a different question:

**The summary** — one line naming what is wrong, in terms of the argument you
passed. It quotes the offending value (``'2bad'``) rather than describing it
abstractly, so the line is greppable and reads correctly in a log.

**The pointer** — a ``file:line:column`` location and a caret span underneath the
source itself. The span covers the *call that caused it*, not the terminal call
that happened to notice. That distinction matters most in a long chain, where the
failure surfaces at ``.to_regex_string()`` many lines below the mistake.

**The note** — the rule you ran into, stated in full. Reading it once should mean
you never hit the same error twice for the same reason.

**The help line** — a concrete edit, with an example. Not "provide a valid name"
but "rename ``'2bad'`` to a bare identifier (e.g. ``'year'``, ``'user_id'``,
``'scheme'``)."

Deferred errors carry their origin
----------------------------------

Some mistakes cannot be detected at the call that made them. An unclosed
:meth:`~edify.RegexBuilder.group` is legal right up until you ask for the regex —
the frame might still be closed on the next line. When the pattern is finally
resolved, edify reports the terminal call *and* lists every frame still open, each
with the location where it was opened:

.. code-block:: python

   from edify import EdifyError, RegexBuilder

   try:
       RegexBuilder().group().digit().to_regex_string()
   except EdifyError as problem:
       print(problem)

.. code-block:: text

   error: cannot merge a subexpression that has an unclosed frame

    --> validators.py:4:5
     |
   4 |     RegexBuilder().group().digit().to_regex_string()
     |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ subexpression merged here
     |
      = note: the subexpression still has 1 open frame(s); only fully-closed
        expressions can be merged into another builder.
   open frames (innermost first):
      1. .group() — opened at validators.py:4:5

   help: add a matching .end() call for each open frame — start by closing the
   innermost .group() frame — before passing the subexpression to .subexpression(...).

The same applies to a dangling quantifier. ``one_or_more()`` queues a repetition
that attaches to the *next* element; if the chain ends first, the error names both
the terminal call and where the orphaned quantifier was queued.

Errors catch mistakes early
---------------------------

Because the builder validates as you go, you hear about problems the moment they
happen — not when the regex finally runs. Each of these raises immediately, at
the call site, with a fix:

- a quantifier with nothing to attach to (:meth:`~edify.RegexBuilder.one_or_more`
  as the last call in a chain)
- an :meth:`~edify.RegexBuilder.end` with no open group to close
- a nonsensical count — ``exactly(0)``, or ``between(5, 2)`` with the bounds
  reversed
- a character :meth:`~edify.RegexBuilder.range` whose bounds run backwards
- a duplicate :meth:`~edify.RegexBuilder.named_capture` name
- a lookbehind the chosen engine can't compile
- a Unicode property class such as :meth:`~edify.RegexBuilder.unicode_letter`
  compiled under the standard library, which has no property escapes
- an assertion that fails — :meth:`~edify.RegexBuilder.assert_matches` names the
  inputs that were rejected (see :doc:`testing`)

.. code-block:: python

   from edify import EdifyError, RegexBuilder

   try:
       RegexBuilder().one_or_more().to_regex_string()   # nothing to repeat
   except EdifyError as problem:
       print(problem)

   # error: dangling .one_or_more() with no operand to apply to
   #   ... help: append the element the quantifier should apply to (e.g. .digit()).

The diagnostics name your arguments
-----------------------------------

The summaries use the parameter names from the signature you called, not internal
ones. ``between(5, 2)`` reports ``lower`` and ``upper`` — the words that appear in
:meth:`~edify.RegexBuilder.between` — so you can go straight to the argument
without a translation step:

.. code-block:: text

   error: lower must be less than upper

    --> validators.py:9:5
     |
   9 |     RegexBuilder().between(5, 2).digit()
     |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ inverted bounds declared here
     |
      = note: the pair (lower, upper) forms a range; lower must be strictly less
        than upper for the range to contain any matches.

   help: swap the two arguments so lower is the smaller value.

The same holds for ``count`` in :meth:`~edify.RegexBuilder.exactly`,
:meth:`~edify.RegexBuilder.at_least`, and :meth:`~edify.RegexBuilder.at_most`, and
for the bounds in :meth:`~edify.RegexBuilder.range`, which also reports each
character's codepoint so an inverted range is unambiguous.

Here is the corrected form — bounds in ascending order, matching two to five
digits:

.. edify-playground::
   :tests: 42|12345|1|123456

   from edify import RegexBuilder

   RegexBuilder().start_of_input() \
       .between(2, 5).digit() \
       .end_of_input()

The error hierarchy
-------------------

All edify errors derive from :class:`~edify.EdifyError`, and the ones that
signal a malformed pattern derive from :class:`~edify.EdifySyntaxError`. Catch
whichever level fits — ``EdifySyntaxError`` for "this pattern is wrong,"
``EdifyError`` for anything edify raises:

.. code-block:: python

   from edify import RegexBuilder, EdifyError

   def try_build(name):
       try:
           return RegexBuilder().named_capture(name).digit().end().to_regex()
       except EdifyError as problem:
           print(f"could not build: {problem}")
           return None

That is exactly what you want when you build patterns from untrusted input — a
bad name or malformed fragment becomes a caught exception carrying the same
annotated message shown above, not a crash deep in the engine.

One thing that arrives as a *warning* rather than an error is worth knowing about:
``ReDoSWarning`` fires on :meth:`~edify.RegexBuilder.to_regex` when the pattern has
a shape prone to catastrophic backtracking. :doc:`../practice/performance` covers
what triggers it and what to do about it.

Next: :doc:`testing`, on the assertions edify gives you for pinning a pattern's
behavior down.
