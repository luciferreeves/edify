From an existing regex
======================

Sometimes you already have a raw regular expression — in a code review, a
config file, a StackOverflow answer — and you want to *understand* it, not
rewrite it by hand. :meth:`~edify.RegexBuilder.from_regex` parses a regex string
back into an edify builder:

.. code-block:: python

   from edify import RegexBuilder

   builder = RegexBuilder.from_regex(r"^\d{4}-\d{2}$")
   builder.to_regex_string()   # '^\\d{4}\\-\\d{2}$'

Now it's an ordinary builder. You can extend it:

.. code-block:: python

   RegexBuilder.from_regex(r"\d{4}").char("-").exactly(2).digit().to_regex_string()
   # '\\d{4}\\-\\d{2}'

or — most usefully — hand it to the introspection tools to find out what that
cryptic line actually does. Pair this with :doc:`seeing` to turn any regex into
a plain-English explanation or a diagram:

.. code-block:: python

   from edify.introspect import explain_elements

   mystery = RegexBuilder.from_regex(r"^(?:0x)?[0-9a-fA-F]{4}$").to_regex()
   print(explain_elements(mystery.elements))

``from_regex`` understands the constructs the builder itself can produce —
literals, character classes, quantifiers, groups, alternation, captures,
backreferences, and lookaround. If it meets something it can't represent, it
raises a clear error naming the construct rather than guessing.

Next: :doc:`matching`, for actually running a compiled pattern against text.
