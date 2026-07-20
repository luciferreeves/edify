Testing and errors
==================

Snapshot assertions for pinning a pattern's output, group-name validation, and
the exception hierarchy every edify error derives from.

Testing
-------

.. autofunction:: edify.testing.assert_snapshot

.. autoexception:: edify.testing.SnapshotMismatchError

.. autoexception:: edify.testing.SnapshotMissingError

Validation
----------

.. autofunction:: edify.validate.is_valid_group_name

Errors
------

.. autoexception:: edify.EdifyError

.. autoexception:: edify.EdifySyntaxError
