Documents
=========

Document formats identified by their content signature — the magic bytes at the
start of a file, or the marker a source format opens with. Each validator is a
callable :class:`~edify.Pattern`: import it, call it with a string, get a ``bool``.

.. code-block:: python

   from edify.library import pdf, svg, readme

   pdf("%PDF-1.7")        # True
   svg("<svg/>")          # True
   readme("README.md")    # True

.. toctree::
   :hidden:

   docx
   epub
   mobi
   odt
   pdf
   pptx
   readme
   rtf
   svg
   tex
   xlsx

Portable documents
------------------

- :doc:`pdf` — the ``%PDF-`` header; :doc:`rtf` — the ``{\\rtfN`` prefix.

Office packages
---------------

These are all ZIP containers, told apart by the entries inside:

- :doc:`docx` — a word-processing package; :doc:`xlsx` — a spreadsheet;
  :doc:`pptx` — a presentation; :doc:`odt` — the OpenDocument equivalent.

E-books
-------

- :doc:`epub` — a ZIP declaring the EPUB media type; :doc:`mobi` — the
  ``BOOKMOBI`` header.

Source and markup
-----------------

- :doc:`tex` — a ``\\documentclass`` source; :doc:`svg` — an ``<svg`` root.
- :doc:`readme` — a README file name.
