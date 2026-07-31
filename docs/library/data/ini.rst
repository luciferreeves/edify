INI
===

The `INI file <https://en.wikipedia.org/wiki/INI_file>`__ has no standard — every
tool that reads one has its own dialect — but the common core is stable:
``[section]`` headers, ``key=value`` assignments, and comments introduced by ``;`` or
``#``. **INI** accepts all three openings, and both assignment separators.

They are the branches of an :func:`~edify.any_of`. The assignment branch accepts
``=`` or ``:`` via :meth:`~edify.RegexBuilder.any_of_chars`, since dialects differ,
and allows spaces inside a key because many real files have them.

Sections and assignments
------------------------

The structure most INI dialects agree on:

.. edify-playground::

   from edify.library import ini

   ini("[server]\nhost=localhost")
   ini("[DEFAULT]\nretries = 3")
   ini("key=value")
   ini("key: value")     # the colon dialect
   ini("log level = 2")  # spaces inside a key

Comments
--------

Both markers are in wide use, so both are accepted:

.. edify-playground::

   from edify.library import ini

   ini("; a semicolon comment")
   ini("# a hash comment")
   ini("; header\n[section]\na=1")

An assignment or a section is required
--------------------------------------

Bare text is not configuration, and markup belongs to another validator:

.. edify-playground::

   from edify.library import ini

   ini("hello-world")   # no assignment or section
   ini("<root/>")       # XML
   ini('{"a": 1}')      # JSON

Because the format is unstandardised this checks the opening rather than enforcing
one dialect's rules — duplicate keys, value quoting, and line continuations all vary
by reader. For the specified modern alternative see :doc:`toml`.
