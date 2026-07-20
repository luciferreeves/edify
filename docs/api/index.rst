API reference
=============

The complete public surface, generated from the source. For a guided tour start
with the :doc:`../guide/index`; for the ready-made validators see the
:doc:`../library/index`.

.. toctree::
   :hidden:

   builder
   factories
   constants
   results
   introspection
   serialization
   testing

The builder
-----------

:doc:`builder` — :class:`~edify.RegexBuilder`, the fluent immutable builder, and
:class:`~edify.Pattern`, the callable reusable fragment. Every token, quantifier,
group, capture, assertion, flag, and match verb lives here.

Composition
-----------

:doc:`factories` — a standalone factory function for every builder method, for a
functional style. :doc:`constants` — ready-made single-token patterns like
``DIGIT`` and ``START``.

Results
-------

:doc:`results` — :class:`~edify.Regex` (a compiled pattern with the full ``re``
surface plus introspection), :class:`~edify.result.Match`, and
:class:`~edify.result.NamedCaptures`.

Introspection and serialization
-------------------------------

:doc:`introspection` — turn a pattern into prose, a diagram, or an annotated
verbose form. :doc:`serialization` — round-trip a pattern through a dict or JSON.

Testing and errors
------------------

:doc:`testing` — snapshot assertions, group-name validation, and the edify error
hierarchy.
