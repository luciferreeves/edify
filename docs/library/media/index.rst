Media
=====

File naming, media types, encodings, and the metadata that describes content. Each
validator is a callable :class:`~edify.Pattern`: import it, call it with a string,
get a ``bool``.

.. code-block:: python

   from edify.library import mimetype, extension, locale

   mimetype("application/json")   # True
   extension(".png")              # True
   locale("en-US")                # True

.. toctree::
   :hidden:

   charset
   codec
   encoding
   extension
   favicon
   filename
   glob
   locale
   mimetype
   regex
   shebang

Naming files
------------

- :doc:`filename` — a name with an extension; :doc:`extension` — the suffix alone.
- :doc:`glob` — a wildcard pattern; :doc:`favicon` — a site icon path.

Describing content
------------------

- :doc:`mimetype` — a ``type/subtype`` media type.
- :doc:`charset` — a character-set name; :doc:`encoding` — an HTTP content coding.
- :doc:`codec` — an audio or video codec name.

Locale and interpretation
-------------------------

- :doc:`locale` — a language and region tag.
- :doc:`shebang` — the interpreter line of a script.
- :doc:`regex` — a string that compiles as a regular expression.
