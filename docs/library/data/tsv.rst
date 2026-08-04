TSV
===

`Tab-separated values <https://www.iana.org/assignments/media-types/text/tab-separated-values>`__
is :doc:`csv`'s simpler sibling: the delimiter is a tab, and
because tabs rarely appear inside data there is no quoting convention to worry
about. **TSV** matches rows of tab-delimited fields, requiring at least one tab per
row for the same reason CSV requires a comma — a single column is just text.

A field is :meth:`~edify.RegexBuilder.zero_or_more`
:meth:`~edify.RegexBuilder.anything_but_chars` over tab and the line-break
characters; a row is a field followed by :meth:`~edify.RegexBuilder.one_or_more`
tab-and-field groups, matched with :meth:`~edify.RegexBuilder.tab`.

Rows of fields
--------------

Two columns or many, one row or several, with trailing newlines allowed:

.. edify-playground::

   from edify.library import tsv

   tsv("name\tage")
   tsv("name\tage\tcity")
   tsv("Ada\t36\nGrace\t45")
   tsv("a\tb\n")

Empty fields are fine
---------------------

A run of tabs is a row of empty values — meaningful in exported data, where a blank
cell still occupies its column:

.. edify-playground::

   from edify.library import tsv

   tsv("\t")          # two empty fields
   tsv("a\t\tc")      # an empty middle field
   tsv("\ta")         # an empty leading field

The delimiter must be a tab
---------------------------

Commas do not count, and a line without any tab is not tabular:

.. edify-playground::

   from edify.library import tsv

   tsv("a\tb")          # a tab delimiter
   tsv("a,b")           # comma-separated: use csv
   tsv("nocols")        # no delimiter
   tsv("hello world")   # a space is not a tab

Like :doc:`csv` this checks the delimiter structure rather than that every row has
the same number of columns.
