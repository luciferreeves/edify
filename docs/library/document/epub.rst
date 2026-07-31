EPUB
====

An `EPUB <https://www.w3.org/TR/epub-33/>`__ publication is a ZIP archive whose
first entry must be an uncompressed ``mimetype`` file containing exactly
``application/epub+zip``. **EPUB** looks for that declaration after the ZIP magic
``PK\x03\x04``.

The construction is the ZIP magic via :meth:`~edify.RegexBuilder.string`, arbitrary
bytes, then the media-type literal, under :meth:`~edify.RegexBuilder.dot_all`.

The publication signature
-------------------------

.. edify-playground::

   from edify.library import epub

   epub("PK\x03\x04mimetypeapplication/epub+zip")
   epub("PK\x03\x04\x14\x00mimetypeapplication/epub+zipMETA-INF/container.xml")

The media type is required
--------------------------

.. edify-playground::

   from edify.library import epub

   epub("PK\x03\x04x application/epub+zip")   # declared
   epub("PK\x03\x04x word/document.xml")      # a .docx
   epub("PK\x03\x04")                          # a ZIP with no declaration
   epub("hello")                               # not an archive

The signature identifies the container; the package document, spine, and navigation
are a reader's concern. For the other common e-book format see :doc:`mobi`.
