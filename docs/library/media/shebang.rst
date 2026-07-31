Shebang
=======

A `shebang <https://en.wikipedia.org/wiki/Shebang_(Unix)>`__ is the first line of an
executable script: ``#!`` followed by the interpreter that should run it. **Shebang**
matches that line, including the ``env`` indirection that finds an interpreter on the
``PATH``.

The construction is the literal ``#!/``, an :meth:`~edify.RegexBuilder.optional`
``usr/``, one of ``bin``, ``sbin``, or ``local``, then an optional ``env`` plus
whitespace, and finally the interpreter path.

Interpreter lines
-----------------

.. edify-playground::

   from edify.library import shebang

   shebang("#!/usr/bin/env python3")   # the portable form
   shebang("#!/bin/sh")                # a direct path
   shebang("#!/usr/bin/perl")
   shebang("#!/bin/bash")
   shebang("#!/usr/local/bin/node")

The marker and path are required
--------------------------------

.. edify-playground::

   from edify.library import shebang

   shebang("#!/bin/sh")     # valid
   shebang("python3")       # no marker
   shebang("#!")            # no path
   shebang("#!/bin/")       # no interpreter
   shebang("# comment")     # a comment, not a shebang

Arguments after the interpreter — ``#!/usr/bin/env -S python3 -u`` — are matched only
insofar as they fit the path character set, and the kernel's own handling of shebang
arguments varies by platform. A shebang line also only takes effect when the file is
executable and run directly.
