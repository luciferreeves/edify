SVG
===

`SVG <https://www.w3.org/TR/SVG2/>`__ is an XML vocabulary for vector graphics, so
an SVG file is a text document rooted at ``<svg``. It may be preceded by an XML
declaration or a comment, and **SVG** accepts all three openings.

The three forms are the branches of an :func:`~edify.any_of`: a declaration then the
root, a comment then the root, or the root directly. All run under
:meth:`~edify.RegexBuilder.dot_all` so the drawing's elements may span lines.

Root element and preambles
--------------------------

.. edify-playground::

   from edify.library import svg

   svg('<svg xmlns="http://www.w3.org/2000/svg"/>')
   svg('<?xml version="1.0"?>\n<svg viewBox="0 0 10 10"><path/></svg>')
   svg("<!-- generated -->\n<svg/>")
   svg("  <svg/>")                                  # leading whitespace

The root must be svg
--------------------

A generic XML document is not an SVG:

.. edify-playground::

   from edify.library import svg

   svg("<svg/>")      # the SVG root
   svg("<html/>")     # HTML
   svg("<root/>")     # generic XML
   svg("hello")       # not markup

SVG is executable content: it can carry ``<script>`` elements and external
references, so a signature match is not a safety judgement — sanitise before
embedding untrusted SVG in a page. For generic markup see :doc:`../data/xml`.
