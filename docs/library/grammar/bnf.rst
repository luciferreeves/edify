BNF
===

`Backus-Naur form <https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form>`__ is the
original grammar notation: a non-terminal in angle brackets, the definition operator
``::=``, and the alternatives it expands to. **BNF** matches that opening.

The construction is ``<``, a run of :meth:`~edify.RegexBuilder.anything_but_chars`
excluding the brackets and line breaks, then ``>``, optional whitespace, and the
:meth:`~edify.RegexBuilder.string` literal ``::=``. The rest of the grammar follows
under :meth:`~edify.RegexBuilder.dot_all`.

Production rules
----------------

.. edify-playground::

   from edify.library import bnf

   bnf('<expr> ::= <term> "+" <expr>')
   bnf('<digit> ::= "0" | "1" | "2"')
   bnf('<digit>::="0"|"1"')                    # whitespace is optional
   bnf('<expr> ::= <term>\n<term> ::= <factor>')

The angle brackets and ``::=``
------------------------------

Both are required — they are what separate BNF from its descendants:

.. edify-playground::

   from edify.library import bnf

   bnf("<expr> ::= <term>")   # BNF
   bnf("expr = term ;")       # EBNF
   bnf("expr <- term")        # PEG
   bnf("expr ::= term")       # no angle brackets
   bnf("hello")               # not a grammar

This matches the first production, not the whole grammar — undefined non-terminals,
left recursion, and unreachable rules are all beyond a pattern's reach. For the
extended notation see :doc:`ebnf`; for the RFC variant, :doc:`abnf`.
