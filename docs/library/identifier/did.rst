DID
===

A `decentralised identifier <https://www.w3.org/TR/did-core/>`__ names a subject
without a central registry: ``did:method:identifier``, where the method says how the
identifier resolves. **DID** matches that structure.

The construction is the :meth:`~edify.RegexBuilder.string` literal ``did:``, a
lowercase alphanumeric method name, another ``:``, and the
method-specific identifier — matched permissively, since each method defines its own
syntax.

Identifiers by method
---------------------

.. edify-playground::

   from edify.library import did

   did("did:example:123456789abcdefghi")
   did("did:web:example.com")          # resolved via a domain
   did("did:key:z6MkhaXgBZDvotDkL5257faiztiGiC2QtKLGpbnnEGta2doK")
   did("did:ion:EiClkZMDxPKqC9c-umQfTkR8")

All three parts are required
----------------------------

.. edify-playground::

   from edify.library import did

   did("did:example:123")   # complete
   did("did:example:")      # no identifier
   did("did:example")       # no second colon
   did("notadid")           # no prefix
   did("DID:example:123")   # the scheme is lowercase
   did("")                  # empty

The method-specific part is deliberately loose, so this cannot tell you whether an
identifier is well formed *for its method* — that requires the method's own rules.
Resolving a DID to its document is a separate step, and a syntactically valid DID may
resolve to nothing.
