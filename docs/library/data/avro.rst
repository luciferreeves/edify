Avro
====

An `Apache Avro <https://avro.apache.org/docs/current/specification/>`__
object-container file stores records together with the schema that describes them.
Every such file opens with the four-byte magic ``Obj`` followed by the version byte
``0x01``, and **Avro** checks for exactly that.

The literal is written with :meth:`~edify.RegexBuilder.string` — including the
non-printing version byte — anchored at
:meth:`~edify.RegexBuilder.start_of_input`, with the remaining bytes matched under
:meth:`~edify.RegexBuilder.dot_all`.

The container signature
-----------------------

The schema and compressed data blocks follow the marker:

.. edify-playground::

   from edify.library import avro

   avro("Obj\x01")                          # the marker alone
   avro("Obj\x01\x04avro.schema{...}")      # schema metadata follows
   avro("Obj\x01\x00block\nmore blocks")    # bytes spanning lines

The version byte matters
------------------------

``Obj`` alone is not the signature, and the marker is case-sensitive:

.. edify-playground::

   from edify.library import avro

   avro("Obj")        # missing the version byte
   avro("OBJ\x01")    # wrong case
   avro("hello")      # not a signature

The signature identifies an object-container file; the embedded schema, codec, and
sync markers are left to a reader. Avro's schemas are themselves :doc:`json`
documents. For columnar alternatives see :doc:`parquet` and :doc:`orc`.
