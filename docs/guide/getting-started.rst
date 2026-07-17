Getting started
===============

Install
-------

Edify needs Python 3.11 or newer. Install it from PyPI:

.. code-block:: bash

   pip install edify

That is everything you need to build patterns and use the whole validator
library. A few features live behind optional extras so a plain install stays
lean:

.. code-block:: bash

   pip install edify[regex]      # the third-party regex engine backend
   pip install edify[pydantic]   # pydantic integration
   pip install edify[fastapi]    # FastAPI integration
   pip install edify[django]     # Django integration
   pip install edify[all]        # everything above

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

To actually match something, compile it once and reuse the result:

.. code-block:: python

   year = four_digit_year.to_regex()

   year.test("2024")     # True
   year.test("abcd")     # False
   year.match("2024")    # a Match object

You can also test straight off the builder while you are exploring:

.. code-block:: python

   four_digit_year.test("2024")   # True

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

Where to go next
----------------

:doc:`thinking-in-edify` explains the two habits that make the rest of the
library predictable — quantifiers-before-tokens and immutability — and then the
guide walks the whole builder surface one topic at a time.
