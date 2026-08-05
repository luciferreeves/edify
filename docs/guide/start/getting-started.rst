Getting started
===============

Install
-------

Edify needs Python 3.11 or newer. Install it from PyPI:

.. code-block:: bash

   pip install edify

That is everything you need to build patterns and use the whole 228-strong
validator library. A few features live behind optional extras so a plain install
stays lean:

.. code-block:: bash

   pip install edify[regex]      # alternate engine: Unicode classes, variable-width lookbehind, timeouts
   pip install edify[graphviz]   # vector (SVG/PNG) pattern diagrams
   pip install edify[pydantic]   # pydantic integration
   pip install edify[fastapi]    # FastAPI integration
   pip install edify[django]     # Django integration
   pip install edify[all]        # everything above

Extras are additive — ``pip install edify[regex,pydantic]`` installs both. None
of them change the core API; they light up an engine, a diagram format, or a
framework binding when you ask for it.

Your first pattern
------------------

A pattern is a chain. You start a builder, describe the shape step by step, and
finish by turning it into a regex:

.. code-block:: python

   from edify import RegexBuilder

   four_digit_year = (
       RegexBuilder()
       .start_of_input()
       .exactly(4).digit()
       .end_of_input()
   )

   four_digit_year.to_regex_string()   # '^\\d{4}$'

Read the chain out loud and it says what it does: *start of input, exactly four
digits, end of input.* That is the whole idea — the code and the intent are the
same thing.

Edit that chain and watch the regex — and the test results — update live:

.. edify-playground::
   :tests: 2024|1999|90210|abcd

   RegexBuilder() \
       .start_of_input() \
       .exactly(4).digit() \
       .end_of_input()

To actually match something, compile it once and reuse the result. A compiled
:class:`~edify.Regex` carries the full ``re`` surface:

.. code-block:: python

   from edify import RegexBuilder

   four_digit_year = RegexBuilder().start_of_input().exactly(4).digit().end_of_input()

   year = four_digit_year.to_regex()

   year.match("2024")             # a Match object
   year.match("abcd")             # None
   bool(year.fullmatch("2024"))   # True

You can also check a string straight off the builder while you are exploring —
every builder carries five match verbs itself (``test``, ``match``, ``search``,
``findall``, ``sub``):

.. code-block:: python

   from edify import RegexBuilder

   four_digit_year = RegexBuilder().start_of_input().exactly(4).digit().end_of_input()

   four_digit_year.test("2024")   # True  — does the pattern match anywhere?

``Pattern`` vs ``RegexBuilder``
-------------------------------

Edify gives you two entry points. They share the exact same building methods,
so anything you can do with one you can do with the other. The difference is
intent:

``RegexBuilder``
   The fluent builder you reach for to describe a **complete** expression, like
   the year matcher above. Immutable: every method returns a new builder and
   never mutates the one you called it on.

``Pattern``
   A named, **reusable fragment** that is also directly **callable** as a
   validator. The entire built-in library is made of ``Pattern`` objects — that
   is why you can call one like a function:

   .. code-block:: python

      from edify import Pattern

      area_code = Pattern().exactly(3).digit()   # a reusable fragment
      area_code("555")                            # True  — call it like a validator
      area_code("55")                             # False

   Drop a ``Pattern`` into any chain with :meth:`~edify.RegexBuilder.use`:

   .. code-block:: python

      from edify import RegexBuilder, Pattern

      area_code = Pattern().exactly(3).digit()
      phone = RegexBuilder().use(area_code).char("-").exactly(4).digit()
      phone.to_regex_string()   # '\\d{3}\\-\\d{4}'

Reach for ``RegexBuilder`` when you are writing an expression, and ``Pattern``
when you are naming a piece to reuse or a rule to check against.

What's in the box
-----------------

The builder is the foundation, but Edify ships a whole toolkit around it:

- **The builder** — anchors, character classes, quantifiers, groups, captures,
  lookaround, and flags, one topic per page starting at :doc:`../builder/anchors`.
- **228 ready-made validators** — email, URL, semver, IBAN, phone, and hundreds
  more, each a callable ``Pattern``. Browse them in the :doc:`../../library/index`.
- **A match API** — five verbs on every builder plus the full ``re`` surface on a
  compiled pattern (:doc:`../beyond/matching`).
- **Introspection** — turn any pattern into a plain-English explanation, an ASCII
  or vector diagram, or an annotated verbose form (:doc:`../beyond/seeing`).
- **Round-trip serialization** — store a pattern as a dict or JSON and rebuild it
  exactly (:doc:`../beyond/serialization`).
- **Framework integrations** — pydantic, FastAPI, and Django bindings
  (:doc:`../beyond/integrations`).

Where to go next
----------------

:doc:`thinking-in-edify` explains the two habits that make the rest of the
library predictable — quantifiers-before-tokens and immutability — and then the
guide walks the whole builder surface one topic at a time.
