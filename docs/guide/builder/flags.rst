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

That also means the flag does **not** travel with ``source``. If you hand the
emitted string to another tool, the narrowing is lost — see :doc:`../practice/unicode`
for when to prefer an explicit character class over a flag for that reason.

.. edify-playground::
   :tests: cat|CAT|Cat|dog

   from edify import RegexBuilder

   RegexBuilder().ignore_case().string("cat")

Delete ``.ignore_case()`` and only the lowercase ``cat`` survives.

ignore_case
-----------

Matches letters regardless of case. It is a per-character fold, so it handles the
common mappings across scripts but cannot match one character against two —
``ß`` does not fold to ``ss``. :doc:`../practice/unicode` covers that edge.

multi_line
----------

``start_of_input`` and ``end_of_input`` match at every line boundary instead of
only the string's ends:

.. code-block:: python

   from edify import RegexBuilder as R

   starts = R().multi_line().start_of_input().one_or_more().word().to_regex()
   [m.group() for m in starts.finditer("one\ntwo\nthree")]   # ['one', 'two', 'three']

Without the flag that same pattern finds only ``'one'``. This is the flag to
reach for when a pattern works against a single line and silently finds nothing
in a document.

.. edify-playground::
   :tests: one|two|three

   from edify import RegexBuilder

   RegexBuilder().multi_line() \
       .start_of_input() \
       .one_or_more().word()

dot_all
-------

``any_char`` matches a newline as well. By default it does not, which surprises
everyone exactly once:

.. code-block:: python

   from edify import RegexBuilder as R

   span = R().start_of_input().one_or_more().any_char().end_of_input()

   span.to_regex().match("a\nb")                 # None — the dot stops at the newline
   span.dot_all().to_regex().match("a\nb")       # a Match

Reach for it whenever a pattern has to span lines — an HTML block, a log entry
with an embedded stack trace, a multi-line quoted string.

ascii_only
----------

Restricts ``\w``, ``\d``, ``\s`` and ``\b`` to ASCII instead of Unicode. Those
classes are Unicode-aware by default, so this is how you narrow the whole pattern
in one call rather than rewriting each token:

.. code-block:: python

   from edify import RegexBuilder as R

   letters = R().start_of_input().one_or_more().word().end_of_input()

   letters.to_regex().match("café")               # a Match — \w is Unicode-aware
   letters.ascii_only().to_regex().match("café")  # None

Whether that is the behavior you want depends entirely on the field.
:doc:`../practice/unicode` walks through choosing. ``ascii_only`` is the mirror
image of the Unicode property classes: this flag narrows a Unicode-aware token to
ASCII, while :meth:`~edify.RegexBuilder.unicode_letter` and its siblings widen an
ASCII-only one to every script.

.. edify-playground::
   :tests: hello|user_1|café|日本語

   from edify import RegexBuilder

   RegexBuilder().ascii_only() \
       .start_of_input() \
       .one_or_more().word() \
       .end_of_input()

verbose
-------

Allows insignificant whitespace and comments in the underlying pattern — the
``re.VERBOSE`` mode. Edify emits a compact pattern regardless, so this matters
when you are feeding in an externally written verbose pattern rather than for
patterns you build here. For a readable rendering of a pattern you *did* build,
use :meth:`~edify.Regex.to_verbose_string` instead, covered in
:doc:`../beyond/seeing`.

debug
-----

Emits the engine's parse output when compiling — the opcode listing the matcher
will run:

.. code-block:: python

   from edify import RegexBuilder as R

   R().digit().to_regex(debug=True)
   # IN
   #   CATEGORY CATEGORY_DIGIT
   # ...

Useful when you need to see what the engine made of a pattern. For everyday
inspection the tools in :doc:`../beyond/seeing` are friendlier.

Combining flags
---------------

Flags stack — chain as many as you need, in any order:

.. code-block:: python

   import re
   from edify import RegexBuilder as R

   both = R().ignore_case().multi_line().string("cat").to_regex()

   bool(both.compiled.flags & re.IGNORECASE)   # True
   bool(both.compiled.flags & re.MULTILINE)    # True

Setting flags at compile time
-----------------------------

You can also pass flags straight to :meth:`~edify.RegexBuilder.to_regex`, which
is handy when the *same* builder should compile different ways:

.. code-block:: python

   from edify import RegexBuilder as R

   word = R().string("cat")

   word.to_regex(ignore_case=True).match("CAT")   # matches
   word.to_regex().match("CAT")                    # no match

This is the right form when the flag is a property of the *call site* rather than
of the pattern — a search box that offers a "match case" checkbox, say. Keep the
flag in the chain when it is part of what the pattern means, so it travels with
the pattern wherever it is reused.

The keyword form uses ``ignore_case``, ``multiline``, ``dotall``, ``ascii_only``,
``verbose``, and ``debug`` — note that two of them differ from the method names.

Choosing the engine
-------------------

By default edify compiles with the standard library's ``re``. Pass
``engine="regex"`` to compile with the third-party engine instead (install it
with ``pip install edify[regex]``), which supports features ``re`` doesn't —
Unicode property classes such as :meth:`~edify.RegexBuilder.unicode_letter`,
match timeouts, and variable-width lookbehind:

.. code-block:: python

   from edify import RegexBuilder as R

   pattern = R().assert_behind().one_or_more().char("$").end().one_or_more().digit()
   pattern.to_regex(engine="regex")   # compiled with the regex engine

If a pattern needs a feature the selected engine lacks, edify raises a clear,
actionable error instead of a cryptic one — the subject of :doc:`../beyond/errors`.

Quick reference
---------------

Each flag as a chain method, its :meth:`~edify.RegexBuilder.to_regex` keyword
(note the names differ), and what it does:

.. list-table::
   :header-rows: 1
   :widths: 26 26 48

   * - Method
     - Compile keyword
     - Effect
   * - ``ignore_case()``
     - ``ignore_case=True``
     - match letters regardless of case
   * - ``multi_line()``
     - ``multiline=True``
     - ``^`` / ``$`` match at every line boundary
   * - ``dot_all()``
     - ``dotall=True``
     - ``any_char`` also matches newlines
   * - ``ascii_only()``
     - ``ascii_only=True``
     - restrict ``\w`` ``\d`` ``\s`` to ASCII
   * - ``verbose()``
     - ``verbose=True``
     - allow insignificant whitespace and comments
   * - ``debug()``
     - ``debug=True``
     - emit the engine's parse debug output

That completes the builder. Next, :doc:`../beyond/composing` shows how to combine and
reuse the patterns you now know how to write.
