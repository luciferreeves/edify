Testing
=======

Two chain methods assert a pattern's behaviour inline, and :mod:`edify.testing`
adds snapshot assertions for a test suite.

Inline assertions
-----------------

These raise immediately, naming the inputs that did not behave as expected — so a
pattern can carry its own examples beside its definition.

.. automethod:: edify.RegexBuilder.assert_matches

.. automethod:: edify.RegexBuilder.assert_rejects

Snapshot assertions
-------------------

.. autofunction:: edify.testing.assert_snapshot

.. autoexception:: edify.testing.SnapshotMismatchError

.. autoexception:: edify.testing.SnapshotMissingError

Group-name validation
---------------------

.. autofunction:: edify.validate.is_valid_group_name
