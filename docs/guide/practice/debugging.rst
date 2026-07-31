Debugging a pattern
===================

The worst moment with a regular expression is when it silently does not match and
the string gives you nothing to go on. Edify has four tools for that moment, each
answering a different question.

Ask what the pattern thinks it means
------------------------------------

:meth:`~edify.Regex.explain` turns a compiled pattern back into prose, plus example
strings it would accept. It is the fastest way to catch a pattern that is correct
but not what you *meant*:

.. code-block:: python

   from edify import RegexBuilder

   phone = (
       RegexBuilder().start_of_input()
       .exactly(3).digit().char("-").exactly(4).digit()
       .end_of_input()
   )
   print(phone.to_regex().explain())

   # - The text must start with exactly 3 digits (0-9).
   # - Then the text must have "-".
   # - Then the text must have exactly 4 digits (0-9).
   #
   # Text this pattern accepts:
   #     123-1234

If the prose describes something other than what you had in mind, the bug is in the
chain — not in the input.

Ask what it compiled to
-----------------------

:meth:`~edify.Regex.to_verbose_string` lays the emitted pattern out one element per
line with a comment naming the chain call that produced it. This is where
off-by-one quantifiers and stray escapes become obvious:

.. code-block:: python

   from edify import RegexBuilder

   phone = (
       RegexBuilder().start_of_input()
       .exactly(3).digit().char("-").exactly(4).digit()
       .end_of_input()
   )
   print(phone.to_regex().to_verbose_string())

   # ^                       # start of input
   # \d{3}                   # exactly 3
   # \-                      # literal "\-"
   # \d{4}                   # exactly 4
   # $                       # end of input

Read the ``source`` when you need the raw string to paste elsewhere, and
``elements`` when you want the tree the checks in :doc:`performance` walk.

Narrow it down by bisecting the chain
-------------------------------------

Because every builder is immutable, you can test any prefix of a chain without
disturbing the whole. Build up one call at a time and find the exact step where the
input stops matching:

.. edify-playground::
   :tests: 555-1234|5551234|555-12345|abc-1234

   from edify import RegexBuilder

   RegexBuilder().start_of_input() \
       .exactly(3).digit() \
       .char("-") \
       .exactly(4).digit() \
       .end_of_input()

Delete the last line in the playground and watch ``555-12345`` start matching —
that is the anchor doing its job. Removing calls one at a time tells you which
element rejects your input far faster than staring at the regex.

The three mistakes that cause most of it
----------------------------------------

**Anchoring.** :meth:`~edify.RegexBuilder.test` and
:meth:`~edify.RegexBuilder.search` look *anywhere* in the string, so an unanchored
pattern reports a hit on any substring. If you meant "the whole string", anchor both
ends — see :doc:`../builder/anchors`.

**Quantifier position.** In edify the quantifier comes *before* the token it
repeats, so ``.exactly(3).digit()`` is three digits. Reading it as "digit, exactly
3" is the single most common source of confusion — :doc:`../start/thinking-in-edify`
covers the rule.

**Greediness.** ``one_or_more`` takes as much as it can and gives back only when
forced, so a pattern ending in a delimiter may swallow several fields. Reach for
:meth:`~edify.RegexBuilder.one_or_more_lazy` when you want the *first* delimiter
rather than the last:

.. edify-playground::
   :tests: <a><b>|<a>|<abc>

   from edify import RegexBuilder

   RegexBuilder().char("<").one_or_more_lazy().any_char().char(">")

Swap ``one_or_more_lazy`` for ``one_or_more`` and the same input matches the whole
``<a><b>`` instead of stopping at the first ``>``.

When it still will not match
----------------------------

Check the flags. A pattern that works in your editor but not in code is usually
missing :meth:`~edify.RegexBuilder.ignore_case`, or matching against multi-line text
without :meth:`~edify.RegexBuilder.dot_all` — ``any_char`` does **not** match a
newline by default, which surprises everyone once. :doc:`../builder/flags` covers
each one.

Next: :doc:`unicode`, for the class of failures that only show up with real-world
names.
