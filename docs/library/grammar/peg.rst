PEG
===

A `parsing expression grammar <https://bford.info/pub/lang/peg.pdf>`__ replaces BNF's
ambiguous choice with an *ordered* one: alternatives are tried left to right and the
first success wins, so a PEG describes a parser rather than a language. Rules are
written with the arrow ``<-``, and **PEG** matches that.

The construction is a :meth:`~edify.RegexBuilder.letter`-led name, optional spaces or
tabs, then the :meth:`~edify.RegexBuilder.string` literal ``<-``. The definition
follows under :meth:`~edify.RegexBuilder.dot_all`.

Rule definitions
----------------

.. edify-playground::

   from edify.library import peg

   peg('expr <- term "+" expr')
   peg("Digit <- [0-9]")
   peg("Spacing <- (Space / Comment)*")
   peg("expr<-term")                    # whitespace is optional

The arrow is required
---------------------

It is what distinguishes a PEG from the equals-based notations:

.. edify-playground::

   from edify.library import peg

   peg("expr <- term")      # PEG
   peg("expr = term ;")     # EBNF
   peg("<expr> ::= term")   # BNF
   peg("hello")             # not a grammar

The ordered-choice semantics that make PEGs distinctive live in the rule bodies, not
the frame this matches — and the classic PEG pitfall, a left-recursive rule that
never terminates, is invisible here. For the pest dialect see :doc:`pest`.
