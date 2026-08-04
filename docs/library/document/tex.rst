TeX
===

A `LaTeX <https://www.latex-project.org/>`__ source file opens by declaring the
document class it is typeset with: ``\documentclass{article}``, optionally with
options in brackets. **TeX** matches that declaration.

The construction is the :meth:`~edify.RegexBuilder.string` literal
``\documentclass``, an :meth:`~edify.RegexBuilder.optional` bracketed options group
built from :meth:`~edify.RegexBuilder.anything_but_chars`, then the required braced
class name — all under :meth:`~edify.RegexBuilder.dot_all` so the document body
follows freely.

The document class
------------------

.. edify-playground::

   from edify.library import tex

   tex("\\documentclass{article}")
   tex("\\documentclass[12pt,a4paper]{report}")     # with options
   tex("\\documentclass{book}\n\\begin{document}\nHi\n\\end{document}")

The class name is required
--------------------------

Options are optional; the braced class is not:

.. edify-playground::

   from edify.library import tex

   tex("\\documentclass{article}")   # complete
   tex("\\documentclass")            # no class name
   tex("\\documentclass{}")          # an empty class name
   tex("\\begin{document}")          # a different command
   tex("hello")                      # not TeX

This matches LaTeX documents specifically. Plain TeX and ConTeXt files open
differently and will not match, and a ``.sty`` package or a fragment meant for
``\input`` has no ``\documentclass`` at all. For the typeset output see :doc:`pdf`.
