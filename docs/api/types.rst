Types
=====

The type names that appear in signatures elsewhere in this reference. You rarely
construct these yourself — they are what edify's own functions accept and return —
but knowing what each one is makes the rest of the reference readable.

Type aliases
------------

.. py:data:: edify.builder.types.engine.Engine

   ``Literal["re", "regex"]`` — which backend compiles a pattern. Passed as the
   ``engine`` argument to :meth:`~edify.RegexBuilder.to_regex`. ``"re"`` is the
   standard library; ``"regex"`` is the third-party module, which supports
   variable-width lookbehind and per-call timeouts.

.. py:data:: edify.serialize.JSONPrimitive

   ``str | int | float | bool | None`` — a scalar that survives a JSON round trip.

.. py:data:: edify.serialize.JSONValue

   ``JSONPrimitive | list[JSONValue] | dict[str, JSONValue]`` — any value a
   canonical pattern document may contain. This is the element type of the dicts
   :func:`~edify.serialize.element_to_dict` and
   :func:`~edify.serialize.state_to_dict` produce.

The builder protocol
--------------------

.. autoclass:: edify.builder.types.protocol.BuilderProtocol
   :members:

Every factory function in :doc:`factories` takes its operand as a
``BuilderProtocol``, which is why a :class:`~edify.Pattern`, a
:class:`~edify.RegexBuilder`, and an atom are all accepted interchangeably. It is
a structural protocol, not a base class — anything carrying the two attributes
below satisfies it.

Builder state
-------------

.. autoclass:: edify.builder.types.state.BuilderState
   :members:

The immutable snapshot a builder carries. Every chain method returns a new builder
wrapping a new state; nothing is ever mutated in place.
:func:`~edify.serialize.state_to_dict` converts one to a canonical document.

.. autoclass:: edify.builder.types.flags.Flags
   :members:

The six pattern-global flags, as a value. Flags only ever turn on: the keyword
arguments to :meth:`~edify.RegexBuilder.to_regex` are OR-merged into whatever the
chain already carries. See :doc:`builder/flags`.

.. autoclass:: edify.builder.types.frame.StackFrame
   :members:

One entry on the stack of open constructs. Opening a
:meth:`~edify.RegexBuilder.group`, :meth:`~edify.RegexBuilder.capture`, or
lookaround pushes a frame; :meth:`~edify.RegexBuilder.end` pops it. Each frame
remembers the call site that opened it, which is how an unbalanced chain can
report the exact line the unclosed frame came from.

Elements
--------

.. autoclass:: edify.elements.types.base.BaseElement
   :members:

The marker base class every concrete element inherits. A compiled pattern exposes
its tree as :attr:`Regex.elements <edify.Regex.elements>`, and the introspection
functions in :doc:`introspection` walk exactly that structure. Each concrete
element is a frozen dataclass whose fields are its arguments — an ``ExactlyElement``
carries ``times`` and ``child``, for instance — which is what makes the tree
serializable and inspectable without parsing a regex string.

Diagnostics
-----------

The pieces an annotated error message is assembled from. See
:doc:`../guide/beyond/errors` for what the rendered result looks like.

.. autoclass:: edify.errors.formatting.CallerContext
   :members:

.. autoclass:: edify.errors.formatting.Problem
   :members:

.. autoclass:: edify.errors.formatting.FixInsertion
   :members:
