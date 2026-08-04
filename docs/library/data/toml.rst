TOML
====

`TOML <https://toml.io/>`__ was designed to be an obvious configuration format: a
file is a flat set of key/value assignments, grouped under bracketed table headers.
**TOML** recognises the three ways such a file can begin — a ``[table]`` header, a
``key =`` assignment, or a ``#`` comment.

Those are the branches of an :func:`~edify.any_of`. The table branch allows the
doubled ``[[…]]`` form used for arrays of tables; the key branch permits dotted keys
and quoted keys, and requires the ``=`` that distinguishes an assignment from a
:doc:`yaml` mapping's colon.

Tables
------

A header groups the assignments that follow it, and the doubled form appends to an
array of tables:

.. edify-playground::

   from edify.library import toml

   toml("[server]\nhost = \"localhost\"")
   toml("[a.b.c]")                       # a dotted table name
   toml("[[products]]\nname = \"hammer\"")  # an array of tables

Assignments and comments
------------------------

A file may open straight into a top-level key, or with a comment:

.. edify-playground::

   from edify.library import toml

   toml('key = "value"')
   toml("port = 8080")
   toml("a.b = 2")                # a dotted key
   toml("# a comment\na = 1")

The equals sign is required
---------------------------

Without it there is no assignment, which is what separates TOML from the
colon-based formats:

.. edify-playground::

   from edify.library import toml

   toml('key = "value"')   # the equals sign makes it TOML
   toml("key: value")   # that is YAML or INI
   toml("hello-world")  # no assignment
   toml("<root/>")      # XML

It matches how the document opens, not that every value parses — dates, arrays, and
multi-line strings are a parser's concern. For the older, less specified convention
see :doc:`ini`; for the indentation-based alternative, :doc:`yaml`.
