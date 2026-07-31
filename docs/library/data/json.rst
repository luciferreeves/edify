JSON
====

`JSON <https://www.json.org/>`__ (:rfc:`8259`) is the most widely used
data-interchange format, and a JSON *document* is a single value: an object, an
array, a string, a number, or one of the three literals. **JSON** accepts any of
them, with whitespace allowed on either side.

The five value shapes are the branches of an :func:`~edify.any_of`, anchored between
:meth:`~edify.RegexBuilder.start_of_input` and
:meth:`~edify.RegexBuilder.end_of_input` so the whole string must be the value —
trailing junk is rejected. :meth:`~edify.RegexBuilder.dot_all` lets the structured
values span lines, which is how real documents are formatted.

Objects and arrays
------------------

The two structured values, empty or populated, on one line or many:

.. edify-playground::

   from edify.library import json

   json('{"id": 1, "name": "Ada"}')
   json("[1, 2, 3]")
   json("{}")
   json("[]")
   json('{\n  "user": {\n    "roles": ["admin"]\n  }\n}')

Scalars
-------

A bare string, number, or literal is a complete JSON document in its own right — a
detail that surprises people expecting only objects:

.. edify-playground::

   from edify.library import json

   json('"just a string"')   # a string document
   json("42")                # an integer
   json("-3.5")              # a negative decimal
   json("1.2e-9")            # scientific notation
   json("true")              # the literals
   json("null")

Whole-string, not a fragment
----------------------------

Because both ends are anchored, a truncated document or trailing content fails —
and JavaScript spellings that JSON does not share are rejected too:

.. edify-playground::

   from edify.library import json

   json('  {"a": 1}  ')     # surrounding whitespace is fine
   json('{"a": 1')          # truncated
   json('{"a":1}trailing')  # trailing content
   json("undefined")        # not a JSON literal
   json("+5")               # a leading plus is not allowed

A regular expression cannot count brackets, so this confirms the document's overall
shape and delimiters rather than that every brace is balanced — parse it to be
certain. For the format's schema-carrying cousins see :doc:`../api/jsonapi` and
:doc:`../api/hal`; for the indentation-based alternative, :doc:`yaml`.
