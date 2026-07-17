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

Pull the captured text out of a match by position:

.. code-block:: python

   pair = R().capture().word().end().char("=").capture().one_or_more().digit().end().to_regex()
   hit = pair.match("x=42")
   hit.group(1)   # 'x'
   hit.group(2)   # '42'

Named captures
--------------

Positions are easy to lose track of. :meth:`~edify.RegexBuilder.named_capture`
gives a capture a name instead:

.. code-block:: python

   year = R().named_capture("year").exactly(4).digit().end()
   year.to_regex_string()   # '(?P<year>\\d{4})'

and you read it back by that name — much clearer than counting parentheses:

.. code-block:: python

   date = (
       R().named_capture("year").exactly(4).digit().end()
       .char("-")
       .named_capture("month").exactly(2).digit().end()
       .to_regex()
   )
   hit = date.match("2024-07")
   hit.captures.year    # '2024'
   hit.captures.month   # '07'

That ``hit.captures`` namespace is edify's own — see :doc:`matching` for the
full match surface.

Backreferences
--------------

A backreference matches *the same text a capture already matched*. Refer to a
numbered capture with :meth:`~edify.RegexBuilder.back_reference` and a named one
with :meth:`~edify.RegexBuilder.named_back_reference`:

.. code-block:: python

   R().capture().word().end().back_reference(1).to_regex_string()
   # '(\\w)\\1'   — a word character, then the same one again

   R().named_capture("q").word().end().named_back_reference("q").to_regex_string()
   # '(?P<q>\\w)(?P=q)'

Backreferences are how you match balanced repetition — a doubled letter, or a
quoted string whose closing quote matches its opening one:

.. code-block:: python

   quoted = (
       R().named_capture("quote").any_of_chars("'\"").end()
       .one_or_more_lazy().any_char()
       .named_back_reference("quote")
       .to_regex()
   )
   quoted.search("say 'hi' now").group()   # "'hi'"
   quoted.search('say "hi" now').group()   # '"hi"'

Next: :doc:`lookaround`, for asserting what surrounds a match without consuming it.
