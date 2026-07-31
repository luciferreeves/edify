Groups and alternation
======================

Grouping bundles several tokens into one unit — so a quantifier can repeat the
whole thing, or an alternation can choose between whole branches.

Grouping
--------

:meth:`~edify.RegexBuilder.group` opens a non-capturing group; everything you
chain until :meth:`~edify.RegexBuilder.end` goes inside it:

.. code-block:: python

   from edify import RegexBuilder as R

   R().group().digit().letter().end().to_regex_string()   # '(?:\\d[a-zA-Z])'

A group on its own changes nothing about what matches — ``(?:\d[a-zA-Z])``
matches the same text as ``\d[a-zA-Z]``. It earns its keep the moment a
quantifier or alternation needs a single unit to operate on:

.. code-block:: python

   from edify import RegexBuilder as R

   R().exactly(3).group().digit().char("-").end().to_regex_string()
   # '(?:\\d\\-){3}'   — three "digit-dash" units

One or more "digit-dash" units — the quantifier repeats the whole group:

.. edify-playground::
   :tests: 1-2-|9-|12|abc

   RegexBuilder() \
       .one_or_more() \
       .group().digit().char("-").end()

A non-capturing group is invisible to the match results. When you actually want
to pull the text back out, reach for a *capturing* group instead — that's the
subject of :doc:`captures`.

Alternation
-----------

:meth:`~edify.RegexBuilder.any_of` matches any one of several branches. Pass the
alternatives as strings for the common case:

.. code-block:: python

   from edify import RegexBuilder as R

   R().any_of("cat", "dog", "fish").to_regex_string()   # '(?:cat|dog|fish)'

For branches that are more than plain strings, open ``any_of`` with no
arguments, add each branch, and close with ``end``. Each branch is its own
sub-chain:

.. code-block:: python

   from edify import RegexBuilder as R

   protocol = (
       R().any_of()
       .string("http")
       .string("https")
       .string("ftp")
       .end()
   )
   protocol.to_regex_string()   # '(?:http|https|ftp)'

:meth:`~edify.RegexBuilder.one_of` is the same idea, specialized to a list of
string literals:

.. code-block:: python

   from edify import RegexBuilder as R

   R().one_of("GET", "POST", "PUT").to_regex_string()   # '(?:GET|POST|PUT)'

.. note::

   When every alternative is a single character, edify folds the alternation into
   a character class instead — ``any_of("a", "b", "c")`` emits ``[abc]``, which
   matches the same text more efficiently.

The functional form
-------------------

:func:`~edify.group` and :func:`~edify.any_of` also exist as factory functions
that take the patterns they wrap, for composing without a leading builder:

.. code-block:: python

   from edify import group, any_of, one_or_more, DIGIT, string

   group(one_or_more(DIGIT)).to_regex_string()       # '(?:\\d+)'
   any_of(string("cat"), string("dog")).to_regex_string()   # '(?:cat|dog)'

Nesting and reuse
-----------------

Groups nest freely, and you can drop a whole pre-built pattern into a chain with
:meth:`~edify.RegexBuilder.subexpression` (or its alias
:meth:`~edify.RegexBuilder.use`). That is how you compose bigger patterns from
named pieces — the subject of :doc:`composing`:

.. code-block:: python

   from edify import RegexBuilder as R

   word = R().one_or_more().word()
   csv_field = (
       R().use(word)
       .zero_or_more().group().char(",").use(word).end()
   )
   csv_field.to_regex_string()   # '\\w+(?:,\\w+)*'

Quick reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 34 30 36

   * - Method
     - Factory
     - Emits
   * - ``group()``
     - ``group(p)``
     - ``(?:…)`` — non-capturing group
   * - ``capture()``
     - ``capture(p)``
     - ``(…)`` — capturing group (see :doc:`captures`)
   * - ``any_of(*branches)``
     - ``any_of(*patterns)``
     - ``(?:a|b|c)`` — alternation
   * - ``one_of(*literals)``
     - —
     - ``(?:a|b|c)`` — alternation of string literals

Try it
------

.. edify-playground::
   :tests: cat|dog|fish|bird

   RegexBuilder() \
       .any_of("cat", "dog", "fish")

Next: :doc:`captures`, for pulling matched text back out.
