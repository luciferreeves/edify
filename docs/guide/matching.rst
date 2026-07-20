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
is this," anchor the pattern (:doc:`anchors`) or use ``fullmatch`` below.

These five are the everyday surface. When you want the full toolkit — including
``fullmatch``, ``finditer``, ``subn``, and ``split`` — compile the pattern into a
:class:`~edify.Regex` with :meth:`~edify.RegexBuilder.to_regex`:

.. code-block:: python

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

Compile once, reuse
-------------------

``to_regex`` caches: calling it again on the same builder returns the *same*
compiled object, so there's no cost to calling it wherever you need it.

.. code-block:: python

   digits.to_regex() is digits.to_regex()   # True

Compile in a module-level constant and match against it as often as you like.

Working with matches
--------------------

``match``, ``search``, and ``fullmatch`` return a :class:`~edify.result.Match` —
a thin wrapper over the standard match object with one extra convenience: named
captures are available as attributes on ``.captures``:

.. code-block:: python

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

Everything else you'd expect from a match object — ``group(n)``, ``groupdict()``,
``start()``, ``end()``, ``span()`` — is there too. See :doc:`captures` for the
capture side of the story.

Next: :doc:`errors`, on the diagnostics edify gives you when a pattern is wrong.
