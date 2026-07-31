ABNF
====

`Augmented BNF <https://datatracker.ietf.org/doc/html/rfc5234>`__ (:rfc:`5234`) is
the notation the RFC series uses to define its own protocols — including the email
and URI grammars behind several validators in this library. A rule is written
``name = definition``, with a space-delimited ``=``, or ``=/`` to add alternatives to
an existing rule.

The construction is a :meth:`~edify.RegexBuilder.letter`-led hyphenated name, one or
more spaces or tabs, then ``=`` with an :meth:`~edify.RegexBuilder.optional` ``/``,
then more whitespace. Requiring whitespace on both sides of the operator is what
keeps this from matching an ordinary assignment.

Rule definitions
----------------

.. edify-playground::

   from edify.library import abnf

   abnf("rule = %x41 / %x42")            # hex terminal values
   abnf("name = 1*ALPHA")                # a repetition
   abnf("obs-fold =/ CRLF")              # an incremental alternative
   abnf("URI = scheme \":\" hier-part")   # a hyphenated name

Whitespace around the operator
------------------------------

.. edify-playground::

   from edify.library import abnf

   abnf("rule = value")     # spaced
   abnf("rule=value")       # unspaced
   abnf("<rule> ::= x")     # BNF
   abnf("hello")            # not a grammar

One overlap worth knowing: in ABNF a ``;`` begins a *comment*, so an EBNF-looking
rule such as ``expr = x ;`` is also valid ABNF with an empty trailing comment, and
both validators accept it. Use the surrounding document to decide which notation you
are reading. For the terminator-based notation see :doc:`ebnf`.
