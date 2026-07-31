Matching
========

You've built a pattern. Now run it against text.

Two ways to run
---------------

For a quick check, the builder itself exposes five verbs — ``test``, ``match``,
``search``, ``findall``, and ``sub``:

.. code-block:: python

   from edify import RegexBuilder as R

   digits = R().one_or_more().digit()

   digits.test("42")             # True   — does the pattern match anywhere?
   digits.match("42")            # a Match at the start, or None
   digits.search("x42").group()  # '42'   — first match anywhere
   digits.findall("1 22 333")    # ['1', '22', '333']
   digits.sub("#", "a1b2")       # 'a#b#'

``test`` uses *search* semantics — it returns ``True`` if the pattern matches
**anywhere** in the string, not only end-to-end. When you mean "the whole string
is this," anchor the pattern (:doc:`../builder/anchors`) or use ``fullmatch`` below.

These five are the everyday surface. When you want the full toolkit — including
``fullmatch``, ``finditer``, ``subn``, and ``split`` — compile the pattern into a
:class:`~edify.Regex` with :meth:`~edify.RegexBuilder.to_regex`:

.. code-block:: python

   from edify import RegexBuilder

   digits = RegexBuilder().one_or_more().digit()

   rx = digits.to_regex()

   rx.fullmatch("42")               # a Match, or None — the whole string must match
   list(rx.finditer("1 22 333"))    # every match, lazily
   rx.subn("#", "a1b2")             # ('a#b#', 2)  — result and count
   rx.split("a1b2c")                # ['a', 'b', 'c']

A compiled :class:`~edify.Regex` forwards every method of the underlying
standard-library pattern, so anything ``re.Pattern`` can do, it can do — plus the
introspection conveniences from :doc:`seeing` (``rx.explain()``,
``rx.visualize()``, ``rx.to_verbose_string()``). The one verb it does *not*
carry is ``test``; that lives on the builder.

Match, search, fullmatch
------------------------

The three finders differ only in *where* the match is allowed to start and end,
and mixing them up is the most common cause of a validator that lets bad input
through:

- :meth:`~edify.Regex.match` anchors at position 0. The match must *start* at the
  beginning, but may end anywhere.
- :meth:`~edify.Regex.search` scans forward until it finds a match anywhere.
- :meth:`~edify.Regex.fullmatch` requires the match to cover the *entire* string.

.. code-block:: python

   from edify import RegexBuilder

   digits = RegexBuilder().one_or_more().digit().to_regex()

   digits.match("42abc")       # a Match — starts at 0, ends early
   digits.match("abc42")       # None    — does not start at 0
   digits.search("abc42")      # a Match — found at position 3
   digits.fullmatch("42abc")   # None    — trailing text is not allowed
   digits.fullmatch("42")      # a Match

Reach for ``fullmatch`` when the pattern is unanchored but you mean the whole
string. Bake the anchors in instead when the pattern will travel — as a library
validator or a constant — so the intent stays attached to it. With the anchors
present, only the bare digits match:

.. edify-playground::
   :tests: 42|42abc|abc42|abc

   from edify import RegexBuilder

   RegexBuilder().start_of_input() \
       .one_or_more().digit() \
       .end_of_input()

Remove ``.start_of_input()`` and ``42abc`` starts matching; remove both and every
string containing a digit does.

Iterating every match
---------------------

:meth:`~edify.Regex.findall` gives you the matched strings.
:meth:`~edify.Regex.finditer` gives you match objects instead, so you also get
positions — and, when the pattern captures, the fields:

.. code-block:: python

   from edify import RegexBuilder as R

   digits = R().one_or_more().digit().to_regex()
   [(m.group(), m.span()) for m in digits.finditer("1 22 333")]
   # [('1', (0, 1)), ('22', (2, 4)), ('333', (5, 8))]

   setting = (
       R().named_capture("k").one_or_more().word().end()
       .char("=")
       .named_capture("v").one_or_more().word().end()
       .to_regex()
   )
   [(m.captures.k, m.captures.v) for m in setting.finditer("a=1 b=2")]
   # [('a', '1'), ('b', '2')]

``finditer`` is lazy, so it costs nothing to point it at a large document and stop
early. Prefer it over ``findall`` whenever you need more than the matched text.

.. edify-playground::
   :tests: a=1 b=2|timeout=30|=1|abc

   from edify import RegexBuilder as R

   R().named_capture("k").one_or_more().word().end() \
       .char("=") \
       .named_capture("v").one_or_more().word().end()

Replacing and splitting
-----------------------

:meth:`~edify.Regex.sub` replaces every match. The replacement can reference
captures with Python's ``\g<name>`` syntax, or be a **function** that receives each
match — which is how you do a replacement that depends on what was matched:

.. code-block:: python

   from edify import RegexBuilder

   digits = RegexBuilder().one_or_more().digit().to_regex()

   digits.sub("#", "a1b2")                                # 'a#b#'
   digits.subn("#", "a1b2")                               # ('a#b#', 2)
   digits.sub(lambda m: str(int(m.group()) * 2), "a1b2")  # 'a2b4'

:meth:`~edify.Regex.split` breaks a string on the pattern, and takes a limit:

.. code-block:: python

   from edify import RegexBuilder

   digits = RegexBuilder().one_or_more().digit().to_regex()

   digits.split("a1b2c3d")      # ['a', 'b', 'c', 'd']
   digits.split("a1b2c3d", 1)   # ['a', 'b2c3d'] — split at most once

Compile once, reuse
-------------------

``to_regex`` caches: calling it again on the same builder returns the *same*
compiled object, so there's no cost to calling it wherever you need it.

.. code-block:: python

   from edify import RegexBuilder

   digits = RegexBuilder().one_or_more().digit()

   digits.to_regex() is digits.to_regex()   # True

Compile in a module-level constant and match against it as often as you like. The
compiled object also carries the raw pieces, for when the pattern has to be handed
to something else:

.. code-block:: python

   from edify import RegexBuilder

   compiled_digits = RegexBuilder().one_or_more().digit().to_regex()

   compiled_digits.source     # '\\d+'              — the emitted pattern string
   compiled_digits.compiled   # re.compile('\\d+')  — the standard-library object
   compiled_digits.engine     # 're'                — which engine compiled it

Working with matches
--------------------

``match``, ``search``, and ``fullmatch`` return a :class:`~edify.result.Match` —
a thin wrapper over the standard match object with one extra convenience: named
captures are available as attributes on ``.captures``:

.. code-block:: python

   from edify import RegexBuilder as R

   date = (
       R().named_capture("year").exactly(4).digit().end()
       .char("-")
       .named_capture("month").exactly(2).digit().end()
       .to_regex()
   )

   hit = date.match("2024-07")
   hit.group()          # '2024-07'   — the whole match
   hit.captures.year    # '2024'
   hit.captures.month   # '07'

Attribute access fails loudly on a typo, where ``groupdict()["yaer"]`` raises a
``KeyError`` far from the mistake. Everything else you'd expect from a match object
is there too — ``group(n)``, ``groups()``, ``groupdict()``, ``start()``, ``end()``,
``span()``, ``expand()``, ``lastgroup``, and the original ``string``:

.. code-block:: python

   from edify import RegexBuilder as R

   month_of = (
       R().named_capture("year").exactly(4).digit().end()
       .char("-")
       .named_capture("month").exactly(2).digit().end()
       .to_regex()
   )
   found = month_of.match("2024-07")

   found.groups()      # ('2024', '07')
   found.groupdict()   # {'year': '2024', 'month': '07'}
   found.span()        # (0, 7)
   found.lastgroup     # 'month'

See :doc:`../builder/captures` for the capture side of the story.

.. edify-playground::
   :tests: 2024-07|2024-7|24-07|2024-07-15

   from edify import RegexBuilder as R

   R().start_of_input() \
       .named_capture("year").exactly(4).digit().end() \
       .char("-") \
       .named_capture("month").exactly(2).digit().end() \
       .end_of_input()

Quick reference
---------------

Which verbs live where, and what each returns:

.. list-table::
   :header-rows: 1
   :widths: 22 14 16 48

   * - Verb
     - Builder
     - Regex
     - Returns
   * - ``test(s)``
     - yes
     - —
     - ``bool`` — matches anywhere?
   * - ``match(s)``
     - yes
     - yes
     - a :class:`~edify.result.Match` at the start, or ``None``
   * - ``search(s)``
     - yes
     - yes
     - the first :class:`~edify.result.Match` anywhere, or ``None``
   * - ``fullmatch(s)``
     - —
     - yes
     - a :class:`~edify.result.Match` if the whole string matches, or ``None``
   * - ``findall(s)``
     - yes
     - yes
     - a ``list`` of every match
   * - ``finditer(s)``
     - —
     - yes
     - an iterator of :class:`~edify.result.Match`
   * - ``sub(repl, s)``
     - yes
     - yes
     - ``str`` with matches replaced
   * - ``subn(repl, s)``
     - —
     - yes
     - ``(str, count)``
   * - ``split(s)``
     - —
     - yes
     - a ``list`` split on the pattern

Next: :doc:`errors`, on the diagnostics edify gives you when a pattern is wrong.
