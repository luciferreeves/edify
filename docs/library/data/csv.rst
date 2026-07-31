CSV
===

`Comma-separated values <https://datatracker.ietf.org/doc/html/rfc4180>`__
(:rfc:`4180`) is the least standardised format in common use, but its core is
simple: rows separated by line breaks, fields separated by commas, and any field
containing a comma wrapped in double quotes. **CSV** matches that shape and requires
at least one comma per row — a single-column file is indistinguishable from plain
text, so it is not accepted.

A field is an :func:`~edify.any_of` of two forms: a quoted run, or an unquoted run of
anything except a comma, quote, or line break. A row is a field followed by
:meth:`~edify.RegexBuilder.one_or_more` comma-and-field groups, and the document is
one or more rows.

Rows and headers
----------------

A header line, data rows, and trailing newlines all behave as you would expect:

.. edify-playground::

   from edify.library import csv

   csv("name,age,city")
   csv("name,age\nAda,36")
   csv("1,2,3\n4,5,6\n")
   csv("a,b\r\nc,d")

Quoted fields
-------------

Quoting is what lets a value contain the delimiter — the reason the format needs
more than a naive split:

.. edify-playground::

   from edify.library import csv

   csv('name,note\n"Doe, John",vip')   # a comma inside a field
   csv('"x","y"')                       # every field quoted
   csv("a,")                            # an empty trailing field
   csv(",")                             # two empty fields

At least one delimiter
----------------------

A line with no comma is just a line of text, and a different delimiter belongs to a
different format:

.. edify-playground::

   from edify.library import csv

   csv("a,b")           # one delimiter is enough
   csv("nocommas")      # a single column is not distinguishable
   csv("hello-world")   # plain text
   csv("a\tb")          # tab-separated: use tsv

This matches the delimiter structure, not the rectangularity of the data — rows with
differing field counts still pass, and a parser is the right tool for that. For the
tab-delimited variant see :doc:`tsv`.
