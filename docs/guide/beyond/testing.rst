Testing your patterns
=====================

A pattern is code, and code deserves tests. Edify gives you two built-in ways to
pin a pattern's behavior down.

Assertions on the builder
-------------------------

:meth:`~edify.RegexBuilder.assert_matches` checks that every string you give it
matches, and :meth:`~edify.RegexBuilder.assert_rejects` checks that every one is
rejected. Both take an iterable of strings and return the builder, so you can
chain them right where you define the pattern:

.. code-block:: python

   from edify import RegexBuilder

   year = (
       RegexBuilder().start_of_input().exactly(4).digit().end_of_input()
       .assert_matches(["2024", "0000", "9999"])
       .assert_rejects(["", "24", "20245", "20x4"])
   )

If any input matches when it shouldn't (or the reverse), the assertion raises
immediately — with the same annotated format as every other edify error (see
:doc:`errors`), naming the exact inputs that broke the contract:

.. code-block:: text

   error: pattern '\d{4}' did not match 1 expected input(s): '12'
     ... help: adjust the pattern to accept these inputs, or drop them from the assert

Because the assertions run at build time and return the builder, putting them
next to a pattern's definition makes it document *and* verify its own contract
the moment the module imports.

Snapshot tests
--------------

For the emitted regex itself, :func:`edify.testing.assert_snapshot` compares a
value against a committed snapshot file, so an accidental change to a pattern's
output surfaces as a failing test with a diff:

.. code-block:: python

   from pathlib import Path
   from edify import RegexBuilder
   from edify.testing import assert_snapshot

   def test_year_pattern_shape():
       emitted = RegexBuilder().start_of_input().exactly(4).digit().end_of_input().to_regex_string()
       assert_snapshot(emitted, Path(__file__).parent / "snapshots" / "year.regex")

The first run writes the snapshot; later runs compare against it. Set
``EDIFY_UPDATE_SNAPSHOTS=1`` in the environment when you *intend* to change a
pattern and want to regenerate its snapshots in one pass. A missing snapshot
raises :class:`~edify.testing.SnapshotMissingError`, and a mismatch raises
:class:`~edify.testing.SnapshotMismatchError` — both carrying the snapshot path
so you know exactly which file to look at.

Snapshots aren't only for regex strings: any text works, so you can snapshot a
pattern's :meth:`~edify.Regex.explain` output or its
:meth:`~edify.Regex.to_verbose_string` form to lock down its *documentation*, not
just its source.

Next: :doc:`seeing`, on turning a pattern into a picture or a plain-English
explanation.
