RSS
===

An `RSS <https://www.rssboard.org/rss-specification>`__ feed is an XML document
whose root element is ``<rss>``. That single element is what **RSS** looks for, with
an optional XML declaration allowed in front of it.

The declaration is wrapped in :meth:`~edify.RegexBuilder.optional`; the root tag is
matched with :meth:`~edify.RegexBuilder.string`, and it must be followed by
whitespace or ``>`` so that a longer element name cannot pass for it. Everything
after the root is free, since a feed's channel and items may run to any length.

A feed document
---------------

With the declaration a real feed carries, and in the bare form a snippet often
takes:

.. edify-playground::

   from edify.library import rss

   rss('<?xml version="1.0"?>\n<rss version="2.0">\n  <channel><title>News</title></channel>\n</rss>')
   rss('<rss version="2.0"><channel/></rss>')
   rss('<rss version="0.91">x</rss>')

The root element must be exact
------------------------------

A tag that merely starts with the same letters is a different element, and the other
syndication format has its own validator:

.. edify-playground::

   from edify.library import rss

   rss("<rssfeed/>")     # a different element
   rss("<feed/>")        # that is Atom
   rss("hello-world")    # not XML

It confirms the document is an RSS feed; the channel metadata, item elements, and
date formats are left to a parser. For the other syndication format see
:doc:`atom`; for XML in general, :doc:`../data/xml`.
