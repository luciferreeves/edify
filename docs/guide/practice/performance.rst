Performance and ReDoS
=====================

A regular expression can be correct and still be dangerous. Certain shapes make a
matcher explore an exponential number of paths before admitting failure, so a short
crafted input can hang a process for minutes. That is a
`ReDoS <https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS>`__
— a denial of service caused by the pattern itself.

Edify checks for the classic shape at build time, which is something a raw regex
string cannot do.

The shape that explodes
-----------------------

The dangerous construct is an unbounded quantifier wrapping a group whose only
child is *also* an unbounded quantifier — ``(x+)+``. Matching ``aaaa…`` against it
is fine; matching ``aaaa…!`` is not, because the engine must try every way of
splitting the a's between the two quantifiers before it can conclude failure.

.. code-block:: python

   import warnings

   from edify import RegexBuilder

   with warnings.catch_warnings(record=True) as caught:
       warnings.simplefilter("always")
       risky = RegexBuilder().one_or_more().group().one_or_more().letter().end().to_regex()

   risky.source                      # '(?:[a-zA-Z]+)+'
   str(caught[0].message)[:60]       # 'nested unbounded quantifier detected: one_or_more() wraps…'

The warning fires when you call :meth:`~edify.RegexBuilder.to_regex` — before the
pattern ever meets user input. That is only possible because edify keeps an element
tree rather than a string: the check is structural, so it inspects what you built
rather than trying to parse a regex back into meaning.

Why edify can see it and a string cannot
----------------------------------------

Given the text ``(?:[a-zA-Z]+)+``, spotting the problem means re-parsing the regex,
rebuilding its structure, and reasoning about nesting. Given an element tree, it is
a walk: find an unbounded quantifier, look at its child, ask whether that child is a
single-child group wrapping another unbounded quantifier.

The check is deliberately **conservative** — it flags only that one shape. A
legitimate composite such as the balanced-parentheses idiom has a group with several
children and is left alone, so the warning stays meaningful instead of becoming
noise you learn to ignore.

.. edify-playground::
   :tests: aaaa|aaaab|abc

   from edify import RegexBuilder

   RegexBuilder().one_or_more().group().one_or_more().letter().end()

Writing patterns that stay linear
---------------------------------

Three habits avoid nearly all of it.

**Anchor both ends.** An unanchored pattern is retried at every position in the
subject, turning one failed match into *n* failed matches. If you mean "the whole
string is this", say so:

.. code-block:: python

   from edify import RegexBuilder

   anchored = RegexBuilder().start_of_input().one_or_more().letter().end_of_input()
   anchored.to_regex_string()   # '^[a-zA-Z]+$'

**Prefer a bounded quantifier.** ``between(1, 64)`` says what you mean and caps the
work; ``one_or_more`` invites an attacker to choose the length:

.. code-block:: python

   from edify import RegexBuilder

   bounded = RegexBuilder().start_of_input().between(1, 64).letter().end_of_input()
   bounded.to_regex_string()   # '^[a-zA-Z]{1,64}$'

**Make alternatives disjoint.** When two branches of an
:func:`~edify.any_of` can match the same text, the engine has to try both on
failure. The :doc:`../../library/address/ipv4` octet is a good model: its five
branches cover 0–255 with no overlap at all, so exactly one can ever apply.

What the check does not cover
-----------------------------

It finds one shape. Other slow constructs — nested quantifiers separated by another
group, ambiguous alternations, heavy lookaround in a loop — are not detected, and no
build-time check can prove a pattern is fast on every input.

So treat the warning as a floor rather than a guarantee. If a pattern will run
against text you do not control, bound its quantifiers, and consider running it with
a timeout. And never compile a pattern supplied by a user without both: see
:doc:`../../library/media/regex`, which tells you a string *compiles* but says
nothing about whether it terminates quickly.

Next: :doc:`debugging`, for when a pattern is fast but simply does not match.
