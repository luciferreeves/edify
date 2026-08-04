pest
====

`pest <https://pest.rs/>`__ is a parsing expression grammar dialect whose rules take
the form ``name = { body }`` — an equals sign, then a *braced* body, optionally
preceded by a modifier that changes how the rule reports itself. **pest** matches
that shape.

The construction is a :meth:`~edify.RegexBuilder.letter`-led name, ``=``, an
:meth:`~edify.RegexBuilder.optional` modifier character from ``_ @ $ !``, then ``{``.
The brace is what separates pest from the ``;``-terminated :doc:`ebnf` and the
arrow-based :doc:`peg`.

Rules and modifiers
-------------------

Each modifier means something different: ``_`` silences a rule, ``@`` makes it
atomic, ``$`` compound-atomic, ``!`` non-atomic:

.. edify-playground::

   from edify.library import pest

   pest('expr = { term ~ "+" ~ expr }')       # a plain rule
   pest('WHITESPACE = _{ " " | "\\t" }')       # silent
   pest("ident = @{ ASCII_ALPHA+ }")           # atomic
   pest('quoted = ${ "\\"" ~ inner ~ "\\"" }')  # compound-atomic

The braced body is required
---------------------------

.. edify-playground::

   from edify.library import pest

   pest("expr = { term }")   # braced
   pest("expr = term ;")     # EBNF
   pest("expr <- term")      # plain PEG
   pest("hello")             # not a grammar

This matches the rule frame; the built-in rules, operators, and stack behaviour
inside the braces are for the pest compiler to check. For the notation pest extends
see :doc:`peg`.
