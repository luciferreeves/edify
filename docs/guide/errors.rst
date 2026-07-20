Errors that guide you
=====================

Most regex mistakes fail silently or blow up with a cryptic message pointing at
a character offset. Edify does the opposite: when you build something invalid, it
tells you *what* went wrong, *where*, and *how to fix it*.

Try giving a named capture an invalid name:

.. code-block:: python

   from edify import RegexBuilder

   RegexBuilder().named_capture("2bad").digit().end().to_regex_string()

Instead of a traceback into the regex engine, you get:

.. code-block:: text

   error: named-group name '2bad' is not a valid identifier

    --> <stdin>:5:5
     |
   5 |     .named_capture("2bad")
     |     ^^^^^^^^^^^^^^^^^^^^^^^ invalid name passed here
     |
      = note: named-group names must be non-empty and contain only letters, digits,
        and underscores (no spaces, hyphens, or punctuation).

   help: rename '2bad' to a bare identifier (e.g. 'year', 'user_id', 'scheme').

Every edify error has the same four parts: a one-line **summary**, a **pointer**
at the exact call that caused it, a ``= note:`` explaining the rule, and a
``help:`` line with a concrete fix.

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
- a lookbehind the chosen engine can't compile
- an assertion that fails — :meth:`~edify.RegexBuilder.assert_matches` names the
  inputs that were rejected (see :doc:`testing`)

.. code-block:: python

   RegexBuilder().one_or_more().to_regex_string()   # dangling quantifier — nothing to repeat

   # error: dangling .one_or_more() with no operand to apply to
   #   ... help: append the element the quantifier should apply to (e.g. .digit()).

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

Next: :doc:`testing`, on the assertions edify gives you for pinning a pattern's
behavior down.
