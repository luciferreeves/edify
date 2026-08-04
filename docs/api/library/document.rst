Documents
=========

Every validator in the :doc:`document <../../library/document/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/document/index>`.

.. py:function:: edify.library.docx(value: str) -> bool

   Word document. See :doc:`../../library/document/docx` for the full description.

   Emits ``^PK.*word/.*$``

.. py:function:: edify.library.epub(value: str) -> bool

   EPUB. See :doc:`../../library/document/epub` for the full description.

   Emits ``^PK.*application/epub\+zip.*$``

.. py:function:: edify.library.mobi(value: str) -> bool

   MOBI. See :doc:`../../library/document/mobi` for the full description.

   Emits ``^.{60}BOOKMOBI.*$``

.. py:function:: edify.library.odt(value: str) -> bool

   OpenDocument text. See :doc:`../../library/document/odt` for the full description.

   Emits ``^PK.*application/vnd\.oasis\.opendocument\.text.*$``

.. py:function:: edify.library.pdf(value: str) -> bool

   PDF. See :doc:`../../library/document/pdf` for the full description.

   Emits ``^%PDF\-\d\.\d.*$``

.. py:function:: edify.library.pptx(value: str) -> bool

   Presentation. See :doc:`../../library/document/pptx` for the full description.

   Emits ``^PK.*ppt/.*$``

.. py:function:: edify.library.readme(value: str) -> bool

   README. See :doc:`../../library/document/readme` for the full description.

   Emits ``^readme(?:\.(?:md|markdown|rst|txt|adoc|org))?$``

.. py:function:: edify.library.rtf(value: str) -> bool

   RTF. See :doc:`../../library/document/rtf` for the full description.

   Emits ``^\{\\rtf\d?.*$``

.. py:function:: edify.library.svg(value: str) -> bool

   SVG. See :doc:`../../library/document/svg` for the full description.

   Emits ``^\s*(?:<\?xml.*<svg|<!\-\-.*<svg|<svg).*$``

.. py:function:: edify.library.tex(value: str) -> bool

   TeX. See :doc:`../../library/document/tex` for the full description.

   Emits ``^\\documentclass(?:\[[^\]]*\])?\{[^}]+\}.*$``

.. py:function:: edify.library.xlsx(value: str) -> bool

   Spreadsheet. See :doc:`../../library/document/xlsx` for the full description.

   Emits ``^PK.*xl/.*$``

