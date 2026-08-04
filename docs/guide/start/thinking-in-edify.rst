Thinking in edify
=================

Three habits make the entire library predictable. Learn them once here and every
later topic reads the same way.

Quantifiers come before the token
---------------------------------

In a raw regex, the quantifier trails the thing it repeats: ``\d{4}``. In
edify, you say the quantity **first**, then the thing — exactly the way you'd
say it in English:

.. code-block:: python

   from edify import RegexBuilder

   RegexBuilder().exactly(4).digit().to_regex_string()      # '\\d{4}'
   RegexBuilder().one_or_more().letter().to_regex_string()  # '[a-zA-Z]+'
   RegexBuilder().optional().char("s").to_regex_string()    # 's?'

*"Exactly four digits." "One or more letters." "An optional s."* The quantifier
modifies whatever token you chain next. This holds everywhere: a quantifier
before a group repeats the whole group, a quantifier before a class repeats the
class.

.. code-block:: python

   from edify import RegexBuilder

   RegexBuilder().exactly(3).group().digit().char("-").end().to_regex_string()
   # '(?:\\d\\-){3}'

   RegexBuilder().exactly(3).any_of_chars("abc").to_regex_string()
   # '[abc]{3}'

There is never any ambiguity about what a ``{3}`` attaches to, because you wrote
the ``3`` before the thing it counts. Compare that to reading ``(?:\d\-){3}``
cold and having to scan backwards for the matching parenthesis.

.. edify-playground::
   :tests: 1-2-3-|1-2-|1-2-3-4-|abc

   from edify import RegexBuilder

   RegexBuilder().start_of_input() \
       .exactly(3).group().digit().char("-").end() \
       .end_of_input()

The rule has a corollary: a quantifier with nothing after it is an error, not a
silent no-op. So is stacking two quantifiers, since the second would have nothing
of its own to repeat:

.. code-block:: python

   from edify import EdifyError, RegexBuilder

   try:
       RegexBuilder().digit().exactly(3).to_regex_string()
   except EdifyError as problem:
       print(problem)   # error: dangling .exactly(3) with no operand to apply to

   try:
       RegexBuilder().exactly(3).one_or_more().digit()
   except EdifyError as problem:
       print(problem)   # error: cannot stack a quantifier on top of another pending quantifier

Both diagnostics point at the exact call and suggest the fix — see
:doc:`../beyond/errors` for the full anatomy.

Every builder is immutable
--------------------------

A chain method never changes the builder you called it on. It returns a **new**
builder and leaves the original exactly as it was:

.. code-block:: python

   from edify import RegexBuilder

   base = RegexBuilder().start_of_input()

   digits = base.one_or_more().digit()
   letters = base.one_or_more().letter()

   base.to_regex_string()      # '^'          — untouched
   digits.to_regex_string()    # '^\\d+'
   letters.to_regex_string()   # '^[a-zA-Z]+'

This is a hard contract, not a convention. Because the receiver is never
mutated, a base builder is safe to share — hold it in a module-level constant,
capture it in a closure, hand it to another thread — and extend it any number
of ways without the extensions ever interfering with each other.

It is also what makes the whole library composable. The 83 fragments in
:doc:`../atoms/index` are shared by every validator in the
:doc:`../../library/index` simultaneously; if a builder could be mutated, each
one would need a defensive copy.

When you want an explicit, independent copy of a builder as-is, ask for one:

.. code-block:: python

   from edify import RegexBuilder

   digits = RegexBuilder().one_or_more().digit()

   snapshot = digits.copy()   # a fresh builder with the same state (alias: .fork())

Because everything is immutable, ``copy`` is rarely necessary — two extensions
of the same base are already independent — but it makes intent obvious when you
are stashing a builder to branch from later.

.. edify-playground::
   :tests: 42|4|abc|42a

   from edify import RegexBuilder

   base = RegexBuilder().start_of_input()
   base.one_or_more().digit().end_of_input()

Patterns compare by what they emit
----------------------------------

Two builders are equal when they emit the **same regex** — regardless of which
methods, factories, or operators produced them:

.. code-block:: python

   from edify import RegexBuilder, exactly, DIGIT

   RegexBuilder().exactly(3).digit() == RegexBuilder().exactly(3).digit()   # True
   RegexBuilder().exactly(3).digit() == exactly(3, DIGIT)                   # True
   RegexBuilder().exactly(3).digit() == RegexBuilder().exactly(4).digit()   # False

Equality is by value, and builders are hashable to match, so you can dedupe
patterns in a ``set`` or key a ``dict`` by them:

.. code-block:: python

   from edify import RegexBuilder, exactly, DIGIT

   distinct = {
       RegexBuilder().exactly(3).digit(),
       exactly(3, DIGIT),                    # same emission — collapses with the first
       RegexBuilder().exactly(4).digit(),
   }
   len(distinct)   # 2

It also makes patterns trivial to test: assert that a chain equals the shape you
expect, and you're comparing intent, not whitespace. A builder's ``repr`` shows
the emission too, so a failing assertion reads clearly:

.. code-block:: python

   from edify import RegexBuilder

   repr(RegexBuilder().exactly(3).digit())   # "<RegexBuilder '\\\\d{3}'>"

One thing to keep straight: equality compares the *emitted regex*, not meaning.
Two chains that match identically but emit different text are not equal:

.. code-block:: python

   from edify import RegexBuilder

   RegexBuilder().one_or_more().digit().to_regex_string()   # '\\d+'
   RegexBuilder().at_least(1).digit().to_regex_string()     # '\\d{1,}'

   RegexBuilder().one_or_more().digit() == RegexBuilder().at_least(1).digit()   # False

Both accept exactly the same strings. Equality is a statement about output, which
is what makes it useful for snapshot tests — and why it is the wrong tool for
asking "do these two patterns accept the same language?"

That's the whole mental model
-----------------------------

Say the quantity before the thing, trust that nothing you build ever mutates
something you built earlier, and remember that two patterns are the same when
they emit the same regex. The rest of the guide is just vocabulary: which tokens
exist, and what each one emits. Start with :doc:`../builder/anchors`.
