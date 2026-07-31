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

.. autoexception:: edify.EdifyError

.. autoexception:: edify.EdifySyntaxError

Input errors
------------

Raised when a chain method is given an argument it cannot use — a reversed range,
a non-positive count, a multi-character value where one was required.

.. automodule:: edify.errors.input
   :members:
   :undoc-members:
   :show-inheritance:

Naming errors
-------------

Raised when a capture group name is not a usable identifier.

.. automodule:: edify.errors.naming
   :members:
   :undoc-members:
   :show-inheritance:

Serialization errors
--------------------

Raised when a canonical dict cannot be read back — a schema version this build does
not understand, or a malformed element.

.. automodule:: edify.errors.serialize
   :members:
   :undoc-members:
   :show-inheritance:

One caveat worth knowing: not every exception the package can raise is an
:class:`~edify.EdifyError`. Reverse-parsing an unsupported construct raises
``UnsupportedReverseParseError``, which is a plain :class:`ValueError` — catch that
type explicitly when calling :meth:`~edify.RegexBuilder.from_regex`.
