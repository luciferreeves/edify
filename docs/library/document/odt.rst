OpenDocument text
=================

An `OpenDocument <https://docs.oasis-open.org/office/OpenDocument/>`__ text file is
a ZIP archive whose first entry is an uncompressed ``mimetype`` file naming the
format — ``application/vnd.oasis.opendocument.text``. That declaration is more
precise than the directory-name test the Microsoft formats need, and **OpenDocument
text** looks for it after the ZIP magic ``PK\x03\x04``.

The construction is the ZIP magic, arbitrary bytes, then the media-type literal via
:meth:`~edify.RegexBuilder.string`, under :meth:`~edify.RegexBuilder.dot_all`.

The package signature
---------------------

.. edify-playground::

   from edify.library import odt

   odt("PK\x03\x04mimetypeapplication/vnd.oasis.opendocument.text")
   odt("PK\x03\x04\x14\x00mimetypeapplication/vnd.oasis.opendocument.textPK")

The media type is required
--------------------------

A ZIP without that declaration — including the Microsoft packages and the
spreadsheet variant of OpenDocument — does not match:

.. edify-playground::

   from edify.library import odt

   odt("PK\x03\x04x application/vnd.oasis.opendocument.text")   # declared
   odt("PK\x03\x04x word/document.xml")                          # a .docx
   odt("PK\x03\x04x application/vnd.oasis.opendocument.spreadsheet")  # a .ods
   odt("hello")                                                   # not an archive

Only the text variant is matched; spreadsheets (``.ods``) and presentations
(``.odp``) declare different media types. For the Microsoft equivalent see
:doc:`docx`.
