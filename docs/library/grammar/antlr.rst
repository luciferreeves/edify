ANTLR
=====

`ANTLR <https://www.antlr.org/>`__ is a parser generator, and its grammar files open
with a declaration naming the grammar: ``grammar Hello;``. That header is unique
among the notations here — the others begin with their first rule — and **ANTLR**
matches it.

The construction is the :meth:`~edify.RegexBuilder.string` literal ``grammar``,
whitespace, a :meth:`~edify.RegexBuilder.letter`-led identifier, then ``;``. The
rules follow under :meth:`~edify.RegexBuilder.dot_all`.

Grammar declarations
--------------------

.. edify-playground::

   from edify.library import antlr

   antlr("grammar Hello;\nr : 'hello' ID ;")
   antlr("grammar Expr;\nprog: stat+ ;")
   antlr("grammar JSON;")                     # the header alone
   antlr("grammar My_Grammar2;\nx : 'a';")     # underscores and digits

The header is required
----------------------

.. edify-playground::

   from edify.library import antlr

   antlr("grammar Hello;")   # declared
   antlr("grammar Hello")    # no semicolon
   antlr("grammar ;")        # no name
   antlr("expr <- term")     # PEG
   antlr("hello")            # not a grammar

The ``lexer grammar`` and ``parser grammar`` variants carry a keyword before
``grammar`` and are not matched here. Rule definitions, actions, and imports are the
generator's concern. For the notation ANTLR's rules resemble see :doc:`ebnf`.
