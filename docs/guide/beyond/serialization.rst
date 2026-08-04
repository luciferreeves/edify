Serialization
=============

A ``Pattern`` can round-trip through plain data — a dict or a JSON string — so
you can store patterns, ship them over the wire, or load them from configuration
and rebuild the exact same matcher on the other side.

What travels is the *structure*, not a regex string. That distinction is the whole
point: the reconstructed pattern can be explained, visualized, extended, and
re-emitted for a different engine, none of which is possible once a pattern has
been flattened to text.

To and from a dict
------------------

:meth:`Pattern.to_dict` turns a pattern into a JSON-compatible dictionary, and
:meth:`Pattern.from_dict` rebuilds it:

.. code-block:: python

   from edify import Pattern

   year = Pattern().named_capture("year").exactly(4).digit().end()

   document = year.to_dict()
   # {'edify': 0,
   #  'pattern': {'kind': 'root',
   #              'children': [{'kind': 'named-capture', 'name': 'year',
   #                            'children': [{'kind': 'exactly', 'times': 4,
   #                                          'child': {'kind': 'digit'}}]}]}}

   rebuilt = Pattern.from_dict(document)
   rebuilt.to_regex_string() == year.to_regex_string()   # True

The structure mirrors the builder chain exactly — each element is a node with a
``kind`` and its arguments — so the serialized form is as readable as the pattern
that produced it. ``named_capture("year")`` becomes ``{'kind': 'named-capture',
'name': 'year'}``; ``exactly(4)`` becomes ``{'kind': 'exactly', 'times': 4}``.
Anyone can read a stored document and know what it matches.

.. edify-playground::
   :tests: 2024|24|20245|abcd

   from edify import Pattern

   Pattern.from_dict({
       "edify": 0,
       "pattern": {
           "kind": "root",
           "children": [
               {"kind": "start"},
               {"kind": "exactly", "times": 4, "child": {"kind": "digit"}},
               {"kind": "end"},
           ],
       },
   })

That playground builds its pattern entirely from data — no chain at all — and it
matches exactly what the equivalent chain would.

To and from JSON
----------------

:meth:`Pattern.to_json` and :meth:`Pattern.from_json` do the same over a JSON
string:

.. code-block:: python

   from edify import Pattern

   year = Pattern().named_capture("year").exactly(4).digit().end()

   blob = year.to_json()
   # '{"edify":0,"pattern":{"children":[{"children":[{"child":{"kind":"digit"},
   #   "kind":"exactly","times":4}],"kind":"named-capture","name":"year"}],"kind":"root"}}'

   Pattern.from_json(blob).to_regex_string() == year.to_regex_string()   # True

Keys are emitted in sorted order and without whitespace, so the same pattern
always produces byte-identical JSON. That makes the output safe to hash, use as a
cache key, or commit to a repository where a diff should mean a real change.

Schema version
--------------

Every document carries an ``"edify"`` schema version (exposed as
:data:`edify.serialize.SCHEMA_VERSION`). Loading a document written by a newer,
incompatible schema raises a clear error rather than silently mis-parsing it — so
stored patterns stay safe to load as the format evolves:

.. code-block:: python

   from edify import EdifyError, Pattern

   try:
       Pattern.from_dict({"edify": 999, "pattern": {"kind": "root", "children": []}})
   except EdifyError as problem:
       print(problem)

.. code-block:: text

   error: canonical dict declares schema version 999, but this build only understands 0

      = note: schema version 0 is experimental; regenerate the payload from the
        producing edify version, or upgrade this side to the version that emitted
        the payload.

   help: check the ``edify`` key in the input matches the emitting build.

The loader is strict about the rest of the document too, and each failure names
what is wrong rather than raising a bare ``KeyError``:

.. code-block:: text

   error: canonical dict is missing the required 'edify' key
   error: canonical dict is missing the required 'pattern' key
   error: unknown element kind 'nope' in canonical dict

That strictness is what makes it reasonable to load patterns from a database or a
config file: a malformed document is a caught, described exception, never a
half-built matcher. See :doc:`errors` for the shape those diagnostics take.

The lower-level functions
-------------------------

The ``Pattern`` methods are built on functions in :mod:`edify.serialize` that you
can call directly when you need finer control — converting a single element or a
whole builder state:

.. code-block:: python

   from edify import Pattern
   from edify.serialize import dict_to_element, element_to_dict

   elements = Pattern().exactly(3).digit().to_regex().elements

   element_to_dict(elements[0])
   # {'kind': 'exactly', 'times': 3, 'child': {'kind': 'digit'}}

   dict_to_element(element_to_dict(elements[0]))
   # ExactlyElement(times=3, child=DigitElement())

- :func:`~edify.serialize.element_to_dict` / :func:`~edify.serialize.dict_to_element`
  convert one pattern element to and from its dict node — no schema envelope, just
  the node. Use these when you are storing fragments rather than whole patterns.
- :func:`~edify.serialize.state_to_dict` / :func:`~edify.serialize.dict_to_state`
  convert a whole builder state — the full document, schema version and all.

Where this pays off
-------------------

Storing structure rather than a regex string means the stored form is still a
first-class pattern when it comes back:

.. code-block:: python

   from edify import Pattern

   stored = Pattern().named_capture("year").exactly(4).digit().end().to_json()

   loaded = Pattern.from_json(stored)
   loaded.to_regex().explain()          # describe it in prose
   extended = loaded.char("-").exactly(2).digit()   # keep building on it

A rule engine can ship validation patterns as configuration; an admin UI can let
someone assemble a pattern and persist it; a test fixture can be a JSON file. In
every case the far side gets the element tree, so :doc:`seeing` and
:doc:`../practice/performance` still apply to it.

Next: :doc:`integrations`, on dropping edify patterns straight into pydantic,
FastAPI, and Django.
