Captures and backreferences
===========================

A capture is a group that *remembers* the text it matched, so you can pull it
back out after a match — or refer to it again later in the same pattern.

Capturing groups
----------------

:meth:`~edify.RegexBuilder.capture` works like :meth:`~edify.RegexBuilder.group`,
but the matched text is saved and numbered:

.. code-block:: python

   from edify import RegexBuilder as R

   R().capture().digit().end().to_regex_string()   # '(\\d)'

Pull the captured text out of a match by position. Group ``0`` is always the
whole match; your captures are numbered ``1``, ``2``, … from left to right by
opening parenthesis:

.. code-block:: python

   from edify import RegexBuilder as R

   pair = R().capture().word().end().char("=").capture().one_or_more().digit().end().to_regex()
   hit = pair.match("x=42")
   hit.group()    # 'x=42'  — group 0, the whole match
   hit.group(1)   # 'x'
   hit.group(2)   # '42'

Numbering follows the **opening** parenthesis, which is what makes nested
captures read in the order you wrote them rather than the order they close.

A ``key=number`` pair — both sides must be present to match:

.. edify-playground::
   :tests: x=42|y=7|z=|=5

   RegexBuilder() \
       .capture().word().end() \
       .char("=") \
       .capture().one_or_more().digit().end()

Named captures
--------------

Positions are easy to lose track of, and they shift the moment you insert a group
earlier in the pattern. :meth:`~edify.RegexBuilder.named_capture` gives a capture
a name instead:

.. code-block:: python

   from edify import RegexBuilder as R

   year = R().named_capture("year").exactly(4).digit().end()
   year.to_regex_string()   # '(?P<year>\\d{4})'

and you read it back by that name — much clearer than counting parentheses:

.. code-block:: python

   from edify import RegexBuilder as R

   date = (
       R().named_capture("year").exactly(4).digit().end()
       .char("-")
       .named_capture("month").exactly(2).digit().end()
       .to_regex()
   )
   hit = date.match("2024-07")
   hit.captures.year    # '2024'
   hit.captures.month   # '07'

That ``hit.captures`` object is a :class:`~edify.result.NamedCaptures` namespace —
edify's own convenience over the standard match. Every named group is an
attribute on it, so a typo fails immediately and tells you what the real names
are, instead of returning a silent ``None``:

.. code-block:: text

   AttributeError: named capture group 'yaer' does not exist on this pattern;
   declared groups are ['month', 'year']

The standard ``hit.groupdict()`` still works too, if you'd rather have a plain
dict:

.. code-block:: python

   from edify import RegexBuilder

   dated = (
       RegexBuilder()
       .named_capture("year").exactly(4).digit().end()
       .char("-")
       .named_capture("month").exactly(2).digit().end()
   )
   hit = dated.to_regex().match("2024-07")

   hit.groupdict()   # {'year': '2024', 'month': '07'}

Named and numbered captures coexist — a named group also has a number, so
``hit.group(1)`` and ``hit.captures.year`` reach the same text. See
:doc:`../beyond/matching` for the full match surface.

.. edify-playground::
   :tests: 2024-07|1999-12|2024|July

   RegexBuilder() \
       .named_capture("year").exactly(4).digit().end() \
       .char("-") \
       .named_capture("month").exactly(2).digit().end()

When a capture does not participate
-----------------------------------

A capture inside an optional part may never match at all. The pattern still
succeeds; that group is simply ``None``:

.. code-block:: python

   from edify import RegexBuilder as R

   tagged = (
       R().start_of_input()
       .named_capture("word").one_or_more().letter().end()
       .optional().group()
           .char("-").named_capture("num").one_or_more().digit().end()
       .end()
       .end_of_input()
       .to_regex()
   )
   tagged.source   # '^(?P<word>[a-zA-Z]+)(?:\\-(?P<num>\\d+))?$'

   tagged.match("abc").groupdict()      # {'word': 'abc', 'num': None}
   tagged.match("abc-12").groupdict()   # {'word': 'abc', 'num': '12'}

``None`` and ``''`` mean different things here — ``None`` is "this group never
matched", an empty string is "it matched nothing". Check for ``None`` explicitly
rather than relying on truthiness, or a legitimately empty capture will take the
same branch as an absent one.

A repeated capture keeps only the **last** repetition, because there is one slot
per group no matter how many times it matches:

.. code-block:: python

   from edify import RegexBuilder as R

   letters = R().one_or_more().capture().letter().end().to_regex()
   letters.source                    # '([a-zA-Z])+'
   letters.match("abc").group(1)     # 'c' — not 'abc'

To capture the whole run, put the quantifier *inside* the capture —
``capture().one_or_more().letter().end()`` — so the group spans every repetition
instead of being re-entered on each one.

.. edify-playground::
   :tests: abc|a|abc-12|-12

   from edify import RegexBuilder as R

   R().start_of_input() \
       .named_capture("word").one_or_more().letter().end() \
       .optional().group().char("-").named_capture("num").one_or_more().digit().end().end() \
       .end_of_input()

Backreferences
--------------

A backreference matches *the same text a capture already matched*. Refer to a
numbered capture with :meth:`~edify.RegexBuilder.back_reference` and a named one
with :meth:`~edify.RegexBuilder.named_back_reference`:

.. code-block:: python

   from edify import RegexBuilder as R

   R().capture().word().end().back_reference(1).to_regex_string()
   # '(\\w)\\1'   — a word character, then the same one again

   R().named_capture("q").word().end().named_back_reference("q").to_regex_string()
   # '(?P<q>\\w)(?P=q)'

This is the one thing on this page that no sequence of tokens can express. A
character class says "any of these"; a backreference says "whichever one you saw
before" — it carries information forward through the match.

Backreferences are how you match balanced repetition — a doubled letter, or a
quoted string whose closing quote matches its opening one:

.. code-block:: python

   from edify import RegexBuilder as R

   quoted = (
       R().named_capture("quote").any_of_chars("'\"").end()
       .one_or_more_lazy().any_char()
       .named_back_reference("quote")
       .to_regex()
   )
   quoted.search("say 'hi' now").group()   # "'hi'"
   quoted.search('say "hi" now').group()   # '"hi"'
   quoted.search("say 'hi\" now")          # None — the quotes must match

The closing quote *must* be the same character as the opening one, because the
backreference demands it. Note the lazy ``one_or_more_lazy``: a greedy body would
run to the *last* quote in the string rather than the first matching one. See
:doc:`quantifiers` for that distinction.

.. edify-playground::
   :tests: 'hi'|"hi"|'hi"|hi

   from edify import RegexBuilder as R

   R().named_capture("quote").any_of_chars("'\"").end() \
       .one_or_more_lazy().any_char() \
       .named_back_reference("quote")

Quick reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 40 24 36

   * - Method
     - Emits
     - Purpose
   * - ``capture()``
     - ``(…)``
     - a numbered capturing group
   * - ``named_capture(name)``
     - ``(?P<name>…)``
     - a named capturing group
   * - ``back_reference(n)``
     - ``\n``
     - rematch what capture ``n`` matched
   * - ``named_back_reference(name)``
     - ``(?P=name)``
     - rematch what the named capture matched

Read numbered captures back with ``hit.group(n)`` and named ones with
``hit.captures.name`` or ``hit.groupdict()``.

Next: :doc:`lookaround`, for asserting what surrounds a match without consuming it.
