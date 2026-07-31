Protocol Buffers
================

`Protocol buffers <https://protobuf.dev/>`__ encode data as compact binary with no
self-describing header — the wire format cannot be recognised on sight. What *can*
be recognised is the schema: a ``.proto`` source file, which is ordinary text with a
small set of opening keywords. **Protocol Buffers** matches that source.

The openings are the branches of an :func:`~edify.any_of`: a ``syntax`` declaration
naming a proto version, a ``//`` comment, or one of the top-level keywords
``package``, ``import``, ``message``, ``service``, and ``enum``, each followed by
whitespace so a longer identifier cannot pass for it.

The syntax declaration
----------------------

Conventionally the first line of a schema, in either quoting style:

.. edify-playground::

   from edify.library import protobuf

   protobuf('syntax = "proto3";\nmessage Order {}')
   protobuf("syntax = 'proto2';")
   protobuf('syntax="proto3";')      # spacing is free

Declarations and comments
-------------------------

A file may open with any top-level declaration, or a comment:

.. edify-playground::

   from edify.library import protobuf

   protobuf("package orders.v1;\n")
   protobuf('import "common.proto";\n')
   protobuf("message Order {\n  int32 id = 1;\n}")
   protobuf("service Orders {\n  rpc Get(Req) returns (Res);\n}")
   protobuf("enum Status {\n  ACTIVE = 0;\n}")
   protobuf("// a comment\nmessage B {}")

Not the wire format
-------------------

This matches schema *source*, not encoded messages — and not unrelated text:

.. edify-playground::

   from edify.library import protobuf

   protobuf("message A {}")   # a schema declaration
   protobuf("hello-world")   # not a schema
   protobuf('{"a": 1}')      # JSON
   protobuf("<root/>")       # XML

It confirms the file opens as a schema; field numbering, type correctness, and
reserved ranges need the compiler. For a schema-carrying binary container see
:doc:`avro`.
