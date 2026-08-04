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

How bad it gets
---------------

"Exponential" is easy to nod at and hard to feel. Matching ``a…a!`` against
``^(?:[a-zA-Z]+)+$`` costs roughly four times as much for every two characters
added:

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Input length
     - ``^(?:[a-zA-Z]+)+$``
     - ``^[a-zA-Z]+$``
   * - 19 characters
     - ~7 ms
     - under 0.01 ms
   * - 21 characters
     - ~29 ms
     - under 0.01 ms
   * - 23 characters
     - ~118 ms
     - under 0.01 ms
   * - 25 characters
     - ~473 ms
     - under 0.01 ms

Two more characters at the bottom of that table is another two seconds. At forty
characters — still a short string, well under any length limit you would think to
impose — the same match takes longer than the age of the request that triggered it.
The safe pattern on the right is flat because it never has a choice to reconsider.

That is why this is a denial-of-service issue and not a tuning problem: the attacker
picks the input, and the input is tiny.

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

A timeout as the last line of defence
-------------------------------------

Bounding the pattern is the fix. A timeout is the seatbelt for the case you did not
anticipate: the match surface takes a ``timeout`` in seconds, and it is available
under the third-party engine.

.. code-block:: python

   from edify import RegexBuilder as R

   pattern = R().start_of_input().one_or_more().letter().end_of_input()
   compiled = pattern.to_regex(engine="regex")

   compiled.match("abcdef", timeout=0.1)

Asking for one under the standard library is an error rather than a silently ignored
argument, so you always know whether you have the protection:

.. code-block:: text

   error: the timeout= kwarg is only supported under engine='regex'

Install it with ``pip install edify[regex]``. Note that the third-party engine also
optimizes away some of the shapes that make ``re`` backtrack, so switching engines
can resolve a slow pattern on its own — but neither the switch nor the timeout is a
substitute for bounding the quantifier.

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
