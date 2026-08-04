Publishing
==========

Every validator in the :doc:`Publishing <../../library/publishing/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/publishing/index>`.

.. py:data:: edify.library.arxiv

   Callable :class:`Pattern` for an arXiv identifier.

   Full description: :doc:`arXiv <../../library/publishing/arxiv>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      _new = (
          Pattern()
          .exactly(4)
          .digit()
          .char(".")
          .between(4, 5)
          .digit()
          .optional()
          .group()
          .char("v")
          .one_or_more()
          .digit()
          .end()
      )
      _old = (
          Pattern()
          .between(2, 10)
          .lowercase()
          .optional()
          .group()
          .char(".")
          .exactly(2)
          .uppercase()
          .end()
          .char("/")
          .exactly(7)
          .digit()
          .optional()
          .group()
          .char("v")
          .one_or_more()
          .digit()
          .end()
      )

      arxiv = Pattern().start_of_input().subexpression(any_of(_new, _old)).end_of_input()

   **Emits** ``^(?:\d{4}\.\d{4,5}(?:v\d+)?|[a-z]{2,10}(?:\.[A-Z]{2})?/\d{7}(?:v\d+)?)$``

.. py:data:: edify.library.doi

   Callable :class:`Pattern` for the DOI shape.

   Full description: :doc:`DOI <../../library/publishing/doi>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      doi = (
          Pattern()
          .start_of_input()
          .string("10.")
          .between(4, 9)
          .digit()
          .char("/")
          .one_or_more()
          .any_of()
          .char("-")
          .char(".")
          .char("_")
          .char(";")
          .char("(")
          .char(")")
          .char("/")
          .char(":")
          .range("A", "Z")
          .range("a", "z")
          .range("0", "9")
          .end()
          .end_of_input()
      )

   **Emits** ``^10\.\d{4,9}/[\-\._;\(\)/:A-Za-z0-9]+$``

.. py:data:: edify.library.isbn

   Callable :class:`Pattern` for ISBN-10 or ISBN-13 shape.

   Full description: :doc:`ISBN <../../library/publishing/isbn>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      _isbn10 = (
          Pattern()
          .start_of_input()
          .exactly(9)
          .group()
          .digit()
          .optional()
          .any_of_chars("- ")
          .end()
          .any_of()
          .digit()
          .char("X")
          .char("x")
          .end()
          .end_of_input()
      )
      _isbn13 = (
          Pattern()
          .start_of_input()
          .exactly(12)
          .group()
          .digit()
          .optional()
          .any_of_chars("- ")
          .end()
          .digit()
          .end_of_input()
      )

      isbn = any_of(_isbn10, _isbn13)

   **Emits** ``(?:^(?:\d[- ]?){9}(?:\d|[Xx])$|^(?:\d[- ]?){12}\d$)``

.. py:data:: edify.library.issn

   Callable :class:`Pattern` for the ISSN shape.

   Full description: :doc:`ISSN <../../library/publishing/issn>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      issn = (
          Pattern()
          .start_of_input()
          .exactly(4)
          .digit()
          .char("-")
          .exactly(3)
          .digit()
          .any_of()
          .digit()
          .char("X")
          .char("x")
          .end()
          .end_of_input()
      )

   **Emits** ``^\d{4}\-\d{3}(?:\d|[Xx])$``

.. py:data:: edify.library.pmc

   Callable :class:`Pattern` for a PubMed Central identifier.

   Full description: :doc:`PMC <../../library/publishing/pmc>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      pmc = Pattern().start_of_input().string("PMC").between(1, 9).digit().end_of_input()

   **Emits** ``^PMC\d{1,9}$``

.. py:data:: edify.library.pmid

   Callable :class:`Pattern` for a PubMed identifier (1-8 digits).

   Full description: :doc:`PMID <../../library/publishing/pmid>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      pmid = Pattern().start_of_input().between(1, 8).digit().end_of_input()

   **Emits** ``^\d{1,8}$``

