Word document
=============

A `.docx <https://learn.microsoft.com/en-us/openspecs/office_standards/ms-docx/>`__
file is not a single document — it is a ZIP archive of XML parts. Its signature is
therefore the ZIP magic ``PK\x03\x04``, and what distinguishes it from a spreadsheet
or a presentation is the ``word/`` directory inside. **Word document** requires
both.

The construction is the ZIP magic via :meth:`~edify.RegexBuilder.string`, then any
bytes, then the literal ``word/``, all under :meth:`~edify.RegexBuilder.dot_all` so
the compressed body's newlines do not break the scan.

The package signature
---------------------

.. edify-playground::

   from edify.library import docx

   docx("PK\x03\x04\x14\x00[Content_Types].xml word/document.xml")
   docx("PK\x03\x04junk word/styles.xml more")

Both parts are required
-----------------------

A ZIP without a ``word/`` entry is a different package — which is exactly how the
three office formats are told apart:

.. edify-playground::

   from edify.library import docx

   docx("PK\x03\x04x word/document.xml")   # a word package
   docx("PK\x03\x04x xl/workbook.xml")     # a spreadsheet: see xlsx
   docx("PK\x03\x04")                      # a ZIP with no entries seen
   docx("hello")                            # not an archive

Because the entry name is searched in the raw bytes, a ZIP that merely *contains* a
file called ``word/`` somewhere would also match — treat this as a strong hint
rather than proof, and open the archive to be certain. For the sibling formats see
:doc:`xlsx` and :doc:`pptx`; for the open standard, :doc:`odt`.
