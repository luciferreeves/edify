Testing your patterns
=====================

A pattern is code, and code deserves tests. Edify gives you two built-in ways to
pin a pattern's behavior down: assertions that live beside the definition, and
snapshots that live in your test suite.

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

Because they return the builder, the assertions are part of the expression — the
pattern documents *and* verifies its own contract the moment the module imports.
There is no separate test to forget to write, and no way for the pattern to drift
from the examples beside it.

.. edify-playground::
   :tests: 2024|0000|9999|24|20x4

   from edify import RegexBuilder

   RegexBuilder().start_of_input() \
       .exactly(4).digit() \
       .end_of_input() \
       .assert_matches(["2024", "0000", "9999"]) \
       .assert_rejects(["", "24", "20245", "20x4"])

Add ``"20x4"`` to the ``assert_matches`` list in the playground and the whole
build fails — the assertion runs before anything else can use the pattern.

What a failure tells you
------------------------

A broken assertion raises immediately, with the same annotated format as every
other edify error (see :doc:`errors`) and — critically — the *exact inputs* that
broke the contract, not just a count:

.. code-block:: text

   error: pattern '^\d{4}$' did not match 1 expected input(s): '12'

    --> validators.py:7:5
     |
   7 |     RegexBuilder().start_of_input().exactly(4).digit().end_of_input()
     |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ .assert_matches([...]) called here
     |
      = note: every string in the argument list must match the pattern to satisfy
        the assertion; the listed inputs were rejected.

   help: adjust the pattern to accept these inputs, or drop them from the
   assertion list.

``assert_rejects`` reports the mirror image — the inputs that matched when they
should not have — and its help line points the other way, at tightening the
pattern:

.. code-block:: text

   error: pattern '^\d{4}$' matched 1 input(s) that were expected to be rejected: '2024'

      = note: every string in the argument list must be rejected by the pattern to
        satisfy the assertion; the listed inputs matched instead.

   help: tighten the pattern so these inputs no longer match, or drop them from
   the assertion list.

Both name the emitted regex in the summary, so a failure in a deeply composed
pattern still shows you what actually got compiled.

Snapshot tests
--------------

Assertions pin *behavior*. Snapshots pin the emitted regex itself, so an
accidental change to a pattern's output surfaces as a failing test with a diff.
:func:`edify.testing.assert_snapshot` takes the value and a path:

.. code-block:: python

   from pathlib import Path
   from edify import RegexBuilder
   from edify.testing import assert_snapshot

   def test_year_pattern_shape():
       emitted = RegexBuilder().start_of_input().exactly(4).digit().end_of_input().to_regex_string()
       assert_snapshot(emitted, Path(__file__).parent / "snapshots" / "year.regex")

Snapshots are never written implicitly. A missing file raises
:class:`~edify.testing.SnapshotMissingError` rather than quietly recording
whatever the code happens to produce — which would make the first run of a broken
pattern its own reference:

.. code-block:: text

   snapshot file missing at tests/snapshots/year.regex

   help: re-run pytest with EDIFY_UPDATE_SNAPSHOTS=1 to create it.

Set ``EDIFY_UPDATE_SNAPSHOTS=1`` in the environment when you *intend* to change a
pattern, and every affected snapshot regenerates in one pass. Reviewing that diff
is the point of the whole mechanism: it is a list of every documented behavior
your change touched.

A mismatch raises :class:`~edify.testing.SnapshotMismatchError`, with the diff
inline so you do not have to open the file to see what moved:

.. code-block:: text

   snapshot mismatch at tests/snapshots/year.regex

   --- tests/snapshots/year.regex (snapshot)
   +++ tests/snapshots/year.regex (actual)
   @@ -1 +1 @@
   -^\d{4}$+^\d{2}$

   help: re-run pytest with EDIFY_UPDATE_SNAPSHOTS=1 to accept the new output as
   the reference.

Snapshotting more than the regex
--------------------------------

``assert_snapshot`` takes any text, so the technique is not limited to
``to_regex_string()``. Snapshot :meth:`~edify.Regex.explain` output and a change
in what a pattern *means* becomes a reviewable diff; snapshot
:meth:`~edify.Regex.to_verbose_string` and you pin the element-by-element
breakdown:

.. code-block:: python

   from pathlib import Path
   from edify import RegexBuilder
   from edify.testing import assert_snapshot

   def test_year_pattern_reads_correctly():
       compiled = RegexBuilder().start_of_input().exactly(4).digit().end_of_input().to_regex()
       here = Path(__file__).parent / "snapshots"
       assert_snapshot(compiled.explain(), here / "year.explain")
       assert_snapshot(compiled.to_verbose_string(), here / "year.verbose")

That is how a pattern's *documentation* stays honest: prose that drifts from the
pattern fails the suite. :doc:`seeing` covers both of those outputs in full.

Choosing between them
---------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Use
     - When
   * - ``assert_matches`` / ``assert_rejects``
     - The contract is *which strings are valid* — the usual case for a validator.
   * - ``assert_snapshot``
     - The contract is *what gets emitted* — for patterns other tools consume, or
       to catch unintended compile-path changes across a whole suite.

Most patterns want both: assertions beside the definition for intent, a snapshot
in the test suite for drift.

Next: :doc:`seeing`, on turning a pattern into a picture or a plain-English
explanation.
