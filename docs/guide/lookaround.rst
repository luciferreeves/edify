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

   before_px = R().one_or_more().digit().assert_ahead().string("px").end().to_regex()
   before_px.search("16px").group()   # '16'  — the 'px' matched the lookahead, but isn't captured

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

   R().assert_behind().char("$").end().one_or_more().digit().to_regex_string()
   # '(?<=\\$)\\d+'    digits, but only right after a '$'

   R().assert_not_behind().char("$").end().one_or_more().digit().to_regex_string()
   # '(?<!\\$)\\d+'    digits, but only when NOT right after a '$'

.. code-block:: python

   price = R().assert_behind().char("$").end().one_or_more().digit().to_regex()
   price.search("$42").group()   # '42'  — the '$' is required but not part of the match

A classic use: match a value only when it carries the right prefix (a ``$``, an
``@``, a ``#``) without swallowing the prefix into your result.

Stacking assertions
-------------------

Because a lookahead consumes nothing, you can stack several at the same position
to require *all* of them at once — the idiom behind a password policy. Each
lookahead scans the whole string for one requirement; the real tokens then match
the length:

.. code-block:: python

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

The functional form
-------------------

Each assertion is also a factory function wrapping the pattern it looks for:

.. code-block:: python

   from edify import assert_ahead, assert_not_ahead, string

   assert_ahead(string("px")).to_regex_string()       # '(?=px)'
   assert_not_ahead(string("px")).to_regex_string()   # '(?!px)'

The four factories — ``assert_ahead``, ``assert_not_ahead``, ``assert_behind``,
``assert_not_behind`` — mirror the methods. See :doc:`composing`.

.. admonition:: Engine note
   :class: note

   Some engines restrict lookbehind to fixed-width patterns. If a variable-width
   lookbehind isn't supported by the standard-library backend, edify raises a
   clear error pointing you at the fix — see :doc:`errors`. You can also select
   the alternate engine on :meth:`~edify.RegexBuilder.to_regex` (see :doc:`flags`).

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

Try it
------

.. edify-playground::
   :tests: Abcdef12|alllower1|NoDigitsHere|Ab1

   RegexBuilder() \
       .start_of_input() \
       .assert_ahead().zero_or_more().any_char().digit().end() \
       .assert_ahead().zero_or_more().any_char().uppercase().end() \
       .at_least(8).any_char() \
       .end_of_input()

Next: :doc:`flags`, for case-insensitivity, multiline, and the other global switches.
