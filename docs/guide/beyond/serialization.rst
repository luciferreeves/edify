Serialization
=============

A ``Pattern`` can round-trip through plain data — a dict or a JSON string — so
you can store patterns, ship them over the wire, or load them from configuration
and rebuild the exact same matcher on the other side.

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
that produced it.

To and from JSON
----------------

:meth:`Pattern.to_json` and :meth:`Pattern.from_json` do the same over a JSON
string:

.. code-block:: python

   blob = year.to_json()
   Pattern.from_json(blob).to_regex_string() == year.to_regex_string()   # True

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
   # error: canonical dict declares schema version 999, but this build only understands 0

The lower-level functions
-------------------------

The ``Pattern`` methods are built on functions in :mod:`edify.serialize` that you
can call directly when you need finer control — converting a single element or a
whole builder state:

.. code-block:: python

   from edify.serialize import element_to_dict, dict_to_element, state_to_dict, dict_to_state

- :func:`~edify.serialize.element_to_dict` / :func:`~edify.serialize.dict_to_element`
  convert one pattern element to and from its dict node.
- :func:`~edify.serialize.state_to_dict` / :func:`~edify.serialize.dict_to_state`
  convert a whole builder state — the full document, schema version and all.

Next: :doc:`integrations`, on dropping edify patterns straight into pydantic,
FastAPI, and Django.
