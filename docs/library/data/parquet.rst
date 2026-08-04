Parquet
=======

`Apache Parquet <https://parquet.apache.org/docs/file-format/>`__ is a columnar
storage format, and its files are bracketed by a four-byte magic number: ``PAR1`` at
the start and again at the very end. **Parquet** checks the leading marker, which is
what a reader inspects first.

The construction is a :meth:`~edify.RegexBuilder.string` literal anchored at
:meth:`~edify.RegexBuilder.start_of_input`, followed by
:meth:`~edify.RegexBuilder.zero_or_more` :meth:`~edify.RegexBuilder.any_char` under
:meth:`~edify.RegexBuilder.dot_all` — the flag matters, because a real file's bytes
certainly contain newlines.

The magic prefix
----------------

Any content may follow, across as many lines of binary as the file holds:

.. edify-playground::

   from edify.library import parquet

   parquet("PAR1")                    # the marker alone
   parquet("PAR1\x15\x00column data") # a file body
   parquet("PAR1row groups\nfooter")  # bytes spanning lines

Exactly those four bytes
------------------------

The marker is case-sensitive and complete — a truncated or lowercased prefix is not
a Parquet file:

.. edify-playground::

   from edify.library import parquet

   parquet("PAR1")    # the complete marker
   parquet("PAR")     # truncated
   parquet("par1")    # wrong case
   parquet("hello")   # not a signature

Matching the signature says the file announces itself as Parquet; it does not
validate the footer, schema, or row groups. For the other columnar format see
:doc:`orc`, and for the row-oriented container, :doc:`avro`.
