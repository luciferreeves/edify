Regex
=====

**Regex** answers a question no pattern can answer about itself: does this string
compile as a `regular expression <https://docs.python.org/3/library/re.html>`__?
Deciding that requires actually running the parser, so — like
:doc:`../auth/password` — this is a :class:`~edify.Pattern` subclass with its own
``__call__`` rather than a compiled pattern. Reading its emitted regex shows an
empty string; call it instead.

Patterns that compile
---------------------

.. edify-playground::

   from edify.library import regex

   regex(r"\d{3}-\d{4}")        # a plain pattern
   regex(r"^[a-z]+$")           # anchors and a class
   regex(r"(?P<year>\d{4})")    # a named group
   regex("")                    # the empty pattern is valid

Patterns that do not
--------------------

The failures are the genuine syntax errors a parser rejects:

.. edify-playground::

   from edify.library import regex

   regex(r"[a-z]")       # the same class, closed
   regex(r"[a-z")        # an unclosed class
   regex(r"(unclosed")   # an unclosed group
   regex(r"a{2,1}")      # an inverted quantifier
   regex(r"*")           # nothing to repeat

Two things to keep in mind. Compiling is not the same as being *safe*: a
catastrophically backtracking pattern such as ``(a+)+$`` compiles perfectly and can
hang on a crafted input, so never accept user-supplied patterns without a timeout or
a safety review. And this checks the syntax one engine accepts — dialects differ, so
a pattern valid here may be rejected elsewhere. To build patterns safely instead of
validating strings, use the builder itself: see the :doc:`../../guide/index`.
