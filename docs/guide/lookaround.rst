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

.. admonition:: Engine note
   :class: note

   Some engines restrict lookbehind to fixed-width patterns. If a variable-width
   lookbehind isn't supported by the standard-library backend, edify raises a
   clear error pointing you at the fix — see :doc:`errors`. You can also select
   the alternate engine on :meth:`~edify.RegexBuilder.to_regex` (see :doc:`flags`).

Next: :doc:`flags`, for case-insensitivity, multiline, and the other global switches.
