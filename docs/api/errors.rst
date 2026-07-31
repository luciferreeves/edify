Errors
======

Every failure edify raises derives from :class:`~edify.EdifyError`, so one
``except`` clause catches the lot. Each carries the four-part diagnostic described
in :doc:`../guide/beyond/errors`: a summary, a pointer at the offending call, a ``= note:``
explaining the rule, and a ``help:`` line with a fix.

.. code-block:: python

   from edify import EdifyError, RegexBuilder

   try:
       RegexBuilder().named_capture("2bad").digit().end().to_regex_string()
   except EdifyError as problem:
       print(problem)

The base classes
----------------

:class:`~edify.EdifyError` is the root of the hierarchy.
:class:`~edify.EdifySyntaxError` derives from it and covers everything that means
"this pattern is malformed" — catch that one when you want build failures but not,
say, a missing optional backend.

.. autoexception:: edify.EdifyError

.. autoexception:: edify.EdifySyntaxError

Input errors
------------

Raised when a chain method is given an argument it cannot use — a reversed range,
a non-positive count, a multi-character value where one was required. Each names
the parameter as it appears in the signature you called.

.. automodule:: edify.errors.input
   :members:
   :undoc-members:
   :show-inheritance:

Quantifier errors
-----------------

Raised when a quantifier has nothing to apply to, or when one is stacked on
another. Both are detected structurally, so the message names the queued
quantifier and where it was written.

.. automodule:: edify.errors.quantifier
   :members:
   :undoc-members:
   :show-inheritance:

Structure errors
----------------

Raised when frames do not balance — an :meth:`~edify.RegexBuilder.end` with
nothing open, or a subexpression merged while it still has an open frame. These
list every frame still open, each with the location that opened it.

.. automodule:: edify.errors.structure
   :members:
   :undoc-members:
   :show-inheritance:

Anchor errors
-------------

Raised when start- or end-of-input anchors are placed impossibly — a second
``start_of_input``, or a ``start_of_input`` after ``end_of_input``.

.. automodule:: edify.errors.anchors
   :members:
   :undoc-members:
   :show-inheritance:

Naming errors
-------------

Raised when a capture group name is not a usable identifier, is already taken, or
is referenced before it is declared.

.. automodule:: edify.errors.naming
   :members:
   :undoc-members:
   :show-inheritance:

Capture errors
--------------

Raised when a numbered back-reference points at a capture group that does not
exist.

.. automodule:: edify.errors.captures
   :members:
   :undoc-members:
   :show-inheritance:

Backend errors
--------------

Raised at engine-dispatch time — when a pattern needs a feature the selected
engine lacks, or when ``engine="regex"`` is requested without the extra installed.

.. automodule:: edify.errors.backend
   :members:
   :undoc-members:
   :show-inheritance:

Comparison errors
-----------------

Raised when an unfinished builder — one with a frame still open — is compared or
hashed. Neither operation has a meaningful answer until the pattern is closed.

.. automodule:: edify.errors.comparison
   :members:
   :undoc-members:
   :show-inheritance:

Testing errors
--------------

Raised by :meth:`~edify.RegexBuilder.assert_matches` and
:meth:`~edify.RegexBuilder.assert_rejects` when a pattern breaks its declared
contract. The message names every input that failed, not just a count.

.. automodule:: edify.errors.testing
   :members:
   :undoc-members:
   :show-inheritance:

Introspection errors
--------------------

Raised by the visualization surface — an unknown format or engine, or a request
for Graphviz output without the extra installed.

.. automodule:: edify.errors.introspect
   :members:
   :undoc-members:
   :show-inheritance:

Serialization errors
--------------------

Raised when a canonical dict cannot be read back — a schema version this build does
not understand, a missing key, or an unregistered element kind.

.. automodule:: edify.errors.serialize
   :members:
   :undoc-members:
   :show-inheritance:

Integration errors
------------------

Raised by the framework adapters in :mod:`edify.integrations` when a value does not
match the pattern a field was pinned to.

.. automodule:: edify.errors.integration
   :members:
   :undoc-members:
   :show-inheritance:

Not every failure is an EdifyError
----------------------------------

One caveat worth knowing: reverse-parsing an unsupported construct raises
``UnsupportedReverseParseError``, which is a plain :class:`ValueError` rather than
an :class:`~edify.EdifyError` — catch that type explicitly when calling
:meth:`~edify.RegexBuilder.from_regex`.

The snapshot helpers in :mod:`edify.testing` are likewise separate:
``SnapshotMissingError`` and ``SnapshotMismatchError`` are documented with the rest
of the testing surface on :doc:`testing`.
