Flags
=====

Flags are global switches that change how the *whole* pattern matches —
case-insensitivity, multiline anchors, and a few others. They don't change the
regex string; they change how the compiled regex behaves.

Setting a flag
--------------

Every flag is a chain method. Set it anywhere in the chain:

.. code-block:: python

   from edify import RegexBuilder as R

   name = R().ignore_case().string("cat").to_regex()

   name.match("cat")   # matches
   name.match("CAT")   # also matches — case is ignored

Notice the emitted string is unchanged — ``ignore_case().string("cat")`` still
emits ``'cat'``. The flag lives on the compiled regex, not in the source, which
keeps the pattern readable and lets the same source compile with or without it.

The available flags:

``ignore_case``
   Match letters regardless of case.
``multi_line``
   ``start_of_input`` / ``end_of_input`` match at every line boundary, not just
   the string's ends.
``dot_all``
   ``any_char`` also matches newlines.
``ascii_only``
   Restrict ``\w``, ``\d``, ``\s`` (and friends) to ASCII instead of Unicode.
``verbose``
   Allow insignificant whitespace and comments in the underlying pattern.
``debug``
   Emit the engine's parse debug output when compiling.

``multi_line`` in action:

.. code-block:: python

   starts = R().multi_line().start_of_input().one_or_more().word().to_regex()
   [m.group() for m in starts.finditer("one\ntwo\nthree")]   # ['one', 'two', 'three']

Setting flags at compile time
-----------------------------

You can also pass flags straight to :meth:`~edify.RegexBuilder.to_regex`, which
is handy when the *same* builder should compile different ways:

.. code-block:: python

   word = R().string("cat")

   word.to_regex(ignore_case=True).match("CAT")   # matches
   word.to_regex().match("CAT")                    # no match

The keyword form uses ``ignore_case``, ``multiline``, ``dotall``, ``ascii_only``,
``verbose``, and ``debug``.

Choosing the engine
-------------------

By default edify compiles with the standard library's ``re``. Pass
``engine="regex"`` to compile with the third-party engine instead (install it
with ``pip install edify[regex]``), which supports features ``re`` doesn't — such
as variable-width lookbehind:

.. code-block:: python

   pattern = R().assert_behind().one_or_more().char("$").end().one_or_more().digit()
   pattern.to_regex(engine="regex")   # compiled with the regex engine

If a pattern needs a feature the selected engine lacks, edify raises a clear,
actionable error instead of a cryptic one — the subject of :doc:`errors`.

Try it
------

The emitted regex below is just ``cat``, but the ``ignore_case`` flag rides on
the compiled pattern — so ``CAT`` and ``Cat`` match too:

.. edify-playground::
   :tests: cat|CAT|Cat|dog

   RegexBuilder() \
       .ignore_case() \
       .string("cat")

That completes the builder. Next, :doc:`composing` shows how to combine and
reuse the patterns you now know how to write.
