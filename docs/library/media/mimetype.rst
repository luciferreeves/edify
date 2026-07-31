MIME type
=========

A `media type <https://datatracker.ietf.org/doc/html/rfc6838>`__ (:rfc:`6838`) names
the format of a payload as ``type/subtype`` — ``text/plain``,
``application/json``. **MIME type** matches that pair.

Each half is a :meth:`~edify.RegexBuilder.letter`-led run of the token characters
:rfc:`6838` permits: alphanumerics plus ``!`` ``#`` ``$`` ``&`` ``-`` ``^`` ``_``
``.`` ``+``. The ``+`` is what allows structured-suffix subtypes such as
``+json``, and the ``.`` covers vendor trees.

Common media types
------------------

.. edify-playground::

   from edify.library import mimetype

   mimetype("text/plain")
   mimetype("application/json")
   mimetype("image/svg+xml")                  # a structured suffix
   mimetype("application/vnd.api+json")       # a vendor tree
   mimetype("application/x-www-form-urlencoded")

Both halves are required
------------------------

.. edify-playground::

   from edify.library import mimetype

   mimetype("text/html")   # a complete type
   mimetype("text")        # no subtype
   mimetype("/plain")      # no type
   mimetype("text/")       # an empty subtype
   mimetype("")            # empty

Parameters such as ``; charset=utf-8`` are part of a Content-Type *header*, not the
media type itself — split them off before validating, and check the charset with
:doc:`charset`. This also matches invented types, since the pattern cannot consult
the IANA registry. For the file suffix that usually implies a type see
:doc:`extension`.
