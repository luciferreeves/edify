Lookaround
==========

Lookaround assertions check what comes before or after the current position
*without consuming it*. The match still ends where your real tokens end — the
assertion just has to hold at that spot.

Lookahead
---------

:meth:`~edify.RegexBuilder.assert_ahead` requires that what follows matches;
:meth:`~edify.RegexBuilder.assert_not_ahead` requires that it does *not*. Open
the assertion, describe what to look for, and close it with
:meth:`~edify.RegexBuilder.end`:

.. code-block:: python

   from edify import RegexBuilder as R

   R().digit().assert_ahead().string("px").end().to_regex_string()
   # '\\d(?=px)'    a digit, but only if 'px' follows

   R().digit().assert_not_ahead().string("px").end().to_regex_string()
   # '\\d(?!px)'    a digit, but only if 'px' does NOT follow

Because the assertion consumes nothing, the ``px`` is checked but not included
in the match:

.. code-block:: python

   from edify import RegexBuilder as R

   before_px = R().one_or_more().digit().assert_ahead().string("px").end().to_regex()
   before_px.search("16px").group()   # '16'  — the 'px' matched the lookahead, but isn't captured

That is the whole point: you constrain the context without paying for it in the
result. A capture group would have got you the same match but also a group you
have to ignore, and it would have consumed the ``px`` so the next match could not
start there.

Digits, but only when ``px`` follows — ``16em`` and a bare ``px`` don't match:

.. edify-playground::
   :tests: 16px|24px|16em|px

   RegexBuilder() \
       .one_or_more().digit() \
       .assert_ahead().string("px").end()

Lookbehind
----------

:meth:`~edify.RegexBuilder.assert_behind` and
:meth:`~edify.RegexBuilder.assert_not_behind` do the same thing looking
*backward* — they assert what precedes the current position:

.. code-block:: python

   from edify import RegexBuilder as R

   R().assert_behind().char("$").end().one_or_more().digit().to_regex_string()
   # '(?<=\\$)\\d+'    digits, but only right after a '$'

   R().assert_not_behind().char("$").end().one_or_more().digit().to_regex_string()
   # '(?<!\\$)\\d+'    digits, but only when NOT right after a '$'

.. code-block:: python

   from edify import RegexBuilder as R

   price = R().assert_behind().char("$").end().one_or_more().digit().to_regex()
   price.search("$42").group()   # '42'  — the '$' is required but not part of the match

A classic use: match a value only when it carries the right prefix (a ``$``, an
``@``, a ``#``) without swallowing the prefix into your result.

.. edify-playground::
   :tests: $42|$7|42|£42

   from edify import RegexBuilder as R

   R().assert_behind().char("$").end().one_or_more().digit()

The negative form is trickier than it looks
-------------------------------------------

``assert_not_behind`` asserts about **one position**, not about the whole match.
So a negative lookbehind does not exclude a value — it only stops the match from
*starting* at a forbidden spot, leaving the engine free to start one character
later:

.. code-block:: python

   from edify import RegexBuilder as R

   loose = R().assert_not_behind().char("$").end().one_or_more().digit().to_regex()
   [m.group() for m in loose.finditer("$42 and 7")]   # ['2', '7']

The ``4`` is rejected because a ``$`` precedes it — and then the engine simply
begins at the ``2``, which is preceded by a ``4``. To exclude the whole number,
assert about the start of the *run*: add a boundary so the match cannot begin
mid-number.

.. edify-playground::
   :tests: 7|42|$42|x7

   from edify import RegexBuilder as R

   R().word_boundary() \
       .assert_not_behind().char("$").end() \
       .one_or_more().digit()

This is the general lesson for negative assertions: they say "not here", never
"not anywhere". Pair them with an anchor or a boundary whenever you mean the
stronger thing.

Stacking assertions
-------------------

Because a lookahead consumes nothing, you can stack several at the same position
to require *all* of them at once — the idiom behind a password policy. Each
lookahead scans the whole string for one requirement; the real tokens then match
the length:

.. code-block:: python

   from edify import RegexBuilder as R

   password = (
       R().start_of_input()
       .assert_ahead().zero_or_more().any_char().digit().end()        # has a digit
       .assert_ahead().zero_or_more().any_char().uppercase().end()    # has an uppercase
       .at_least(8).any_char()                                        # at least 8 chars
       .end_of_input()
   )
   password.to_regex_string()   # '^(?=.*\\d)(?=.*[A-Z]).{8,}$'

   rx = password.to_regex()
   rx.match("Abcdef12")   # matches
   rx.match("alllower1")  # None — no uppercase
   rx.match("Ab1")        # None — too short

Each requirement is one independent line, which is why this scales: adding "must
contain a symbol" is one more ``assert_ahead``, not a rewrite of the pattern. A
single expression trying to require all three at once would be unreadable and
almost certainly wrong.

.. edify-playground::
   :tests: Abcdef12|alllower1|NoDigitsHere|Ab1

   RegexBuilder() \
       .start_of_input() \
       .assert_ahead().zero_or_more().any_char().digit().end() \
       .assert_ahead().zero_or_more().any_char().uppercase().end() \
       .at_least(8).any_char() \
       .end_of_input()

Width limits on lookbehind
--------------------------

The standard library requires every lookbehind branch to be **fixed-width**. A
quantifier inside one — or an alternation whose branches differ in length — will
not compile. Edify catches this at build time and says so precisely:

.. code-block:: text

   error: assert_behind / assert_not_behind has a variable-width body, which the
   stdlib 're' engine does not accept

      = note: stdlib re requires every lookbehind branch to be fixed-width, so a
        quantifier like +/*/?/{m,n} or a same-frame alternation with differing
        branch widths inside a lookbehind will fail to compile.

   help: switch to the third-party engine with .to_regex(engine='regex'), which
   supports variable-width lookbehind.

Taking that advice works:

.. code-block:: python

   from edify import RegexBuilder as R

   flexible = R().assert_behind().one_or_more().char("$").end().one_or_more().digit()

   compiled = flexible.to_regex(engine="regex")
   compiled.source                    # '(?<=\\$+)\\d+'
   compiled.search("$$42").group()    # '42'

Install it with ``pip install edify[regex]``. See :doc:`flags` for the engine
argument and :doc:`../beyond/errors` for the diagnostic format.

The functional form
-------------------

Each assertion is also a factory function wrapping the pattern it looks for:

.. code-block:: python

   from edify import assert_ahead, assert_not_ahead, string

   assert_ahead(string("px")).to_regex_string()       # '(?=px)'
   assert_not_ahead(string("px")).to_regex_string()   # '(?!px)'

The four factories — ``assert_ahead``, ``assert_not_ahead``, ``assert_behind``,
``assert_not_behind`` — mirror the methods. See :doc:`../beyond/composing`.

Quick reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 28 28 16 28

   * - Method
     - Factory
     - Emits
     - Holds when
   * - ``assert_ahead()``
     - ``assert_ahead(p)``
     - ``(?=…)``
     - the text ahead matches
   * - ``assert_not_ahead()``
     - ``assert_not_ahead(p)``
     - ``(?!…)``
     - the text ahead does not match
   * - ``assert_behind()``
     - ``assert_behind(p)``
     - ``(?<=…)``
     - the text behind matches
   * - ``assert_not_behind()``
     - ``assert_not_behind(p)``
     - ``(?<!…)``
     - the text behind does not match

Next: :doc:`flags`, for case-insensitivity, multiline, and the other global switches.
