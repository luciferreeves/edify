HTML
====

An `HTML <https://html.spec.whatwg.org/>`__ document begins in one of three ways: a
``<!DOCTYPE html>`` declaration, the ``<html>`` root element, or a comment placed
before either. **HTML** accepts all three, and because HTML tag names and the
doctype keyword are case-insensitive, the whole pattern is matched with
:meth:`~edify.RegexBuilder.ignore_case`.

The three openings are the branches of an :func:`~edify.any_of`, with
:meth:`~edify.RegexBuilder.dot_all` allowing the document body to span lines. The
case-insensitivity is applied as a compile flag, so ``<HTML>`` and ``<!doctype
html>`` match even though the emitted pattern reads lowercase.

Doctype and root element
------------------------

The standard opening, and the bare root element a fragment often starts with:

.. edify-playground::

   from edify.library import html

   html("<!DOCTYPE html>\n<html>\n  <body>Hi</body>\n</html>")
   html('<html lang="en">x</html>')
   html("<!doctype HTML>")
   html("<HTML>")             # tag names are case-insensitive

Leading comments
----------------

Conditional comments and licence headers frequently precede the doctype:

.. edify-playground::

   from edify.library import html

   html("<!-- generated -->\n<html>")
   html("  <!DOCTYPE html>")   # leading whitespace is fine

Not any markup
--------------

A generic XML document is not HTML, and plain text is not markup:

.. edify-playground::

   from edify.library import html

   html("<html>")        # an HTML root
   html("<root/>")       # XML, not HTML
   html('{"a": 1}')      # JSON, not markup
   html("hello-world")   # plain text

HTML is famously forgiving, so this identifies the document rather than validating
it — unclosed tags and misnested elements are exactly what browsers accept and a
regular expression cannot detect. For generic markup see :doc:`xml`.
