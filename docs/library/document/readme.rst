README
======

**README** is the odd one out in this category: a
`README <https://en.wikipedia.org/wiki/README>`__ has no content signature, because
it can be plain text, Markdown, or reStructuredText. What identifies it is the
*file name*, so that is what this validator matches — ``README`` with an optional
documentation extension.

The construction is the :meth:`~edify.RegexBuilder.string` literal ``readme``, then
an :meth:`~edify.RegexBuilder.optional` group of ``.`` plus an
:func:`~edify.any_of` of the common extensions. The whole pattern carries
:meth:`~edify.RegexBuilder.ignore_case`, since the file is written ``README``,
``readme``, and ``Readme`` in roughly equal measure.

File names
----------

.. edify-playground::

   from edify.library import readme

   readme("README")            # no extension
   readme("README.md")         # Markdown
   readme("readme.rst")        # reStructuredText
   readme("Readme.txt")        # plain text
   readme("README.markdown")   # the long form
   readme("readme.adoc")       # AsciiDoc

The name must be exact
----------------------

A different stem, or an extension outside the documentation set, does not match:

.. edify-playground::

   from edify.library import readme

   readme("README.md")    # valid
   readme("READ.ME")      # a different name
   readme("README.pdf")   # not a documentation extension
   readme("readme.")      # a trailing dot with no extension
   readme("CONTRIBUTING.md")   # a different document

Because this matches a name rather than content, it takes a bare file name — strip
any directory path before calling it. For the file's actual contents see
:doc:`../data/html` or the Markdown you render it with.
