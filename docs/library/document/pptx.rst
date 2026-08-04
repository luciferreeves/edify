Presentation
============

A `.pptx <https://learn.microsoft.com/en-us/openspecs/office_standards/ms-pptx/>`__
deck is the third of the ZIP-based office formats, carrying a ``ppt/`` directory
next to the ZIP magic ``PK\x03\x04``. **Presentation** requires both.

The construction follows :doc:`docx` and :doc:`xlsx` exactly, differing only in the
entry name it looks for, and runs under :meth:`~edify.RegexBuilder.dot_all`.

The package signature
---------------------

.. edify-playground::

   from edify.library import pptx

   pptx("PK\x03\x04\x14\x00[Content_Types].xml ppt/presentation.xml")
   pptx("PK\x03\x04junk ppt/slides/slide1.xml")

Told apart by its entries
-------------------------

.. edify-playground::

   from edify.library import pptx

   pptx("PK\x03\x04x ppt/presentation.xml")   # a presentation
   pptx("PK\x03\x04x word/document.xml")      # a document: see docx
   pptx("PK\x03\x04x xl/workbook.xml")        # a spreadsheet: see xlsx
   pptx("hello")                               # not an archive

As with the other packages, confirm by opening the archive when it matters.
