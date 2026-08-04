Documents
=========

Every validator in the :doc:`Documents <../../library/document/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/document/index>`.

.. py:data:: edify.library.docx

   Callable :class:`Pattern` for a Word document package: a ZIP container whose
   entries include ``word/``.

   Full description: :doc:`Word document <../../library/document/docx>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      docx = (
          Pattern()
          .start_of_input()
          .string("PK\x03\x04")
          .zero_or_more()
          .any_char()
          .string("word/")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^PK.*word/.*$``

.. py:data:: edify.library.epub

   Callable :class:`Pattern` for an EPUB publication: a ZIP container declaring
   the ``application/epub+zip`` media type.

   Full description: :doc:`EPUB <../../library/document/epub>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      epub = (
          Pattern()
          .start_of_input()
          .string("PK\x03\x04")
          .zero_or_more()
          .any_char()
          .string("application/epub+zip")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^PK.*application/epub\+zip.*$``

.. py:data:: edify.library.mobi

   Callable :class:`Pattern` for a MOBI e-book: the ``BOOKMOBI`` type/creator
   pair at offset 60 of the database header.

   Full description: :doc:`MOBI <../../library/document/mobi>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      mobi = (
          Pattern()
          .start_of_input()
          .exactly(60)
          .any_char()
          .string("BOOKMOBI")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^.{60}BOOKMOBI.*$``

.. py:data:: edify.library.odt

   Callable :class:`Pattern` for an OpenDocument text package: a ZIP container
   declaring the ``application/vnd.oasis.opendocument.text`` media type.

   Full description: :doc:`OpenDocument text <../../library/document/odt>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      odt = (
          Pattern()
          .start_of_input()
          .string("PK\x03\x04")
          .zero_or_more()
          .any_char()
          .string("application/vnd.oasis.opendocument.text")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^PK.*application/vnd\.oasis\.opendocument\.text.*$``

.. py:data:: edify.library.pdf

   Callable :class:`Pattern` for a PDF document (``%PDF-1.x`` header).

   Full description: :doc:`PDF <../../library/document/pdf>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      pdf = (
          Pattern()
          .start_of_input()
          .string("%PDF-")
          .digit()
          .char(".")
          .digit()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^%PDF\-\d\.\d.*$``

.. py:data:: edify.library.pptx

   Callable :class:`Pattern` for a presentation package: a ZIP container whose
   entries include ``ppt/``.

   Full description: :doc:`Presentation <../../library/document/pptx>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      pptx = (
          Pattern()
          .start_of_input()
          .string("PK\x03\x04")
          .zero_or_more()
          .any_char()
          .string("ppt/")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^PK.*ppt/.*$``

.. py:data:: edify.library.readme

   Callable :class:`Pattern` for a README file name, with or without a common
   documentation extension.

   Full description: :doc:`README <../../library/document/readme>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      readme = (
          Pattern()
          .start_of_input()
          .string("readme")
          .optional()
          .group()
          .char(".")
          .any_of()
          .string("md")
          .string("markdown")
          .string("rst")
          .string("txt")
          .string("adoc")
          .string("org")
          .end()
          .end()
          .end_of_input()
          .ignore_case()
      )

   **Emits** ``^readme(?:\.(?:md|markdown|rst|txt|adoc|org))?$``

.. py:data:: edify.library.rtf

   Callable :class:`Pattern` for an RTF document (``{\rtfN`` prefix).

   Full description: :doc:`RTF <../../library/document/rtf>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      rtf = (
          Pattern()
          .start_of_input()
          .string("{\\rtf")
          .optional()
          .digit()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\{\\rtf\d?.*$``

.. py:data:: edify.library.svg

   Callable :class:`Pattern` for an SVG document: an ``<svg`` root element,
   optionally preceded by an XML declaration or a comment.

   Full description: :doc:`SVG <../../library/document/svg>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _declaration = Pattern().string("<?xml").zero_or_more().any_char().string("<svg")

      _root = Pattern().string("<svg")

      _comment = Pattern().string("<!--").zero_or_more().any_char().string("<svg")

      svg = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_declaration)
          .use(_comment)
          .use(_root)
          .end()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:<\?xml.*<svg|<!\-\-.*<svg|<svg).*$``

.. py:data:: edify.library.tex

   Callable :class:`Pattern` for a LaTeX document source (``\documentclass`` prefix).

   Full description: :doc:`TeX <../../library/document/tex>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      tex = (
          Pattern()
          .start_of_input()
          .string("\\documentclass")
          .optional()
          .group()
          .char("[")
          .zero_or_more()
          .anything_but_chars("]")
          .char("]")
          .end()
          .char("{")
          .one_or_more()
          .anything_but_chars("}")
          .char("}")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\\documentclass(?:\[[^\]]*\])?\{[^}]+\}.*$``

.. py:data:: edify.library.xlsx

   Callable :class:`Pattern` for a spreadsheet package: a ZIP container whose
   entries include ``xl/``.

   Full description: :doc:`Spreadsheet <../../library/document/xlsx>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      xlsx = (
          Pattern()
          .start_of_input()
          .string("PK\x03\x04")
          .zero_or_more()
          .any_char()
          .string("xl/")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^PK.*xl/.*$``

