XML
===

An `XML <https://www.w3.org/TR/xml/>`__ document opens in one of two ways: with the
optional XML *declaration* — ``<?xml version="1.0"?>`` — or straight into its root
element. **XML** accepts either, with leading whitespace allowed.

The two openings are the branches of an :func:`~edify.any_of`. The element branch
enforces the naming rule that catches most malformed markup: a name starts with a
letter or underscore, never a digit, and continues with letters, digits, and the
punctuation ``.``, ``-``, ``_``, and ``:`` for namespace prefixes.
:meth:`~edify.RegexBuilder.dot_all` allows the document to run to any length.

With a declaration
------------------

The form a serialiser emits, carrying version and encoding:

.. edify-playground::

   from edify.library import xml

   xml('<?xml version="1.0"?>\n<root/>')
   xml('<?xml version="1.0" encoding="UTF-8"?>\n<catalog>\n  <book id="1"/>\n</catalog>')
   xml('  <?xml version="1.0"?>\n<a/>')

Bare root elements
------------------

A fragment or a document written without the declaration, including namespace-
prefixed and underscore-led names:

.. edify-playground::

   from edify.library import xml

   xml("<root><a>1</a></root>")
   xml('<ns:tag attr="v"/>')
   xml("<_private/>")
   xml('<html lang="en">x</html>')

Element names have rules
------------------------

A name may not begin with a digit, and a stray space after ``<`` means it is not a
tag at all:

.. edify-playground::

   from edify.library import xml

   xml("<1bad/>")     # a name cannot start with a digit
   xml("< root>")     # a space after the angle bracket
   xml('{"a": 1}')    # that is JSON
   xml("not xml")     # no markup

It confirms the document opens as XML; it does not check that tags nest correctly or
that every element is closed — a regular expression cannot match balanced structure.
For the HTML dialect see :doc:`html`, and for specific XML vocabularies,
:doc:`../api/rss`, :doc:`../api/atom`, and :doc:`../api/soap`.
