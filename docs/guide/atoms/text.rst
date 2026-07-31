Text atoms
==========

Fourteen fragments for characters, classes, and simple word shapes — the pieces
behind the :doc:`../../library/text/index` validators.

Compose them into an anchored pattern rather than calling them directly; see
:doc:`index`.

Single characters
-----------------

Five atoms match exactly one character each, differing only in which characters
they admit:

.. list-table::
   :header-rows: 1
   :widths: 18 24 58

   * - Atom
     - Emits
     - Matches
   * - ``letter``
     - ``[a-zA-Z]``
     - one ASCII letter, either case
   * - ``lower``
     - ``[a-z]``
     - one lowercase ASCII letter
   * - ``upper``
     - ``[A-Z]``
     - one uppercase ASCII letter
   * - ``alnum``
     - ``[a-zA-Z0-9]``
     - one ASCII letter or digit
   * - ``space``
     - ``\s``
     - one whitespace character, any script

All five are ASCII-only except ``space``, which is the Unicode-aware ``\s``. That
asymmetry is deliberate — it mirrors the builder's own
:meth:`~edify.RegexBuilder.letter` and :meth:`~edify.RegexBuilder.whitespace_char`.
:doc:`../practice/unicode` covers when the ASCII restriction is what you want and
when it quietly breaks on real input.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import letter, lower, upper, alnum

   one_letter = Pattern().start_of_input().use(letter).end_of_input()
   one_lower = Pattern().start_of_input().use(lower).end_of_input()
   one_upper = Pattern().start_of_input().use(upper).end_of_input()
   one_alnum = Pattern().start_of_input().use(alnum).end_of_input()

   one_letter("a")     # a single letter
   one_letter("ab")    # not two
   one_lower("a")
   one_lower("A")      # case matters
   one_upper("A")
   one_alnum("7")      # digits count as alphanumeric

Because each is exactly one character, quantify it in your own chain when you
want a run — ``Pattern().one_or_more().use(letter)`` rather than looking for a
plural atom.

Character ranges
----------------

``ascii`` and ``printable`` are also single characters, but defined by codepoint
range rather than by class. ``ascii`` emits ``[\x00-\x7f]`` — the whole 7-bit
range, control characters included. ``printable`` emits ``[ -~]``, which is space
through tilde: the visible ASCII characters plus the space, and nothing else.

.. code-block:: python

   from edify import Pattern
   from edify.atoms import ascii, printable

   Pattern().use(ascii).to_regex_string()       # '[\\x00-\\x7f]'
   Pattern().use(printable).to_regex_string()   # '[ -~]'

The gap between them is where the bugs live: a tab is ``ascii`` but not
``printable``, and ``é`` is neither. Reach for ``printable`` when you are
rejecting control characters from a field a human typed, and ``ascii`` when you
genuinely mean the byte range.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import ascii, printable

   any_ascii = Pattern().start_of_input().use(ascii).end_of_input()
   visible = Pattern().start_of_input().use(printable).end_of_input()

   any_ascii("a")          # inside the 7-bit range
   any_ascii("\t")         # a tab is still ASCII
   any_ascii("é")          # but this is not
   visible("~")            # the top of the printable range
   visible(" ")            # space is printable
   visible("\t")           # a tab is not

Runs
----

Two atoms match more than one character. ``word`` is ``\w+`` — a run of word
characters, and Unicode-aware, so it accepts ``héllo`` as readily as ``hello``.
``line`` is ``[^\r\n]+`` — everything up to a line break, and it requires at least
one character, so an empty line does not match.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import line, word

   run = Pattern().start_of_input().use(word).end_of_input()
   whole_line = Pattern().start_of_input().use(line).end_of_input()

   run("hello_world")     # letters, digits, underscore
   run("héllo")           # \w is Unicode-aware
   run("hello world")     # a space is not a word character
   whole_line("a whole line")
   whole_line("x")

Word shapes
-----------

``slug`` is a lowercase hyphenated identifier: one or more groups of ``[a-z0-9]``
joined by single hyphens. That structure is what rejects a leading hyphen, a
trailing hyphen, and a doubled one — a plain ``[a-z0-9-]+`` would accept all
three.

``quoted`` is a double-quoted span, ``"[^"]*"``. The quotes are part of the match,
the body may be empty, and it cannot span two separate quoted strings because the
body excludes the quote character.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import quoted, slug

   handle = Pattern().start_of_input().use(slug).end_of_input()
   span = Pattern().start_of_input().use(quoted).end_of_input()

   handle("hello-world")
   handle("Hello-World")     # slugs are lowercase
   handle("hello--world")    # single hyphens only
   handle("-a")              # and not at the edges
   span('"a value"')         # quotes included
   span('""')                # quotes with nothing between them still match
   span('"a" and "b"')       # but not two spans

Neither handles escaping. A quoted string containing ``\"`` needs a pattern that
understands the escape — build it with :meth:`~edify.RegexBuilder.any_of` rather
than reaching for this atom.

Truthy words
------------

Three atoms cover the ways a boolean is spelled in configuration and data files,
and they nest: everything ``truefalse`` accepts, ``boolean`` accepts too.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Atom
     - Accepts
   * - ``truefalse``
     - ``true`` / ``false`` in lower, title, and upper case
   * - ``yesno``
     - ``yes`` / ``no`` in three cases, plus the single letters ``y`` and ``n``
   * - ``boolean``
     - all of the above, plus ``on`` / ``off`` and the digits ``1`` and ``0``

Pick the narrowest one that covers your format. ``boolean`` accepting ``1`` and
``0`` is exactly right for an environment variable and exactly wrong for a field
where a bare digit should be a number.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import boolean, truefalse, yesno

   b = Pattern().start_of_input().use(boolean).end_of_input()
   tf = Pattern().start_of_input().use(truefalse).end_of_input()
   yn = Pattern().start_of_input().use(yesno).end_of_input()

   b("true")
   b("on")        # boolean accepts on/off
   b("1")         # and bare digits
   tf("on")       # truefalse does not
   tf("TRUE")     # but does accept any case spelling
   yn("y")        # single letters count
   yn("maybe")

Next: :doc:`encodings`.
