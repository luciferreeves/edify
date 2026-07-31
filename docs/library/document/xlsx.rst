Spreadsheet
===========

A `.xlsx <https://learn.microsoft.com/en-us/openspecs/office_standards/ms-xlsx/>`__
workbook is a ZIP archive like its siblings, identified by the ``xl/`` directory it
contains alongside the ZIP magic ``PK\x03\x04``. **Spreadsheet** requires both.

The construction mirrors :doc:`docx`: the ZIP magic via
:meth:`~edify.RegexBuilder.string`, arbitrary bytes, then the ``xl/`` entry name,
under :meth:`~edify.RegexBuilder.dot_all`.

The package signature
---------------------

.. edify-playground::

   from edify.library import xlsx

   xlsx("PK\x03\x04\x14\x00[Content_Types].xml xl/workbook.xml")
   xlsx("PK\x03\x04junk xl/worksheets/sheet1.xml")

Told apart by its entries
-------------------------

.. edify-playground::

   from edify.library import xlsx

   xlsx("PK\x03\x04x xl/workbook.xml")     # a spreadsheet
   xlsx("PK\x03\x04x word/document.xml")   # a document: see docx
   xlsx("PK\x03\x04x ppt/presentation.xml")  # a presentation: see pptx
   xlsx("hello")                            # not an archive

The same caveat as :doc:`docx` applies — the entry name is matched in the raw bytes,
so open the archive when certainty matters. Spreadsheets can also carry macros and
external links; a signature match says nothing about safety.
