Quantifiers
===========

A quantifier says *how many* of the next token to match. Remember the one habit
from :doc:`../start/thinking-in-edify`: the quantifier comes **before** the token it
governs.

Fixed counts
------------

.. code-block:: python

   from edify import RegexBuilder as R

   R().exactly(3).digit().to_regex_string()      # '\\d{3}'      exactly three
   R().at_least(2).digit().to_regex_string()     # '\\d{2,}'     two or more
   R().at_most(4).digit().to_regex_string()      # '\\d{0,4}'    up to four
   R().between(2, 5).digit().to_regex_string()   # '\\d{2,5}'    two to five

Exactly three digits — no more, no less:

.. edify-playground::
   :tests: 123|12|1234|abc

   RegexBuilder() \
       .start_of_input() \
       .exactly(3).digit() \
       .end_of_input()

Open-ended counts
-----------------

The three classic quantifiers have plain-English names:

.. code-block:: python

   from edify import RegexBuilder as R

   R().optional().char("s").to_regex_string()    # 's?'    zero or one
   R().zero_or_more().digit().to_regex_string()  # '\\d*'  zero or more
   R().one_or_more().digit().to_regex_string()   # '\\d+'  one or more

Greedy vs lazy
--------------

By default a quantifier is **greedy** — it matches as much as it can, then gives
characters back only if the rest of the pattern needs them. The ``_lazy``
variants flip that: they match as *little* as possible and expand only when
forced. Every open-ended and range quantifier has a lazy twin:

.. code-block:: python

   from edify import RegexBuilder as R

   R().one_or_more_lazy().digit().to_regex_string()    # '\\d+?'
   R().zero_or_more_lazy().digit().to_regex_string()   # '\\d*?'
   R().between_lazy(2, 5).digit().to_regex_string()    # '\\d{2,5}?'

The difference matters the moment you match between two delimiters. Greedy runs
to the *last* delimiter; lazy stops at the *first*:

.. code-block:: python

   from edify import RegexBuilder as R

   greedy = R().char("<").one_or_more().any_char().char(">").to_regex()
   lazy = R().char("<").one_or_more_lazy().any_char().char(">").to_regex()

   greedy.search("<a><b>").group()   # '<a><b>'  — grabbed everything
   lazy.search("<a><b>").group()     # '<a>'     — stopped at the first '>'

Reach for lazy when you want the *smallest* match; leave it greedy otherwise.

.. edify-playground::
   :tests: <a><b>|<hello>|<>|plain text

   RegexBuilder() \
       .char("<") \
       .one_or_more_lazy().any_char() \
       .char(">")

Swap ``one_or_more_lazy`` for ``one_or_more`` in that playground: the emitted regex
loses its ``?`` and ``<a><b>`` starts matching as a single span.

Lazy is not a performance fix. Both variants explore the same set of positions;
they differ only in which order they try them, so a lazy quantifier finds a
*different* match, not a faster one.

Possessive: no giving back
--------------------------

The one that *is* a performance fix is the third variant. A possessive quantifier
matches as much as it can, like a greedy one, and then refuses to give any of it
back — so there are no positions left to reconsider:

.. code-block:: python

   from edify import RegexBuilder as R

   R().one_or_more_possessive().digit().to_regex_string()      # '\\d++'
   R().zero_or_more_possessive().digit().to_regex_string()     # '\\d*+'
   R().optional_possessive().digit().to_regex_string()         # '\\d?+'
   R().at_least_possessive(2).digit().to_regex_string()        # '\\d{2,}+'
   R().at_most_possessive(4).digit().to_regex_string()         # '\\d{0,4}+'
   R().between_possessive(2, 5).digit().to_regex_string()      # '\\d{2,5}+'

That refusal changes what matches, not just how fast. Greedy ``a+`` will hand a
character back so a trailing ``a`` can match; possessive ``a++`` will not:

.. edify-playground::

   from edify import Pattern

   greedy = Pattern().start_of_input().one_or_more().char("a").char("a").end_of_input()
   possessive = Pattern().start_of_input().one_or_more_possessive().char("a").char("a").end_of_input()

   greedy("aa")       # the quantifier gives one 'a' back
   possessive("aa")   # it keeps both, so nothing is left for the final 'a'

So the three are a spectrum: **greedy** takes everything and negotiates,
**lazy** takes nothing and negotiates, **possessive** takes everything and does
not negotiate. Reach for possessive when the sub-pattern is genuinely
all-or-nothing — a token, a quoted string, a run of digits — and the rest of the
pattern has no business borrowing from it.

Both possessive quantifiers and :meth:`~edify.RegexBuilder.atomic` work on the
default engine; they reached the standard library in Python 3.11, which edify
already requires. For why this is the fix that matters, see
:doc:`../practice/performance`.

Bounded beats unbounded
-----------------------

When a field has a real maximum length, say so. ``between(1, 64)`` documents the
constraint, rejects oversized input for you, and caps the work an attacker can
force:

.. code-block:: python

   from edify import RegexBuilder as R

   bounded = R().start_of_input().between(1, 64).letter().end_of_input()
   bounded.to_regex_string()   # '^[a-zA-Z]{1,64}$'

``one_or_more`` is the right default only when the length genuinely has no limit.
Whenever it does, the bounded form is both more honest and safer against the
denial-of-service shapes covered in :doc:`../practice/performance`.

.. edify-playground::
   :tests: abc|a|ABCdef|abc1

   from edify import RegexBuilder

   RegexBuilder().start_of_input() \
       .between(1, 64).letter() \
       .end_of_input()

Quantifying a group
-------------------

A quantifier before a group repeats the entire group — see :doc:`groups` for the
grouping tokens:

.. code-block:: python

   from edify import RegexBuilder as R

   R().one_or_more().group().digit().char("-").end().to_regex_string()
   # '(?:\\d\\-)+'   — one or more "digit-dash" units

The same holds for a character class, an alternation, or a subexpression: the
quantifier attaches to whatever single token comes next, and a group *is* a
single token.

The functional form
-------------------

Every quantifier is also a standalone factory function that wraps the pattern it
counts — reading *"exactly three digits"* left to right:

.. code-block:: python

   from edify import exactly, one_or_more, between, DIGIT

   exactly(3, DIGIT).to_regex_string()       # '\\d{3}'
   one_or_more(DIGIT).to_regex_string()      # '\\d+'
   between(2, 5, DIGIT).to_regex_string()    # '\\d{2,5}'

The factories mirror the methods one-for-one — ``at_least``, ``at_most``,
``between``, ``optional``, ``zero_or_more``, ``one_or_more`` and their ``_lazy``
twins. See :doc:`../beyond/composing`.

Counts are validated
--------------------

The bounds have to make sense, and edify tells you when they don't rather than
emitting a nonsensical regex:

.. code-block:: python

   from edify import RegexBuilder as R

   from edify import EdifyError

   for build in (lambda: R().exactly(0).digit(), lambda: R().between(5, 2).digit()):
       try:
           build()
       except EdifyError as problem:
           print(problem)

   # error: count must be a positive integer
   #   help: pass an int >= 1 for count; use .optional() if you meant zero-or-one.
   # error: lower must be less than upper
   #   help: swap the two arguments so lower is the smaller value.

Both raise immediately at the call site, naming the parameter as it appears in the
signature you called — the diagnostics are covered on :doc:`../beyond/errors`.

A quantifier also has to have something to quantify. Ending a chain on one, or
stacking two, is an error rather than a silent no-op:

.. code-block:: python

   from edify import EdifyError, RegexBuilder as R

   try:
       R().digit().exactly(3).to_regex_string()
   except EdifyError as problem:
       print(problem)   # error: dangling .exactly(3) with no operand to apply to

   try:
       R().exactly(3).one_or_more().digit()
   except EdifyError as problem:
       print(problem)   # error: cannot stack a quantifier on top of another pending quantifier

Quick reference
---------------

Every quantifier, its factory function, and what it emits (``p`` is the token or
pattern it governs):

.. list-table::
   :header-rows: 1
   :widths: 34 34 32

   * - Method
     - Factory
     - Emits
   * - ``exactly(n)``
     - ``exactly(n, p)``
     - ``{n}``
   * - ``at_least(n)``
     - ``at_least(n, p)``
     - ``{n,}``
   * - ``at_most(n)``
     - ``at_most(n, p)``
     - ``{0,n}``
   * - ``between(a, b)``
     - ``between(a, b, p)``
     - ``{a,b}``
   * - ``optional()``
     - ``optional(p)``
     - ``?``
   * - ``zero_or_more()``
     - ``zero_or_more(p)``
     - ``*``
   * - ``one_or_more()``
     - ``one_or_more(p)``
     - ``+``
   * - ``between_lazy(a, b)``
     - ``between_lazy(a, b, p)``
     - ``{a,b}?``
   * - ``zero_or_more_lazy()``
     - ``zero_or_more_lazy(p)``
     - ``*?``
   * - ``one_or_more_lazy()``
     - ``one_or_more_lazy(p)``
     - ``+?``

Try it
------

.. edify-playground::
   :tests: <a><b>|<hello>|<>|plain text

   RegexBuilder() \
       .char("<") \
       .one_or_more_lazy().any_char() \
       .char(">")

Next: :doc:`groups`, for grouping and alternation.
