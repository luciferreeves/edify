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

A ``key=number`` pair — both sides must be present to match:

.. edify-playground::
   :tests: x=42|y=7|z=|=5

   RegexBuilder() \
       .capture().word().end() \
       .char("=") \
       .capture().one_or_more().digit().end()

Named captures
--------------

Positions are easy to lose track of. :meth:`~edify.RegexBuilder.named_capture`
gives a capture a name instead:

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
attribute on it, so you get autocomplete and a clear ``KeyError`` for a typo'd
name instead of a silent ``None``. The standard ``hit.groupdict()`` still works
too, if you'd rather have a plain dict:

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
:doc:`matching` for the full match surface.

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

The closing quote *must* be the same character as the opening one, because the
backreference demands it — a ``'`` opener will not match a ``"`` closer.

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

Try it
------

.. edify-playground::
   :tests: 2024-07|1999-12|2024|July

   RegexBuilder() \
       .named_capture("year").exactly(4).digit().end() \
       .char("-") \
       .named_capture("month").exactly(2).digit().end()

Next: :doc:`lookaround`, for asserting what surrounds a match without consuming it.
