Sitemap
=======

An XML `sitemap <https://www.sitemaps.org/protocol.html>`__ lists the URLs of a site
for search engines. It is an XML document rooted at ``<urlset>`` — or
``<sitemapindex>`` when it points at other sitemaps — and bound to the sitemap
schema namespace. **Sitemap** requires the root element *and* the namespace, since
``urlset`` alone is not distinctive.

The root is an :func:`~edify.any_of` over the two element names, followed by any
attributes and then the ``http://www.sitemaps.org/schemas/sitemap/`` namespace, under
:meth:`~edify.RegexBuilder.dot_all`. An XML declaration may precede it.

Sitemaps and indexes
--------------------

.. edify-playground::

   from edify.library import sitemap

   sitemap('<?xml version="1.0"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>https://a.io/</loc></url>\n</urlset>')
   sitemap('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"/>')

The namespace is required
-------------------------

.. edify-playground::

   from edify.library import sitemap

   sitemap('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"/>')   # bound
   sitemap("<urlset/>")                                                        # no namespace
   sitemap('<urlset xmlns="urn:other"/>')                                      # the wrong namespace
   sitemap("hello")                                                            # not XML

This confirms the document is a sitemap; the ``<loc>`` entries, the 50,000-URL limit,
and the file-size cap are a generator's concern. For the file that usually points at
it see :doc:`robots`; for generic markup, :doc:`../data/xml`.
