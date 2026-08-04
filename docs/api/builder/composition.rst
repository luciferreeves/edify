Composition
===========

Embed one pattern inside another. ``use`` is an alias for ``subexpression`` —
they are the same method, named for whichever reads better in your chain.

.. automethod:: edify.RegexBuilder.use

.. automethod:: edify.RegexBuilder.subexpression

Copying
-------

Every chain method already returns a new builder, so two extensions of a shared
base never interfere. These make an independent copy explicit when you are
stashing a builder to branch from later.

.. automethod:: edify.RegexBuilder.copy

.. automethod:: edify.RegexBuilder.fork

Parsing an existing regex
-------------------------

.. automethod:: edify.RegexBuilder.from_regex

Low-level state
---------------

The two members every builder carries to satisfy
:class:`~edify.builder.types.protocol.BuilderProtocol`. You need them only when
writing a mixin or a tool that manipulates builders generically.

.. automethod:: edify.RegexBuilder.with_state

.. automethod:: edify.RegexBuilder.lazy_regex
