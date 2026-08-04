Atom
====

An `Atom <https://datatracker.ietf.org/doc/html/rfc4287>`__ feed (:rfc:`4287`) is an
XML document rooted at ``<feed>`` and bound to the Atom namespace
``http://www.w3.org/2005/Atom``. Unlike :doc:`rss`, whose root tag is distinctive on
its own, ``feed`` is a common word — so **Atom** requires the namespace as well, and
that pairing is the whole test.

An optional XML declaration may come first. The root tag is matched with
:meth:`~edify.RegexBuilder.string`, and the namespace must appear somewhere in the
attributes that follow, with :meth:`~edify.RegexBuilder.dot_all` allowing the
document to span lines.

A feed document
---------------

The namespace usually sits on the root element, with or without a declaration in
front:

.. edify-playground::

   from edify.library import atom

   atom('<?xml version="1.0"?>\n<feed xmlns="http://www.w3.org/2005/Atom">\n  <title>News</title>\n</feed>')
   atom('<feed xmlns="http://www.w3.org/2005/Atom"><entry/></feed>')

The namespace is required
-------------------------

A bare ``<feed>`` or one bound elsewhere is not an Atom document, and the other
syndication format has its own root:

.. edify-playground::

   from edify.library import atom

   atom('<feed xmlns="http://www.w3.org/2005/Atom"/>')   # the namespace makes it Atom
   atom("<feed/>")                          # no namespace
   atom('<feed xmlns="urn:other"/>')        # the wrong namespace
   atom('<rss version="2.0"/>')             # that is RSS
   atom("hello-world")                       # not XML

It confirms the document is an Atom feed; entry contents, required identifiers, and
timestamp formats are a parser's job. For the other syndication format see
:doc:`rss`.
