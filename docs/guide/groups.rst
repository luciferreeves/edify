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

   R().exactly(3).group().digit().char("-").end().to_regex_string()
   # '(?:\\d\\-){3}'   — three "digit-dash" units

Alternation
-----------

:meth:`~edify.RegexBuilder.any_of` matches any one of several branches. Pass the
alternatives as strings for the common case:

.. code-block:: python

   R().any_of("cat", "dog", "fish").to_regex_string()   # '(?:cat|dog|fish)'

For branches that are more than plain strings, open ``any_of`` with no
arguments, add each branch, and close with ``end``. Each branch is its own
sub-chain:

.. code-block:: python

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

   R().one_of("GET", "POST", "PUT").to_regex_string()   # '(?:GET|POST|PUT)'

Nesting and reuse
-----------------

Groups nest freely, and you can drop a whole pre-built pattern into a chain with
:meth:`~edify.RegexBuilder.subexpression` (or its alias
:meth:`~edify.RegexBuilder.use`). That is how you compose bigger patterns from
named pieces — the subject of :doc:`composing`:

.. code-block:: python

   word = R().one_or_more().word()
   csv_field = R().subexpression(word).zero_or_more().group().char(",").subexpression(word).end()

Next: :doc:`captures`, for pulling matched text back out.
