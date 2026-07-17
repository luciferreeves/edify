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
happen — not when the regex finally runs. A quantifier with nothing to attach
to, an ``end()`` with no open group, a lookbehind the chosen engine can't
compile: each raises immediately, at the call site, with a fix.

.. code-block:: python

   RegexBuilder().one_or_more().to_regex_string()   # dangling quantifier — nothing to repeat

   # error: dangling .one_or_more() with no operand to apply to
   #   ... help: append the element the quantifier should apply to (e.g. .digit()).

Catching them
-------------

All edify errors derive from :class:`~edify.EdifyError`, and the ones that
signal a malformed pattern derive from :class:`~edify.EdifySyntaxError`, so you
can catch broadly when you're building patterns from untrusted input:

.. code-block:: python

   from edify import RegexBuilder, EdifyError

   def try_build(name):
       try:
           return RegexBuilder().named_capture(name).digit().end().to_regex()
       except EdifyError as problem:
           print(f"could not build: {problem}")
           return None

The annotated message you'd print is the same one shown above — useful,
specific, and pointed straight at the fix.

Next: :doc:`testing`, on the assertions edify gives you for pinning a pattern's
behavior down.
