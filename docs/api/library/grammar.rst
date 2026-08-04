Grammar
=======

Every validator in the :doc:`grammar <../../library/grammar/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/grammar/index>`.

.. py:function:: edify.library.abnf(value: str) -> bool

   ABNF. See :doc:`../../library/grammar/abnf` for the full description.

   Emits ``^\s*[a-zA-Z](?:[a-zA-Z0-9]|[\-])*[ \t]+=/?[ \t]+.*$``

.. py:function:: edify.library.antlr(value: str) -> bool

   ANTLR. See :doc:`../../library/grammar/antlr` for the full description.

   Emits ``^grammar\s+[a-zA-Z][a-zA-Z0-9_]*;.*$``

.. py:function:: edify.library.bnf(value: str) -> bool

   BNF. See :doc:`../../library/grammar/bnf` for the full description.

   Emits ``^\s*<[^<>\r\n]+>\s*::=.*$``

.. py:function:: edify.library.ebnf(value: str) -> bool

   EBNF. See :doc:`../../library/grammar/ebnf` for the full description.

   Emits ``^\s*[a-zA-Z](?:[a-zA-Z0-9]|[_\- ])*=.*;\s*$``

.. py:function:: edify.library.peg(value: str) -> bool

   PEG. See :doc:`../../library/grammar/peg` for the full description.

   Emits ``^\s*[a-zA-Z](?:[a-zA-Z0-9]|[_])*[ \t]*<\-.*$``

.. py:function:: edify.library.pest(value: str) -> bool

   pest. See :doc:`../../library/grammar/pest` for the full description.

   Emits ``^\s*[a-zA-Z](?:[a-zA-Z0-9]|[_])*[ \t]*=[ \t]*[_@$!]?\{.*$``

