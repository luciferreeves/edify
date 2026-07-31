EBNF
====

`Extended BNF <https://www.iso.org/standard/26153.html>`__ drops the angle brackets
and adds repetition and optionality operators. Its rules are written ``name = …
;`` — a bare name, an equals sign, and a semicolon terminator. **EBNF** matches
that shape.

The construction is a :meth:`~edify.RegexBuilder.letter`-led name, ``=``, then any
content, and finally the ``;`` that ends every rule. That terminator is the
distinguishing feature: :doc:`abnf` uses the same ``name =`` opening but does not
require it.

Production rules
----------------

.. edify-playground::

   from edify.library import ebnf

   ebnf('expr = term , "+" , expr ;')
   ebnf('digit = "0" | "1" | "2" ;')
   ebnf('letter = "a" ... "z" ;\n')
   ebnf('opt = [ "-" ] , digit ;')     # optionality brackets

The semicolon is required
-------------------------

.. edify-playground::

   from edify.library import ebnf

   ebnf("expr = term ;")     # terminated
   ebnf("expr = term")       # no terminator
   ebnf("<expr> ::= term")   # BNF
   ebnf("expr <- term")      # PEG
   ebnf("hello")             # not a grammar

Dialects of EBNF differ in their operators — the ISO standard, the W3C variant, and
various tool-specific forms all disagree — so this matches the rule *frame* rather
than any one dialect's body syntax. For the original notation see :doc:`bnf`.
