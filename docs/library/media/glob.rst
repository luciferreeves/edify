Glob
====

A `glob <https://en.wikipedia.org/wiki/Glob_(programming)>`__ is a wildcard pattern
for matching file paths — ``*.py``, ``src/**/*.ts``. **Glob** requires that a
wildcard actually be present: without one, the string is a plain path rather than a
pattern.

The construction is a run of characters, then a required wildcard from ``*``, ``?``,
``[``, or ``]``, then more characters — with control codes excluded throughout via
:meth:`~edify.RegexBuilder.assert_not_ahead`.

Wildcard patterns
-----------------

.. edify-playground::

   from edify.library import glob

   glob("*.py")             # a suffix match
   glob("src/**/*.ts")      # a recursive match
   glob("?.txt")            # a single-character wildcard
   glob("data[0-9].csv")    # a character class
   glob("**/test_*.py")

A wildcard is required
----------------------

.. edify-playground::

   from edify.library import glob

   glob("*.py")           # a pattern
   glob("src/main.py")    # a literal path
   glob("report.pdf")     # likewise
   glob("")               # empty

Glob dialects differ — whether ``**`` crosses directory boundaries, whether braces
expand — so this confirms a pattern *contains* wildcards rather than validating one
dialect. Be careful passing user-supplied globs to a filesystem walk: a broad pattern
can traverse far more than intended. For literal paths see
:doc:`../address/path`.
