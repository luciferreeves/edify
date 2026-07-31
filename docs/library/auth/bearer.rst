Bearer
======

The `bearer <https://datatracker.ietf.org/doc/html/rfc6750>`__ authorization scheme
(:rfc:`6750`) is how a token travels in an HTTP request: the literal word
``Bearer``, a single space, then the credential. **Bearer** matches that header
value — the part after ``Authorization:``.

The scheme name is a :meth:`~edify.RegexBuilder.string` literal followed by a
space, then :meth:`~edify.RegexBuilder.one_or_more` of the token character class —
letters, digits, ``.``, ``_``, and ``-``, which covers both opaque tokens and the
dotted :doc:`jwt` form.

Header values
-------------

Whatever the token itself looks like, the prefix is fixed:

.. edify-playground::

   from edify.library import bearer

   bearer("Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIn0.sig")   # a JWT
   bearer("Bearer 4f9a2c7e-opaque-token")                      # an opaque token
   bearer("Bearer a")                                          # the shortest form

The scheme is case-sensitive and spaced
---------------------------------------

:rfc:`7235` treats scheme names case-insensitively, but this validator matches the
canonical spelling that every server emits — so a lowercased or unspaced variant is
rejected, as is the bare token without its scheme:

.. edify-playground::

   from edify.library import bearer

   bearer("Bearer abc123")   # canonical
   bearer("bearer abc123")   # lowercase scheme
   bearer("Bearer  abc")     # two spaces
   bearer("abc123")          # no scheme
   bearer("Basic abc123")    # a different scheme

Matching the header says nothing about the token inside it — parse and verify that
separately. For the token's own structure see :doc:`jwt` or :doc:`token`.
