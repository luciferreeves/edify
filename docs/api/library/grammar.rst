Grammar
=======

Every validator in the :doc:`Grammar <../../library/grammar/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/grammar/index>`.

.. py:data:: edify.library.abnf

   Callable :class:`Pattern` for an augmented Backus-Naur form grammar: a rule
   name followed by a space-delimited ``=`` or ``=/`` definition.

   Full description: :doc:`ABNF <../../library/grammar/abnf>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _name = Pattern().letter().zero_or_more().any_of().alphanumeric().char("-").end()

      abnf = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .use(_name)
          .one_or_more()
          .any_of_chars(" \t")
          .char("=")
          .optional()
          .char("/")
          .one_or_more()
          .any_of_chars(" \t")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*[a-zA-Z](?:[a-zA-Z0-9]|[\-])*[ \t]+=/?[ \t]+.*$``

.. py:data:: edify.library.antlr

   Callable :class:`Pattern` for an ANTLR grammar source (``grammar Name;`` header + rules).

   Full description: :doc:`ANTLR <../../library/grammar/antlr>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      antlr = (
          Pattern()
          .start_of_input()
          .string("grammar")
          .one_or_more()
          .whitespace_char()
          .letter()
          .zero_or_more()
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char("_")
          .end()
          .char(";")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^grammar\s+[a-zA-Z][a-zA-Z0-9_]*;.*$``

.. py:data:: edify.library.bnf

   Callable :class:`Pattern` for a Backus-Naur form grammar: an
   ``<angle-bracketed>`` rule name followed by ``::=``.

   Full description: :doc:`BNF <../../library/grammar/bnf>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _name = Pattern().char("<").one_or_more().anything_but_chars("<>\r\n").char(">")

      bnf = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .use(_name)
          .zero_or_more()
          .whitespace_char()
          .string("::=")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*<[^<>\r\n]+>\s*::=.*$``

.. py:data:: edify.library.ebnf

   Callable :class:`Pattern` for an extended Backus-Naur form grammar: a bare
   rule name, ``=``, and a ``;``-terminated definition.

   Full description: :doc:`EBNF <../../library/grammar/ebnf>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _name = Pattern().letter().zero_or_more().any_of().alphanumeric().any_of_chars("_- ").end()

      ebnf = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .use(_name)
          .char("=")
          .zero_or_more()
          .any_char()
          .char(";")
          .zero_or_more()
          .whitespace_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*[a-zA-Z](?:[a-zA-Z0-9]|[_\- ])*=.*;\s*$``

.. py:data:: edify.library.peg

   Callable :class:`Pattern` for a parsing expression grammar: a rule name
   followed by the ``<-`` arrow.

   Full description: :doc:`PEG <../../library/grammar/peg>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _name = Pattern().letter().zero_or_more().any_of().alphanumeric().char("_").end()

      peg = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .use(_name)
          .zero_or_more()
          .any_of_chars(" \t")
          .string("<-")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*[a-zA-Z](?:[a-zA-Z0-9]|[_])*[ \t]*<\-.*$``

.. py:data:: edify.library.pest

   Callable :class:`Pattern` for a pest parser grammar: a rule name, ``=``, and
   a brace-delimited body with an optional silent/atomic modifier.

   Full description: :doc:`pest <../../library/grammar/pest>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _name = Pattern().letter().zero_or_more().any_of().alphanumeric().char("_").end()

      pest = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .use(_name)
          .zero_or_more()
          .any_of_chars(" \t")
          .char("=")
          .zero_or_more()
          .any_of_chars(" \t")
          .optional()
          .any_of_chars("_@$!")
          .char("{")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*[a-zA-Z](?:[a-zA-Z0-9]|[_])*[ \t]*=[ \t]*[_@$!]?\{.*$``

