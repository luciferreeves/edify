PDF
===

Every `PDF <https://www.iso.org/standard/75839.html>`__ file begins with a header
naming the format and its version: ``%PDF-1.7``, ``%PDF-2.0``. **PDF** checks for
that header.

The construction is the :meth:`~edify.RegexBuilder.string` literal ``%PDF-``,
then :meth:`~edify.RegexBuilder.digit`, ``.``, and another digit, anchored at
:meth:`~edify.RegexBuilder.start_of_input`. The rest of the file is matched under
:meth:`~edify.RegexBuilder.dot_all`, which matters because a PDF's body is binary
and full of newlines.

The version header
------------------

.. edify-playground::

   from edify.library import pdf

   pdf("%PDF-1.4")                      # a common version
   pdf("%PDF-1.7")
   pdf("%PDF-2.0")                      # the ISO 32000-2 era
   pdf("%PDF-1.7\n%\xe2\xe3\nbody")     # a real file continues in binary

The header must be complete
---------------------------

A version number is required, and the marker is case-sensitive:

.. edify-playground::

   from edify.library import pdf

   pdf("%PDF-1.4")   # complete
   pdf("%PDF")       # no version
   pdf("%PDF-x.y")   # not digits
   pdf("PDF-1.4")    # missing the percent sign
   pdf("hello")      # not a signature

The header identifies the format; it does not validate the cross-reference table,
object structure, or that the document opens in a reader. Note also that a PDF may
carry active content — matching the signature is not a safety judgement. For the
other portable document format see :doc:`rtf`.
