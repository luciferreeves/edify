Groups and alternation
======================

Grouping bundles several tokens into one unit — so a quantifier can repeat the
whole thing, or an alternation can choose between whole branches.

Grouping
--------

:meth:`~edify.RegexBuilder.group` opens a non-capturing group; everything you
chain until :meth:`~edify.RegexBuilder.end` goes inside it:

.. code-block:: python

   from edify import RegexBuilder as R

   R().group().digit().letter().end().to_regex_string()   # '(?:\\d[a-zA-Z])'

A group on its own changes nothing about what matches — ``(?:\d[a-zA-Z])``
matches the same text as ``\d[a-zA-Z]``. It earns its keep the moment a
quantifier or alternation needs a single unit to operate on:

.. code-block:: python

   from edify import RegexBuilder as R

   R().exactly(3).group().digit().char("-").end().to_regex_string()
   # '(?:\\d\\-){3}'   — three "digit-dash" units

Without the group, ``exactly(3)`` would apply to whichever single token came
next, so ``\d-`` would become ``\d{3}-``: three digits and one dash, rather than
three of the pair. The group is what makes "the whole thing" a thing.

One or more "digit-dash" units — the quantifier repeats the whole group:

.. edify-playground::
   :tests: 1-2-|9-|12|abc

   RegexBuilder() \
       .one_or_more() \
       .group().digit().char("-").end()

A non-capturing group is invisible to the match results. When you actually want
to pull the text back out, reach for a *capturing* group instead — that's the
subject of :doc:`captures`.

Alternation
-----------

:meth:`~edify.RegexBuilder.any_of` matches any one of several branches. Pass the
alternatives as strings for the common case:

.. code-block:: python

   from edify import RegexBuilder as R

   R().any_of("cat", "dog", "fish").to_regex_string()   # '(?:cat|dog|fish)'

Open ``any_of`` with no arguments to add branches one at a time, closing with
``end``. **Every call inside becomes its own branch**, so a chain of four calls
gives four alternatives, not one four-token branch:

.. code-block:: python

   from edify import RegexBuilder as R

   R().any_of().string("cat").string("dog").end().to_regex_string()
   # '(?:cat|dog)'   — two branches

For a branch that is more than one token, build it as a pattern and drop it in
with :meth:`~edify.RegexBuilder.use`. That is the only way to keep several tokens
together inside a single alternative:

.. code-block:: python

   from edify import Pattern, RegexBuilder as R

   numbered = Pattern().string("id-").one_or_more().digit()
   named = Pattern().string("name-").one_or_more().letter()

   R().any_of().use(numbered).use(named).end().to_regex_string()
   # '(?:id\\-\\d+|name\\-[a-zA-Z]+)'

.. edify-playground::
   :tests: id-42|name-bob|id-bob|other

   from edify import Pattern, RegexBuilder as R

   numbered = Pattern().string("id-").one_or_more().digit()
   named = Pattern().string("name-").one_or_more().letter()

   R().start_of_input().any_of().use(numbered).use(named).end().end_of_input()

:meth:`~edify.RegexBuilder.one_of` is the same idea, specialized to a list of
string literals:

.. code-block:: python

   from edify import RegexBuilder as R

   R().one_of("GET", "POST", "PUT").to_regex_string()   # '(?:GET|POST|PUT)'

.. note::

   When every alternative is a single character, edify folds the alternation into
   a character class instead — ``any_of("a", "b", "c")`` emits ``[abc]``, which
   matches the same text more efficiently.

Branch order matters
--------------------

A regex alternation is **first-match-wins**, not longest-match-wins. The engine
tries branches left to right and stops at the first that succeeds — so a branch
that is a prefix of a later one will shadow it:

.. code-block:: python

   from edify import RegexBuilder as R

   R().any_of("http", "https").to_regex().search("https").group()   # 'http'
   R().any_of("https", "http").to_regex().search("https").group()   # 'https'

Put the **longest** alternative first whenever one branch prefixes another. The
same rule is why the ``hexcolor`` atom orders its branches ``8|6|4|3``, and why
:doc:`../../library/address/ipv4` orders its octet branches from ``25[0-5]``
downward.

Anchoring hides the problem — ``^(?:http|https)$`` matches ``https`` correctly,
because the shorter branch fails the end anchor and the engine backtracks into
the longer one. That is exactly what makes this bug so easy to ship: it passes
every test against an anchored pattern and then misbehaves the first time the
fragment is reused unanchored.

.. edify-playground::
   :tests: https|http|ftp

   from edify import RegexBuilder

   RegexBuilder().any_of("https", "http")

Making branches disjoint
------------------------

Better than ordering carefully is not needing to. When no two branches can match
the same text, order is irrelevant and the engine never has to backtrack between
them — which also removes a source of the slowdowns in
:doc:`../practice/performance`.

The octet pattern is the model: ``(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)`` covers
0–255 in five branches that share no input at all. Exactly one can ever apply, for
any string.

The functional form
-------------------

:func:`~edify.group` and :func:`~edify.any_of` also exist as factory functions
that take the patterns they wrap, for composing without a leading builder:

.. code-block:: python

   from edify import group, any_of, one_or_more, DIGIT, string

   group(one_or_more(DIGIT)).to_regex_string()       # '(?:\\d+)'
   any_of(string("cat"), string("dog")).to_regex_string()   # '(?:cat|dog)'

Nesting and reuse
-----------------

Groups nest freely, and you can drop a whole pre-built pattern into a chain with
:meth:`~edify.RegexBuilder.subexpression` (or its alias
:meth:`~edify.RegexBuilder.use`). That is how you compose bigger patterns from
named pieces — the subject of :doc:`../beyond/composing`:

.. code-block:: python

   from edify import RegexBuilder as R

   word = R().one_or_more().word()
   csv_field = (
       R().use(word)
       .zero_or_more().group().char(",").use(word).end()
   )
   csv_field.to_regex_string()   # '\\w+(?:,\\w+)*'

That ``item (separator item)*`` shape is the standard idiom for a delimited list:
it requires at least one item and permits no trailing separator, which a simpler
``(item separator)+`` would wrongly accept.

.. edify-playground::
   :tests: a,b,c|single|a,b,|,a

   from edify import RegexBuilder as R

   word = R().one_or_more().word()
   R().start_of_input() \
       .use(word) \
       .zero_or_more().group().char(",").use(word).end() \
       .end_of_input()

Quick reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 34 30 36

   * - Method
     - Factory
     - Emits
   * - ``group()``
     - ``group(p)``
     - ``(?:…)`` — non-capturing group
   * - ``capture()``
     - ``capture(p)``
     - ``(…)`` — capturing group (see :doc:`captures`)
   * - ``any_of(*branches)``
     - ``any_of(*patterns)``
     - ``(?:a|b|c)`` — alternation
   * - ``one_of(*literals)``
     - —
     - ``(?:a|b|c)`` — alternation of string literals

Next: :doc:`captures`, for pulling matched text back out.
