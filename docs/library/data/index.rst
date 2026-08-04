Data
====

Serialisation and data-interchange formats — the text formats you read and write by
hand, and the binary containers you identify by their signature. Each validator is a
callable :class:`~edify.Pattern`: import it, call it with a string, get a ``bool``.

.. code-block:: python

   from edify.library import json, yaml, csv

   json('{"a": 1}')      # True
   yaml("key: value")    # True
   csv("name,age")       # True

.. toctree::
   :hidden:

   avro
   csv
   hdf5
   html
   ini
   json
   msgpack
   orc
   parquet
   protobuf
   toml
   tsv
   xml
   yaml

Structured text
---------------

- :doc:`json` — an object, array, string, number, or literal.
- :doc:`yaml` — a document marker, mapping, sequence, or comment.
- :doc:`toml` — a table header or key assignment; :doc:`ini` — its older cousin.

Markup
------

- :doc:`xml` — a declaration or root element; :doc:`html` — a doctype or
  ``<html>`` root.

Tabular
-------

- :doc:`csv` — comma-separated rows; :doc:`tsv` — tab-separated rows.

Binary containers
-----------------

- :doc:`avro`, :doc:`parquet`, :doc:`orc` — analytics file signatures.
- :doc:`hdf5` — the scientific-data container signature.
- :doc:`msgpack` — a binary payload whose root is a map or array.

Schemas
-------

- :doc:`protobuf` — a protocol-buffer schema source file.
