Groups and alternation
======================

Grouping opens a scope that :meth:`~edify.RegexBuilder.end` closes. ``any_of``
and ``one_of`` build alternations. ``atomic`` groups without allowing the engine
to backtrack into what it matched.

.. automethod:: edify.RegexBuilder.group

.. automethod:: edify.RegexBuilder.atomic

.. automethod:: edify.RegexBuilder.any_of

.. automethod:: edify.RegexBuilder.one_of

.. automethod:: edify.RegexBuilder.end
