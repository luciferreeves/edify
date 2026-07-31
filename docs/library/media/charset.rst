Charset
=======

A `character set <https://www.iana.org/assignments/character-sets/character-sets.xhtml>`__
name identifies the encoding a byte stream uses — ``utf-8``, ``ISO-8859-1``. It is
what follows ``charset=`` in a Content-Type header. **Charset** matches the name
shape IANA registers.

The construction is a leading :meth:`~edify.RegexBuilder.letter` then
:meth:`~edify.RegexBuilder.between`\ ``(1, 39)`` over an
:meth:`~edify.RegexBuilder.any_of` class of alphanumerics plus ``_``, ``+``, ``.``,
and ``-`` — the punctuation registered names use.

Registered names
----------------

.. edify-playground::

   from edify.library import charset

   charset("utf-8")
   charset("UTF-8")           # case is not constrained
   charset("ISO-8859-1")
   charset("windows-1252")
   charset("Shift_JIS")       # an underscore

A letter must lead
------------------

.. edify-playground::

   from edify.library import charset

   charset("utf-8")    # valid
   charset("8859")     # starts with a digit
   charset("x")        # too short
   charset("")         # empty

This matches the name's shape, not the IANA registry, so an invented encoding still
passes — and matching says nothing about whether your runtime can decode it. For the
compression coding in ``Content-Encoding`` see :doc:`encoding`; for the media type
itself, :doc:`mimetype`.
