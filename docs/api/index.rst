API reference
=============

The complete public surface, generated from the source. For a guided tour start
with the :doc:`../guide/index`; for the ready-made validators see the
:doc:`../library/index`.

.. toctree::
   :hidden:

   builder/index
   builder/anchors
   builder/characters
   builder/classes
   builder/quantifiers
   builder/groups
   builder/captures
   builder/assertions
   builder/flags
   builder/composition
   builder/matching
   builder/output
   factories
   constants
   results
   introspection
   serialization
   testing
   errors

Building patterns
-----------------

:doc:`builder/index` — :class:`~edify.RegexBuilder`, the fluent immutable builder,
and :class:`~edify.Pattern`, the callable reusable fragment. Their 65 chain methods
are grouped by what they do:

- :doc:`builder/anchors` — ``start_of_input``, ``end_of_input``.
- :doc:`builder/characters` — literal characters, strings, ranges, and inline sets.
- :doc:`builder/classes` — ``digit``, ``letter``, ``word``, and the other named
  classes.
- :doc:`builder/quantifiers` — ``exactly``, ``between``, ``one_or_more``, and the
  lazy variants.
- :doc:`builder/groups` — grouping and alternation.
- :doc:`builder/captures` — capturing groups and backreferences.
- :doc:`builder/assertions` — lookahead and lookbehind.
- :doc:`builder/flags` — ``ignore_case``, ``dot_all``, ``multi_line``, and friends.
- :doc:`builder/composition` — embedding one pattern in another.
- :doc:`builder/matching` — running a pattern straight from the builder.
- :doc:`builder/output` — compiling to a :class:`~edify.Regex` or a string.

Other ways to build
-------------------

:doc:`factories` — a standalone factory function for every builder method, for a
functional style. :doc:`constants` — ready-made single-token patterns such as
``DIGIT`` and ``START``.

Working with results
--------------------

:doc:`results` — :class:`~edify.Regex`, a compiled pattern with the full ``re``
surface plus introspection, and the match objects it returns.

Inspecting and storing
----------------------

:doc:`introspection` — turn a pattern into prose, a diagram, or an annotated
verbose form. :doc:`serialization` — round-trip a pattern through a dict or JSON.

Testing and errors
------------------

:doc:`testing` — snapshot assertions and group-name validation.
:doc:`errors` — the diagnostic hierarchy every failure is raised from.
