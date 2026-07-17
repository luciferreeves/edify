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
immediately, naming the offending input. Put these next to a pattern's
definition and it documents *and* verifies its own contract at import time.

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
``EDIFY_UPDATE_SNAPSHOTS=1`` when you *intend* to change a pattern and want to
regenerate its snapshots in one pass. A missing snapshot or a mismatch raises a
clear :class:`~edify.testing.SnapshotMissingError` or
:class:`~edify.testing.SnapshotMismatchError`.

Next: :doc:`seeing`, on turning a pattern into a picture or a plain-English
explanation.
