Filename
========

**Filename** matches a single
`file name <https://en.wikipedia.org/wiki/Filename>`__ — a stem, a dot, and a short extension — and
crucially *excludes* the characters that would make it a path or an illegal name on
common filesystems.

The stem uses :meth:`~edify.RegexBuilder.assert_not_ahead` over the forbidden set:
control codes, ``/``, ``\``, ``:``, ``*``, ``?``, ``"``, ``<``, ``>``, ``|``. The
extension is 1–10 alphanumerics after a dot.

File names
----------

Spaces and most punctuation are legal in a name, so they are accepted:

.. edify-playground::

   from edify.library import filename

   filename("report.pdf")
   filename("my file.txt")          # spaces are allowed
   filename("archive.tar.gz")       # the last dot wins
   filename("data-2024_final.csv")

No path separators
------------------

This is the point of the validator — a name is not a path, and rejecting separators
is what stops a traversal payload from being treated as a file name:

.. edify-playground::

   from edify.library import filename

   filename("report.pdf")        # a bare name
   filename("a/b.txt")           # a path separator
   filename("..\\secret.txt")    # a Windows separator
   filename("bad:name.txt")      # illegal on Windows
   filename("noextension")       # no extension

Rejecting separators is a useful first line against path traversal, but it is not
sufficient on its own — always resolve an upload path and confirm it stays inside
the intended directory. For a full path see :doc:`../address/path`; for the
extension alone, :doc:`extension`.
