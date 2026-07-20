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
class. There is never any ambiguity about what a ``{4}`` attaches to, because
you wrote the ``4`` before the thing it counts.

Every builder is immutable
--------------------------

A chain method never changes the builder you called it on. It returns a **new**
builder and leaves the original exactly as it was:

.. code-block:: python

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

When you want an explicit, independent copy of a builder as-is, ask for one:

.. code-block:: python

   snapshot = digits.copy()   # a fresh builder with the same state (alias: .fork())

Because everything is immutable, ``copy`` is rarely necessary — two extensions
of the same base are already independent — but it makes intent obvious when you
are stashing a builder to branch from later.

Patterns compare by what they emit
----------------------------------

Two builders are equal when they emit the **same regex** — regardless of which
methods, factories, or operators produced them:

.. code-block:: python

   from edify import RegexBuilder, exactly, DIGIT

   RegexBuilder().exactly(3).digit() == RegexBuilder().exactly(3).digit()   # True
   RegexBuilder().exactly(3).digit() == exactly(3, DIGIT)                   # True
   RegexBuilder().exactly(3).digit() == RegexBuilder().exactly(4).digit()   # False

Equality is by value, and builders are hashable, so you can dedupe patterns in a
``set`` or key a ``dict`` by them. It also makes patterns trivial to test: assert
that a chain equals the shape you expect, and you're comparing intent, not
whitespace.

That's the whole mental model
-----------------------------

Say the quantity before the thing, trust that nothing you build ever mutates
something you built earlier, and remember that two patterns are the same when
they emit the same regex. The rest of the guide is just vocabulary: which tokens
exist, and what each one emits. Start with :doc:`anchors`.
