Grammar
=======

Grammar notations — the metalanguages used to define syntax, each recognised by the
way it writes a production rule. Each validator is a callable
:class:`~edify.Pattern`: import it, call it with a string, get a ``bool``.

.. code-block:: python

   from edify.library import bnf, peg, antlr

   bnf("<expr> ::= <term>")       # True
   peg("expr <- term")            # True
   antlr("grammar Hello;")        # True

.. toctree::
   :hidden:

   abnf
   antlr
   bnf
   ebnf
   peg
   pest

Backus-Naur family
------------------

- :doc:`bnf` — ``<name> ::= …`` with angle-bracketed names.
- :doc:`ebnf` — ``name = … ;`` with a semicolon terminator.
- :doc:`abnf` — the :rfc:`5234` variant used throughout the RFC series.

Parsing expression family
-------------------------

- :doc:`peg` — ``name <- …`` with the arrow operator.
- :doc:`pest` — ``name = { … }`` with a braced body.

Parser generators
-----------------

- :doc:`antlr` — a ``grammar Name;`` source file.
